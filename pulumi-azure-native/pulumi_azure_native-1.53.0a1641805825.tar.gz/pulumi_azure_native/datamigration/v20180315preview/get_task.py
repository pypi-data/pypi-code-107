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
    'GetTaskResult',
    'AwaitableGetTaskResult',
    'get_task',
    'get_task_output',
]

@pulumi.output_type
class GetTaskResult:
    """
    A task resource
    """
    def __init__(__self__, etag=None, id=None, name=None, properties=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        HTTP strong entity tag value. This is ignored if submitted.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> Any:
        """
        Custom task properties
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetTaskResult(GetTaskResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTaskResult(
            etag=self.etag,
            id=self.id,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_task(expand: Optional[str] = None,
             group_name: Optional[str] = None,
             project_name: Optional[str] = None,
             service_name: Optional[str] = None,
             task_name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTaskResult:
    """
    A task resource


    :param str expand: Expand the response
    :param str group_name: Name of the resource group
    :param str project_name: Name of the project
    :param str service_name: Name of the service
    :param str task_name: Name of the Task
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['groupName'] = group_name
    __args__['projectName'] = project_name
    __args__['serviceName'] = service_name
    __args__['taskName'] = task_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:datamigration/v20180315preview:getTask', __args__, opts=opts, typ=GetTaskResult).value

    return AwaitableGetTaskResult(
        etag=__ret__.etag,
        id=__ret__.id,
        name=__ret__.name,
        properties=__ret__.properties,
        type=__ret__.type)


@_utilities.lift_output_func(get_task)
def get_task_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                    group_name: Optional[pulumi.Input[str]] = None,
                    project_name: Optional[pulumi.Input[str]] = None,
                    service_name: Optional[pulumi.Input[str]] = None,
                    task_name: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTaskResult]:
    """
    A task resource


    :param str expand: Expand the response
    :param str group_name: Name of the resource group
    :param str project_name: Name of the project
    :param str service_name: Name of the service
    :param str task_name: Name of the Task
    """
    ...
