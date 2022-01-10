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

__all__ = ['SpatialAnchorsAccountArgs', 'SpatialAnchorsAccount']

@pulumi.input_type
class SpatialAnchorsAccountArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 account_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['IdentityArgs']] = None,
                 kind: Optional[pulumi.Input['SkuArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input['IdentityArgs']] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a SpatialAnchorsAccount resource.
        :param pulumi.Input[str] resource_group_name: Name of an Azure resource group.
        :param pulumi.Input[str] account_name: Name of an Mixed Reality Account.
        :param pulumi.Input['IdentityArgs'] identity: The identity associated with this account
        :param pulumi.Input['SkuArgs'] kind: The kind of account, if supported
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['IdentityArgs'] plan: The plan associated with this account
        :param pulumi.Input['SkuArgs'] sku: The sku associated with this account
        :param pulumi.Input[str] storage_account_name: The name of the storage account associated with this accountId
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if account_name is not None:
            pulumi.set(__self__, "account_name", account_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if plan is not None:
            pulumi.set(__self__, "plan", plan)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if storage_account_name is not None:
            pulumi.set(__self__, "storage_account_name", storage_account_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of an Azure resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of an Mixed Reality Account.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['IdentityArgs']]:
        """
        The identity associated with this account
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['IdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input['SkuArgs']]:
        """
        The kind of account, if supported
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input['SkuArgs']]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input['IdentityArgs']]:
        """
        The plan associated with this account
        """
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: Optional[pulumi.Input['IdentityArgs']]):
        pulumi.set(self, "plan", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuArgs']]:
        """
        The sku associated with this account
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the storage account associated with this accountId
        """
        return pulumi.get(self, "storage_account_name")

    @storage_account_name.setter
    def storage_account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_account_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class SpatialAnchorsAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 kind: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        SpatialAnchorsAccount Response.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: Name of an Mixed Reality Account.
        :param pulumi.Input[pulumi.InputType['IdentityArgs']] identity: The identity associated with this account
        :param pulumi.Input[pulumi.InputType['SkuArgs']] kind: The kind of account, if supported
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[pulumi.InputType['IdentityArgs']] plan: The plan associated with this account
        :param pulumi.Input[str] resource_group_name: Name of an Azure resource group.
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: The sku associated with this account
        :param pulumi.Input[str] storage_account_name: The name of the storage account associated with this accountId
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SpatialAnchorsAccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        SpatialAnchorsAccount Response.

        :param str resource_name: The name of the resource.
        :param SpatialAnchorsAccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SpatialAnchorsAccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 kind: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = SpatialAnchorsAccountArgs.__new__(SpatialAnchorsAccountArgs)

            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["identity"] = identity
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            __props__.__dict__["plan"] = plan
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["storage_account_name"] = storage_account_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["account_domain"] = None
            __props__.__dict__["account_id"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:mixedreality:SpatialAnchorsAccount"), pulumi.Alias(type_="azure-native:mixedreality/v20190228preview:SpatialAnchorsAccount"), pulumi.Alias(type_="azure-native:mixedreality/v20191202preview:SpatialAnchorsAccount"), pulumi.Alias(type_="azure-native:mixedreality/v20200501:SpatialAnchorsAccount"), pulumi.Alias(type_="azure-native:mixedreality/v20210101:SpatialAnchorsAccount")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SpatialAnchorsAccount, __self__).__init__(
            'azure-native:mixedreality/v20210301preview:SpatialAnchorsAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SpatialAnchorsAccount':
        """
        Get an existing SpatialAnchorsAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SpatialAnchorsAccountArgs.__new__(SpatialAnchorsAccountArgs)

        __props__.__dict__["account_domain"] = None
        __props__.__dict__["account_id"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["plan"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["storage_account_name"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return SpatialAnchorsAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountDomain")
    def account_domain(self) -> pulumi.Output[str]:
        """
        Correspond domain name of certain Spatial Anchors Account
        """
        return pulumi.get(self, "account_domain")

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        unique id of certain account.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityResponse']]:
        """
        The identity associated with this account
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        The kind of account, if supported
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def plan(self) -> pulumi.Output[Optional['outputs.IdentityResponse']]:
        """
        The plan associated with this account
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        The sku associated with this account
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the storage account associated with this accountId
        """
        return pulumi.get(self, "storage_account_name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        System metadata for this account
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

