# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetStandardResult',
    'AwaitableGetStandardResult',
    'get_standard',
    'get_standard_output',
]

@pulumi.output_type
class GetStandardResult:
    """
    Security Standard on a resource
    """
    def __init__(__self__, category=None, components=None, description=None, display_name=None, etag=None, id=None, kind=None, location=None, name=None, standard_type=None, system_data=None, tags=None, type=None):
        if category and not isinstance(category, str):
            raise TypeError("Expected argument 'category' to be a str")
        pulumi.set(__self__, "category", category)
        if components and not isinstance(components, list):
            raise TypeError("Expected argument 'components' to be a list")
        pulumi.set(__self__, "components", components)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if standard_type and not isinstance(standard_type, str):
            raise TypeError("Expected argument 'standard_type' to be a str")
        pulumi.set(__self__, "standard_type", standard_type)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def category(self) -> Optional[str]:
        """
        category of the standard provided
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter
    def components(self) -> Optional[Sequence['outputs.StandardComponentPropertiesResponse']]:
        """
        List of component objects containing component unique keys (such as assessment keys) to apply to standard scope.  Currently only supports assessment keys.
        """
        return pulumi.get(self, "components")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        description of the standard
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        display name of the standard, equivalent to the standardId
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Entity tag is used for comparing two or more entities from the same requested resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of the resource
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Location where the resource is stored
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="standardType")
    def standard_type(self) -> str:
        """
        standard type (Custom or BuiltIn only currently)
        """
        return pulumi.get(self, "standard_type")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        A list of key value pairs that describe the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetStandardResult(GetStandardResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStandardResult(
            category=self.category,
            components=self.components,
            description=self.description,
            display_name=self.display_name,
            etag=self.etag,
            id=self.id,
            kind=self.kind,
            location=self.location,
            name=self.name,
            standard_type=self.standard_type,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_standard(resource_group_name: Optional[str] = None,
                 standard_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStandardResult:
    """
    Security Standard on a resource
    API Version: 2021-08-01-preview.


    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    :param str standard_id: The Security Standard key - unique key for the standard type
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['standardId'] = standard_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:security:getStandard', __args__, opts=opts, typ=GetStandardResult).value

    return AwaitableGetStandardResult(
        category=__ret__.category,
        components=__ret__.components,
        description=__ret__.description,
        display_name=__ret__.display_name,
        etag=__ret__.etag,
        id=__ret__.id,
        kind=__ret__.kind,
        location=__ret__.location,
        name=__ret__.name,
        standard_type=__ret__.standard_type,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_standard)
def get_standard_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                        standard_id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStandardResult]:
    """
    Security Standard on a resource
    API Version: 2021-08-01-preview.


    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    :param str standard_id: The Security Standard key - unique key for the standard type
    """
    ...
