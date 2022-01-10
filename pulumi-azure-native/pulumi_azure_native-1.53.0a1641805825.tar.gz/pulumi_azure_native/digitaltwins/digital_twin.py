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

__all__ = ['DigitalTwinArgs', 'DigitalTwin']

@pulumi.input_type
class DigitalTwinArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 identity: Optional[pulumi.Input['DigitalTwinsIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 private_endpoint_connections: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateEndpointConnectionArgs']]]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DigitalTwin resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the DigitalTwinsInstance.
        :param pulumi.Input['DigitalTwinsIdentityArgs'] identity: The managed identity for the DigitalTwinsInstance.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: Public network access for the DigitalTwinsInstance.
        :param pulumi.Input[str] resource_name: The name of the DigitalTwinsInstance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if private_endpoint_connections is not None:
            pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the DigitalTwinsInstance.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['DigitalTwinsIdentityArgs']]:
        """
        The managed identity for the DigitalTwinsInstance.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['DigitalTwinsIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrivateEndpointConnectionArgs']]]]:
        return pulumi.get(self, "private_endpoint_connections")

    @private_endpoint_connections.setter
    def private_endpoint_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateEndpointConnectionArgs']]]]):
        pulumi.set(self, "private_endpoint_connections", value)

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]:
        """
        Public network access for the DigitalTwinsInstance.
        """
        return pulumi.get(self, "public_network_access")

    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]):
        pulumi.set(self, "public_network_access", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the DigitalTwinsInstance.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class DigitalTwin(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['DigitalTwinsIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 private_endpoint_connections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivateEndpointConnectionArgs']]]]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The description of the DigitalTwins service.
        API Version: 2020-12-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['DigitalTwinsIdentityArgs']] identity: The managed identity for the DigitalTwinsInstance.
        :param pulumi.Input[str] location: The resource location.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: Public network access for the DigitalTwinsInstance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the DigitalTwinsInstance.
        :param pulumi.Input[str] resource_name_: The name of the DigitalTwinsInstance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DigitalTwinArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The description of the DigitalTwins service.
        API Version: 2020-12-01.

        :param str resource_name: The name of the resource.
        :param DigitalTwinArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DigitalTwinArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['DigitalTwinsIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 private_endpoint_connections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivateEndpointConnectionArgs']]]]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = DigitalTwinArgs.__new__(DigitalTwinArgs)

            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["private_endpoint_connections"] = private_endpoint_connections
            __props__.__dict__["public_network_access"] = public_network_access
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["tags"] = tags
            __props__.__dict__["created_time"] = None
            __props__.__dict__["host_name"] = None
            __props__.__dict__["last_updated_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:digitaltwins/v20200301preview:DigitalTwin"), pulumi.Alias(type_="azure-native:digitaltwins/v20201031:DigitalTwin"), pulumi.Alias(type_="azure-native:digitaltwins/v20201201:DigitalTwin")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DigitalTwin, __self__).__init__(
            'azure-native:digitaltwins:DigitalTwin',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DigitalTwin':
        """
        Get an existing DigitalTwin resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DigitalTwinArgs.__new__(DigitalTwinArgs)

        __props__.__dict__["created_time"] = None
        __props__.__dict__["host_name"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["last_updated_time"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_endpoint_connections"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_network_access"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return DigitalTwin(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[str]:
        """
        Time when DigitalTwinsInstance was created.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Output[str]:
        """
        Api endpoint to work with DigitalTwinsInstance.
        """
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.DigitalTwinsIdentityResponse']]:
        """
        The managed identity for the DigitalTwinsInstance.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> pulumi.Output[str]:
        """
        Time when DigitalTwinsInstance was updated.
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Optional[Sequence['outputs.PrivateEndpointConnectionResponse']]]:
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[str]]:
        """
        Public network access for the DigitalTwinsInstance.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

