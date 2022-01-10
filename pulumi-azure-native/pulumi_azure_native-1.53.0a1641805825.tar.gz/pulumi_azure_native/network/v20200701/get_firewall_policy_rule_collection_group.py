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
    'GetFirewallPolicyRuleCollectionGroupResult',
    'AwaitableGetFirewallPolicyRuleCollectionGroupResult',
    'get_firewall_policy_rule_collection_group',
    'get_firewall_policy_rule_collection_group_output',
]

@pulumi.output_type
class GetFirewallPolicyRuleCollectionGroupResult:
    """
    Rule Collection Group resource.
    """
    def __init__(__self__, etag=None, id=None, name=None, priority=None, provisioning_state=None, rule_collections=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if priority and not isinstance(priority, int):
            raise TypeError("Expected argument 'priority' to be a int")
        pulumi.set(__self__, "priority", priority)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if rule_collections and not isinstance(rule_collections, list):
            raise TypeError("Expected argument 'rule_collections' to be a list")
        pulumi.set(__self__, "rule_collections", rule_collections)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> Optional[int]:
        """
        Priority of the Firewall Policy Rule Collection Group resource.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the firewall policy rule collection group resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="ruleCollections")
    def rule_collections(self) -> Optional[Sequence[Any]]:
        """
        Group of Firewall Policy rule collections.
        """
        return pulumi.get(self, "rule_collections")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Rule Group type.
        """
        return pulumi.get(self, "type")


class AwaitableGetFirewallPolicyRuleCollectionGroupResult(GetFirewallPolicyRuleCollectionGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFirewallPolicyRuleCollectionGroupResult(
            etag=self.etag,
            id=self.id,
            name=self.name,
            priority=self.priority,
            provisioning_state=self.provisioning_state,
            rule_collections=self.rule_collections,
            type=self.type)


def get_firewall_policy_rule_collection_group(firewall_policy_name: Optional[str] = None,
                                              resource_group_name: Optional[str] = None,
                                              rule_collection_group_name: Optional[str] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFirewallPolicyRuleCollectionGroupResult:
    """
    Rule Collection Group resource.


    :param str firewall_policy_name: The name of the Firewall Policy.
    :param str resource_group_name: The name of the resource group.
    :param str rule_collection_group_name: The name of the FirewallPolicyRuleCollectionGroup.
    """
    __args__ = dict()
    __args__['firewallPolicyName'] = firewall_policy_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['ruleCollectionGroupName'] = rule_collection_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20200701:getFirewallPolicyRuleCollectionGroup', __args__, opts=opts, typ=GetFirewallPolicyRuleCollectionGroupResult).value

    return AwaitableGetFirewallPolicyRuleCollectionGroupResult(
        etag=__ret__.etag,
        id=__ret__.id,
        name=__ret__.name,
        priority=__ret__.priority,
        provisioning_state=__ret__.provisioning_state,
        rule_collections=__ret__.rule_collections,
        type=__ret__.type)


@_utilities.lift_output_func(get_firewall_policy_rule_collection_group)
def get_firewall_policy_rule_collection_group_output(firewall_policy_name: Optional[pulumi.Input[str]] = None,
                                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                                     rule_collection_group_name: Optional[pulumi.Input[str]] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFirewallPolicyRuleCollectionGroupResult]:
    """
    Rule Collection Group resource.


    :param str firewall_policy_name: The name of the Firewall Policy.
    :param str resource_group_name: The name of the resource group.
    :param str rule_collection_group_name: The name of the FirewallPolicyRuleCollectionGroup.
    """
    ...
