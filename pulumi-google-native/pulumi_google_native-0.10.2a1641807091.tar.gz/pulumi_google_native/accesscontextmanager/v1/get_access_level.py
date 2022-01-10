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
    'GetAccessLevelResult',
    'AwaitableGetAccessLevelResult',
    'get_access_level',
    'get_access_level_output',
]

@pulumi.output_type
class GetAccessLevelResult:
    def __init__(__self__, basic=None, custom=None, description=None, name=None, title=None):
        if basic and not isinstance(basic, dict):
            raise TypeError("Expected argument 'basic' to be a dict")
        pulumi.set(__self__, "basic", basic)
        if custom and not isinstance(custom, dict):
            raise TypeError("Expected argument 'custom' to be a dict")
        pulumi.set(__self__, "custom", custom)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if title and not isinstance(title, str):
            raise TypeError("Expected argument 'title' to be a str")
        pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter
    def basic(self) -> 'outputs.BasicLevelResponse':
        """
        A `BasicLevel` composed of `Conditions`.
        """
        return pulumi.get(self, "basic")

    @property
    @pulumi.getter
    def custom(self) -> 'outputs.CustomLevelResponse':
        """
        A `CustomLevel` written in the Common Expression Language.
        """
        return pulumi.get(self, "custom")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the `AccessLevel` and its use. Does not affect behavior.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name for the Access Level. The `short_name` component must begin with a letter and only include alphanumeric and '_'. Format: `accessPolicies/{access_policy}/accessLevels/{access_level}`. The maximum length of the `access_level` component is 50 characters.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def title(self) -> str:
        """
        Human readable title. Must be unique within the Policy.
        """
        return pulumi.get(self, "title")


class AwaitableGetAccessLevelResult(GetAccessLevelResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccessLevelResult(
            basic=self.basic,
            custom=self.custom,
            description=self.description,
            name=self.name,
            title=self.title)


def get_access_level(access_level_format: Optional[str] = None,
                     access_level_id: Optional[str] = None,
                     access_policy_id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccessLevelResult:
    """
    Gets an access level based on the resource name.
    """
    __args__ = dict()
    __args__['accessLevelFormat'] = access_level_format
    __args__['accessLevelId'] = access_level_id
    __args__['accessPolicyId'] = access_policy_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:accesscontextmanager/v1:getAccessLevel', __args__, opts=opts, typ=GetAccessLevelResult).value

    return AwaitableGetAccessLevelResult(
        basic=__ret__.basic,
        custom=__ret__.custom,
        description=__ret__.description,
        name=__ret__.name,
        title=__ret__.title)


@_utilities.lift_output_func(get_access_level)
def get_access_level_output(access_level_format: Optional[pulumi.Input[Optional[str]]] = None,
                            access_level_id: Optional[pulumi.Input[str]] = None,
                            access_policy_id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAccessLevelResult]:
    """
    Gets an access level based on the resource name.
    """
    ...
