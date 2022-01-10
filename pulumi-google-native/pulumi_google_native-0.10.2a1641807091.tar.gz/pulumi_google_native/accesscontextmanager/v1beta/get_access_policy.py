# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetAccessPolicyResult',
    'AwaitableGetAccessPolicyResult',
    'get_access_policy',
    'get_access_policy_output',
]

@pulumi.output_type
class GetAccessPolicyResult:
    def __init__(__self__, name=None, parent=None, title=None):
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parent and not isinstance(parent, str):
            raise TypeError("Expected argument 'parent' to be a str")
        pulumi.set(__self__, "parent", parent)
        if title and not isinstance(title, str):
            raise TypeError("Expected argument 'title' to be a str")
        pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name of the `AccessPolicy`. Format: `accessPolicies/{policy_id}`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parent(self) -> str:
        """
        The parent of this `AccessPolicy` in the Cloud Resource Hierarchy. Currently immutable once created. Format: `organizations/{organization_id}`
        """
        return pulumi.get(self, "parent")

    @property
    @pulumi.getter
    def title(self) -> str:
        """
        Human readable title. Does not affect behavior.
        """
        return pulumi.get(self, "title")


class AwaitableGetAccessPolicyResult(GetAccessPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccessPolicyResult(
            name=self.name,
            parent=self.parent,
            title=self.title)


def get_access_policy(access_policy_id: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccessPolicyResult:
    """
    Get an AccessPolicy by name.
    """
    __args__ = dict()
    __args__['accessPolicyId'] = access_policy_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:accesscontextmanager/v1beta:getAccessPolicy', __args__, opts=opts, typ=GetAccessPolicyResult).value

    return AwaitableGetAccessPolicyResult(
        name=__ret__.name,
        parent=__ret__.parent,
        title=__ret__.title)


@_utilities.lift_output_func(get_access_policy)
def get_access_policy_output(access_policy_id: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccessPolicyResult]:
    """
    Get an AccessPolicy by name.
    """
    ...
