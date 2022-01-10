# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['TopicArgs', 'Topic']

@pulumi.input_type
class TopicArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 inbound_ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input['InboundIpRuleArgs']]]] = None,
                 input_schema: Optional[pulumi.Input[Union[str, 'InputSchema']]] = None,
                 input_schema_mapping: Optional[pulumi.Input['JsonInputSchemaMappingArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 topic_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Topic resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input[Sequence[pulumi.Input['InboundIpRuleArgs']]] inbound_ip_rules: This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.
        :param pulumi.Input[Union[str, 'InputSchema']] input_schema: This determines the format that Event Grid should expect for incoming events published to the topic.
        :param pulumi.Input['JsonInputSchemaMappingArgs'] input_schema_mapping: This enables publishing using custom event schemas. An InputSchemaMapping can be specified to map various properties of a source schema to various required properties of the EventGridEvent schema.
        :param pulumi.Input[str] location: Location of the resource.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: This determines if traffic is allowed over public network. By default it is enabled. 
               You can further restrict to specific IPs by configuring <seealso cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.TopicProperties.InboundIpRules" />
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags of the resource.
        :param pulumi.Input[str] topic_name: Name of the topic.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if inbound_ip_rules is not None:
            pulumi.set(__self__, "inbound_ip_rules", inbound_ip_rules)
        if input_schema is None:
            input_schema = 'EventGridSchema'
        if input_schema is not None:
            pulumi.set(__self__, "input_schema", input_schema)
        if input_schema_mapping is not None:
            pulumi.set(__self__, "input_schema_mapping", input_schema_mapping)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if public_network_access is None:
            public_network_access = 'Enabled'
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if topic_name is not None:
            pulumi.set(__self__, "topic_name", topic_name)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the user's subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="inboundIpRules")
    def inbound_ip_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InboundIpRuleArgs']]]]:
        """
        This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.
        """
        return pulumi.get(self, "inbound_ip_rules")

    @inbound_ip_rules.setter
    def inbound_ip_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InboundIpRuleArgs']]]]):
        pulumi.set(self, "inbound_ip_rules", value)

    @property
    @pulumi.getter(name="inputSchema")
    def input_schema(self) -> Optional[pulumi.Input[Union[str, 'InputSchema']]]:
        """
        This determines the format that Event Grid should expect for incoming events published to the topic.
        """
        return pulumi.get(self, "input_schema")

    @input_schema.setter
    def input_schema(self, value: Optional[pulumi.Input[Union[str, 'InputSchema']]]):
        pulumi.set(self, "input_schema", value)

    @property
    @pulumi.getter(name="inputSchemaMapping")
    def input_schema_mapping(self) -> Optional[pulumi.Input['JsonInputSchemaMappingArgs']]:
        """
        This enables publishing using custom event schemas. An InputSchemaMapping can be specified to map various properties of a source schema to various required properties of the EventGridEvent schema.
        """
        return pulumi.get(self, "input_schema_mapping")

    @input_schema_mapping.setter
    def input_schema_mapping(self, value: Optional[pulumi.Input['JsonInputSchemaMappingArgs']]):
        pulumi.set(self, "input_schema_mapping", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]:
        """
        This determines if traffic is allowed over public network. By default it is enabled. 
        You can further restrict to specific IPs by configuring <seealso cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.TopicProperties.InboundIpRules" />
        """
        return pulumi.get(self, "public_network_access")

    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]):
        pulumi.set(self, "public_network_access", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Tags of the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="topicName")
    def topic_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the topic.
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
                 inbound_ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InboundIpRuleArgs']]]]] = None,
                 input_schema: Optional[pulumi.Input[Union[str, 'InputSchema']]] = None,
                 input_schema_mapping: Optional[pulumi.Input[pulumi.InputType['JsonInputSchemaMappingArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 topic_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        EventGrid Topic
        API Version: 2020-06-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InboundIpRuleArgs']]]] inbound_ip_rules: This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.
        :param pulumi.Input[Union[str, 'InputSchema']] input_schema: This determines the format that Event Grid should expect for incoming events published to the topic.
        :param pulumi.Input[pulumi.InputType['JsonInputSchemaMappingArgs']] input_schema_mapping: This enables publishing using custom event schemas. An InputSchemaMapping can be specified to map various properties of a source schema to various required properties of the EventGridEvent schema.
        :param pulumi.Input[str] location: Location of the resource.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: This determines if traffic is allowed over public network. By default it is enabled. 
               You can further restrict to specific IPs by configuring <seealso cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.TopicProperties.InboundIpRules" />
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Tags of the resource.
        :param pulumi.Input[str] topic_name: Name of the topic.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TopicArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        EventGrid Topic
        API Version: 2020-06-01.

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
                 inbound_ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InboundIpRuleArgs']]]]] = None,
                 input_schema: Optional[pulumi.Input[Union[str, 'InputSchema']]] = None,
                 input_schema_mapping: Optional[pulumi.Input[pulumi.InputType['JsonInputSchemaMappingArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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

            __props__.__dict__["inbound_ip_rules"] = inbound_ip_rules
            if input_schema is None:
                input_schema = 'EventGridSchema'
            __props__.__dict__["input_schema"] = input_schema
            __props__.__dict__["input_schema_mapping"] = input_schema_mapping
            __props__.__dict__["location"] = location
            if public_network_access is None:
                public_network_access = 'Enabled'
            __props__.__dict__["public_network_access"] = public_network_access
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["topic_name"] = topic_name
            __props__.__dict__["endpoint"] = None
            __props__.__dict__["metric_resource_id"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["private_endpoint_connections"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:eventgrid/v20170615preview:Topic"), pulumi.Alias(type_="azure-native:eventgrid/v20170915preview:Topic"), pulumi.Alias(type_="azure-native:eventgrid/v20180101:Topic"), pulumi.Alias(type_="azure-native:eventgrid/v20180501preview:Topic"), pulumi.Alias(type_="azure-native:eventgrid/v20180915preview:Topic"), pulumi.Alias(type_="azure-native:eventgrid/v20190101:Topic"), pulumi.Alias(type_="azure-native:eventgrid/v20190201preview:Topic"), pulumi.Alias(type_="azure-native:eventgrid/v20190601:Topic"), pulumi.Alias(type_="azure-native:eventgrid/v20200101preview:Topic"), pulumi.Alias(type_="azure-native:eventgrid/v20200401preview:Topic"), pulumi.Alias(type_="azure-native:eventgrid/v20200601:Topic"), pulumi.Alias(type_="azure-native:eventgrid/v20201015preview:Topic"), pulumi.Alias(type_="azure-native:eventgrid/v20210601preview:Topic"), pulumi.Alias(type_="azure-native:eventgrid/v20211201:Topic")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Topic, __self__).__init__(
            'azure-native:eventgrid:Topic',
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

        __props__.__dict__["endpoint"] = None
        __props__.__dict__["inbound_ip_rules"] = None
        __props__.__dict__["input_schema"] = None
        __props__.__dict__["input_schema_mapping"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["metric_resource_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_endpoint_connections"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_network_access"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Topic(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[str]:
        """
        Endpoint for the topic.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter(name="inboundIpRules")
    def inbound_ip_rules(self) -> pulumi.Output[Optional[Sequence['outputs.InboundIpRuleResponse']]]:
        """
        This can be used to restrict traffic from specific IPs instead of all IPs. Note: These are considered only if PublicNetworkAccess is enabled.
        """
        return pulumi.get(self, "inbound_ip_rules")

    @property
    @pulumi.getter(name="inputSchema")
    def input_schema(self) -> pulumi.Output[Optional[str]]:
        """
        This determines the format that Event Grid should expect for incoming events published to the topic.
        """
        return pulumi.get(self, "input_schema")

    @property
    @pulumi.getter(name="inputSchemaMapping")
    def input_schema_mapping(self) -> pulumi.Output[Optional['outputs.JsonInputSchemaMappingResponse']]:
        """
        This enables publishing using custom event schemas. An InputSchemaMapping can be specified to map various properties of a source schema to various required properties of the EventGridEvent schema.
        """
        return pulumi.get(self, "input_schema_mapping")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="metricResourceId")
    def metric_resource_id(self) -> pulumi.Output[str]:
        """
        Metric resource id for the topic.
        """
        return pulumi.get(self, "metric_resource_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Sequence['outputs.PrivateEndpointConnectionResponse']]:
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the topic.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[str]]:
        """
        This determines if traffic is allowed over public network. By default it is enabled. 
        You can further restrict to specific IPs by configuring <seealso cref="P:Microsoft.Azure.Events.ResourceProvider.Common.Contracts.TopicProperties.InboundIpRules" />
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to Topic resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")

