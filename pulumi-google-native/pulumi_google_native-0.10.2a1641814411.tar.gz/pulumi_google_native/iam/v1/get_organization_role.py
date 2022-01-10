# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetOrganizationRoleResult',
    'AwaitableGetOrganizationRoleResult',
    'get_organization_role',
    'get_organization_role_output',
]

@pulumi.output_type
class GetOrganizationRoleResult:
    def __init__(__self__, deleted=None, description=None, etag=None, included_permissions=None, name=None, stage=None, title=None):
        if deleted and not isinstance(deleted, bool):
            raise TypeError("Expected argument 'deleted' to be a bool")
        pulumi.set(__self__, "deleted", deleted)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if included_permissions and not isinstance(included_permissions, list):
            raise TypeError("Expected argument 'included_permissions' to be a list")
        pulumi.set(__self__, "included_permissions", included_permissions)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if stage and not isinstance(stage, str):
            raise TypeError("Expected argument 'stage' to be a str")
        pulumi.set(__self__, "stage", stage)
        if title and not isinstance(title, str):
            raise TypeError("Expected argument 'title' to be a str")
        pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter
    def deleted(self) -> bool:
        """
        The current deleted state of the role. This field is read only. It will be ignored in calls to CreateRole and UpdateRole.
        """
        return pulumi.get(self, "deleted")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Optional. A human-readable description for the role.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Used to perform a consistent read-modify-write.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="includedPermissions")
    def included_permissions(self) -> Sequence[str]:
        """
        The names of the permissions this role grants when bound in an IAM policy.
        """
        return pulumi.get(self, "included_permissions")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the role. When Role is used in CreateRole, the role name must not be set. When Role is used in output and other input such as UpdateRole, the role name is the complete path, e.g., roles/logging.viewer for predefined roles and organizations/{ORGANIZATION_ID}/roles/logging.viewer for custom roles.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def stage(self) -> str:
        """
        The current launch stage of the role. If the `ALPHA` launch stage has been selected for a role, the `stage` field will not be included in the returned definition for the role.
        """
        return pulumi.get(self, "stage")

    @property
    @pulumi.getter
    def title(self) -> str:
        """
        Optional. A human-readable title for the role. Typically this is limited to 100 UTF-8 bytes.
        """
        return pulumi.get(self, "title")


class AwaitableGetOrganizationRoleResult(GetOrganizationRoleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOrganizationRoleResult(
            deleted=self.deleted,
            description=self.description,
            etag=self.etag,
            included_permissions=self.included_permissions,
            name=self.name,
            stage=self.stage,
            title=self.title)


def get_organization_role(organization_id: Optional[str] = None,
                          role_id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOrganizationRoleResult:
    """
    Gets the definition of a Role.
    """
    __args__ = dict()
    __args__['organizationId'] = organization_id
    __args__['roleId'] = role_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:iam/v1:getOrganizationRole', __args__, opts=opts, typ=GetOrganizationRoleResult).value

    return AwaitableGetOrganizationRoleResult(
        deleted=__ret__.deleted,
        description=__ret__.description,
        etag=__ret__.etag,
        included_permissions=__ret__.included_permissions,
        name=__ret__.name,
        stage=__ret__.stage,
        title=__ret__.title)


@_utilities.lift_output_func(get_organization_role)
def get_organization_role_output(organization_id: Optional[pulumi.Input[str]] = None,
                                 role_id: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOrganizationRoleResult]:
    """
    Gets the definition of a Role.
    """
    ...
