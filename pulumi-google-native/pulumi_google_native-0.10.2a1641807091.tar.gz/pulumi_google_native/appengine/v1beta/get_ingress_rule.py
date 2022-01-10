# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetIngressRuleResult',
    'AwaitableGetIngressRuleResult',
    'get_ingress_rule',
    'get_ingress_rule_output',
]

@pulumi.output_type
class GetIngressRuleResult:
    def __init__(__self__, action=None, description=None, priority=None, source_range=None):
        if action and not isinstance(action, str):
            raise TypeError("Expected argument 'action' to be a str")
        pulumi.set(__self__, "action", action)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if priority and not isinstance(priority, int):
            raise TypeError("Expected argument 'priority' to be a int")
        pulumi.set(__self__, "priority", priority)
        if source_range and not isinstance(source_range, str):
            raise TypeError("Expected argument 'source_range' to be a str")
        pulumi.set(__self__, "source_range", source_range)

    @property
    @pulumi.getter
    def action(self) -> str:
        """
        The action to take on matched requests.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        An optional string description of this rule. This field has a maximum length of 400 characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def priority(self) -> int:
        """
        A positive integer between 1, Int32.MaxValue-1 that defines the order of rule evaluation. Rules with the lowest priority are evaluated first.A default rule at priority Int32.MaxValue matches all IPv4 and IPv6 traffic when no previous rule matches. Only the action of this rule can be modified by the user.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="sourceRange")
    def source_range(self) -> str:
        """
        IP address or range, defined using CIDR notation, of requests that this rule applies to. You can use the wildcard character "*" to match all IPs equivalent to "0/0" and "::/0" together. Examples: 192.168.1.1 or 192.168.0.0/16 or 2001:db8::/32 or 2001:0db8:0000:0042:0000:8a2e:0370:7334. Truncation will be silently performed on addresses which are not properly truncated. For example, 1.2.3.4/24 is accepted as the same address as 1.2.3.0/24. Similarly, for IPv6, 2001:db8::1/32 is accepted as the same address as 2001:db8::/32.
        """
        return pulumi.get(self, "source_range")


class AwaitableGetIngressRuleResult(GetIngressRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIngressRuleResult(
            action=self.action,
            description=self.description,
            priority=self.priority,
            source_range=self.source_range)


def get_ingress_rule(app_id: Optional[str] = None,
                     ingress_rule_id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIngressRuleResult:
    """
    Gets the specified firewall rule.
    """
    __args__ = dict()
    __args__['appId'] = app_id
    __args__['ingressRuleId'] = ingress_rule_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:appengine/v1beta:getIngressRule', __args__, opts=opts, typ=GetIngressRuleResult).value

    return AwaitableGetIngressRuleResult(
        action=__ret__.action,
        description=__ret__.description,
        priority=__ret__.priority,
        source_range=__ret__.source_range)


@_utilities.lift_output_func(get_ingress_rule)
def get_ingress_rule_output(app_id: Optional[pulumi.Input[str]] = None,
                            ingress_rule_id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIngressRuleResult]:
    """
    Gets the specified firewall rule.
    """
    ...
