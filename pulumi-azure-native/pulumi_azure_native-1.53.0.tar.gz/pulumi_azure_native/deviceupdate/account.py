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

__all__ = ['AccountArgs', 'Account']

@pulumi.input_type
class AccountArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 account_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['ManagedServiceIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 private_endpoint_connections: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateEndpointConnectionArgs']]]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Account resource.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] account_name: Account name.
        :param pulumi.Input['ManagedServiceIdentityArgs'] identity: The type of identity used for the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Sequence[pulumi.Input['PrivateEndpointConnectionArgs']]] private_endpoint_connections: List of private endpoint connections associated with the account.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: Whether or not public network access is allowed for the account.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if account_name is not None:
            pulumi.set(__self__, "account_name", account_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if private_endpoint_connections is not None:
            pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if public_network_access is None:
            public_network_access = 'Enabled'
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[str]]:
        """
        Account name.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ManagedServiceIdentityArgs']]:
        """
        The type of identity used for the resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ManagedServiceIdentityArgs']]):
        pulumi.set(self, "identity", value)

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
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PrivateEndpointConnectionArgs']]]]:
        """
        List of private endpoint connections associated with the account.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @private_endpoint_connections.setter
    def private_endpoint_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PrivateEndpointConnectionArgs']]]]):
        pulumi.set(self, "private_endpoint_connections", value)

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]:
        """
        Whether or not public network access is allowed for the account.
        """
        return pulumi.get(self, "public_network_access")

    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]]):
        pulumi.set(self, "public_network_access", value)

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


class Account(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 private_endpoint_connections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivateEndpointConnectionArgs']]]]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Device Update account details.
        API Version: 2020-03-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: Account name.
        :param pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']] identity: The type of identity used for the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivateEndpointConnectionArgs']]]] private_endpoint_connections: List of private endpoint connections associated with the account.
        :param pulumi.Input[Union[str, 'PublicNetworkAccess']] public_network_access: Whether or not public network access is allowed for the account.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Device Update account details.
        API Version: 2020-03-01-preview.

        :param str resource_name: The name of the resource.
        :param AccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 private_endpoint_connections: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PrivateEndpointConnectionArgs']]]]] = None,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccess']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = AccountArgs.__new__(AccountArgs)

            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["private_endpoint_connections"] = private_endpoint_connections
            if public_network_access is None:
                public_network_access = 'Enabled'
            __props__.__dict__["public_network_access"] = public_network_access
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["host_name"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:deviceupdate/v20200301preview:Account")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Account, __self__).__init__(
            'azure-native:deviceupdate:Account',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Account':
        """
        Get an existing Account resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AccountArgs.__new__(AccountArgs)

        __props__.__dict__["host_name"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_endpoint_connections"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_network_access"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Account(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Output[str]:
        """
        API host name.
        """
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ManagedServiceIdentityResponse']]:
        """
        The type of identity used for the resource.
        """
        return pulumi.get(self, "identity")

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
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> pulumi.Output[Optional[Sequence['outputs.PrivateEndpointConnectionResponse']]]:
        """
        List of private endpoint connections associated with the account.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> pulumi.Output[Optional[str]]:
        """
        Whether or not public network access is allowed for the account.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
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

