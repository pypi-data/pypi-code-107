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

__all__ = ['DatastoreArgs', 'Datastore']

@pulumi.input_type
class DatastoreArgs:
    def __init__(__self__, *,
                 cluster_name: pulumi.Input[str],
                 private_cloud_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 datastore_name: Optional[pulumi.Input[str]] = None,
                 disk_pool_volume: Optional[pulumi.Input['DiskPoolVolumeArgs']] = None,
                 net_app_volume: Optional[pulumi.Input['NetAppVolumeArgs']] = None):
        """
        The set of arguments for constructing a Datastore resource.
        :param pulumi.Input[str] cluster_name: Name of the cluster in the private cloud
        :param pulumi.Input[str] private_cloud_name: Name of the private cloud
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] datastore_name: Name of the datastore in the private cloud cluster
        :param pulumi.Input['DiskPoolVolumeArgs'] disk_pool_volume: An iSCSI volume
        :param pulumi.Input['NetAppVolumeArgs'] net_app_volume: An Azure NetApp Files volume
        """
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "private_cloud_name", private_cloud_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if datastore_name is not None:
            pulumi.set(__self__, "datastore_name", datastore_name)
        if disk_pool_volume is not None:
            pulumi.set(__self__, "disk_pool_volume", disk_pool_volume)
        if net_app_volume is not None:
            pulumi.set(__self__, "net_app_volume", net_app_volume)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        Name of the cluster in the private cloud
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

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
    @pulumi.getter(name="datastoreName")
    def datastore_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the datastore in the private cloud cluster
        """
        return pulumi.get(self, "datastore_name")

    @datastore_name.setter
    def datastore_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datastore_name", value)

    @property
    @pulumi.getter(name="diskPoolVolume")
    def disk_pool_volume(self) -> Optional[pulumi.Input['DiskPoolVolumeArgs']]:
        """
        An iSCSI volume
        """
        return pulumi.get(self, "disk_pool_volume")

    @disk_pool_volume.setter
    def disk_pool_volume(self, value: Optional[pulumi.Input['DiskPoolVolumeArgs']]):
        pulumi.set(self, "disk_pool_volume", value)

    @property
    @pulumi.getter(name="netAppVolume")
    def net_app_volume(self) -> Optional[pulumi.Input['NetAppVolumeArgs']]:
        """
        An Azure NetApp Files volume
        """
        return pulumi.get(self, "net_app_volume")

    @net_app_volume.setter
    def net_app_volume(self, value: Optional[pulumi.Input['NetAppVolumeArgs']]):
        pulumi.set(self, "net_app_volume", value)


class Datastore(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 datastore_name: Optional[pulumi.Input[str]] = None,
                 disk_pool_volume: Optional[pulumi.Input[pulumi.InputType['DiskPoolVolumeArgs']]] = None,
                 net_app_volume: Optional[pulumi.Input[pulumi.InputType['NetAppVolumeArgs']]] = None,
                 private_cloud_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A datastore resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: Name of the cluster in the private cloud
        :param pulumi.Input[str] datastore_name: Name of the datastore in the private cloud cluster
        :param pulumi.Input[pulumi.InputType['DiskPoolVolumeArgs']] disk_pool_volume: An iSCSI volume
        :param pulumi.Input[pulumi.InputType['NetAppVolumeArgs']] net_app_volume: An Azure NetApp Files volume
        :param pulumi.Input[str] private_cloud_name: Name of the private cloud
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DatastoreArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A datastore resource

        :param str resource_name: The name of the resource.
        :param DatastoreArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DatastoreArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 datastore_name: Optional[pulumi.Input[str]] = None,
                 disk_pool_volume: Optional[pulumi.Input[pulumi.InputType['DiskPoolVolumeArgs']]] = None,
                 net_app_volume: Optional[pulumi.Input[pulumi.InputType['NetAppVolumeArgs']]] = None,
                 private_cloud_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = DatastoreArgs.__new__(DatastoreArgs)

            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["datastore_name"] = datastore_name
            __props__.__dict__["disk_pool_volume"] = disk_pool_volume
            __props__.__dict__["net_app_volume"] = net_app_volume
            if private_cloud_name is None and not opts.urn:
                raise TypeError("Missing required property 'private_cloud_name'")
            __props__.__dict__["private_cloud_name"] = private_cloud_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:avs:Datastore"), pulumi.Alias(type_="azure-native:avs/v20210101preview:Datastore"), pulumi.Alias(type_="azure-native:avs/v20211201:Datastore")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Datastore, __self__).__init__(
            'azure-native:avs/v20210601:Datastore',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Datastore':
        """
        Get an existing Datastore resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DatastoreArgs.__new__(DatastoreArgs)

        __props__.__dict__["disk_pool_volume"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["net_app_volume"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return Datastore(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="diskPoolVolume")
    def disk_pool_volume(self) -> pulumi.Output[Optional['outputs.DiskPoolVolumeResponse']]:
        """
        An iSCSI volume
        """
        return pulumi.get(self, "disk_pool_volume")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="netAppVolume")
    def net_app_volume(self) -> pulumi.Output[Optional['outputs.NetAppVolumeResponse']]:
        """
        An Azure NetApp Files volume
        """
        return pulumi.get(self, "net_app_volume")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The state of the datastore provisioning
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

