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
    'GetPrivateConnectionResult',
    'AwaitableGetPrivateConnectionResult',
    'get_private_connection',
    'get_private_connection_output',
]

@pulumi.output_type
class GetPrivateConnectionResult:
    def __init__(__self__, create_time=None, display_name=None, error=None, labels=None, name=None, state=None, update_time=None, vpc_peering_config=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if error and not isinstance(error, dict):
            raise TypeError("Expected argument 'error' to be a dict")
        pulumi.set(__self__, "error", error)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)
        if vpc_peering_config and not isinstance(vpc_peering_config, dict):
            raise TypeError("Expected argument 'vpc_peering_config' to be a dict")
        pulumi.set(__self__, "vpc_peering_config", vpc_peering_config)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The create time of the resource.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def error(self) -> 'outputs.ErrorResponse':
        """
        In case of error, the details of the error in a user-friendly format.
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Labels.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource's name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of the Private Connection.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The update time of the resource.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter(name="vpcPeeringConfig")
    def vpc_peering_config(self) -> 'outputs.VpcPeeringConfigResponse':
        """
        VPC Peering Config
        """
        return pulumi.get(self, "vpc_peering_config")


class AwaitableGetPrivateConnectionResult(GetPrivateConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrivateConnectionResult(
            create_time=self.create_time,
            display_name=self.display_name,
            error=self.error,
            labels=self.labels,
            name=self.name,
            state=self.state,
            update_time=self.update_time,
            vpc_peering_config=self.vpc_peering_config)


def get_private_connection(location: Optional[str] = None,
                           private_connection_id: Optional[str] = None,
                           project: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrivateConnectionResult:
    """
    Use this method to get details about a private connectivity configuration.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['privateConnectionId'] = private_connection_id
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:datastream/v1alpha1:getPrivateConnection', __args__, opts=opts, typ=GetPrivateConnectionResult).value

    return AwaitableGetPrivateConnectionResult(
        create_time=__ret__.create_time,
        display_name=__ret__.display_name,
        error=__ret__.error,
        labels=__ret__.labels,
        name=__ret__.name,
        state=__ret__.state,
        update_time=__ret__.update_time,
        vpc_peering_config=__ret__.vpc_peering_config)


@_utilities.lift_output_func(get_private_connection)
def get_private_connection_output(location: Optional[pulumi.Input[str]] = None,
                                  private_connection_id: Optional[pulumi.Input[str]] = None,
                                  project: Optional[pulumi.Input[Optional[str]]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPrivateConnectionResult]:
    """
    Use this method to get details about a private connectivity configuration.
    """
    ...
