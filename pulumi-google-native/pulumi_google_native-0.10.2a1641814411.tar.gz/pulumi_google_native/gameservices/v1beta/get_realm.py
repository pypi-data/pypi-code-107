# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetRealmResult',
    'AwaitableGetRealmResult',
    'get_realm',
    'get_realm_output',
]

@pulumi.output_type
class GetRealmResult:
    def __init__(__self__, create_time=None, description=None, etag=None, labels=None, name=None, time_zone=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if time_zone and not isinstance(time_zone, str):
            raise TypeError("Expected argument 'time_zone' to be a str")
        pulumi.set(__self__, "time_zone", time_zone)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The creation time.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Human readable description of the realm.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        ETag of the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        The labels associated with this realm. Each label is a key-value pair.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the realm, in the following form: `projects/{project}/locations/{location}/realms/{realm}`. For example, `projects/my-project/locations/{location}/realms/my-realm`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> str:
        """
        Time zone where all policies targeting this realm are evaluated. The value of this field must be from the IANA time zone database: https://www.iana.org/time-zones.
        """
        return pulumi.get(self, "time_zone")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The last-modified time.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetRealmResult(GetRealmResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRealmResult(
            create_time=self.create_time,
            description=self.description,
            etag=self.etag,
            labels=self.labels,
            name=self.name,
            time_zone=self.time_zone,
            update_time=self.update_time)


def get_realm(location: Optional[str] = None,
              project: Optional[str] = None,
              realm_id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRealmResult:
    """
    Gets details of a single realm.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['project'] = project
    __args__['realmId'] = realm_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:gameservices/v1beta:getRealm', __args__, opts=opts, typ=GetRealmResult).value

    return AwaitableGetRealmResult(
        create_time=__ret__.create_time,
        description=__ret__.description,
        etag=__ret__.etag,
        labels=__ret__.labels,
        name=__ret__.name,
        time_zone=__ret__.time_zone,
        update_time=__ret__.update_time)


@_utilities.lift_output_func(get_realm)
def get_realm_output(location: Optional[pulumi.Input[str]] = None,
                     project: Optional[pulumi.Input[Optional[str]]] = None,
                     realm_id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRealmResult]:
    """
    Gets details of a single realm.
    """
    ...
