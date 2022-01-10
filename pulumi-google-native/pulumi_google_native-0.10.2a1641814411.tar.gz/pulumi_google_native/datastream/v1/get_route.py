# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetRouteResult',
    'AwaitableGetRouteResult',
    'get_route',
    'get_route_output',
]

@pulumi.output_type
class GetRouteResult:
    def __init__(__self__, create_time=None, destination_address=None, destination_port=None, display_name=None, labels=None, name=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if destination_address and not isinstance(destination_address, str):
            raise TypeError("Expected argument 'destination_address' to be a str")
        pulumi.set(__self__, "destination_address", destination_address)
        if destination_port and not isinstance(destination_port, int):
            raise TypeError("Expected argument 'destination_port' to be a int")
        pulumi.set(__self__, "destination_port", destination_port)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The create time of the resource.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="destinationAddress")
    def destination_address(self) -> str:
        """
        Destination address for connection
        """
        return pulumi.get(self, "destination_address")

    @property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> int:
        """
        Destination port for connection
        """
        return pulumi.get(self, "destination_port")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Display name.
        """
        return pulumi.get(self, "display_name")

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
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The update time of the resource.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetRouteResult(GetRouteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRouteResult(
            create_time=self.create_time,
            destination_address=self.destination_address,
            destination_port=self.destination_port,
            display_name=self.display_name,
            labels=self.labels,
            name=self.name,
            update_time=self.update_time)


def get_route(location: Optional[str] = None,
              private_connection_id: Optional[str] = None,
              project: Optional[str] = None,
              route_id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRouteResult:
    """
    Use this method to get details about a route.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['privateConnectionId'] = private_connection_id
    __args__['project'] = project
    __args__['routeId'] = route_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:datastream/v1:getRoute', __args__, opts=opts, typ=GetRouteResult).value

    return AwaitableGetRouteResult(
        create_time=__ret__.create_time,
        destination_address=__ret__.destination_address,
        destination_port=__ret__.destination_port,
        display_name=__ret__.display_name,
        labels=__ret__.labels,
        name=__ret__.name,
        update_time=__ret__.update_time)


@_utilities.lift_output_func(get_route)
def get_route_output(location: Optional[pulumi.Input[str]] = None,
                     private_connection_id: Optional[pulumi.Input[str]] = None,
                     project: Optional[pulumi.Input[Optional[str]]] = None,
                     route_id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRouteResult]:
    """
    Use this method to get details about a route.
    """
    ...
