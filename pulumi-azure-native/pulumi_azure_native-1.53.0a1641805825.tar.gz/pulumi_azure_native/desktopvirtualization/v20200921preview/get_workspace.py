# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetWorkspaceResult',
    'AwaitableGetWorkspaceResult',
    'get_workspace',
    'get_workspace_output',
]

@pulumi.output_type
class GetWorkspaceResult:
    """
    Represents a Workspace definition.
    """
    def __init__(__self__, application_group_references=None, description=None, friendly_name=None, id=None, location=None, name=None, tags=None, type=None):
        if application_group_references and not isinstance(application_group_references, list):
            raise TypeError("Expected argument 'application_group_references' to be a list")
        pulumi.set(__self__, "application_group_references", application_group_references)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if friendly_name and not isinstance(friendly_name, str):
            raise TypeError("Expected argument 'friendly_name' to be a str")
        pulumi.set(__self__, "friendly_name", friendly_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="applicationGroupReferences")
    def application_group_references(self) -> Optional[Sequence[str]]:
        """
        List of applicationGroup resource Ids.
        """
        return pulumi.get(self, "application_group_references")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of Workspace.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[str]:
        """
        Friendly name of Workspace.
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetWorkspaceResult(GetWorkspaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkspaceResult(
            application_group_references=self.application_group_references,
            description=self.description,
            friendly_name=self.friendly_name,
            id=self.id,
            location=self.location,
            name=self.name,
            tags=self.tags,
            type=self.type)


def get_workspace(resource_group_name: Optional[str] = None,
                  workspace_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkspaceResult:
    """
    Represents a Workspace definition.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:desktopvirtualization/v20200921preview:getWorkspace', __args__, opts=opts, typ=GetWorkspaceResult).value

    return AwaitableGetWorkspaceResult(
        application_group_references=__ret__.application_group_references,
        description=__ret__.description,
        friendly_name=__ret__.friendly_name,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_workspace)
def get_workspace_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                         workspace_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkspaceResult]:
    """
    Represents a Workspace definition.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace
    """
    ...
