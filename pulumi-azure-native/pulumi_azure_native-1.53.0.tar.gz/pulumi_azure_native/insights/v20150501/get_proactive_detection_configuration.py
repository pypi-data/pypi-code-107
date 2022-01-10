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
    'GetProactiveDetectionConfigurationResult',
    'AwaitableGetProactiveDetectionConfigurationResult',
    'get_proactive_detection_configuration',
    'get_proactive_detection_configuration_output',
]

@pulumi.output_type
class GetProactiveDetectionConfigurationResult:
    """
    Properties that define a ProactiveDetection configuration.
    """
    def __init__(__self__, custom_emails=None, enabled=None, last_updated_time=None, name=None, rule_definitions=None, send_emails_to_subscription_owners=None):
        if custom_emails and not isinstance(custom_emails, list):
            raise TypeError("Expected argument 'custom_emails' to be a list")
        pulumi.set(__self__, "custom_emails", custom_emails)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if last_updated_time and not isinstance(last_updated_time, str):
            raise TypeError("Expected argument 'last_updated_time' to be a str")
        pulumi.set(__self__, "last_updated_time", last_updated_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if rule_definitions and not isinstance(rule_definitions, dict):
            raise TypeError("Expected argument 'rule_definitions' to be a dict")
        pulumi.set(__self__, "rule_definitions", rule_definitions)
        if send_emails_to_subscription_owners and not isinstance(send_emails_to_subscription_owners, bool):
            raise TypeError("Expected argument 'send_emails_to_subscription_owners' to be a bool")
        pulumi.set(__self__, "send_emails_to_subscription_owners", send_emails_to_subscription_owners)

    @property
    @pulumi.getter(name="customEmails")
    def custom_emails(self) -> Optional[Sequence[str]]:
        """
        Custom email addresses for this rule notifications
        """
        return pulumi.get(self, "custom_emails")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        A flag that indicates whether this rule is enabled by the user
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[str]:
        """
        The last time this rule was updated
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The rule name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ruleDefinitions")
    def rule_definitions(self) -> Optional['outputs.ApplicationInsightsComponentProactiveDetectionConfigurationResponseRuleDefinitions']:
        """
        Static definitions of the ProactiveDetection configuration rule (same values for all components).
        """
        return pulumi.get(self, "rule_definitions")

    @property
    @pulumi.getter(name="sendEmailsToSubscriptionOwners")
    def send_emails_to_subscription_owners(self) -> Optional[bool]:
        """
        A flag that indicated whether notifications on this rule should be sent to subscription owners
        """
        return pulumi.get(self, "send_emails_to_subscription_owners")


class AwaitableGetProactiveDetectionConfigurationResult(GetProactiveDetectionConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProactiveDetectionConfigurationResult(
            custom_emails=self.custom_emails,
            enabled=self.enabled,
            last_updated_time=self.last_updated_time,
            name=self.name,
            rule_definitions=self.rule_definitions,
            send_emails_to_subscription_owners=self.send_emails_to_subscription_owners)


def get_proactive_detection_configuration(configuration_id: Optional[str] = None,
                                          resource_group_name: Optional[str] = None,
                                          resource_name: Optional[str] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProactiveDetectionConfigurationResult:
    """
    Properties that define a ProactiveDetection configuration.


    :param str configuration_id: The ProactiveDetection configuration ID. This is unique within a Application Insights component.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the Application Insights component resource.
    """
    __args__ = dict()
    __args__['configurationId'] = configuration_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:insights/v20150501:getProactiveDetectionConfiguration', __args__, opts=opts, typ=GetProactiveDetectionConfigurationResult).value

    return AwaitableGetProactiveDetectionConfigurationResult(
        custom_emails=__ret__.custom_emails,
        enabled=__ret__.enabled,
        last_updated_time=__ret__.last_updated_time,
        name=__ret__.name,
        rule_definitions=__ret__.rule_definitions,
        send_emails_to_subscription_owners=__ret__.send_emails_to_subscription_owners)


@_utilities.lift_output_func(get_proactive_detection_configuration)
def get_proactive_detection_configuration_output(configuration_id: Optional[pulumi.Input[str]] = None,
                                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                                 resource_name: Optional[pulumi.Input[str]] = None,
                                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProactiveDetectionConfigurationResult]:
    """
    Properties that define a ProactiveDetection configuration.


    :param str configuration_id: The ProactiveDetection configuration ID. This is unique within a Application Insights component.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the Application Insights component resource.
    """
    ...
