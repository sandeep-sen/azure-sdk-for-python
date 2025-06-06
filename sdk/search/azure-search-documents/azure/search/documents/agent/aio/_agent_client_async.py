# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
from typing import Union, Any, Optional, IO

from azure.core.credentials import AzureKeyCredential
from azure.core.credentials_async import AsyncTokenCredential
from azure.core.tracing.decorator_async import distributed_trace_async
from ..._utils import get_authentication_policy
from .._generated.aio import KnowledgeAgentRetrievalClient as _KnowledgeAgentRetrievalClient
from .._generated.models import (
    KnowledgeAgentRetrievalRequest,
    RequestOptions,
    KnowledgeAgentRetrievalResponse,
)
from ..._api_versions import DEFAULT_VERSION
from ..._headers_mixin import HeadersMixin
from ..._version import SDK_MONIKER


class KnowledgeAgentRetrievalClient(HeadersMixin):
    """A client that can be used to query an agent.

    :param endpoint: The URL endpoint of an Azure search service
    :type endpoint: str
    :param agent_name: The name of the agent. Required.
    :type agent_name: str
    :param credential: A credential to authorize search client requests
    :type credential: ~azure.core.credentials.AzureKeyCredential or ~azure.core.credentials_async.AsyncTokenCredential
    :keyword str api_version: The Search API version to use for requests.
    :keyword str audience: sets the Audience to use for authentication with Microsoft Entra ID. The
        audience is not considered when using a shared key. If audience is not provided, the public cloud audience
        will be assumed.
    """

    _ODATA_ACCEPT: str = "application/json;odata.metadata=none"
    _client: _KnowledgeAgentRetrievalClient

    def __init__(
        self, endpoint: str, agent_name: str, credential: Union[AzureKeyCredential, AsyncTokenCredential], **kwargs: Any
    ) -> None:
        self._api_version = kwargs.pop("api_version", DEFAULT_VERSION)
        self._endpoint: str = endpoint
        self._agent_name: str = agent_name
        self._credential = credential
        audience = kwargs.pop("audience", None)
        if isinstance(credential, AzureKeyCredential):
            self._aad = False
            self._client = _KnowledgeAgentRetrievalClient(
                endpoint=endpoint,
                agent_name=agent_name,
                sdk_moniker=SDK_MONIKER,
                api_version=self._api_version,
                **kwargs
            )
        else:
            self._aad = True
            authentication_policy = get_authentication_policy(credential, audience=audience, is_async=True)
            self._client = _KnowledgeAgentRetrievalClient(
                endpoint=endpoint,
                agent_name=agent_name,
                authentication_policy=authentication_policy,
                sdk_moniker=SDK_MONIKER,
                api_version=self._api_version,
                **kwargs
            )

    def __repr__(self) -> str:
        return "<KnowledgeAgentRetrievalClient [endpoint={}, agent={}]>".format(
            repr(self._endpoint), repr(self._agent_name)
        )[:1024]

    async def close(self) -> None:
        """Close the session.

        :return: None
        :rtype: None
        """
        return await self._client.close()

    @distributed_trace_async
    async def retrieve(
        self,
        retrieval_request: Union[KnowledgeAgentRetrievalRequest, IO[bytes]],
        x_ms_query_source_authorization: Optional[str] = None,
        request_options: Optional[RequestOptions] = None,
        **kwargs: Any
    ) -> KnowledgeAgentRetrievalResponse:
        kwargs["headers"] = self._merge_client_headers(kwargs.get("headers"))
        return await self._client.knowledge_retrieval.retrieve(
            retrieval_request=retrieval_request,
            x_ms_query_source_authorization=x_ms_query_source_authorization,
            request_options=request_options,
            **kwargs
        )
