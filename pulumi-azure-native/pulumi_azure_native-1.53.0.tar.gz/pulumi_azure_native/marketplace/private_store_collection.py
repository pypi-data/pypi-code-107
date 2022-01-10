# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = ['PrivateStoreCollectionArgs', 'PrivateStoreCollection']

@pulumi.input_type
class PrivateStoreCollectionArgs:
    def __init__(__self__, *,
                 private_store_id: pulumi.Input[str],
                 all_subscriptions: Optional[pulumi.Input[bool]] = None,
                 claim: Optional[pulumi.Input[str]] = None,
                 collection_id: Optional[pulumi.Input[str]] = None,
                 collection_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 subscriptions_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a PrivateStoreCollection resource.
        :param pulumi.Input[str] private_store_id: The store ID - must use the tenant ID
        :param pulumi.Input[bool] all_subscriptions: Indicating whether all subscriptions are selected (=true) or not (=false).
        :param pulumi.Input[str] claim: Gets or sets the association with Commercial's Billing Account.
        :param pulumi.Input[str] collection_id: The collection ID
        :param pulumi.Input[str] collection_name: Gets or sets collection name.
        :param pulumi.Input[bool] enabled: Indicating whether the collection is enabled or disabled.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subscriptions_list: Gets or sets subscription ids list. Empty list indicates all subscriptions are selected, null indicates no update is done, explicit list indicates the explicit selected subscriptions. On insert, null is considered as bad request
        """
        pulumi.set(__self__, "private_store_id", private_store_id)
        if all_subscriptions is not None:
            pulumi.set(__self__, "all_subscriptions", all_subscriptions)
        if claim is not None:
            pulumi.set(__self__, "claim", claim)
        if collection_id is not None:
            pulumi.set(__self__, "collection_id", collection_id)
        if collection_name is not None:
            pulumi.set(__self__, "collection_name", collection_name)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if subscriptions_list is not None:
            pulumi.set(__self__, "subscriptions_list", subscriptions_list)

    @property
    @pulumi.getter(name="privateStoreId")
    def private_store_id(self) -> pulumi.Input[str]:
        """
        The store ID - must use the tenant ID
        """
        return pulumi.get(self, "private_store_id")

    @private_store_id.setter
    def private_store_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "private_store_id", value)

    @property
    @pulumi.getter(name="allSubscriptions")
    def all_subscriptions(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicating whether all subscriptions are selected (=true) or not (=false).
        """
        return pulumi.get(self, "all_subscriptions")

    @all_subscriptions.setter
    def all_subscriptions(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "all_subscriptions", value)

    @property
    @pulumi.getter
    def claim(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the association with Commercial's Billing Account.
        """
        return pulumi.get(self, "claim")

    @claim.setter
    def claim(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "claim", value)

    @property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> Optional[pulumi.Input[str]]:
        """
        The collection ID
        """
        return pulumi.get(self, "collection_id")

    @collection_id.setter
    def collection_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "collection_id", value)

    @property
    @pulumi.getter(name="collectionName")
    def collection_name(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets collection name.
        """
        return pulumi.get(self, "collection_name")

    @collection_name.setter
    def collection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "collection_name", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicating whether the collection is enabled or disabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="subscriptionsList")
    def subscriptions_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Gets or sets subscription ids list. Empty list indicates all subscriptions are selected, null indicates no update is done, explicit list indicates the explicit selected subscriptions. On insert, null is considered as bad request
        """
        return pulumi.get(self, "subscriptions_list")

    @subscriptions_list.setter
    def subscriptions_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "subscriptions_list", value)


class PrivateStoreCollection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 all_subscriptions: Optional[pulumi.Input[bool]] = None,
                 claim: Optional[pulumi.Input[str]] = None,
                 collection_id: Optional[pulumi.Input[str]] = None,
                 collection_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 private_store_id: Optional[pulumi.Input[str]] = None,
                 subscriptions_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The Collection data structure.
        API Version: 2021-06-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] all_subscriptions: Indicating whether all subscriptions are selected (=true) or not (=false).
        :param pulumi.Input[str] claim: Gets or sets the association with Commercial's Billing Account.
        :param pulumi.Input[str] collection_id: The collection ID
        :param pulumi.Input[str] collection_name: Gets or sets collection name.
        :param pulumi.Input[bool] enabled: Indicating whether the collection is enabled or disabled.
        :param pulumi.Input[str] private_store_id: The store ID - must use the tenant ID
        :param pulumi.Input[Sequence[pulumi.Input[str]]] subscriptions_list: Gets or sets subscription ids list. Empty list indicates all subscriptions are selected, null indicates no update is done, explicit list indicates the explicit selected subscriptions. On insert, null is considered as bad request
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PrivateStoreCollectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Collection data structure.
        API Version: 2021-06-01.

        :param str resource_name: The name of the resource.
        :param PrivateStoreCollectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PrivateStoreCollectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 all_subscriptions: Optional[pulumi.Input[bool]] = None,
                 claim: Optional[pulumi.Input[str]] = None,
                 collection_id: Optional[pulumi.Input[str]] = None,
                 collection_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 private_store_id: Optional[pulumi.Input[str]] = None,
                 subscriptions_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            __props__ = PrivateStoreCollectionArgs.__new__(PrivateStoreCollectionArgs)

            __props__.__dict__["all_subscriptions"] = all_subscriptions
            __props__.__dict__["claim"] = claim
            __props__.__dict__["collection_id"] = collection_id
            __props__.__dict__["collection_name"] = collection_name
            __props__.__dict__["enabled"] = enabled
            if private_store_id is None and not opts.urn:
                raise TypeError("Missing required property 'private_store_id'")
            __props__.__dict__["private_store_id"] = private_store_id
            __props__.__dict__["subscriptions_list"] = subscriptions_list
            __props__.__dict__["name"] = None
            __props__.__dict__["number_of_offers"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:marketplace/v20210601:PrivateStoreCollection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(PrivateStoreCollection, __self__).__init__(
            'azure-native:marketplace:PrivateStoreCollection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PrivateStoreCollection':
        """
        Get an existing PrivateStoreCollection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PrivateStoreCollectionArgs.__new__(PrivateStoreCollectionArgs)

        __props__.__dict__["all_subscriptions"] = None
        __props__.__dict__["claim"] = None
        __props__.__dict__["collection_id"] = None
        __props__.__dict__["collection_name"] = None
        __props__.__dict__["enabled"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["number_of_offers"] = None
        __props__.__dict__["subscriptions_list"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return PrivateStoreCollection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allSubscriptions")
    def all_subscriptions(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicating whether all subscriptions are selected (=true) or not (=false).
        """
        return pulumi.get(self, "all_subscriptions")

    @property
    @pulumi.getter
    def claim(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the association with Commercial's Billing Account.
        """
        return pulumi.get(self, "claim")

    @property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> pulumi.Output[str]:
        """
        Gets collection Id.
        """
        return pulumi.get(self, "collection_id")

    @property
    @pulumi.getter(name="collectionName")
    def collection_name(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets collection name.
        """
        return pulumi.get(self, "collection_name")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicating whether the collection is enabled or disabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="numberOfOffers")
    def number_of_offers(self) -> pulumi.Output[float]:
        """
        Gets the number of offers associated with the collection.
        """
        return pulumi.get(self, "number_of_offers")

    @property
    @pulumi.getter(name="subscriptionsList")
    def subscriptions_list(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Gets or sets subscription ids list. Empty list indicates all subscriptions are selected, null indicates no update is done, explicit list indicates the explicit selected subscriptions. On insert, null is considered as bad request
        """
        return pulumi.get(self, "subscriptions_list")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Metadata pertaining to creation and last modification of the resource
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

