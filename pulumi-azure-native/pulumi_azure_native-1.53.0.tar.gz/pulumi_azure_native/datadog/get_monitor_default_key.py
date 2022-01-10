# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetMonitorDefaultKeyResult',
    'AwaitableGetMonitorDefaultKeyResult',
    'get_monitor_default_key',
    'get_monitor_default_key_output',
]

@pulumi.output_type
class GetMonitorDefaultKeyResult:
    def __init__(__self__, created=None, created_by=None, key=None, name=None):
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if created_by and not isinstance(created_by, str):
            raise TypeError("Expected argument 'created_by' to be a str")
        pulumi.set(__self__, "created_by", created_by)
        if key and not isinstance(key, str):
            raise TypeError("Expected argument 'key' to be a str")
        pulumi.set(__self__, "key", key)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def created(self) -> Optional[str]:
        """
        The time of creation of the API key.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The user that created the API key.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The value of the API key.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the API key.
        """
        return pulumi.get(self, "name")


class AwaitableGetMonitorDefaultKeyResult(GetMonitorDefaultKeyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMonitorDefaultKeyResult(
            created=self.created,
            created_by=self.created_by,
            key=self.key,
            name=self.name)


def get_monitor_default_key(monitor_name: Optional[str] = None,
                            resource_group_name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMonitorDefaultKeyResult:
    """
    API Version: 2021-03-01.


    :param str monitor_name: Monitor resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['monitorName'] = monitor_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:datadog:getMonitorDefaultKey', __args__, opts=opts, typ=GetMonitorDefaultKeyResult).value

    return AwaitableGetMonitorDefaultKeyResult(
        created=__ret__.created,
        created_by=__ret__.created_by,
        key=__ret__.key,
        name=__ret__.name)


@_utilities.lift_output_func(get_monitor_default_key)
def get_monitor_default_key_output(monitor_name: Optional[pulumi.Input[str]] = None,
                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMonitorDefaultKeyResult]:
    """
    API Version: 2021-03-01.


    :param str monitor_name: Monitor resource name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
