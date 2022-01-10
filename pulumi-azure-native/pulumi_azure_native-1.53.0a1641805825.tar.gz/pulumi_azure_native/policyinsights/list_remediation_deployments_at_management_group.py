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
    'ListRemediationDeploymentsAtManagementGroupResult',
    'AwaitableListRemediationDeploymentsAtManagementGroupResult',
    'list_remediation_deployments_at_management_group',
    'list_remediation_deployments_at_management_group_output',
]

@pulumi.output_type
class ListRemediationDeploymentsAtManagementGroupResult:
    """
    List of deployments for a remediation.
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> str:
        """
        The URL to get the next set of results.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Sequence['outputs.RemediationDeploymentResponse']:
        """
        Array of deployments for the remediation.
        """
        return pulumi.get(self, "value")


class AwaitableListRemediationDeploymentsAtManagementGroupResult(ListRemediationDeploymentsAtManagementGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListRemediationDeploymentsAtManagementGroupResult(
            next_link=self.next_link,
            value=self.value)


def list_remediation_deployments_at_management_group(management_group_id: Optional[str] = None,
                                                     management_groups_namespace: Optional[str] = None,
                                                     remediation_name: Optional[str] = None,
                                                     top: Optional[int] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListRemediationDeploymentsAtManagementGroupResult:
    """
    List of deployments for a remediation.
    API Version: 2019-07-01.


    :param str management_group_id: Management group ID.
    :param str management_groups_namespace: The namespace for Microsoft Management RP; only "Microsoft.Management" is allowed.
    :param str remediation_name: The name of the remediation.
    :param int top: Maximum number of records to return.
    """
    __args__ = dict()
    __args__['managementGroupId'] = management_group_id
    __args__['managementGroupsNamespace'] = management_groups_namespace
    __args__['remediationName'] = remediation_name
    __args__['top'] = top
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:policyinsights:listRemediationDeploymentsAtManagementGroup', __args__, opts=opts, typ=ListRemediationDeploymentsAtManagementGroupResult).value

    return AwaitableListRemediationDeploymentsAtManagementGroupResult(
        next_link=__ret__.next_link,
        value=__ret__.value)


@_utilities.lift_output_func(list_remediation_deployments_at_management_group)
def list_remediation_deployments_at_management_group_output(management_group_id: Optional[pulumi.Input[str]] = None,
                                                            management_groups_namespace: Optional[pulumi.Input[str]] = None,
                                                            remediation_name: Optional[pulumi.Input[str]] = None,
                                                            top: Optional[pulumi.Input[Optional[int]]] = None,
                                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListRemediationDeploymentsAtManagementGroupResult]:
    """
    List of deployments for a remediation.
    API Version: 2019-07-01.


    :param str management_group_id: Management group ID.
    :param str management_groups_namespace: The namespace for Microsoft Management RP; only "Microsoft.Management" is allowed.
    :param str remediation_name: The name of the remediation.
    :param int top: Maximum number of records to return.
    """
    ...
