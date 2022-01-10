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
    'GetKustoClusterDataSetResult',
    'AwaitableGetKustoClusterDataSetResult',
    'get_kusto_cluster_data_set',
    'get_kusto_cluster_data_set_output',
]

@pulumi.output_type
class GetKustoClusterDataSetResult:
    """
    A kusto cluster data set.
    """
    def __init__(__self__, data_set_id=None, id=None, kind=None, kusto_cluster_resource_id=None, location=None, name=None, provisioning_state=None, system_data=None, type=None):
        if data_set_id and not isinstance(data_set_id, str):
            raise TypeError("Expected argument 'data_set_id' to be a str")
        pulumi.set(__self__, "data_set_id", data_set_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if kusto_cluster_resource_id and not isinstance(kusto_cluster_resource_id, str):
            raise TypeError("Expected argument 'kusto_cluster_resource_id' to be a str")
        pulumi.set(__self__, "kusto_cluster_resource_id", kusto_cluster_resource_id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> str:
        """
        Unique id for identifying a data set resource
        """
        return pulumi.get(self, "data_set_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource id of the azure resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of data set.
        Expected value is 'KustoCluster'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="kustoClusterResourceId")
    def kusto_cluster_resource_id(self) -> str:
        """
        Resource id of the kusto cluster.
        """
        return pulumi.get(self, "kusto_cluster_resource_id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Location of the kusto cluster.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the azure resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the kusto cluster data set.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        System Data of the Azure resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the azure resource
        """
        return pulumi.get(self, "type")


class AwaitableGetKustoClusterDataSetResult(GetKustoClusterDataSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKustoClusterDataSetResult(
            data_set_id=self.data_set_id,
            id=self.id,
            kind=self.kind,
            kusto_cluster_resource_id=self.kusto_cluster_resource_id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_kusto_cluster_data_set(account_name: Optional[str] = None,
                               data_set_name: Optional[str] = None,
                               resource_group_name: Optional[str] = None,
                               share_name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKustoClusterDataSetResult:
    """
    A kusto cluster data set.
    API Version: 2020-09-01.


    :param str account_name: The name of the share account.
    :param str data_set_name: The name of the dataSet.
    :param str resource_group_name: The resource group name.
    :param str share_name: The name of the share.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['dataSetName'] = data_set_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['shareName'] = share_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:datashare:getKustoClusterDataSet', __args__, opts=opts, typ=GetKustoClusterDataSetResult).value

    return AwaitableGetKustoClusterDataSetResult(
        data_set_id=__ret__.data_set_id,
        id=__ret__.id,
        kind=__ret__.kind,
        kusto_cluster_resource_id=__ret__.kusto_cluster_resource_id,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_kusto_cluster_data_set)
def get_kusto_cluster_data_set_output(account_name: Optional[pulumi.Input[str]] = None,
                                      data_set_name: Optional[pulumi.Input[str]] = None,
                                      resource_group_name: Optional[pulumi.Input[str]] = None,
                                      share_name: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKustoClusterDataSetResult]:
    """
    A kusto cluster data set.
    API Version: 2020-09-01.


    :param str account_name: The name of the share account.
    :param str data_set_name: The name of the dataSet.
    :param str resource_group_name: The resource group name.
    :param str share_name: The name of the share.
    """
    ...
