# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['WorkloadNetworkPortMirroringArgs', 'WorkloadNetworkPortMirroring']

@pulumi.input_type
class WorkloadNetworkPortMirroringArgs:
    def __init__(__self__, *,
                 private_cloud_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 destination: Optional[pulumi.Input[str]] = None,
                 direction: Optional[pulumi.Input[Union[str, 'PortMirroringDirectionEnum']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 port_mirroring_id: Optional[pulumi.Input[str]] = None,
                 revision: Optional[pulumi.Input[float]] = None,
                 source: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WorkloadNetworkPortMirroring resource.
        :param pulumi.Input[str] private_cloud_name: Name of the private cloud
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] destination: Destination VM Group.
        :param pulumi.Input[Union[str, 'PortMirroringDirectionEnum']] direction: Direction of port mirroring profile.
        :param pulumi.Input[str] display_name: Display name of the port mirroring profile.
        :param pulumi.Input[str] port_mirroring_id: NSX Port Mirroring identifier. Generally the same as the Port Mirroring display name
        :param pulumi.Input[float] revision: NSX revision number.
        :param pulumi.Input[str] source: Source VM Group.
        """
        pulumi.set(__self__, "private_cloud_name", private_cloud_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if destination is not None:
            pulumi.set(__self__, "destination", destination)
        if direction is not None:
            pulumi.set(__self__, "direction", direction)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if port_mirroring_id is not None:
            pulumi.set(__self__, "port_mirroring_id", port_mirroring_id)
        if revision is not None:
            pulumi.set(__self__, "revision", revision)
        if source is not None:
            pulumi.set(__self__, "source", source)

    @property
    @pulumi.getter(name="privateCloudName")
    def private_cloud_name(self) -> pulumi.Input[str]:
        """
        Name of the private cloud
        """
        return pulumi.get(self, "private_cloud_name")

    @private_cloud_name.setter
    def private_cloud_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "private_cloud_name", value)

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
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[str]]:
        """
        Destination VM Group.
        """
        return pulumi.get(self, "destination")

    @destination.setter
    def destination(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination", value)

    @property
    @pulumi.getter
    def direction(self) -> Optional[pulumi.Input[Union[str, 'PortMirroringDirectionEnum']]]:
        """
        Direction of port mirroring profile.
        """
        return pulumi.get(self, "direction")

    @direction.setter
    def direction(self, value: Optional[pulumi.Input[Union[str, 'PortMirroringDirectionEnum']]]):
        pulumi.set(self, "direction", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name of the port mirroring profile.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="portMirroringId")
    def port_mirroring_id(self) -> Optional[pulumi.Input[str]]:
        """
        NSX Port Mirroring identifier. Generally the same as the Port Mirroring display name
        """
        return pulumi.get(self, "port_mirroring_id")

    @port_mirroring_id.setter
    def port_mirroring_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "port_mirroring_id", value)

    @property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[float]]:
        """
        NSX revision number.
        """
        return pulumi.get(self, "revision")

    @revision.setter
    def revision(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "revision", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        """
        Source VM Group.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)


class WorkloadNetworkPortMirroring(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination: Optional[pulumi.Input[str]] = None,
                 direction: Optional[pulumi.Input[Union[str, 'PortMirroringDirectionEnum']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 port_mirroring_id: Optional[pulumi.Input[str]] = None,
                 private_cloud_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 revision: Optional[pulumi.Input[float]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        NSX Port Mirroring

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] destination: Destination VM Group.
        :param pulumi.Input[Union[str, 'PortMirroringDirectionEnum']] direction: Direction of port mirroring profile.
        :param pulumi.Input[str] display_name: Display name of the port mirroring profile.
        :param pulumi.Input[str] port_mirroring_id: NSX Port Mirroring identifier. Generally the same as the Port Mirroring display name
        :param pulumi.Input[str] private_cloud_name: Name of the private cloud
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[float] revision: NSX revision number.
        :param pulumi.Input[str] source: Source VM Group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkloadNetworkPortMirroringArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        NSX Port Mirroring

        :param str resource_name: The name of the resource.
        :param WorkloadNetworkPortMirroringArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkloadNetworkPortMirroringArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination: Optional[pulumi.Input[str]] = None,
                 direction: Optional[pulumi.Input[Union[str, 'PortMirroringDirectionEnum']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 port_mirroring_id: Optional[pulumi.Input[str]] = None,
                 private_cloud_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 revision: Optional[pulumi.Input[float]] = None,
                 source: Optional[pulumi.Input[str]] = None,
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
            __props__ = WorkloadNetworkPortMirroringArgs.__new__(WorkloadNetworkPortMirroringArgs)

            __props__.__dict__["destination"] = destination
            __props__.__dict__["direction"] = direction
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["port_mirroring_id"] = port_mirroring_id
            if private_cloud_name is None and not opts.urn:
                raise TypeError("Missing required property 'private_cloud_name'")
            __props__.__dict__["private_cloud_name"] = private_cloud_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["revision"] = revision
            __props__.__dict__["source"] = source
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:avs:WorkloadNetworkPortMirroring"), pulumi.Alias(type_="azure-native:avs/v20200717preview:WorkloadNetworkPortMirroring"), pulumi.Alias(type_="azure-native:avs/v20210101preview:WorkloadNetworkPortMirroring"), pulumi.Alias(type_="azure-native:avs/v20210601:WorkloadNetworkPortMirroring")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WorkloadNetworkPortMirroring, __self__).__init__(
            'azure-native:avs/v20211201:WorkloadNetworkPortMirroring',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkloadNetworkPortMirroring':
        """
        Get an existing WorkloadNetworkPortMirroring resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkloadNetworkPortMirroringArgs.__new__(WorkloadNetworkPortMirroringArgs)

        __props__.__dict__["destination"] = None
        __props__.__dict__["direction"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["revision"] = None
        __props__.__dict__["source"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["type"] = None
        return WorkloadNetworkPortMirroring(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def destination(self) -> pulumi.Output[Optional[str]]:
        """
        Destination VM Group.
        """
        return pulumi.get(self, "destination")

    @property
    @pulumi.getter
    def direction(self) -> pulumi.Output[Optional[str]]:
        """
        Direction of port mirroring profile.
        """
        return pulumi.get(self, "direction")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        Display name of the port mirroring profile.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def revision(self) -> pulumi.Output[Optional[float]]:
        """
        NSX revision number.
        """
        return pulumi.get(self, "revision")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional[str]]:
        """
        Source VM Group.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Port Mirroring Status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

