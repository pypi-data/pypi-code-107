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
from ._inputs import *

__all__ = ['EventHubArgs', 'EventHub']

@pulumi.input_type
class EventHubArgs:
    def __init__(__self__, *,
                 namespace_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 capture_description: Optional[pulumi.Input['CaptureDescriptionArgs']] = None,
                 event_hub_name: Optional[pulumi.Input[str]] = None,
                 message_retention_in_days: Optional[pulumi.Input[float]] = None,
                 partition_count: Optional[pulumi.Input[float]] = None,
                 status: Optional[pulumi.Input['EntityStatus']] = None):
        """
        The set of arguments for constructing a EventHub resource.
        :param pulumi.Input[str] namespace_name: The Namespace name
        :param pulumi.Input[str] resource_group_name: Name of the resource group within the azure subscription.
        :param pulumi.Input['CaptureDescriptionArgs'] capture_description: Properties of capture description
        :param pulumi.Input[str] event_hub_name: The Event Hub name
        :param pulumi.Input[float] message_retention_in_days: Number of days to retain the events for this Event Hub, value should be 1 to 7 days
        :param pulumi.Input[float] partition_count: Number of partitions created for the Event Hub, allowed values are from 1 to 32 partitions.
        :param pulumi.Input['EntityStatus'] status: Enumerates the possible values for the status of the Event Hub.
        """
        pulumi.set(__self__, "namespace_name", namespace_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if capture_description is not None:
            pulumi.set(__self__, "capture_description", capture_description)
        if event_hub_name is not None:
            pulumi.set(__self__, "event_hub_name", event_hub_name)
        if message_retention_in_days is not None:
            pulumi.set(__self__, "message_retention_in_days", message_retention_in_days)
        if partition_count is not None:
            pulumi.set(__self__, "partition_count", partition_count)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[str]:
        """
        The Namespace name
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group within the azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="captureDescription")
    def capture_description(self) -> Optional[pulumi.Input['CaptureDescriptionArgs']]:
        """
        Properties of capture description
        """
        return pulumi.get(self, "capture_description")

    @capture_description.setter
    def capture_description(self, value: Optional[pulumi.Input['CaptureDescriptionArgs']]):
        pulumi.set(self, "capture_description", value)

    @property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Event Hub name
        """
        return pulumi.get(self, "event_hub_name")

    @event_hub_name.setter
    def event_hub_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "event_hub_name", value)

    @property
    @pulumi.getter(name="messageRetentionInDays")
    def message_retention_in_days(self) -> Optional[pulumi.Input[float]]:
        """
        Number of days to retain the events for this Event Hub, value should be 1 to 7 days
        """
        return pulumi.get(self, "message_retention_in_days")

    @message_retention_in_days.setter
    def message_retention_in_days(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "message_retention_in_days", value)

    @property
    @pulumi.getter(name="partitionCount")
    def partition_count(self) -> Optional[pulumi.Input[float]]:
        """
        Number of partitions created for the Event Hub, allowed values are from 1 to 32 partitions.
        """
        return pulumi.get(self, "partition_count")

    @partition_count.setter
    def partition_count(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "partition_count", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input['EntityStatus']]:
        """
        Enumerates the possible values for the status of the Event Hub.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input['EntityStatus']]):
        pulumi.set(self, "status", value)


class EventHub(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capture_description: Optional[pulumi.Input[pulumi.InputType['CaptureDescriptionArgs']]] = None,
                 event_hub_name: Optional[pulumi.Input[str]] = None,
                 message_retention_in_days: Optional[pulumi.Input[float]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 partition_count: Optional[pulumi.Input[float]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['EntityStatus']] = None,
                 __props__=None):
        """
        Single item in List or Get Event Hub operation

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['CaptureDescriptionArgs']] capture_description: Properties of capture description
        :param pulumi.Input[str] event_hub_name: The Event Hub name
        :param pulumi.Input[float] message_retention_in_days: Number of days to retain the events for this Event Hub, value should be 1 to 7 days
        :param pulumi.Input[str] namespace_name: The Namespace name
        :param pulumi.Input[float] partition_count: Number of partitions created for the Event Hub, allowed values are from 1 to 32 partitions.
        :param pulumi.Input[str] resource_group_name: Name of the resource group within the azure subscription.
        :param pulumi.Input['EntityStatus'] status: Enumerates the possible values for the status of the Event Hub.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EventHubArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Single item in List or Get Event Hub operation

        :param str resource_name: The name of the resource.
        :param EventHubArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EventHubArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 capture_description: Optional[pulumi.Input[pulumi.InputType['CaptureDescriptionArgs']]] = None,
                 event_hub_name: Optional[pulumi.Input[str]] = None,
                 message_retention_in_days: Optional[pulumi.Input[float]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 partition_count: Optional[pulumi.Input[float]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['EntityStatus']] = None,
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
            __props__ = EventHubArgs.__new__(EventHubArgs)

            __props__.__dict__["capture_description"] = capture_description
            __props__.__dict__["event_hub_name"] = event_hub_name
            __props__.__dict__["message_retention_in_days"] = message_retention_in_days
            if namespace_name is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_name'")
            __props__.__dict__["namespace_name"] = namespace_name
            __props__.__dict__["partition_count"] = partition_count
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["status"] = status
            __props__.__dict__["created_at"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["partition_ids"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["updated_at"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:eventhub:EventHub"), pulumi.Alias(type_="azure-native:eventhub/v20140901:EventHub"), pulumi.Alias(type_="azure-native:eventhub/v20150801:EventHub"), pulumi.Alias(type_="azure-native:eventhub/v20170401:EventHub"), pulumi.Alias(type_="azure-native:eventhub/v20180101preview:EventHub"), pulumi.Alias(type_="azure-native:eventhub/v20210101preview:EventHub"), pulumi.Alias(type_="azure-native:eventhub/v20211101:EventHub")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(EventHub, __self__).__init__(
            'azure-native:eventhub/v20210601preview:EventHub',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EventHub':
        """
        Get an existing EventHub resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EventHubArgs.__new__(EventHubArgs)

        __props__.__dict__["capture_description"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["message_retention_in_days"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["partition_count"] = None
        __props__.__dict__["partition_ids"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["updated_at"] = None
        return EventHub(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="captureDescription")
    def capture_description(self) -> pulumi.Output[Optional['outputs.CaptureDescriptionResponse']]:
        """
        Properties of capture description
        """
        return pulumi.get(self, "capture_description")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Exact time the Event Hub was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="messageRetentionInDays")
    def message_retention_in_days(self) -> pulumi.Output[Optional[float]]:
        """
        Number of days to retain the events for this Event Hub, value should be 1 to 7 days
        """
        return pulumi.get(self, "message_retention_in_days")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="partitionCount")
    def partition_count(self) -> pulumi.Output[Optional[float]]:
        """
        Number of partitions created for the Event Hub, allowed values are from 1 to 32 partitions.
        """
        return pulumi.get(self, "partition_count")

    @property
    @pulumi.getter(name="partitionIds")
    def partition_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        Current number of shards on the Event Hub.
        """
        return pulumi.get(self, "partition_ids")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        Enumerates the possible values for the status of the Event Hub.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system meta data relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        The exact time the message was updated.
        """
        return pulumi.get(self, "updated_at")

