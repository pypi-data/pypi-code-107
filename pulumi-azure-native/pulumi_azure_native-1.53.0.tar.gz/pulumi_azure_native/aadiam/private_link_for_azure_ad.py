# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['PrivateLinkForAzureAdArgs', 'PrivateLinkForAzureAd']

@pulumi.input_type
class PrivateLinkForAzureAdArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 all_tenants: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner_tenant_id: Optional[pulumi.Input[str]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 resource_group: Optional[pulumi.Input[str]] = None,
                 resource_name: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tenants: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a PrivateLinkForAzureAd resource.
        :param pulumi.Input[str] resource_group_name: Name of an Azure resource group.
        :param pulumi.Input[bool] all_tenants: Flag indicating whether all tenants are allowed
        :param pulumi.Input[str] name: Name of this resource.
        :param pulumi.Input[str] owner_tenant_id: Guid of the owner tenant
        :param pulumi.Input[str] policy_name: The name of the private link policy in Azure AD.
        :param pulumi.Input[str] resource_group: Name of the resource group
        :param pulumi.Input[str] resource_name: Name of the private link policy resource
        :param pulumi.Input[str] subscription_id: Subscription Identifier
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tenants: The list of tenantIds.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if all_tenants is not None:
            pulumi.set(__self__, "all_tenants", all_tenants)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if owner_tenant_id is not None:
            pulumi.set(__self__, "owner_tenant_id", owner_tenant_id)
        if policy_name is not None:
            pulumi.set(__self__, "policy_name", policy_name)
        if resource_group is not None:
            pulumi.set(__self__, "resource_group", resource_group)
        if resource_name is not None:
            pulumi.set(__self__, "resource_name", resource_name)
        if subscription_id is not None:
            pulumi.set(__self__, "subscription_id", subscription_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if tenants is not None:
            pulumi.set(__self__, "tenants", tenants)

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
    @pulumi.getter(name="allTenants")
    def all_tenants(self) -> Optional[pulumi.Input[bool]]:
        """
        Flag indicating whether all tenants are allowed
        """
        return pulumi.get(self, "all_tenants")

    @all_tenants.setter
    def all_tenants(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "all_tenants", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of this resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="ownerTenantId")
    def owner_tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        Guid of the owner tenant
        """
        return pulumi.get(self, "owner_tenant_id")

    @owner_tenant_id.setter
    def owner_tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner_tenant_id", value)

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the private link policy in Azure AD.
        """
        return pulumi.get(self, "policy_name")

    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_name", value)

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the resource group
        """
        return pulumi.get(self, "resource_group")

    @resource_group.setter
    def resource_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the private link policy resource
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        Subscription Identifier
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_id", value)

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

    @property
    @pulumi.getter
    def tenants(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of tenantIds.
        """
        return pulumi.get(self, "tenants")

    @tenants.setter
    def tenants(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tenants", value)


class PrivateLinkForAzureAd(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 all_tenants: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner_tenant_id: Optional[pulumi.Input[str]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 resource_group: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tenants: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        PrivateLink Policy configuration object.
        API Version: 2020-03-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] all_tenants: Flag indicating whether all tenants are allowed
        :param pulumi.Input[str] name: Name of this resource.
        :param pulumi.Input[str] owner_tenant_id: Guid of the owner tenant
        :param pulumi.Input[str] policy_name: The name of the private link policy in Azure AD.
        :param pulumi.Input[str] resource_group: Name of the resource group
        :param pulumi.Input[str] resource_group_name: Name of an Azure resource group.
        :param pulumi.Input[str] resource_name_: Name of the private link policy resource
        :param pulumi.Input[str] subscription_id: Subscription Identifier
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tenants: The list of tenantIds.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PrivateLinkForAzureAdArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        PrivateLink Policy configuration object.
        API Version: 2020-03-01.

        :param str resource_name: The name of the resource.
        :param PrivateLinkForAzureAdArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrivateLinkForAzureAdArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 all_tenants: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner_tenant_id: Optional[pulumi.Input[str]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 resource_group: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tenants: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            __props__ = PrivateLinkForAzureAdArgs.__new__(PrivateLinkForAzureAdArgs)

            __props__.__dict__["all_tenants"] = all_tenants
            __props__.__dict__["name"] = name
            __props__.__dict__["owner_tenant_id"] = owner_tenant_id
            __props__.__dict__["policy_name"] = policy_name
            __props__.__dict__["resource_group"] = resource_group
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["subscription_id"] = subscription_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["tenants"] = tenants
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:aadiam/v20200301:privateLinkForAzureAd"), pulumi.Alias(type_="azure-native:aadiam/v20200301preview:privateLinkForAzureAd")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PrivateLinkForAzureAd, __self__).__init__(
            'azure-native:aadiam:privateLinkForAzureAd',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PrivateLinkForAzureAd':
        """
        Get an existing PrivateLinkForAzureAd resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PrivateLinkForAzureAdArgs.__new__(PrivateLinkForAzureAdArgs)

        __props__.__dict__["all_tenants"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["owner_tenant_id"] = None
        __props__.__dict__["resource_group"] = None
        __props__.__dict__["resource_name"] = None
        __props__.__dict__["subscription_id"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["tenants"] = None
        __props__.__dict__["type"] = None
        return PrivateLinkForAzureAd(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allTenants")
    def all_tenants(self) -> pulumi.Output[Optional[bool]]:
        """
        Flag indicating whether all tenants are allowed
        """
        return pulumi.get(self, "all_tenants")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of this resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ownerTenantId")
    def owner_tenant_id(self) -> pulumi.Output[Optional[str]]:
        """
        Guid of the owner tenant
        """
        return pulumi.get(self, "owner_tenant_id")

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the resource group
        """
        return pulumi.get(self, "resource_group")

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the private link policy resource
        """
        return pulumi.get(self, "resource_name")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> pulumi.Output[Optional[str]]:
        """
        Subscription Identifier
        """
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def tenants(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of tenantIds.
        """
        return pulumi.get(self, "tenants")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of this resource.
        """
        return pulumi.get(self, "type")

