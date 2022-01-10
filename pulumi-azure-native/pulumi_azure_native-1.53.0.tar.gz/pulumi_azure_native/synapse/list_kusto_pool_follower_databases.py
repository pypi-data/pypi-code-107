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
    'ListKustoPoolFollowerDatabasesResult',
    'AwaitableListKustoPoolFollowerDatabasesResult',
    'list_kusto_pool_follower_databases',
    'list_kusto_pool_follower_databases_output',
]

@pulumi.output_type
class ListKustoPoolFollowerDatabasesResult:
    """
    The list Kusto database principals operation response.
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.FollowerDatabaseDefinitionResponse']]:
        """
        The list of follower database result.
        """
        return pulumi.get(self, "value")


class AwaitableListKustoPoolFollowerDatabasesResult(ListKustoPoolFollowerDatabasesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListKustoPoolFollowerDatabasesResult(
            value=self.value)


def list_kusto_pool_follower_databases(kusto_pool_name: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       workspace_name: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListKustoPoolFollowerDatabasesResult:
    """
    The list Kusto database principals operation response.
    API Version: 2021-06-01-preview.


    :param str kusto_pool_name: The name of the Kusto pool.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['kustoPoolName'] = kusto_pool_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:synapse:listKustoPoolFollowerDatabases', __args__, opts=opts, typ=ListKustoPoolFollowerDatabasesResult).value

    return AwaitableListKustoPoolFollowerDatabasesResult(
        value=__ret__.value)


@_utilities.lift_output_func(list_kusto_pool_follower_databases)
def list_kusto_pool_follower_databases_output(kusto_pool_name: Optional[pulumi.Input[str]] = None,
                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                              workspace_name: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListKustoPoolFollowerDatabasesResult]:
    """
    The list Kusto database principals operation response.
    API Version: 2021-06-01-preview.


    :param str kusto_pool_name: The name of the Kusto pool.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    ...
