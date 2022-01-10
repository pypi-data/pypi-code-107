# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *

__all__ = ['EventGridDataConnectionArgs', 'EventGridDataConnection']

@pulumi.input_type
class EventGridDataConnectionArgs:
    def __init__(__self__, *,
                 consumer_group: pulumi.Input[str],
                 database_name: pulumi.Input[str],
                 event_hub_resource_id: pulumi.Input[str],
                 kind: pulumi.Input[str],
                 kusto_pool_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 storage_account_resource_id: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 blob_storage_event_type: Optional[pulumi.Input[Union[str, 'BlobStorageEventType']]] = None,
                 data_connection_name: Optional[pulumi.Input[str]] = None,
                 data_format: Optional[pulumi.Input[Union[str, 'EventGridDataFormat']]] = None,
                 ignore_first_record: Optional[pulumi.Input[bool]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mapping_rule_name: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a EventGridDataConnection resource.
        :param pulumi.Input[str] consumer_group: The event hub consumer group.
        :param pulumi.Input[str] database_name: The name of the database in the Kusto pool.
        :param pulumi.Input[str] event_hub_resource_id: The resource ID where the event grid is configured to send events.
        :param pulumi.Input[str] kind: Kind of the endpoint for the data connection
               Expected value is 'EventGrid'.
        :param pulumi.Input[str] kusto_pool_name: The name of the Kusto pool.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] storage_account_resource_id: The resource ID of the storage account where the data resides.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[Union[str, 'BlobStorageEventType']] blob_storage_event_type: The name of blob storage event type to process.
        :param pulumi.Input[str] data_connection_name: The name of the data connection.
        :param pulumi.Input[Union[str, 'EventGridDataFormat']] data_format: The data format of the message. Optionally the data format can be added to each message.
        :param pulumi.Input[bool] ignore_first_record: A Boolean value that, if set to true, indicates that ingestion should ignore the first record of every file
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] mapping_rule_name: The mapping rule to be used to ingest the data. Optionally the mapping information can be added to each message.
        :param pulumi.Input[str] table_name: The table where the data should be ingested. Optionally the table information can be added to each message.
        """
        pulumi.set(__self__, "consumer_group", consumer_group)
        pulumi.set(__self__, "database_name", database_name)
        pulumi.set(__self__, "event_hub_resource_id", event_hub_resource_id)
        pulumi.set(__self__, "kind", 'EventGrid')
        pulumi.set(__self__, "kusto_pool_name", kusto_pool_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "storage_account_resource_id", storage_account_resource_id)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if blob_storage_event_type is not None:
            pulumi.set(__self__, "blob_storage_event_type", blob_storage_event_type)
        if data_connection_name is not None:
            pulumi.set(__self__, "data_connection_name", data_connection_name)
        if data_format is not None:
            pulumi.set(__self__, "data_format", data_format)
        if ignore_first_record is not None:
            pulumi.set(__self__, "ignore_first_record", ignore_first_record)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if mapping_rule_name is not None:
            pulumi.set(__self__, "mapping_rule_name", mapping_rule_name)
        if table_name is not None:
            pulumi.set(__self__, "table_name", table_name)

    @property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> pulumi.Input[str]:
        """
        The event hub consumer group.
        """
        return pulumi.get(self, "consumer_group")

    @consumer_group.setter
    def consumer_group(self, value: pulumi.Input[str]):
        pulumi.set(self, "consumer_group", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[str]:
        """
        The name of the database in the Kusto pool.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter(name="eventHubResourceId")
    def event_hub_resource_id(self) -> pulumi.Input[str]:
        """
        The resource ID where the event grid is configured to send events.
        """
        return pulumi.get(self, "event_hub_resource_id")

    @event_hub_resource_id.setter
    def event_hub_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "event_hub_resource_id", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        Kind of the endpoint for the data connection
        Expected value is 'EventGrid'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="kustoPoolName")
    def kusto_pool_name(self) -> pulumi.Input[str]:
        """
        The name of the Kusto pool.
        """
        return pulumi.get(self, "kusto_pool_name")

    @kusto_pool_name.setter
    def kusto_pool_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "kusto_pool_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the storage account where the data resides.
        """
        return pulumi.get(self, "storage_account_resource_id")

    @storage_account_resource_id.setter
    def storage_account_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_account_resource_id", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="blobStorageEventType")
    def blob_storage_event_type(self) -> Optional[pulumi.Input[Union[str, 'BlobStorageEventType']]]:
        """
        The name of blob storage event type to process.
        """
        return pulumi.get(self, "blob_storage_event_type")

    @blob_storage_event_type.setter
    def blob_storage_event_type(self, value: Optional[pulumi.Input[Union[str, 'BlobStorageEventType']]]):
        pulumi.set(self, "blob_storage_event_type", value)

    @property
    @pulumi.getter(name="dataConnectionName")
    def data_connection_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the data connection.
        """
        return pulumi.get(self, "data_connection_name")

    @data_connection_name.setter
    def data_connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_connection_name", value)

    @property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> Optional[pulumi.Input[Union[str, 'EventGridDataFormat']]]:
        """
        The data format of the message. Optionally the data format can be added to each message.
        """
        return pulumi.get(self, "data_format")

    @data_format.setter
    def data_format(self, value: Optional[pulumi.Input[Union[str, 'EventGridDataFormat']]]):
        pulumi.set(self, "data_format", value)

    @property
    @pulumi.getter(name="ignoreFirstRecord")
    def ignore_first_record(self) -> Optional[pulumi.Input[bool]]:
        """
        A Boolean value that, if set to true, indicates that ingestion should ignore the first record of every file
        """
        return pulumi.get(self, "ignore_first_record")

    @ignore_first_record.setter
    def ignore_first_record(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_first_record", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="mappingRuleName")
    def mapping_rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The mapping rule to be used to ingest the data. Optionally the mapping information can be added to each message.
        """
        return pulumi.get(self, "mapping_rule_name")

    @mapping_rule_name.setter
    def mapping_rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mapping_rule_name", value)

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[pulumi.Input[str]]:
        """
        The table where the data should be ingested. Optionally the table information can be added to each message.
        """
        return pulumi.get(self, "table_name")

    @table_name.setter
    def table_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "table_name", value)


class EventGridDataConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 blob_storage_event_type: Optional[pulumi.Input[Union[str, 'BlobStorageEventType']]] = None,
                 consumer_group: Optional[pulumi.Input[str]] = None,
                 data_connection_name: Optional[pulumi.Input[str]] = None,
                 data_format: Optional[pulumi.Input[Union[str, 'EventGridDataFormat']]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 event_hub_resource_id: Optional[pulumi.Input[str]] = None,
                 ignore_first_record: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 kusto_pool_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mapping_rule_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account_resource_id: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Class representing an Event Grid data connection.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'BlobStorageEventType']] blob_storage_event_type: The name of blob storage event type to process.
        :param pulumi.Input[str] consumer_group: The event hub consumer group.
        :param pulumi.Input[str] data_connection_name: The name of the data connection.
        :param pulumi.Input[Union[str, 'EventGridDataFormat']] data_format: The data format of the message. Optionally the data format can be added to each message.
        :param pulumi.Input[str] database_name: The name of the database in the Kusto pool.
        :param pulumi.Input[str] event_hub_resource_id: The resource ID where the event grid is configured to send events.
        :param pulumi.Input[bool] ignore_first_record: A Boolean value that, if set to true, indicates that ingestion should ignore the first record of every file
        :param pulumi.Input[str] kind: Kind of the endpoint for the data connection
               Expected value is 'EventGrid'.
        :param pulumi.Input[str] kusto_pool_name: The name of the Kusto pool.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] mapping_rule_name: The mapping rule to be used to ingest the data. Optionally the mapping information can be added to each message.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] storage_account_resource_id: The resource ID of the storage account where the data resides.
        :param pulumi.Input[str] table_name: The table where the data should be ingested. Optionally the table information can be added to each message.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EventGridDataConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Class representing an Event Grid data connection.

        :param str resource_name: The name of the resource.
        :param EventGridDataConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EventGridDataConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 blob_storage_event_type: Optional[pulumi.Input[Union[str, 'BlobStorageEventType']]] = None,
                 consumer_group: Optional[pulumi.Input[str]] = None,
                 data_connection_name: Optional[pulumi.Input[str]] = None,
                 data_format: Optional[pulumi.Input[Union[str, 'EventGridDataFormat']]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 event_hub_resource_id: Optional[pulumi.Input[str]] = None,
                 ignore_first_record: Optional[pulumi.Input[bool]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 kusto_pool_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mapping_rule_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account_resource_id: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EventGridDataConnectionArgs.__new__(EventGridDataConnectionArgs)

            __props__.__dict__["blob_storage_event_type"] = blob_storage_event_type
            if consumer_group is None and not opts.urn:
                raise TypeError("Missing required property 'consumer_group'")
            __props__.__dict__["consumer_group"] = consumer_group
            __props__.__dict__["data_connection_name"] = data_connection_name
            __props__.__dict__["data_format"] = data_format
            if database_name is None and not opts.urn:
                raise TypeError("Missing required property 'database_name'")
            __props__.__dict__["database_name"] = database_name
            if event_hub_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'event_hub_resource_id'")
            __props__.__dict__["event_hub_resource_id"] = event_hub_resource_id
            __props__.__dict__["ignore_first_record"] = ignore_first_record
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'EventGrid'
            if kusto_pool_name is None and not opts.urn:
                raise TypeError("Missing required property 'kusto_pool_name'")
            __props__.__dict__["kusto_pool_name"] = kusto_pool_name
            __props__.__dict__["location"] = location
            __props__.__dict__["mapping_rule_name"] = mapping_rule_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if storage_account_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account_resource_id'")
            __props__.__dict__["storage_account_resource_id"] = storage_account_resource_id
            __props__.__dict__["table_name"] = table_name
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:synapse:EventGridDataConnection"), pulumi.Alias(type_="azure-native:synapse/v20210401preview:EventGridDataConnection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(EventGridDataConnection, __self__).__init__(
            'azure-native:synapse/v20210601preview:EventGridDataConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EventGridDataConnection':
        """
        Get an existing EventGridDataConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EventGridDataConnectionArgs.__new__(EventGridDataConnectionArgs)

        __props__.__dict__["blob_storage_event_type"] = None
        __props__.__dict__["consumer_group"] = None
        __props__.__dict__["data_format"] = None
        __props__.__dict__["event_hub_resource_id"] = None
        __props__.__dict__["ignore_first_record"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["mapping_rule_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["storage_account_resource_id"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["table_name"] = None
        __props__.__dict__["type"] = None
        return EventGridDataConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="blobStorageEventType")
    def blob_storage_event_type(self) -> pulumi.Output[Optional[str]]:
        """
        The name of blob storage event type to process.
        """
        return pulumi.get(self, "blob_storage_event_type")

    @property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> pulumi.Output[str]:
        """
        The event hub consumer group.
        """
        return pulumi.get(self, "consumer_group")

    @property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> pulumi.Output[Optional[str]]:
        """
        The data format of the message. Optionally the data format can be added to each message.
        """
        return pulumi.get(self, "data_format")

    @property
    @pulumi.getter(name="eventHubResourceId")
    def event_hub_resource_id(self) -> pulumi.Output[str]:
        """
        The resource ID where the event grid is configured to send events.
        """
        return pulumi.get(self, "event_hub_resource_id")

    @property
    @pulumi.getter(name="ignoreFirstRecord")
    def ignore_first_record(self) -> pulumi.Output[Optional[bool]]:
        """
        A Boolean value that, if set to true, indicates that ingestion should ignore the first record of every file
        """
        return pulumi.get(self, "ignore_first_record")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Kind of the endpoint for the data connection
        Expected value is 'EventGrid'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mappingRuleName")
    def mapping_rule_name(self) -> pulumi.Output[Optional[str]]:
        """
        The mapping rule to be used to ingest the data. Optionally the mapping information can be added to each message.
        """
        return pulumi.get(self, "mapping_rule_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioned state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the storage account where the data resides.
        """
        return pulumi.get(self, "storage_account_resource_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Output[Optional[str]]:
        """
        The table where the data should be ingested. Optionally the table information can be added to each message.
        """
        return pulumi.get(self, "table_name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

