# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetPublicDelegatedPrefixResult',
    'AwaitableGetPublicDelegatedPrefixResult',
    'get_public_delegated_prefix',
    'get_public_delegated_prefix_output',
]

@pulumi.output_type
class GetPublicDelegatedPrefixResult:
    def __init__(__self__, creation_timestamp=None, description=None, fingerprint=None, ip_cidr_range=None, is_live_migration=None, kind=None, name=None, parent_prefix=None, public_delegated_sub_prefixs=None, region=None, self_link=None, status=None):
        if creation_timestamp and not isinstance(creation_timestamp, str):
            raise TypeError("Expected argument 'creation_timestamp' to be a str")
        pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if fingerprint and not isinstance(fingerprint, str):
            raise TypeError("Expected argument 'fingerprint' to be a str")
        pulumi.set(__self__, "fingerprint", fingerprint)
        if ip_cidr_range and not isinstance(ip_cidr_range, str):
            raise TypeError("Expected argument 'ip_cidr_range' to be a str")
        pulumi.set(__self__, "ip_cidr_range", ip_cidr_range)
        if is_live_migration and not isinstance(is_live_migration, bool):
            raise TypeError("Expected argument 'is_live_migration' to be a bool")
        pulumi.set(__self__, "is_live_migration", is_live_migration)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parent_prefix and not isinstance(parent_prefix, str):
            raise TypeError("Expected argument 'parent_prefix' to be a str")
        pulumi.set(__self__, "parent_prefix", parent_prefix)
        if public_delegated_sub_prefixs and not isinstance(public_delegated_sub_prefixs, list):
            raise TypeError("Expected argument 'public_delegated_sub_prefixs' to be a list")
        pulumi.set(__self__, "public_delegated_sub_prefixs", public_delegated_sub_prefixs)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> str:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        An optional description of this resource. Provide this property when you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def fingerprint(self) -> str:
        """
        Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a new PublicDelegatedPrefix. An up-to-date fingerprint must be provided in order to update the PublicDelegatedPrefix, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a PublicDelegatedPrefix.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter(name="ipCidrRange")
    def ip_cidr_range(self) -> str:
        """
        The IPv4 address range, in CIDR format, represented by this public delegated prefix.
        """
        return pulumi.get(self, "ip_cidr_range")

    @property
    @pulumi.getter(name="isLiveMigration")
    def is_live_migration(self) -> bool:
        """
        If true, the prefix will be live migrated.
        """
        return pulumi.get(self, "is_live_migration")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Type of the resource. Always compute#publicDelegatedPrefix for public delegated prefixes.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parentPrefix")
    def parent_prefix(self) -> str:
        """
        The URL of parent prefix. Either PublicAdvertisedPrefix or PublicDelegatedPrefix.
        """
        return pulumi.get(self, "parent_prefix")

    @property
    @pulumi.getter(name="publicDelegatedSubPrefixs")
    def public_delegated_sub_prefixs(self) -> Sequence['outputs.PublicDelegatedPrefixPublicDelegatedSubPrefixResponse']:
        """
        The list of sub public delegated prefixes that exist for this public delegated prefix.
        """
        return pulumi.get(self, "public_delegated_sub_prefixs")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        URL of the region where the public delegated prefix resides. This field applies only to the region resource. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the public delegated prefix, which can be one of following values: - `INITIALIZING` The public delegated prefix is being initialized and addresses cannot be created yet. - `READY_TO_ANNOUNCE` The public delegated prefix is a live migration prefix and is active. - `ANNOUNCED` The public delegated prefix is active. - `DELETING` The public delegated prefix is being deprovsioned. 
        """
        return pulumi.get(self, "status")


class AwaitableGetPublicDelegatedPrefixResult(GetPublicDelegatedPrefixResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPublicDelegatedPrefixResult(
            creation_timestamp=self.creation_timestamp,
            description=self.description,
            fingerprint=self.fingerprint,
            ip_cidr_range=self.ip_cidr_range,
            is_live_migration=self.is_live_migration,
            kind=self.kind,
            name=self.name,
            parent_prefix=self.parent_prefix,
            public_delegated_sub_prefixs=self.public_delegated_sub_prefixs,
            region=self.region,
            self_link=self.self_link,
            status=self.status)


def get_public_delegated_prefix(project: Optional[str] = None,
                                public_delegated_prefix: Optional[str] = None,
                                region: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPublicDelegatedPrefixResult:
    """
    Returns the specified PublicDelegatedPrefix resource in the given region.
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['publicDelegatedPrefix'] = public_delegated_prefix
    __args__['region'] = region
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:compute/v1:getPublicDelegatedPrefix', __args__, opts=opts, typ=GetPublicDelegatedPrefixResult).value

    return AwaitableGetPublicDelegatedPrefixResult(
        creation_timestamp=__ret__.creation_timestamp,
        description=__ret__.description,
        fingerprint=__ret__.fingerprint,
        ip_cidr_range=__ret__.ip_cidr_range,
        is_live_migration=__ret__.is_live_migration,
        kind=__ret__.kind,
        name=__ret__.name,
        parent_prefix=__ret__.parent_prefix,
        public_delegated_sub_prefixs=__ret__.public_delegated_sub_prefixs,
        region=__ret__.region,
        self_link=__ret__.self_link,
        status=__ret__.status)


@_utilities.lift_output_func(get_public_delegated_prefix)
def get_public_delegated_prefix_output(project: Optional[pulumi.Input[Optional[str]]] = None,
                                       public_delegated_prefix: Optional[pulumi.Input[str]] = None,
                                       region: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPublicDelegatedPrefixResult]:
    """
    Returns the specified PublicDelegatedPrefix resource in the given region.
    """
    ...
