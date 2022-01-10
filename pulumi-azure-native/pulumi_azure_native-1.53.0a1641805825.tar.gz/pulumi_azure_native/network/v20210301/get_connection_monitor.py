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
    'GetConnectionMonitorResult',
    'AwaitableGetConnectionMonitorResult',
    'get_connection_monitor',
    'get_connection_monitor_output',
]

@pulumi.output_type
class GetConnectionMonitorResult:
    """
    Information about the connection monitor.
    """
    def __init__(__self__, auto_start=None, connection_monitor_type=None, destination=None, endpoints=None, etag=None, id=None, location=None, monitoring_interval_in_seconds=None, monitoring_status=None, name=None, notes=None, outputs=None, provisioning_state=None, source=None, start_time=None, tags=None, test_configurations=None, test_groups=None, type=None):
        if auto_start and not isinstance(auto_start, bool):
            raise TypeError("Expected argument 'auto_start' to be a bool")
        pulumi.set(__self__, "auto_start", auto_start)
        if connection_monitor_type and not isinstance(connection_monitor_type, str):
            raise TypeError("Expected argument 'connection_monitor_type' to be a str")
        pulumi.set(__self__, "connection_monitor_type", connection_monitor_type)
        if destination and not isinstance(destination, dict):
            raise TypeError("Expected argument 'destination' to be a dict")
        pulumi.set(__self__, "destination", destination)
        if endpoints and not isinstance(endpoints, list):
            raise TypeError("Expected argument 'endpoints' to be a list")
        pulumi.set(__self__, "endpoints", endpoints)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if monitoring_interval_in_seconds and not isinstance(monitoring_interval_in_seconds, int):
            raise TypeError("Expected argument 'monitoring_interval_in_seconds' to be a int")
        pulumi.set(__self__, "monitoring_interval_in_seconds", monitoring_interval_in_seconds)
        if monitoring_status and not isinstance(monitoring_status, str):
            raise TypeError("Expected argument 'monitoring_status' to be a str")
        pulumi.set(__self__, "monitoring_status", monitoring_status)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if notes and not isinstance(notes, str):
            raise TypeError("Expected argument 'notes' to be a str")
        pulumi.set(__self__, "notes", notes)
        if outputs and not isinstance(outputs, list):
            raise TypeError("Expected argument 'outputs' to be a list")
        pulumi.set(__self__, "outputs", outputs)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if source and not isinstance(source, dict):
            raise TypeError("Expected argument 'source' to be a dict")
        pulumi.set(__self__, "source", source)
        if start_time and not isinstance(start_time, str):
            raise TypeError("Expected argument 'start_time' to be a str")
        pulumi.set(__self__, "start_time", start_time)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if test_configurations and not isinstance(test_configurations, list):
            raise TypeError("Expected argument 'test_configurations' to be a list")
        pulumi.set(__self__, "test_configurations", test_configurations)
        if test_groups and not isinstance(test_groups, list):
            raise TypeError("Expected argument 'test_groups' to be a list")
        pulumi.set(__self__, "test_groups", test_groups)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="autoStart")
    def auto_start(self) -> Optional[bool]:
        """
        Determines if the connection monitor will start automatically once created.
        """
        return pulumi.get(self, "auto_start")

    @property
    @pulumi.getter(name="connectionMonitorType")
    def connection_monitor_type(self) -> str:
        """
        Type of connection monitor.
        """
        return pulumi.get(self, "connection_monitor_type")

    @property
    @pulumi.getter
    def destination(self) -> Optional['outputs.ConnectionMonitorDestinationResponse']:
        """
        Describes the destination of connection monitor.
        """
        return pulumi.get(self, "destination")

    @property
    @pulumi.getter
    def endpoints(self) -> Optional[Sequence['outputs.ConnectionMonitorEndpointResponse']]:
        """
        List of connection monitor endpoints.
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        ID of the connection monitor.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Connection monitor location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="monitoringIntervalInSeconds")
    def monitoring_interval_in_seconds(self) -> Optional[int]:
        """
        Monitoring interval in seconds.
        """
        return pulumi.get(self, "monitoring_interval_in_seconds")

    @property
    @pulumi.getter(name="monitoringStatus")
    def monitoring_status(self) -> str:
        """
        The monitoring status of the connection monitor.
        """
        return pulumi.get(self, "monitoring_status")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the connection monitor.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def notes(self) -> Optional[str]:
        """
        Optional notes to be associated with the connection monitor.
        """
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter
    def outputs(self) -> Optional[Sequence['outputs.ConnectionMonitorOutputResponse']]:
        """
        List of connection monitor outputs.
        """
        return pulumi.get(self, "outputs")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the connection monitor.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def source(self) -> Optional['outputs.ConnectionMonitorSourceResponse']:
        """
        Describes the source of connection monitor.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> str:
        """
        The date and time when the connection monitor was started.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Connection monitor tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="testConfigurations")
    def test_configurations(self) -> Optional[Sequence['outputs.ConnectionMonitorTestConfigurationResponse']]:
        """
        List of connection monitor test configurations.
        """
        return pulumi.get(self, "test_configurations")

    @property
    @pulumi.getter(name="testGroups")
    def test_groups(self) -> Optional[Sequence['outputs.ConnectionMonitorTestGroupResponse']]:
        """
        List of connection monitor test groups.
        """
        return pulumi.get(self, "test_groups")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Connection monitor type.
        """
        return pulumi.get(self, "type")


class AwaitableGetConnectionMonitorResult(GetConnectionMonitorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConnectionMonitorResult(
            auto_start=self.auto_start,
            connection_monitor_type=self.connection_monitor_type,
            destination=self.destination,
            endpoints=self.endpoints,
            etag=self.etag,
            id=self.id,
            location=self.location,
            monitoring_interval_in_seconds=self.monitoring_interval_in_seconds,
            monitoring_status=self.monitoring_status,
            name=self.name,
            notes=self.notes,
            outputs=self.outputs,
            provisioning_state=self.provisioning_state,
            source=self.source,
            start_time=self.start_time,
            tags=self.tags,
            test_configurations=self.test_configurations,
            test_groups=self.test_groups,
            type=self.type)


def get_connection_monitor(connection_monitor_name: Optional[str] = None,
                           network_watcher_name: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConnectionMonitorResult:
    """
    Information about the connection monitor.


    :param str connection_monitor_name: The name of the connection monitor.
    :param str network_watcher_name: The name of the Network Watcher resource.
    :param str resource_group_name: The name of the resource group containing Network Watcher.
    """
    __args__ = dict()
    __args__['connectionMonitorName'] = connection_monitor_name
    __args__['networkWatcherName'] = network_watcher_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20210301:getConnectionMonitor', __args__, opts=opts, typ=GetConnectionMonitorResult).value

    return AwaitableGetConnectionMonitorResult(
        auto_start=__ret__.auto_start,
        connection_monitor_type=__ret__.connection_monitor_type,
        destination=__ret__.destination,
        endpoints=__ret__.endpoints,
        etag=__ret__.etag,
        id=__ret__.id,
        location=__ret__.location,
        monitoring_interval_in_seconds=__ret__.monitoring_interval_in_seconds,
        monitoring_status=__ret__.monitoring_status,
        name=__ret__.name,
        notes=__ret__.notes,
        outputs=__ret__.outputs,
        provisioning_state=__ret__.provisioning_state,
        source=__ret__.source,
        start_time=__ret__.start_time,
        tags=__ret__.tags,
        test_configurations=__ret__.test_configurations,
        test_groups=__ret__.test_groups,
        type=__ret__.type)


@_utilities.lift_output_func(get_connection_monitor)
def get_connection_monitor_output(connection_monitor_name: Optional[pulumi.Input[str]] = None,
                                  network_watcher_name: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConnectionMonitorResult]:
    """
    Information about the connection monitor.


    :param str connection_monitor_name: The name of the connection monitor.
    :param str network_watcher_name: The name of the Network Watcher resource.
    :param str resource_group_name: The name of the resource group containing Network Watcher.
    """
    ...
