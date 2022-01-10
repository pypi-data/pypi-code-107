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
    'ListClusterLanguageExtensionsResult',
    'AwaitableListClusterLanguageExtensionsResult',
    'list_cluster_language_extensions',
    'list_cluster_language_extensions_output',
]

@pulumi.output_type
class ListClusterLanguageExtensionsResult:
    """
    The list of language extension objects.
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.LanguageExtensionResponse']]:
        """
        The list of language extensions.
        """
        return pulumi.get(self, "value")


class AwaitableListClusterLanguageExtensionsResult(ListClusterLanguageExtensionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListClusterLanguageExtensionsResult(
            value=self.value)


def list_cluster_language_extensions(cluster_name: Optional[str] = None,
                                     resource_group_name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListClusterLanguageExtensionsResult:
    """
    The list of language extension objects.


    :param str cluster_name: The name of the Kusto cluster.
    :param str resource_group_name: The name of the resource group containing the Kusto cluster.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:kusto/v20200614:listClusterLanguageExtensions', __args__, opts=opts, typ=ListClusterLanguageExtensionsResult).value

    return AwaitableListClusterLanguageExtensionsResult(
        value=__ret__.value)


@_utilities.lift_output_func(list_cluster_language_extensions)
def list_cluster_language_extensions_output(cluster_name: Optional[pulumi.Input[str]] = None,
                                            resource_group_name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListClusterLanguageExtensionsResult]:
    """
    The list of language extension objects.


    :param str cluster_name: The name of the Kusto cluster.
    :param str resource_group_name: The name of the resource group containing the Kusto cluster.
    """
    ...
