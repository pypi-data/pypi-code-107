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
    'GetSkusNestedResourceTypeFirstResult',
    'AwaitableGetSkusNestedResourceTypeFirstResult',
    'get_skus_nested_resource_type_first',
    'get_skus_nested_resource_type_first_output',
]

@pulumi.output_type
class GetSkusNestedResourceTypeFirstResult:
    def __init__(__self__, id=None, name=None, properties=None, type=None):
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
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.SkuResourceResponseProperties':
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetSkusNestedResourceTypeFirstResult(GetSkusNestedResourceTypeFirstResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSkusNestedResourceTypeFirstResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_skus_nested_resource_type_first(nested_resource_type_first: Optional[str] = None,
                                        provider_namespace: Optional[str] = None,
                                        resource_type: Optional[str] = None,
                                        sku: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSkusNestedResourceTypeFirstResult:
    """
    Use this data source to access information about an existing resource.

    :param str nested_resource_type_first: The first child resource type.
    :param str provider_namespace: The name of the resource provider hosted within ProviderHub.
    :param str resource_type: The resource type.
    :param str sku: The SKU.
    """
    __args__ = dict()
    __args__['nestedResourceTypeFirst'] = nested_resource_type_first
    __args__['providerNamespace'] = provider_namespace
    __args__['resourceType'] = resource_type
    __args__['sku'] = sku
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:providerhub/v20210501preview:getSkusNestedResourceTypeFirst', __args__, opts=opts, typ=GetSkusNestedResourceTypeFirstResult).value

    return AwaitableGetSkusNestedResourceTypeFirstResult(
        id=__ret__.id,
        name=__ret__.name,
        properties=__ret__.properties,
        type=__ret__.type)


@_utilities.lift_output_func(get_skus_nested_resource_type_first)
def get_skus_nested_resource_type_first_output(nested_resource_type_first: Optional[pulumi.Input[str]] = None,
                                               provider_namespace: Optional[pulumi.Input[str]] = None,
                                               resource_type: Optional[pulumi.Input[str]] = None,
                                               sku: Optional[pulumi.Input[str]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSkusNestedResourceTypeFirstResult]:
    """
    Use this data source to access information about an existing resource.

    :param str nested_resource_type_first: The first child resource type.
    :param str provider_namespace: The name of the resource provider hosted within ProviderHub.
    :param str resource_type: The resource type.
    :param str sku: The SKU.
    """
    ...
