# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['RouteArgs', 'Route']

@pulumi.input_type
class RouteArgs:
    def __init__(__self__, *,
                 endpoint_name: pulumi.Input[str],
                 origin_group: pulumi.Input['ResourceReferenceArgs'],
                 profile_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 cache_configuration: Optional[pulumi.Input['AfdRouteCacheConfigurationArgs']] = None,
                 custom_domains: Optional[pulumi.Input[Sequence[pulumi.Input['ActivatedResourceReferenceArgs']]]] = None,
                 enabled_state: Optional[pulumi.Input[Union[str, 'EnabledState']]] = None,
                 forwarding_protocol: Optional[pulumi.Input[Union[str, 'ForwardingProtocol']]] = None,
                 https_redirect: Optional[pulumi.Input[Union[str, 'HttpsRedirect']]] = None,
                 link_to_default_domain: Optional[pulumi.Input[Union[str, 'LinkToDefaultDomain']]] = None,
                 origin_path: Optional[pulumi.Input[str]] = None,
                 patterns_to_match: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 route_name: Optional[pulumi.Input[str]] = None,
                 rule_sets: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceReferenceArgs']]]] = None,
                 supported_protocols: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AFDEndpointProtocols']]]]] = None):
        """
        The set of arguments for constructing a Route resource.
        :param pulumi.Input[str] endpoint_name: Name of the endpoint under the profile which is unique globally.
        :param pulumi.Input['ResourceReferenceArgs'] origin_group: A reference to the origin group.
        :param pulumi.Input[str] profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input['AfdRouteCacheConfigurationArgs'] cache_configuration: The caching configuration for this route. To disable caching, do not provide a cacheConfiguration object.
        :param pulumi.Input[Sequence[pulumi.Input['ActivatedResourceReferenceArgs']]] custom_domains: Domains referenced by this endpoint.
        :param pulumi.Input[Union[str, 'EnabledState']] enabled_state: Whether to enable use of this rule. Permitted values are 'Enabled' or 'Disabled'
        :param pulumi.Input[Union[str, 'ForwardingProtocol']] forwarding_protocol: Protocol this rule will use when forwarding traffic to backends.
        :param pulumi.Input[Union[str, 'HttpsRedirect']] https_redirect: Whether to automatically redirect HTTP traffic to HTTPS traffic. Note that this is a easy way to set up this rule and it will be the first rule that gets executed.
        :param pulumi.Input[Union[str, 'LinkToDefaultDomain']] link_to_default_domain: whether this route will be linked to the default endpoint domain.
        :param pulumi.Input[str] origin_path: A directory path on the origin that AzureFrontDoor can use to retrieve content from, e.g. contoso.cloudapp.net/originpath.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] patterns_to_match: The route patterns of the rule.
        :param pulumi.Input[str] route_name: Name of the routing rule.
        :param pulumi.Input[Sequence[pulumi.Input['ResourceReferenceArgs']]] rule_sets: rule sets referenced by this endpoint.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'AFDEndpointProtocols']]]] supported_protocols: List of supported protocols for this route.
        """
        pulumi.set(__self__, "endpoint_name", endpoint_name)
        pulumi.set(__self__, "origin_group", origin_group)
        pulumi.set(__self__, "profile_name", profile_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if cache_configuration is not None:
            pulumi.set(__self__, "cache_configuration", cache_configuration)
        if custom_domains is not None:
            pulumi.set(__self__, "custom_domains", custom_domains)
        if enabled_state is not None:
            pulumi.set(__self__, "enabled_state", enabled_state)
        if forwarding_protocol is not None:
            pulumi.set(__self__, "forwarding_protocol", forwarding_protocol)
        if https_redirect is not None:
            pulumi.set(__self__, "https_redirect", https_redirect)
        if link_to_default_domain is not None:
            pulumi.set(__self__, "link_to_default_domain", link_to_default_domain)
        if origin_path is not None:
            pulumi.set(__self__, "origin_path", origin_path)
        if patterns_to_match is not None:
            pulumi.set(__self__, "patterns_to_match", patterns_to_match)
        if route_name is not None:
            pulumi.set(__self__, "route_name", route_name)
        if rule_sets is not None:
            pulumi.set(__self__, "rule_sets", rule_sets)
        if supported_protocols is not None:
            pulumi.set(__self__, "supported_protocols", supported_protocols)

    @property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> pulumi.Input[str]:
        """
        Name of the endpoint under the profile which is unique globally.
        """
        return pulumi.get(self, "endpoint_name")

    @endpoint_name.setter
    def endpoint_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint_name", value)

    @property
    @pulumi.getter(name="originGroup")
    def origin_group(self) -> pulumi.Input['ResourceReferenceArgs']:
        """
        A reference to the origin group.
        """
        return pulumi.get(self, "origin_group")

    @origin_group.setter
    def origin_group(self, value: pulumi.Input['ResourceReferenceArgs']):
        pulumi.set(self, "origin_group", value)

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[str]:
        """
        Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.
        """
        return pulumi.get(self, "profile_name")

    @profile_name.setter
    def profile_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "profile_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the Resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="cacheConfiguration")
    def cache_configuration(self) -> Optional[pulumi.Input['AfdRouteCacheConfigurationArgs']]:
        """
        The caching configuration for this route. To disable caching, do not provide a cacheConfiguration object.
        """
        return pulumi.get(self, "cache_configuration")

    @cache_configuration.setter
    def cache_configuration(self, value: Optional[pulumi.Input['AfdRouteCacheConfigurationArgs']]):
        pulumi.set(self, "cache_configuration", value)

    @property
    @pulumi.getter(name="customDomains")
    def custom_domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ActivatedResourceReferenceArgs']]]]:
        """
        Domains referenced by this endpoint.
        """
        return pulumi.get(self, "custom_domains")

    @custom_domains.setter
    def custom_domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ActivatedResourceReferenceArgs']]]]):
        pulumi.set(self, "custom_domains", value)

    @property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[pulumi.Input[Union[str, 'EnabledState']]]:
        """
        Whether to enable use of this rule. Permitted values are 'Enabled' or 'Disabled'
        """
        return pulumi.get(self, "enabled_state")

    @enabled_state.setter
    def enabled_state(self, value: Optional[pulumi.Input[Union[str, 'EnabledState']]]):
        pulumi.set(self, "enabled_state", value)

    @property
    @pulumi.getter(name="forwardingProtocol")
    def forwarding_protocol(self) -> Optional[pulumi.Input[Union[str, 'ForwardingProtocol']]]:
        """
        Protocol this rule will use when forwarding traffic to backends.
        """
        return pulumi.get(self, "forwarding_protocol")

    @forwarding_protocol.setter
    def forwarding_protocol(self, value: Optional[pulumi.Input[Union[str, 'ForwardingProtocol']]]):
        pulumi.set(self, "forwarding_protocol", value)

    @property
    @pulumi.getter(name="httpsRedirect")
    def https_redirect(self) -> Optional[pulumi.Input[Union[str, 'HttpsRedirect']]]:
        """
        Whether to automatically redirect HTTP traffic to HTTPS traffic. Note that this is a easy way to set up this rule and it will be the first rule that gets executed.
        """
        return pulumi.get(self, "https_redirect")

    @https_redirect.setter
    def https_redirect(self, value: Optional[pulumi.Input[Union[str, 'HttpsRedirect']]]):
        pulumi.set(self, "https_redirect", value)

    @property
    @pulumi.getter(name="linkToDefaultDomain")
    def link_to_default_domain(self) -> Optional[pulumi.Input[Union[str, 'LinkToDefaultDomain']]]:
        """
        whether this route will be linked to the default endpoint domain.
        """
        return pulumi.get(self, "link_to_default_domain")

    @link_to_default_domain.setter
    def link_to_default_domain(self, value: Optional[pulumi.Input[Union[str, 'LinkToDefaultDomain']]]):
        pulumi.set(self, "link_to_default_domain", value)

    @property
    @pulumi.getter(name="originPath")
    def origin_path(self) -> Optional[pulumi.Input[str]]:
        """
        A directory path on the origin that AzureFrontDoor can use to retrieve content from, e.g. contoso.cloudapp.net/originpath.
        """
        return pulumi.get(self, "origin_path")

    @origin_path.setter
    def origin_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "origin_path", value)

    @property
    @pulumi.getter(name="patternsToMatch")
    def patterns_to_match(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The route patterns of the rule.
        """
        return pulumi.get(self, "patterns_to_match")

    @patterns_to_match.setter
    def patterns_to_match(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "patterns_to_match", value)

    @property
    @pulumi.getter(name="routeName")
    def route_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the routing rule.
        """
        return pulumi.get(self, "route_name")

    @route_name.setter
    def route_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "route_name", value)

    @property
    @pulumi.getter(name="ruleSets")
    def rule_sets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ResourceReferenceArgs']]]]:
        """
        rule sets referenced by this endpoint.
        """
        return pulumi.get(self, "rule_sets")

    @rule_sets.setter
    def rule_sets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceReferenceArgs']]]]):
        pulumi.set(self, "rule_sets", value)

    @property
    @pulumi.getter(name="supportedProtocols")
    def supported_protocols(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AFDEndpointProtocols']]]]]:
        """
        List of supported protocols for this route.
        """
        return pulumi.get(self, "supported_protocols")

    @supported_protocols.setter
    def supported_protocols(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AFDEndpointProtocols']]]]]):
        pulumi.set(self, "supported_protocols", value)


class Route(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cache_configuration: Optional[pulumi.Input[pulumi.InputType['AfdRouteCacheConfigurationArgs']]] = None,
                 custom_domains: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ActivatedResourceReferenceArgs']]]]] = None,
                 enabled_state: Optional[pulumi.Input[Union[str, 'EnabledState']]] = None,
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 forwarding_protocol: Optional[pulumi.Input[Union[str, 'ForwardingProtocol']]] = None,
                 https_redirect: Optional[pulumi.Input[Union[str, 'HttpsRedirect']]] = None,
                 link_to_default_domain: Optional[pulumi.Input[Union[str, 'LinkToDefaultDomain']]] = None,
                 origin_group: Optional[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]] = None,
                 origin_path: Optional[pulumi.Input[str]] = None,
                 patterns_to_match: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 route_name: Optional[pulumi.Input[str]] = None,
                 rule_sets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]]]] = None,
                 supported_protocols: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AFDEndpointProtocols']]]]] = None,
                 __props__=None):
        """
        Friendly Routes name mapping to the any Routes or secret related information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AfdRouteCacheConfigurationArgs']] cache_configuration: The caching configuration for this route. To disable caching, do not provide a cacheConfiguration object.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ActivatedResourceReferenceArgs']]]] custom_domains: Domains referenced by this endpoint.
        :param pulumi.Input[Union[str, 'EnabledState']] enabled_state: Whether to enable use of this rule. Permitted values are 'Enabled' or 'Disabled'
        :param pulumi.Input[str] endpoint_name: Name of the endpoint under the profile which is unique globally.
        :param pulumi.Input[Union[str, 'ForwardingProtocol']] forwarding_protocol: Protocol this rule will use when forwarding traffic to backends.
        :param pulumi.Input[Union[str, 'HttpsRedirect']] https_redirect: Whether to automatically redirect HTTP traffic to HTTPS traffic. Note that this is a easy way to set up this rule and it will be the first rule that gets executed.
        :param pulumi.Input[Union[str, 'LinkToDefaultDomain']] link_to_default_domain: whether this route will be linked to the default endpoint domain.
        :param pulumi.Input[pulumi.InputType['ResourceReferenceArgs']] origin_group: A reference to the origin group.
        :param pulumi.Input[str] origin_path: A directory path on the origin that AzureFrontDoor can use to retrieve content from, e.g. contoso.cloudapp.net/originpath.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] patterns_to_match: The route patterns of the rule.
        :param pulumi.Input[str] profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[str] route_name: Name of the routing rule.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]]] rule_sets: rule sets referenced by this endpoint.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'AFDEndpointProtocols']]]] supported_protocols: List of supported protocols for this route.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RouteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Friendly Routes name mapping to the any Routes or secret related information.

        :param str resource_name: The name of the resource.
        :param RouteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RouteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cache_configuration: Optional[pulumi.Input[pulumi.InputType['AfdRouteCacheConfigurationArgs']]] = None,
                 custom_domains: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ActivatedResourceReferenceArgs']]]]] = None,
                 enabled_state: Optional[pulumi.Input[Union[str, 'EnabledState']]] = None,
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 forwarding_protocol: Optional[pulumi.Input[Union[str, 'ForwardingProtocol']]] = None,
                 https_redirect: Optional[pulumi.Input[Union[str, 'HttpsRedirect']]] = None,
                 link_to_default_domain: Optional[pulumi.Input[Union[str, 'LinkToDefaultDomain']]] = None,
                 origin_group: Optional[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]] = None,
                 origin_path: Optional[pulumi.Input[str]] = None,
                 patterns_to_match: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 route_name: Optional[pulumi.Input[str]] = None,
                 rule_sets: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]]]] = None,
                 supported_protocols: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'AFDEndpointProtocols']]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RouteArgs.__new__(RouteArgs)

            __props__.__dict__["cache_configuration"] = cache_configuration
            __props__.__dict__["custom_domains"] = custom_domains
            __props__.__dict__["enabled_state"] = enabled_state
            if endpoint_name is None and not opts.urn:
                raise TypeError("Missing required property 'endpoint_name'")
            __props__.__dict__["endpoint_name"] = endpoint_name
            __props__.__dict__["forwarding_protocol"] = forwarding_protocol
            __props__.__dict__["https_redirect"] = https_redirect
            __props__.__dict__["link_to_default_domain"] = link_to_default_domain
            if origin_group is None and not opts.urn:
                raise TypeError("Missing required property 'origin_group'")
            __props__.__dict__["origin_group"] = origin_group
            __props__.__dict__["origin_path"] = origin_path
            __props__.__dict__["patterns_to_match"] = patterns_to_match
            if profile_name is None and not opts.urn:
                raise TypeError("Missing required property 'profile_name'")
            __props__.__dict__["profile_name"] = profile_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["route_name"] = route_name
            __props__.__dict__["rule_sets"] = rule_sets
            __props__.__dict__["supported_protocols"] = supported_protocols
            __props__.__dict__["deployment_status"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:cdn:Route"), pulumi.Alias(type_="azure-native:cdn/v20200901:Route")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Route, __self__).__init__(
            'azure-native:cdn/v20210601:Route',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Route':
        """
        Get an existing Route resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RouteArgs.__new__(RouteArgs)

        __props__.__dict__["cache_configuration"] = None
        __props__.__dict__["custom_domains"] = None
        __props__.__dict__["deployment_status"] = None
        __props__.__dict__["enabled_state"] = None
        __props__.__dict__["endpoint_name"] = None
        __props__.__dict__["forwarding_protocol"] = None
        __props__.__dict__["https_redirect"] = None
        __props__.__dict__["link_to_default_domain"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["origin_group"] = None
        __props__.__dict__["origin_path"] = None
        __props__.__dict__["patterns_to_match"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["rule_sets"] = None
        __props__.__dict__["supported_protocols"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return Route(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cacheConfiguration")
    def cache_configuration(self) -> pulumi.Output[Optional['outputs.AfdRouteCacheConfigurationResponse']]:
        """
        The caching configuration for this route. To disable caching, do not provide a cacheConfiguration object.
        """
        return pulumi.get(self, "cache_configuration")

    @property
    @pulumi.getter(name="customDomains")
    def custom_domains(self) -> pulumi.Output[Optional[Sequence['outputs.ActivatedResourceReferenceResponse']]]:
        """
        Domains referenced by this endpoint.
        """
        return pulumi.get(self, "custom_domains")

    @property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> pulumi.Output[str]:
        return pulumi.get(self, "deployment_status")

    @property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> pulumi.Output[Optional[str]]:
        """
        Whether to enable use of this rule. Permitted values are 'Enabled' or 'Disabled'
        """
        return pulumi.get(self, "enabled_state")

    @property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> pulumi.Output[str]:
        """
        The name of the endpoint which holds the route.
        """
        return pulumi.get(self, "endpoint_name")

    @property
    @pulumi.getter(name="forwardingProtocol")
    def forwarding_protocol(self) -> pulumi.Output[Optional[str]]:
        """
        Protocol this rule will use when forwarding traffic to backends.
        """
        return pulumi.get(self, "forwarding_protocol")

    @property
    @pulumi.getter(name="httpsRedirect")
    def https_redirect(self) -> pulumi.Output[Optional[str]]:
        """
        Whether to automatically redirect HTTP traffic to HTTPS traffic. Note that this is a easy way to set up this rule and it will be the first rule that gets executed.
        """
        return pulumi.get(self, "https_redirect")

    @property
    @pulumi.getter(name="linkToDefaultDomain")
    def link_to_default_domain(self) -> pulumi.Output[Optional[str]]:
        """
        whether this route will be linked to the default endpoint domain.
        """
        return pulumi.get(self, "link_to_default_domain")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="originGroup")
    def origin_group(self) -> pulumi.Output['outputs.ResourceReferenceResponse']:
        """
        A reference to the origin group.
        """
        return pulumi.get(self, "origin_group")

    @property
    @pulumi.getter(name="originPath")
    def origin_path(self) -> pulumi.Output[Optional[str]]:
        """
        A directory path on the origin that AzureFrontDoor can use to retrieve content from, e.g. contoso.cloudapp.net/originpath.
        """
        return pulumi.get(self, "origin_path")

    @property
    @pulumi.getter(name="patternsToMatch")
    def patterns_to_match(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The route patterns of the rule.
        """
        return pulumi.get(self, "patterns_to_match")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning status
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="ruleSets")
    def rule_sets(self) -> pulumi.Output[Optional[Sequence['outputs.ResourceReferenceResponse']]]:
        """
        rule sets referenced by this endpoint.
        """
        return pulumi.get(self, "rule_sets")

    @property
    @pulumi.getter(name="supportedProtocols")
    def supported_protocols(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of supported protocols for this route.
        """
        return pulumi.get(self, "supported_protocols")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Read only system data
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

