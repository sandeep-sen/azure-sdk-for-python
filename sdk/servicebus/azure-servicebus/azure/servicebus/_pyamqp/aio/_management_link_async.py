# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import time
import logging
from uuid import uuid4
from functools import partial
from typing import Optional, Union

from ..management_link import PendingManagementOperation
from ._sender_async import SenderLink
from ._receiver_async import ReceiverLink
from ..constants import (
    ManagementLinkState,
    LinkState,
    SenderSettleMode,
    ReceiverSettleMode,
    ManagementExecuteOperationResult,
    ManagementOpenResult,
    SEND_DISPOSITION_REJECT,
    MessageDeliveryState,
    LinkDeliverySettleReason,
)
from ..error import AMQPException, ErrorCondition
from ..message import Properties, _MessageDelivery

_LOGGER = logging.getLogger(__name__)


class ManagementLink(object):  # pylint:disable=too-many-instance-attributes
    """
    # TODO: Fill in docstring
    """

    def __init__(self, session, endpoint, **kwargs):
        self.state = ManagementLinkState.IDLE
        self._pending_operations = []
        self._session = session
        self._network_trace_params = kwargs.get("network_trace_params")
        self._request_link: SenderLink = session.create_sender_link(
            endpoint,
            source_address=endpoint,
            on_link_state_change=self._on_sender_state_change,
            send_settle_mode=SenderSettleMode.Unsettled,
            rcv_settle_mode=ReceiverSettleMode.First,
            network_trace=kwargs.get("network_trace", False),
        )
        self._response_link: ReceiverLink = session.create_receiver_link(
            endpoint,
            target_address=endpoint,
            on_link_state_change=self._on_receiver_state_change,
            on_transfer=self._on_message_received,
            send_settle_mode=SenderSettleMode.Unsettled,
            rcv_settle_mode=ReceiverSettleMode.First,
            network_trace=kwargs.get("network_trace", False),
        )
        self._on_amqp_management_error = kwargs.get("on_amqp_management_error")
        self._on_amqp_management_open_complete = kwargs.get("on_amqp_management_open_complete")

        self._status_code_field = kwargs.get("status_code_field", b"statusCode")
        self._status_description_field = kwargs.get("status_description_field", b"statusDescription")

        self._sender_connected = False
        self._receiver_connected = False

    async def __aenter__(self):
        await self.open()
        return self

    async def __aexit__(self, *args):
        await self.close()

    async def _on_sender_state_change(self, previous_state, new_state):
        _LOGGER.info(
            "Management link sender state changed: %r -> %r",
            previous_state,
            new_state,
            extra=self._network_trace_params,
        )
        if new_state == previous_state:
            return
        if self.state == ManagementLinkState.OPENING:
            if new_state == LinkState.ATTACHED:
                self._sender_connected = True
                if self._receiver_connected:
                    self.state = ManagementLinkState.OPEN
                    await self._on_amqp_management_open_complete(ManagementOpenResult.OK)
            elif new_state in [LinkState.DETACHED, LinkState.DETACH_SENT, LinkState.DETACH_RCVD, LinkState.ERROR]:
                self.state = ManagementLinkState.IDLE
                await self._on_amqp_management_open_complete(ManagementOpenResult.ERROR)
        elif self.state == ManagementLinkState.OPEN:
            if new_state is not LinkState.ATTACHED:
                self.state = ManagementLinkState.ERROR
                await self._on_amqp_management_error()
        elif self.state == ManagementLinkState.CLOSING:
            if new_state not in [LinkState.DETACHED, LinkState.DETACH_SENT, LinkState.DETACH_RCVD]:
                self.state = ManagementLinkState.ERROR
                await self._on_amqp_management_error()
        elif self.state == ManagementLinkState.ERROR:
            # All state transitions shall be ignored.
            return

    async def _on_receiver_state_change(self, previous_state, new_state):
        _LOGGER.info(
            "Management link receiver state changed: %r -> %r",
            previous_state,
            new_state,
            extra=self._network_trace_params,
        )
        if new_state == previous_state:
            return
        if self.state == ManagementLinkState.OPENING:
            if new_state == LinkState.ATTACHED:
                self._receiver_connected = True
                if self._sender_connected:
                    self.state = ManagementLinkState.OPEN
                    await self._on_amqp_management_open_complete(ManagementOpenResult.OK)
            elif new_state in [LinkState.DETACHED, LinkState.DETACH_SENT, LinkState.DETACH_RCVD, LinkState.ERROR]:
                self.state = ManagementLinkState.IDLE
                await self._on_amqp_management_open_complete(ManagementOpenResult.ERROR)
        elif self.state == ManagementLinkState.OPEN:
            if new_state is not LinkState.ATTACHED:
                self.state = ManagementLinkState.ERROR
                await self._on_amqp_management_error()
        elif self.state == ManagementLinkState.CLOSING:
            if new_state not in [LinkState.DETACHED, LinkState.DETACH_SENT, LinkState.DETACH_RCVD]:
                self.state = ManagementLinkState.ERROR
                await self._on_amqp_management_error()
        elif self.state == ManagementLinkState.ERROR:
            # All state transitions shall be ignored.
            return

    async def _on_message_received(self, _, message):
        message_properties = message.properties
        correlation_id = message_properties[5]
        response_detail = message.application_properties

        status_code = response_detail.get(self._status_code_field)
        status_description = response_detail.get(self._status_description_field)

        to_remove_operation = None
        for operation in self._pending_operations:
            if operation.message.properties.message_id == correlation_id:
                to_remove_operation = operation
                break
        if to_remove_operation:
            mgmt_result = (
                ManagementExecuteOperationResult.OK
                if 200 <= status_code <= 299
                else ManagementExecuteOperationResult.FAILED_BAD_STATUS
            )
            await to_remove_operation.on_execute_operation_complete(
                mgmt_result, status_code, status_description, message, response_detail.get(b"error-condition")
            )
            self._pending_operations.remove(to_remove_operation)

    async def _on_send_complete(self, message_delivery, reason, state):
        if reason == LinkDeliverySettleReason.DISPOSITION_RECEIVED and SEND_DISPOSITION_REJECT in state:
            # sample reject state: {'rejected': [[b'amqp:not-allowed', b"Invalid command 'RE1AD'.", None]]}
            to_remove_operation = None
            for operation in self._pending_operations:
                if message_delivery.message == operation.message:
                    to_remove_operation = operation
                    break
            self._pending_operations.remove(to_remove_operation)
            # TODO: better error handling
            #  AMQPException is too general? to be more specific: MessageReject(Error) or AMQPManagementError?
            #  or should there an error mapping which maps the condition to the error type

            # The callback is defined in management_operation.py
            await to_remove_operation.on_execute_operation_complete(
                ManagementExecuteOperationResult.ERROR,
                None,
                None,
                message_delivery.message,
                error=AMQPException(
                    condition=state[SEND_DISPOSITION_REJECT][0][0],  # 0 is error condition
                    description=state[SEND_DISPOSITION_REJECT][0][1],  # 1 is error description
                    info=state[SEND_DISPOSITION_REJECT][0][2],  # 2 is error info
                ),
            )

    async def open(self):
        if self.state != ManagementLinkState.IDLE:
            raise ValueError("Management links are already open or opening.")
        self.state = ManagementLinkState.OPENING
        await self._response_link.attach()
        await self._request_link.attach()

    async def execute_operation(
        self,
        message,
        on_execute_operation_complete,
        *,
        operation: Optional[Union[bytes, str]] = None,
        type: Optional[Union[bytes, str]] = None,
        locales: Optional[str] = None,
        timeout: Optional[float] = None
    ):
        """Execute a request and wait on a response.

        :param message: The message to send in the management request.
        :type message: ~uamqp.message.Message
        :param on_execute_operation_complete: Callback to be called when the operation is complete.
         The following value will be passed to the callback: operation_id, operation_result, status_code,
         status_description, raw_message and error.
        :type on_execute_operation_complete: Callable[[str, str, int, str, ~uamqp.message.Message, Exception], None]
        :keyword operation: The type of operation to be performed. This value will
         be service-specific, but common values include READ, CREATE and UPDATE.
         This value will be added as an application property on the message.
        :paramtype operation: bytes or str
        :keyword type: The type on which to carry out the operation. This will
         be specific to the entities of the service. This value will be added as
         an application property on the message.
        :paramtype type: bytes or str
        :keyword str locales: A list of locales that the sending peer permits for incoming
         informational text in response messages.
        :keyword float timeout: Provide an optional timeout in seconds within which a response
         to the management request must be received.
        :rtype: None
        """
        message.application_properties["operation"] = operation
        message.application_properties["type"] = type
        if locales:
            message.application_properties["locales"] = locales
        try:
            # TODO: namedtuple is immutable, which may push us to re-think about the namedtuple approach for Message
            new_properties = message.properties._replace(message_id=uuid4())
        except AttributeError:
            new_properties = Properties(message_id=uuid4())
        message = message._replace(properties=new_properties)
        expire_time = (time.time() + timeout) if timeout else None
        message_delivery = _MessageDelivery(message, MessageDeliveryState.WaitingToBeSent, expire_time)

        on_send_complete = partial(self._on_send_complete, message_delivery)

        await self._request_link.send_transfer(message, on_send_complete=on_send_complete, timeout=timeout)
        self._pending_operations.append(PendingManagementOperation(message, on_execute_operation_complete))

    async def close(self):
        if self.state != ManagementLinkState.IDLE:
            self.state = ManagementLinkState.CLOSING
            await self._response_link.detach(close=True)
            await self._request_link.detach(close=True)
            for pending_operation in self._pending_operations:
                await pending_operation.on_execute_operation_complete(
                    ManagementExecuteOperationResult.LINK_CLOSED,
                    None,
                    None,
                    pending_operation.message,
                    AMQPException(condition=ErrorCondition.ClientError, description="Management link already closed."),
                )
            self._pending_operations = []
        self.state = ManagementLinkState.IDLE
