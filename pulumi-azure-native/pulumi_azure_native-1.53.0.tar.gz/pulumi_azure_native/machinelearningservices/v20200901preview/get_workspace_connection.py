# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetWorkspaceConnectionResult',
    'AwaitableGetWorkspaceConnectionResult',
    'get_workspace_connection',
    'get_workspace_connection_output',
]

@pulumi.output_type
class GetWorkspaceConnectionResult:
    """
    Workspace connection.
    """
    def __init__(__self__, auth_type=None, category=None, id=None, name=None, target=None, type=None, value=None):
        if auth_type and not isinstance(auth_type, str):
            raise TypeError("Expected argument 'auth_type' to be a str")
        pulumi.set(__self__, "auth_type", auth_type)
        if category and not isinstance(category, str):
            raise TypeError("Expected argument 'category' to be a str")
        pulumi.set(__self__, "category", category)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if target and not isinstance(target, str):
            raise TypeError("Expected argument 'target' to be a str")
        pulumi.set(__self__, "target", target)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[str]:
        """
        Authorization type of the workspace connection.
        """
        return pulumi.get(self, "auth_type")

    @property
    @pulumi.getter
    def category(self) -> Optional[str]:
        """
        Category of the workspace connection.
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        ResourceId of the workspace connection.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Friendly name of the workspace connection.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def target(self) -> Optional[str]:
        """
        Target of the workspace connection.
        """
        return pulumi.get(self, "target")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type of workspace connection.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        Value details of the workspace connection.
        """
        return pulumi.get(self, "value")


class AwaitableGetWorkspaceConnectionResult(GetWorkspaceConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspaceConnectionResult(
            auth_type=self.auth_type,
            category=self.category,
            id=self.id,
            name=self.name,
            target=self.target,
            type=self.type,
            value=self.value)


def get_workspace_connection(connection_name: Optional[str] = None,
                             resource_group_name: Optional[str] = None,
                             workspace_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspaceConnectionResult:
    """
    Workspace connection.


    :param str connection_name: Friendly name of the workspace connection
    :param str resource_group_name: Name of the resource group in which workspace is located.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    __args__ = dict()
    __args__['connectionName'] = connection_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningservices/v20200901preview:getWorkspaceConnection', __args__, opts=opts, typ=GetWorkspaceConnectionResult).value

    return AwaitableGetWorkspaceConnectionResult(
        auth_type=__ret__.auth_type,
        category=__ret__.category,
        id=__ret__.id,
        name=__ret__.name,
        target=__ret__.target,
        type=__ret__.type,
        value=__ret__.value)


@_utilities.lift_output_func(get_workspace_connection)
def get_workspace_connection_output(connection_name: Optional[pulumi.Input[str]] = None,
                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                    workspace_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkspaceConnectionResult]:
    """
    Workspace connection.


    :param str connection_name: Friendly name of the workspace connection
    :param str resource_group_name: Name of the resource group in which workspace is located.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    ...
