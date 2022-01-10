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

__all__ = ['TopicArgs', 'Topic']

@pulumi.input_type
class TopicArgs:
    def __init__(__self__, *,
                 namespace_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 auto_delete_on_idle: Optional[pulumi.Input[str]] = None,
                 default_message_time_to_live: Optional[pulumi.Input[str]] = None,
                 duplicate_detection_history_time_window: Optional[pulumi.Input[str]] = None,
                 enable_batched_operations: Optional[pulumi.Input[bool]] = None,
                 enable_express: Optional[pulumi.Input[bool]] = None,
                 enable_partitioning: Optional[pulumi.Input[bool]] = None,
                 max_message_size_in_kilobytes: Optional[pulumi.Input[float]] = None,
                 max_size_in_megabytes: Optional[pulumi.Input[int]] = None,
                 requires_duplicate_detection: Optional[pulumi.Input[bool]] = None,
                 status: Optional[pulumi.Input['EntityStatus']] = None,
                 support_ordering: Optional[pulumi.Input[bool]] = None,
                 topic_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Topic resource.
        :param pulumi.Input[str] namespace_name: The namespace name
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[str] auto_delete_on_idle: ISO 8601 timespan idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes.
        :param pulumi.Input[str] default_message_time_to_live: ISO 8601 Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.
        :param pulumi.Input[str] duplicate_detection_history_time_window: ISO8601 timespan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.
        :param pulumi.Input[bool] enable_batched_operations: Value that indicates whether server-side batched operations are enabled.
        :param pulumi.Input[bool] enable_express: Value that indicates whether Express Entities are enabled. An express topic holds a message in memory temporarily before writing it to persistent storage.
        :param pulumi.Input[bool] enable_partitioning: Value that indicates whether the topic to be partitioned across multiple message brokers is enabled.
        :param pulumi.Input[float] max_message_size_in_kilobytes: Maximum size (in KB) of the message payload that can be accepted by the topic. This property is only used in Premium today and default is 1024.
        :param pulumi.Input[int] max_size_in_megabytes: Maximum size of the topic in megabytes, which is the size of the memory allocated for the topic. Default is 1024.
        :param pulumi.Input[bool] requires_duplicate_detection: Value indicating if this topic requires duplicate detection.
        :param pulumi.Input['EntityStatus'] status: Enumerates the possible values for the status of a messaging entity.
        :param pulumi.Input[bool] support_ordering: Value that indicates whether the topic supports ordering.
        :param pulumi.Input[str] topic_name: The topic name.
        """
        pulumi.set(__self__, "namespace_name", namespace_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if auto_delete_on_idle is not None:
            pulumi.set(__self__, "auto_delete_on_idle", auto_delete_on_idle)
        if default_message_time_to_live is not None:
            pulumi.set(__self__, "default_message_time_to_live", default_message_time_to_live)
        if duplicate_detection_history_time_window is not None:
            pulumi.set(__self__, "duplicate_detection_history_time_window", duplicate_detection_history_time_window)
        if enable_batched_operations is not None:
            pulumi.set(__self__, "enable_batched_operations", enable_batched_operations)
        if enable_express is not None:
            pulumi.set(__self__, "enable_express", enable_express)
        if enable_partitioning is not None:
            pulumi.set(__self__, "enable_partitioning", enable_partitioning)
        if max_message_size_in_kilobytes is not None:
            pulumi.set(__self__, "max_message_size_in_kilobytes", max_message_size_in_kilobytes)
        if max_size_in_megabytes is not None:
            pulumi.set(__self__, "max_size_in_megabytes", max_size_in_megabytes)
        if requires_duplicate_detection is not None:
            pulumi.set(__self__, "requires_duplicate_detection", requires_duplicate_detection)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if support_ordering is not None:
            pulumi.set(__self__, "support_ordering", support_ordering)
        if topic_name is not None:
            pulumi.set(__self__, "topic_name", topic_name)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[str]:
        """
        The namespace name
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the Resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="autoDeleteOnIdle")
    def auto_delete_on_idle(self) -> Optional[pulumi.Input[str]]:
        """
        ISO 8601 timespan idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes.
        """
        return pulumi.get(self, "auto_delete_on_idle")

    @auto_delete_on_idle.setter
    def auto_delete_on_idle(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auto_delete_on_idle", value)

    @property
    @pulumi.getter(name="defaultMessageTimeToLive")
    def default_message_time_to_live(self) -> Optional[pulumi.Input[str]]:
        """
        ISO 8601 Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.
        """
        return pulumi.get(self, "default_message_time_to_live")

    @default_message_time_to_live.setter
    def default_message_time_to_live(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_message_time_to_live", value)

    @property
    @pulumi.getter(name="duplicateDetectionHistoryTimeWindow")
    def duplicate_detection_history_time_window(self) -> Optional[pulumi.Input[str]]:
        """
        ISO8601 timespan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.
        """
        return pulumi.get(self, "duplicate_detection_history_time_window")

    @duplicate_detection_history_time_window.setter
    def duplicate_detection_history_time_window(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "duplicate_detection_history_time_window", value)

    @property
    @pulumi.getter(name="enableBatchedOperations")
    def enable_batched_operations(self) -> Optional[pulumi.Input[bool]]:
        """
        Value that indicates whether server-side batched operations are enabled.
        """
        return pulumi.get(self, "enable_batched_operations")

    @enable_batched_operations.setter
    def enable_batched_operations(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_batched_operations", value)

    @property
    @pulumi.getter(name="enableExpress")
    def enable_express(self) -> Optional[pulumi.Input[bool]]:
        """
        Value that indicates whether Express Entities are enabled. An express topic holds a message in memory temporarily before writing it to persistent storage.
        """
        return pulumi.get(self, "enable_express")

    @enable_express.setter
    def enable_express(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_express", value)

    @property
    @pulumi.getter(name="enablePartitioning")
    def enable_partitioning(self) -> Optional[pulumi.Input[bool]]:
        """
        Value that indicates whether the topic to be partitioned across multiple message brokers is enabled.
        """
        return pulumi.get(self, "enable_partitioning")

    @enable_partitioning.setter
    def enable_partitioning(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_partitioning", value)

    @property
    @pulumi.getter(name="maxMessageSizeInKilobytes")
    def max_message_size_in_kilobytes(self) -> Optional[pulumi.Input[float]]:
        """
        Maximum size (in KB) of the message payload that can be accepted by the topic. This property is only used in Premium today and default is 1024.
        """
        return pulumi.get(self, "max_message_size_in_kilobytes")

    @max_message_size_in_kilobytes.setter
    def max_message_size_in_kilobytes(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "max_message_size_in_kilobytes", value)

    @property
    @pulumi.getter(name="maxSizeInMegabytes")
    def max_size_in_megabytes(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum size of the topic in megabytes, which is the size of the memory allocated for the topic. Default is 1024.
        """
        return pulumi.get(self, "max_size_in_megabytes")

    @max_size_in_megabytes.setter
    def max_size_in_megabytes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_size_in_megabytes", value)

    @property
    @pulumi.getter(name="requiresDuplicateDetection")
    def requires_duplicate_detection(self) -> Optional[pulumi.Input[bool]]:
        """
        Value indicating if this topic requires duplicate detection.
        """
        return pulumi.get(self, "requires_duplicate_detection")

    @requires_duplicate_detection.setter
    def requires_duplicate_detection(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "requires_duplicate_detection", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input['EntityStatus']]:
        """
        Enumerates the possible values for the status of a messaging entity.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input['EntityStatus']]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="supportOrdering")
    def support_ordering(self) -> Optional[pulumi.Input[bool]]:
        """
        Value that indicates whether the topic supports ordering.
        """
        return pulumi.get(self, "support_ordering")

    @support_ordering.setter
    def support_ordering(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "support_ordering", value)

    @property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> Optional[pulumi.Input[str]]:
        """
        The topic name.
        """
        return pulumi.get(self, "topic_name")

    @topic_name.setter
    def topic_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic_name", value)


class Topic(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_delete_on_idle: Optional[pulumi.Input[str]] = None,
                 default_message_time_to_live: Optional[pulumi.Input[str]] = None,
                 duplicate_detection_history_time_window: Optional[pulumi.Input[str]] = None,
                 enable_batched_operations: Optional[pulumi.Input[bool]] = None,
                 enable_express: Optional[pulumi.Input[bool]] = None,
                 enable_partitioning: Optional[pulumi.Input[bool]] = None,
                 max_message_size_in_kilobytes: Optional[pulumi.Input[float]] = None,
                 max_size_in_megabytes: Optional[pulumi.Input[int]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 requires_duplicate_detection: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['EntityStatus']] = None,
                 support_ordering: Optional[pulumi.Input[bool]] = None,
                 topic_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Description of topic resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auto_delete_on_idle: ISO 8601 timespan idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes.
        :param pulumi.Input[str] default_message_time_to_live: ISO 8601 Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.
        :param pulumi.Input[str] duplicate_detection_history_time_window: ISO8601 timespan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.
        :param pulumi.Input[bool] enable_batched_operations: Value that indicates whether server-side batched operations are enabled.
        :param pulumi.Input[bool] enable_express: Value that indicates whether Express Entities are enabled. An express topic holds a message in memory temporarily before writing it to persistent storage.
        :param pulumi.Input[bool] enable_partitioning: Value that indicates whether the topic to be partitioned across multiple message brokers is enabled.
        :param pulumi.Input[float] max_message_size_in_kilobytes: Maximum size (in KB) of the message payload that can be accepted by the topic. This property is only used in Premium today and default is 1024.
        :param pulumi.Input[int] max_size_in_megabytes: Maximum size of the topic in megabytes, which is the size of the memory allocated for the topic. Default is 1024.
        :param pulumi.Input[str] namespace_name: The namespace name
        :param pulumi.Input[bool] requires_duplicate_detection: Value indicating if this topic requires duplicate detection.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input['EntityStatus'] status: Enumerates the possible values for the status of a messaging entity.
        :param pulumi.Input[bool] support_ordering: Value that indicates whether the topic supports ordering.
        :param pulumi.Input[str] topic_name: The topic name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TopicArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Description of topic resource.

        :param str resource_name: The name of the resource.
        :param TopicArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TopicArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_delete_on_idle: Optional[pulumi.Input[str]] = None,
                 default_message_time_to_live: Optional[pulumi.Input[str]] = None,
                 duplicate_detection_history_time_window: Optional[pulumi.Input[str]] = None,
                 enable_batched_operations: Optional[pulumi.Input[bool]] = None,
                 enable_express: Optional[pulumi.Input[bool]] = None,
                 enable_partitioning: Optional[pulumi.Input[bool]] = None,
                 max_message_size_in_kilobytes: Optional[pulumi.Input[float]] = None,
                 max_size_in_megabytes: Optional[pulumi.Input[int]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 requires_duplicate_detection: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['EntityStatus']] = None,
                 support_ordering: Optional[pulumi.Input[bool]] = None,
                 topic_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = TopicArgs.__new__(TopicArgs)

            __props__.__dict__["auto_delete_on_idle"] = auto_delete_on_idle
            __props__.__dict__["default_message_time_to_live"] = default_message_time_to_live
            __props__.__dict__["duplicate_detection_history_time_window"] = duplicate_detection_history_time_window
            __props__.__dict__["enable_batched_operations"] = enable_batched_operations
            __props__.__dict__["enable_express"] = enable_express
            __props__.__dict__["enable_partitioning"] = enable_partitioning
            __props__.__dict__["max_message_size_in_kilobytes"] = max_message_size_in_kilobytes
            __props__.__dict__["max_size_in_megabytes"] = max_size_in_megabytes
            if namespace_name is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_name'")
            __props__.__dict__["namespace_name"] = namespace_name
            __props__.__dict__["requires_duplicate_detection"] = requires_duplicate_detection
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["status"] = status
            __props__.__dict__["support_ordering"] = support_ordering
            __props__.__dict__["topic_name"] = topic_name
            __props__.__dict__["accessed_at"] = None
            __props__.__dict__["count_details"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["location"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["size_in_bytes"] = None
            __props__.__dict__["subscription_count"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["updated_at"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:servicebus:Topic"), pulumi.Alias(type_="azure-native:servicebus/v20140901:Topic"), pulumi.Alias(type_="azure-native:servicebus/v20150801:Topic"), pulumi.Alias(type_="azure-native:servicebus/v20170401:Topic"), pulumi.Alias(type_="azure-native:servicebus/v20180101preview:Topic"), pulumi.Alias(type_="azure-native:servicebus/v20210101preview:Topic"), pulumi.Alias(type_="azure-native:servicebus/v20210601preview:Topic")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Topic, __self__).__init__(
            'azure-native:servicebus/v20211101:Topic',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Topic':
        """
        Get an existing Topic resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TopicArgs.__new__(TopicArgs)

        __props__.__dict__["accessed_at"] = None
        __props__.__dict__["auto_delete_on_idle"] = None
        __props__.__dict__["count_details"] = None
        __props__.__dict__["created_at"] = None
        __props__.__dict__["default_message_time_to_live"] = None
        __props__.__dict__["duplicate_detection_history_time_window"] = None
        __props__.__dict__["enable_batched_operations"] = None
        __props__.__dict__["enable_express"] = None
        __props__.__dict__["enable_partitioning"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["max_message_size_in_kilobytes"] = None
        __props__.__dict__["max_size_in_megabytes"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["requires_duplicate_detection"] = None
        __props__.__dict__["size_in_bytes"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["subscription_count"] = None
        __props__.__dict__["support_ordering"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["updated_at"] = None
        return Topic(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessedAt")
    def accessed_at(self) -> pulumi.Output[str]:
        """
        Last time the message was sent, or a request was received, for this topic.
        """
        return pulumi.get(self, "accessed_at")

    @property
    @pulumi.getter(name="autoDeleteOnIdle")
    def auto_delete_on_idle(self) -> pulumi.Output[Optional[str]]:
        """
        ISO 8601 timespan idle interval after which the topic is automatically deleted. The minimum duration is 5 minutes.
        """
        return pulumi.get(self, "auto_delete_on_idle")

    @property
    @pulumi.getter(name="countDetails")
    def count_details(self) -> pulumi.Output['outputs.MessageCountDetailsResponse']:
        """
        Message count details
        """
        return pulumi.get(self, "count_details")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Exact time the message was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="defaultMessageTimeToLive")
    def default_message_time_to_live(self) -> pulumi.Output[Optional[str]]:
        """
        ISO 8601 Default message timespan to live value. This is the duration after which the message expires, starting from when the message is sent to Service Bus. This is the default value used when TimeToLive is not set on a message itself.
        """
        return pulumi.get(self, "default_message_time_to_live")

    @property
    @pulumi.getter(name="duplicateDetectionHistoryTimeWindow")
    def duplicate_detection_history_time_window(self) -> pulumi.Output[Optional[str]]:
        """
        ISO8601 timespan structure that defines the duration of the duplicate detection history. The default value is 10 minutes.
        """
        return pulumi.get(self, "duplicate_detection_history_time_window")

    @property
    @pulumi.getter(name="enableBatchedOperations")
    def enable_batched_operations(self) -> pulumi.Output[Optional[bool]]:
        """
        Value that indicates whether server-side batched operations are enabled.
        """
        return pulumi.get(self, "enable_batched_operations")

    @property
    @pulumi.getter(name="enableExpress")
    def enable_express(self) -> pulumi.Output[Optional[bool]]:
        """
        Value that indicates whether Express Entities are enabled. An express topic holds a message in memory temporarily before writing it to persistent storage.
        """
        return pulumi.get(self, "enable_express")

    @property
    @pulumi.getter(name="enablePartitioning")
    def enable_partitioning(self) -> pulumi.Output[Optional[bool]]:
        """
        Value that indicates whether the topic to be partitioned across multiple message brokers is enabled.
        """
        return pulumi.get(self, "enable_partitioning")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maxMessageSizeInKilobytes")
    def max_message_size_in_kilobytes(self) -> pulumi.Output[Optional[float]]:
        """
        Maximum size (in KB) of the message payload that can be accepted by the topic. This property is only used in Premium today and default is 1024.
        """
        return pulumi.get(self, "max_message_size_in_kilobytes")

    @property
    @pulumi.getter(name="maxSizeInMegabytes")
    def max_size_in_megabytes(self) -> pulumi.Output[Optional[int]]:
        """
        Maximum size of the topic in megabytes, which is the size of the memory allocated for the topic. Default is 1024.
        """
        return pulumi.get(self, "max_size_in_megabytes")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="requiresDuplicateDetection")
    def requires_duplicate_detection(self) -> pulumi.Output[Optional[bool]]:
        """
        Value indicating if this topic requires duplicate detection.
        """
        return pulumi.get(self, "requires_duplicate_detection")

    @property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> pulumi.Output[float]:
        """
        Size of the topic, in bytes.
        """
        return pulumi.get(self, "size_in_bytes")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        Enumerates the possible values for the status of a messaging entity.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subscriptionCount")
    def subscription_count(self) -> pulumi.Output[int]:
        """
        Number of subscriptions.
        """
        return pulumi.get(self, "subscription_count")

    @property
    @pulumi.getter(name="supportOrdering")
    def support_ordering(self) -> pulumi.Output[Optional[bool]]:
        """
        Value that indicates whether the topic supports ordering.
        """
        return pulumi.get(self, "support_ordering")

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
        The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        The exact time the message was updated.
        """
        return pulumi.get(self, "updated_at")

