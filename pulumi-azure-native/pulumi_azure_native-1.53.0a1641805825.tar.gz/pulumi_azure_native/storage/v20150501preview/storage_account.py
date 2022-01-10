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

__all__ = ['StorageAccountArgs', 'StorageAccount']

@pulumi.input_type
class StorageAccountArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 account_name: Optional[pulumi.Input[str]] = None,
                 account_type: Optional[pulumi.Input['AccountType']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a StorageAccount resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.  
        :param pulumi.Input['AccountType'] account_type: Gets or sets the account type.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if account_name is not None:
            pulumi.set(__self__, "account_name", account_name)
        if account_type is not None:
            pulumi.set(__self__, "account_type", account_type)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="accountName")
    def account_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.  
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="accountType")
    def account_type(self) -> Optional[pulumi.Input['AccountType']]:
        """
        Gets or sets the account type.
        """
        return pulumi.get(self, "account_type")

    @account_type.setter
    def account_type(self, value: Optional[pulumi.Input['AccountType']]):
        pulumi.set(self, "account_type", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class StorageAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 account_type: Optional[pulumi.Input['AccountType']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The storage account.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.  
        :param pulumi.Input['AccountType'] account_type: Gets or sets the account type.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the user's subscription.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StorageAccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The storage account.

        :param str resource_name: The name of the resource.
        :param StorageAccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StorageAccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 account_type: Optional[pulumi.Input['AccountType']] = None,
                 location: Optional[pulumi.Input[str]] = None,
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
            __props__ = StorageAccountArgs.__new__(StorageAccountArgs)

            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["account_type"] = account_type
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["custom_domain"] = None
            __props__.__dict__["last_geo_failover_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["primary_endpoints"] = None
            __props__.__dict__["primary_location"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["secondary_endpoints"] = None
            __props__.__dict__["secondary_location"] = None
            __props__.__dict__["status_of_primary"] = None
            __props__.__dict__["status_of_secondary"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:storage:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20150615:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20160101:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20160501:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20161201:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20170601:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20171001:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20180201:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20180301preview:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20180701:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20181101:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20190401:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20190601:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20200801preview:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20210101:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20210201:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20210401:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20210601:StorageAccount"), pulumi.Alias(type_="azure-native:storage/v20210801:StorageAccount")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(StorageAccount, __self__).__init__(
            'azure-native:storage/v20150501preview:StorageAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StorageAccount':
        """
        Get an existing StorageAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StorageAccountArgs.__new__(StorageAccountArgs)

        __props__.__dict__["account_type"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["custom_domain"] = None
        __props__.__dict__["last_geo_failover_time"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["primary_endpoints"] = None
        __props__.__dict__["primary_location"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["secondary_endpoints"] = None
        __props__.__dict__["secondary_location"] = None
        __props__.__dict__["status_of_primary"] = None
        __props__.__dict__["status_of_secondary"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return StorageAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountType")
    def account_type(self) -> pulumi.Output[Optional[str]]:
        """
        Gets the type of the storage account.
        """
        return pulumi.get(self, "account_type")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[Optional[str]]:
        """
        Gets the creation date and time of the storage account in UTC.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="customDomain")
    def custom_domain(self) -> pulumi.Output[Optional['outputs.CustomDomainResponse']]:
        """
        Gets the user assigned custom domain assigned to this storage account.
        """
        return pulumi.get(self, "custom_domain")

    @property
    @pulumi.getter(name="lastGeoFailoverTime")
    def last_geo_failover_time(self) -> pulumi.Output[Optional[str]]:
        """
        Gets the timestamp of the most recent instance of a failover to the secondary location. Only the most recent timestamp is retained. This element is not returned if there has never been a failover instance. Only available if the accountType is StandardGRS or StandardRAGRS.
        """
        return pulumi.get(self, "last_geo_failover_time")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="primaryEndpoints")
    def primary_endpoints(self) -> pulumi.Output[Optional['outputs.EndpointsResponse']]:
        """
        Gets the URLs that are used to perform a retrieval of a public blob, queue or table object.Note that StandardZRS and PremiumLRS accounts only return the blob endpoint.
        """
        return pulumi.get(self, "primary_endpoints")

    @property
    @pulumi.getter(name="primaryLocation")
    def primary_location(self) -> pulumi.Output[Optional[str]]:
        """
        Gets the location of the primary for the storage account.
        """
        return pulumi.get(self, "primary_location")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        Gets the status of the storage account at the time the operation was called.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="secondaryEndpoints")
    def secondary_endpoints(self) -> pulumi.Output[Optional['outputs.EndpointsResponse']]:
        """
        Gets the URLs that are used to perform a retrieval of a public blob, queue or table object from the secondary location of the storage account. Only available if the accountType is StandardRAGRS.
        """
        return pulumi.get(self, "secondary_endpoints")

    @property
    @pulumi.getter(name="secondaryLocation")
    def secondary_location(self) -> pulumi.Output[Optional[str]]:
        """
        Gets the location of the geo replicated secondary for the storage account. Only available if the accountType is StandardGRS or StandardRAGRS.
        """
        return pulumi.get(self, "secondary_location")

    @property
    @pulumi.getter(name="statusOfPrimary")
    def status_of_primary(self) -> pulumi.Output[Optional[str]]:
        """
        Gets the status indicating whether the primary location of the storage account is available or unavailable.
        """
        return pulumi.get(self, "status_of_primary")

    @property
    @pulumi.getter(name="statusOfSecondary")
    def status_of_secondary(self) -> pulumi.Output[Optional[str]]:
        """
        Gets the status indicating whether the secondary location of the storage account is available or unavailable. Only available if the accountType is StandardGRS or StandardRAGRS.
        """
        return pulumi.get(self, "status_of_secondary")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

