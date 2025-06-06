# Release History

## 1.3.0 (2025-04-23)

### Features Added

  - Added operation ReplicationProtectionContainersOperations.begin_switch_cluster_protection
  - Added operation group ClusterRecoveryPointOperations
  - Added operation group ClusterRecoveryPointsOperations
  - Added operation group ReplicationProtectionClustersOperations
  - Model A2AEnableProtectionInput has a new parameter protection_cluster_id
  - Model A2AReplicationDetails has a new parameter is_cluster_infra_ready
  - Model A2AReplicationDetails has a new parameter protection_cluster_id
  - Model HyperVReplicaAzureDiskInputDetails has a new parameter sector_size_in_bytes
  - Model HyperVReplicaAzureEnableProtectionInput has a new parameter linux_license_type
  - Model HyperVReplicaAzureEnableProtectionInput has a new parameter target_vm_security_profile
  - Model HyperVReplicaAzureEnableProtectionInput has a new parameter user_selected_os_name
  - Model HyperVReplicaAzureManagedDiskDetails has a new parameter sector_size_in_bytes
  - Model HyperVReplicaAzureManagedDiskDetails has a new parameter target_disk_account_type
  - Model HyperVReplicaAzureReplicationDetails has a new parameter linux_license_type
  - Model HyperVReplicaAzureReplicationDetails has a new parameter target_vm_security_profile
  - Model HyperVReplicaAzureUpdateReplicationProtectedItemInput has a new parameter linux_license_type
  - Model HyperVReplicaAzureUpdateReplicationProtectedItemInput has a new parameter user_selected_os_name
  - Model InMageRcmDiskInput has a new parameter sector_size_in_bytes
  - Model InMageRcmDisksDefaultInput has a new parameter sector_size_in_bytes
  - Model InMageRcmEnableProtectionInput has a new parameter linux_license_type
  - Model InMageRcmEnableProtectionInput has a new parameter seed_managed_disk_tags
  - Model InMageRcmEnableProtectionInput has a new parameter sql_server_license_type
  - Model InMageRcmEnableProtectionInput has a new parameter target_managed_disk_tags
  - Model InMageRcmEnableProtectionInput has a new parameter target_nic_tags
  - Model InMageRcmEnableProtectionInput has a new parameter target_vm_security_profile
  - Model InMageRcmEnableProtectionInput has a new parameter target_vm_tags
  - Model InMageRcmEnableProtectionInput has a new parameter user_selected_os_name
  - Model InMageRcmNicDetails has a new parameter target_nic_name
  - Model InMageRcmNicInput has a new parameter target_nic_name
  - Model InMageRcmProtectedDiskDetails has a new parameter custom_target_disk_name
  - Model InMageRcmProtectedDiskDetails has a new parameter disk_state
  - Model InMageRcmProtectedDiskDetails has a new parameter sector_size_in_bytes
  - Model InMageRcmReplicationDetails has a new parameter linux_license_type
  - Model InMageRcmReplicationDetails has a new parameter os_name
  - Model InMageRcmReplicationDetails has a new parameter seed_managed_disk_tags
  - Model InMageRcmReplicationDetails has a new parameter sql_server_license_type
  - Model InMageRcmReplicationDetails has a new parameter supported_os_versions
  - Model InMageRcmReplicationDetails has a new parameter target_managed_disk_tags
  - Model InMageRcmReplicationDetails has a new parameter target_nic_tags
  - Model InMageRcmReplicationDetails has a new parameter target_vm_security_profile
  - Model InMageRcmReplicationDetails has a new parameter target_vm_tags
  - Model InMageRcmReplicationDetails has a new parameter unprotected_disks
  - Model InMageRcmTestFailoverInput has a new parameter os_upgrade_version
  - Model InMageRcmUnplannedFailoverInput has a new parameter os_upgrade_version
  - Model InMageRcmUpdateReplicationProtectedItemInput has a new parameter linux_license_type
  - Model InMageRcmUpdateReplicationProtectedItemInput has a new parameter sql_server_license_type
  - Model InMageRcmUpdateReplicationProtectedItemInput has a new parameter target_managed_disk_tags
  - Model InMageRcmUpdateReplicationProtectedItemInput has a new parameter target_nic_tags
  - Model InMageRcmUpdateReplicationProtectedItemInput has a new parameter target_vm_tags
  - Model InMageRcmUpdateReplicationProtectedItemInput has a new parameter user_selected_os_name
  - Model OSDetails has a new parameter user_selected_os_name
  - Model VMwareCbtDiskInput has a new parameter sector_size_in_bytes
  - Model VMwareCbtEnableMigrationInput has a new parameter linux_license_type
  - Model VMwareCbtEnableMigrationInput has a new parameter user_selected_os_name
  - Model VMwareCbtMigrateInput has a new parameter post_migration_steps
  - Model VMwareCbtMigrationDetails has a new parameter linux_license_type
  - Model VMwareCbtProtectedDiskDetails has a new parameter sector_size_in_bytes
  - Model VMwareCbtTestMigrateInput has a new parameter post_migration_steps
  - Model VMwareCbtUpdateMigrationItemInput has a new parameter linux_license_type
  - Model VMwareCbtUpdateMigrationItemInput has a new parameter user_selected_os_name

## 1.2.0 (2024-02-22)

### Features Added

  - Added operation ReplicationFabricsOperations.begin_remove_infra
  - Model A2AEnableProtectionInput has a new parameter auto_protection_of_data_disk

## 1.1.0 (2023-09-15)

### Features Added

  - Model A2AReplicationDetails has a new parameter churn_option_selected
  - Model AzureFabricSpecificDetails has a new parameter location_details
  - Model FabricQueryParameter has a new parameter extended_location_mappings
  - Model FabricQueryParameter has a new parameter location_details
  - Model HyperVReplicaAzurePlannedFailoverProviderInput has a new parameter os_upgrade_version
  - Model HyperVReplicaAzureReplicationDetails has a new parameter all_available_os_upgrade_configurations
  - Model HyperVReplicaAzureTestFailoverInput has a new parameter os_upgrade_version
  - Model InMageAzureV2ReplicationDetails has a new parameter all_available_os_upgrade_configurations
  - Model InMageAzureV2ReplicationDetails has a new parameter os_name
  - Model InMageAzureV2ReplicationDetails has a new parameter supported_os_versions
  - Model InMageAzureV2TestFailoverInput has a new parameter os_upgrade_version
  - Model InMageAzureV2UnplannedFailoverInput has a new parameter os_upgrade_version
  - Model VMwareCbtEnableMigrationInput has a new parameter confidential_vm_key_vault_id
  - Model VMwareCbtEnableMigrationInput has a new parameter target_vm_security_profile
  - Model VMwareCbtMigrateInput has a new parameter os_upgrade_version
  - Model VMwareCbtMigrationDetails has a new parameter appliance_monitoring_details
  - Model VMwareCbtMigrationDetails has a new parameter confidential_vm_key_vault_id
  - Model VMwareCbtMigrationDetails has a new parameter delta_sync_progress_percentage
  - Model VMwareCbtMigrationDetails has a new parameter delta_sync_retry_count
  - Model VMwareCbtMigrationDetails has a new parameter gateway_operation_details
  - Model VMwareCbtMigrationDetails has a new parameter is_check_sum_resync_cycle
  - Model VMwareCbtMigrationDetails has a new parameter operation_name
  - Model VMwareCbtMigrationDetails has a new parameter os_name
  - Model VMwareCbtMigrationDetails has a new parameter supported_os_versions
  - Model VMwareCbtMigrationDetails has a new parameter target_vm_security_profile
  - Model VMwareCbtProtectedDiskDetails has a new parameter gateway_operation_details
  - Model VMwareCbtProtectionContainerMappingDetails has a new parameter excluded_skus
  - Model VMwareCbtTestMigrateInput has a new parameter os_upgrade_version

## 1.0.0 (2022-12-15)

### Features Added

  - Model AzureFabricSpecificDetails has a new parameter extended_locations
  - Model RecoveryPlanA2ADetails has a new parameter primary_extended_location
  - Model RecoveryPlanA2ADetails has a new parameter recovery_extended_location

## 1.0.0b2 (2022-11-18)

### Features Added

  - Added operation ReplicationMigrationItemsOperations.begin_pause_replication
  - Added operation ReplicationMigrationItemsOperations.begin_resume_replication
  - Added operation ReplicationProtectedItemsOperations.begin_switch_provider
  - Added operation group ReplicationAppliancesOperations
  - Model A2AContainerMappingInput has a new parameter automation_account_authentication_type
  - Model A2ACreateProtectionIntentInput has a new parameter agent_auto_update_status
  - Model A2ACreateProtectionIntentInput has a new parameter automation_account_arm_id
  - Model A2ACreateProtectionIntentInput has a new parameter automation_account_authentication_type
  - Model A2AEnableProtectionInput has a new parameter recovery_capacity_reservation_group_id
  - Model A2AEnableProtectionInput has a new parameter recovery_extended_location
  - Model A2AProtectionContainerMappingDetails has a new parameter automation_account_authentication_type
  - Model A2AReplicationDetails has a new parameter initial_primary_extended_location
  - Model A2AReplicationDetails has a new parameter initial_recovery_extended_location
  - Model A2AReplicationDetails has a new parameter primary_extended_location
  - Model A2AReplicationDetails has a new parameter recovery_capacity_reservation_group_id
  - Model A2AReplicationDetails has a new parameter recovery_extended_location
  - Model A2AReplicationIntentDetails has a new parameter agent_auto_update_status
  - Model A2AReplicationIntentDetails has a new parameter automation_account_arm_id
  - Model A2AReplicationIntentDetails has a new parameter automation_account_authentication_type
  - Model A2ASwitchProtectionInput has a new parameter recovery_capacity_reservation_group_id
  - Model A2AUpdateContainerMappingInput has a new parameter automation_account_authentication_type
  - Model A2AUpdateReplicationProtectedItemInput has a new parameter recovery_capacity_reservation_group_id
  - Model HyperVVirtualMachineDetails has a new parameter hyper_v_host_id
  - Model InMageAzureV2ProtectedDiskDetails has a new parameter seconds_to_take_switch_provider
  - Model InMageAzureV2ReplicationDetails has a new parameter switch_provider_blocking_error_details
  - Model InMageAzureV2ReplicationDetails has a new parameter switch_provider_details
  - Model InMageRcmProtectedDiskDetails has a new parameter seed_blob_uri
  - Model InMageRcmReplicationDetails has a new parameter storage_account_id
  - Model MigrationItemProperties has a new parameter critical_job_history
  - Model MigrationItemProperties has a new parameter last_migration_status
  - Model MigrationItemProperties has a new parameter last_migration_time
  - Model MigrationItemProperties has a new parameter recovery_services_provider_id
  - Model MigrationItemProperties has a new parameter replication_status
  - Model RecoveryPlanA2AInput has a new parameter primary_extended_location
  - Model RecoveryPlanA2AInput has a new parameter recovery_extended_location
  - Model ReplicationProtectedItemProperties has a new parameter switch_provider_state
  - Model ReplicationProtectedItemProperties has a new parameter switch_provider_state_description
  - Model VMwareCbtEnableMigrationInput has a new parameter perform_sql_bulk_registration
  - Model VMwareCbtEnableMigrationInput has a new parameter test_network_id
  - Model VMwareCbtEnableMigrationInput has a new parameter test_subnet_name
  - Model VMwareCbtMigrationDetails has a new parameter resume_progress_percentage
  - Model VMwareCbtMigrationDetails has a new parameter resume_retry_count
  - Model VMwareCbtMigrationDetails has a new parameter storage_account_id
  - Model VMwareCbtMigrationDetails has a new parameter test_network_id
  - Model VMwareCbtNicDetails has a new parameter test_ip_address
  - Model VMwareCbtNicDetails has a new parameter test_ip_address_type
  - Model VMwareCbtNicDetails has a new parameter test_network_id
  - Model VMwareCbtNicDetails has a new parameter test_subnet_name
  - Model VMwareCbtNicInput has a new parameter test_static_ip_address
  - Model VMwareCbtNicInput has a new parameter test_subnet_name
  - Model VMwareCbtProtectedDiskDetails has a new parameter seed_blob_uri
  - Model VMwareCbtProtectedDiskDetails has a new parameter target_blob_uri
  - Model VMwareCbtProtectionContainerMappingDetails has a new parameter role_size_to_nic_count_map
  - Model VMwareCbtTestMigrateInput has a new parameter vm_nics
  - Model VMwareCbtUpdateDiskInput has a new parameter is_os_disk
  - Model VMwareCbtUpdateMigrationItemInput has a new parameter test_network_id
  - Model VMwareDetails has a new parameter switch_provider_blocking_error_details
  - Model VmmVirtualMachineDetails has a new parameter hyper_v_host_id

### Breaking Changes

  - Operation ReplicationProtectedItemsOperations.begin_update_mobility_service has a new required parameter replicated_protected_item_name
  - Operation ReplicationProtectedItemsOperations.begin_update_mobility_service no longer has parameter replication_protected_item_name

## 1.0.0b1 (2021-07-28)

* Initial Release
