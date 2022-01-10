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

__all__ = ['ApplicationGatewayArgs', 'ApplicationGateway']

@pulumi.input_type
class ApplicationGatewayArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 application_gateway_name: Optional[pulumi.Input[str]] = None,
                 backend_address_pools: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayBackendAddressPoolArgs']]]] = None,
                 backend_http_settings_collection: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayBackendHttpSettingsArgs']]]] = None,
                 frontend_ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayFrontendIPConfigurationArgs']]]] = None,
                 frontend_ports: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayFrontendPortArgs']]]] = None,
                 gateway_ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayIPConfigurationArgs']]]] = None,
                 http_listeners: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayHttpListenerArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 request_routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayRequestRoutingRuleArgs']]]] = None,
                 resource_guid: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['ApplicationGatewaySkuArgs']] = None,
                 ssl_certificates: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewaySslCertificateArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ApplicationGateway resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] application_gateway_name: The name of the ApplicationGateway.
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayBackendAddressPoolArgs']]] backend_address_pools: Gets or sets backend address pool of application gateway resource
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayBackendHttpSettingsArgs']]] backend_http_settings_collection: Gets or sets backend http settings of application gateway resource
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayFrontendIPConfigurationArgs']]] frontend_ip_configurations: Gets or sets frontend IP addresses of application gateway resource
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayFrontendPortArgs']]] frontend_ports: Gets or sets frontend ports of application gateway resource
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayIPConfigurationArgs']]] gateway_ip_configurations: Gets or sets subnets of application gateway resource
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayHttpListenerArgs']]] http_listeners: Gets or sets HTTP listeners of application gateway resource
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] provisioning_state: Gets or sets Provisioning state of the ApplicationGateway resource Updating/Deleting/Failed
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayRequestRoutingRuleArgs']]] request_routing_rules: Gets or sets request routing rules of application gateway resource
        :param pulumi.Input[str] resource_guid: Gets or sets resource guid property of the ApplicationGateway resource
        :param pulumi.Input['ApplicationGatewaySkuArgs'] sku: Gets or sets sku of application gateway resource
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationGatewaySslCertificateArgs']]] ssl_certificates: Gets or sets ssl certificates of application gateway resource
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if application_gateway_name is not None:
            pulumi.set(__self__, "application_gateway_name", application_gateway_name)
        if backend_address_pools is not None:
            pulumi.set(__self__, "backend_address_pools", backend_address_pools)
        if backend_http_settings_collection is not None:
            pulumi.set(__self__, "backend_http_settings_collection", backend_http_settings_collection)
        if frontend_ip_configurations is not None:
            pulumi.set(__self__, "frontend_ip_configurations", frontend_ip_configurations)
        if frontend_ports is not None:
            pulumi.set(__self__, "frontend_ports", frontend_ports)
        if gateway_ip_configurations is not None:
            pulumi.set(__self__, "gateway_ip_configurations", gateway_ip_configurations)
        if http_listeners is not None:
            pulumi.set(__self__, "http_listeners", http_listeners)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if request_routing_rules is not None:
            pulumi.set(__self__, "request_routing_rules", request_routing_rules)
        if resource_guid is not None:
            pulumi.set(__self__, "resource_guid", resource_guid)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if ssl_certificates is not None:
            pulumi.set(__self__, "ssl_certificates", ssl_certificates)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="applicationGatewayName")
    def application_gateway_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the ApplicationGateway.
        """
        return pulumi.get(self, "application_gateway_name")

    @application_gateway_name.setter
    def application_gateway_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_gateway_name", value)

    @property
    @pulumi.getter(name="backendAddressPools")
    def backend_address_pools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayBackendAddressPoolArgs']]]]:
        """
        Gets or sets backend address pool of application gateway resource
        """
        return pulumi.get(self, "backend_address_pools")

    @backend_address_pools.setter
    def backend_address_pools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayBackendAddressPoolArgs']]]]):
        pulumi.set(self, "backend_address_pools", value)

    @property
    @pulumi.getter(name="backendHttpSettingsCollection")
    def backend_http_settings_collection(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayBackendHttpSettingsArgs']]]]:
        """
        Gets or sets backend http settings of application gateway resource
        """
        return pulumi.get(self, "backend_http_settings_collection")

    @backend_http_settings_collection.setter
    def backend_http_settings_collection(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayBackendHttpSettingsArgs']]]]):
        pulumi.set(self, "backend_http_settings_collection", value)

    @property
    @pulumi.getter(name="frontendIPConfigurations")
    def frontend_ip_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayFrontendIPConfigurationArgs']]]]:
        """
        Gets or sets frontend IP addresses of application gateway resource
        """
        return pulumi.get(self, "frontend_ip_configurations")

    @frontend_ip_configurations.setter
    def frontend_ip_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayFrontendIPConfigurationArgs']]]]):
        pulumi.set(self, "frontend_ip_configurations", value)

    @property
    @pulumi.getter(name="frontendPorts")
    def frontend_ports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayFrontendPortArgs']]]]:
        """
        Gets or sets frontend ports of application gateway resource
        """
        return pulumi.get(self, "frontend_ports")

    @frontend_ports.setter
    def frontend_ports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayFrontendPortArgs']]]]):
        pulumi.set(self, "frontend_ports", value)

    @property
    @pulumi.getter(name="gatewayIPConfigurations")
    def gateway_ip_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayIPConfigurationArgs']]]]:
        """
        Gets or sets subnets of application gateway resource
        """
        return pulumi.get(self, "gateway_ip_configurations")

    @gateway_ip_configurations.setter
    def gateway_ip_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayIPConfigurationArgs']]]]):
        pulumi.set(self, "gateway_ip_configurations", value)

    @property
    @pulumi.getter(name="httpListeners")
    def http_listeners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayHttpListenerArgs']]]]:
        """
        Gets or sets HTTP listeners of application gateway resource
        """
        return pulumi.get(self, "http_listeners")

    @http_listeners.setter
    def http_listeners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayHttpListenerArgs']]]]):
        pulumi.set(self, "http_listeners", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets Provisioning state of the ApplicationGateway resource Updating/Deleting/Failed
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="requestRoutingRules")
    def request_routing_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayRequestRoutingRuleArgs']]]]:
        """
        Gets or sets request routing rules of application gateway resource
        """
        return pulumi.get(self, "request_routing_rules")

    @request_routing_rules.setter
    def request_routing_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayRequestRoutingRuleArgs']]]]):
        pulumi.set(self, "request_routing_rules", value)

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets resource guid property of the ApplicationGateway resource
        """
        return pulumi.get(self, "resource_guid")

    @resource_guid.setter
    def resource_guid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_guid", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['ApplicationGatewaySkuArgs']]:
        """
        Gets or sets sku of application gateway resource
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['ApplicationGatewaySkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="sslCertificates")
    def ssl_certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewaySslCertificateArgs']]]]:
        """
        Gets or sets ssl certificates of application gateway resource
        """
        return pulumi.get(self, "ssl_certificates")

    @ssl_certificates.setter
    def ssl_certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewaySslCertificateArgs']]]]):
        pulumi.set(self, "ssl_certificates", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class ApplicationGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_gateway_name: Optional[pulumi.Input[str]] = None,
                 backend_address_pools: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendAddressPoolArgs']]]]] = None,
                 backend_http_settings_collection: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendHttpSettingsArgs']]]]] = None,
                 frontend_ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendIPConfigurationArgs']]]]] = None,
                 frontend_ports: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendPortArgs']]]]] = None,
                 gateway_ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayIPConfigurationArgs']]]]] = None,
                 http_listeners: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayHttpListenerArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 request_routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRequestRoutingRuleArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_guid: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['ApplicationGatewaySkuArgs']]] = None,
                 ssl_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewaySslCertificateArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        ApplicationGateways resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_gateway_name: The name of the ApplicationGateway.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendAddressPoolArgs']]]] backend_address_pools: Gets or sets backend address pool of application gateway resource
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendHttpSettingsArgs']]]] backend_http_settings_collection: Gets or sets backend http settings of application gateway resource
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendIPConfigurationArgs']]]] frontend_ip_configurations: Gets or sets frontend IP addresses of application gateway resource
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendPortArgs']]]] frontend_ports: Gets or sets frontend ports of application gateway resource
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayIPConfigurationArgs']]]] gateway_ip_configurations: Gets or sets subnets of application gateway resource
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayHttpListenerArgs']]]] http_listeners: Gets or sets HTTP listeners of application gateway resource
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] provisioning_state: Gets or sets Provisioning state of the ApplicationGateway resource Updating/Deleting/Failed
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRequestRoutingRuleArgs']]]] request_routing_rules: Gets or sets request routing rules of application gateway resource
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] resource_guid: Gets or sets resource guid property of the ApplicationGateway resource
        :param pulumi.Input[pulumi.InputType['ApplicationGatewaySkuArgs']] sku: Gets or sets sku of application gateway resource
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewaySslCertificateArgs']]]] ssl_certificates: Gets or sets ssl certificates of application gateway resource
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplicationGatewayArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ApplicationGateways resource

        :param str resource_name: The name of the resource.
        :param ApplicationGatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationGatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_gateway_name: Optional[pulumi.Input[str]] = None,
                 backend_address_pools: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendAddressPoolArgs']]]]] = None,
                 backend_http_settings_collection: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendHttpSettingsArgs']]]]] = None,
                 frontend_ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendIPConfigurationArgs']]]]] = None,
                 frontend_ports: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendPortArgs']]]]] = None,
                 gateway_ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayIPConfigurationArgs']]]]] = None,
                 http_listeners: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayHttpListenerArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 request_routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRequestRoutingRuleArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_guid: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['ApplicationGatewaySkuArgs']]] = None,
                 ssl_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewaySslCertificateArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = ApplicationGatewayArgs.__new__(ApplicationGatewayArgs)

            __props__.__dict__["application_gateway_name"] = application_gateway_name
            __props__.__dict__["backend_address_pools"] = backend_address_pools
            __props__.__dict__["backend_http_settings_collection"] = backend_http_settings_collection
            __props__.__dict__["frontend_ip_configurations"] = frontend_ip_configurations
            __props__.__dict__["frontend_ports"] = frontend_ports
            __props__.__dict__["gateway_ip_configurations"] = gateway_ip_configurations
            __props__.__dict__["http_listeners"] = http_listeners
            __props__.__dict__["location"] = location
            __props__.__dict__["provisioning_state"] = provisioning_state
            __props__.__dict__["request_routing_rules"] = request_routing_rules
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_guid"] = resource_guid
            __props__.__dict__["sku"] = sku
            __props__.__dict__["ssl_certificates"] = ssl_certificates
            __props__.__dict__["tags"] = tags
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["operational_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20150615:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20160330:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20160601:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20160901:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20161201:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20170301:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20170601:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20170801:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20170901:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20171001:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20171101:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20180101:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20180201:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20180401:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20180601:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20180701:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20180801:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20181001:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20181101:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20181201:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20190201:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20190401:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20190601:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20190701:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20190801:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20190901:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20191101:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20191201:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20200301:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20200401:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20200501:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20200601:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20200701:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20200801:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20201101:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20210201:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20210301:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20210501:ApplicationGateway")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ApplicationGateway, __self__).__init__(
            'azure-native:network/v20150501preview:ApplicationGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ApplicationGateway':
        """
        Get an existing ApplicationGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApplicationGatewayArgs.__new__(ApplicationGatewayArgs)

        __props__.__dict__["backend_address_pools"] = None
        __props__.__dict__["backend_http_settings_collection"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["frontend_ip_configurations"] = None
        __props__.__dict__["frontend_ports"] = None
        __props__.__dict__["gateway_ip_configurations"] = None
        __props__.__dict__["http_listeners"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["operational_state"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["request_routing_rules"] = None
        __props__.__dict__["resource_guid"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["ssl_certificates"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return ApplicationGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backendAddressPools")
    def backend_address_pools(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayBackendAddressPoolResponse']]]:
        """
        Gets or sets backend address pool of application gateway resource
        """
        return pulumi.get(self, "backend_address_pools")

    @property
    @pulumi.getter(name="backendHttpSettingsCollection")
    def backend_http_settings_collection(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayBackendHttpSettingsResponse']]]:
        """
        Gets or sets backend http settings of application gateway resource
        """
        return pulumi.get(self, "backend_http_settings_collection")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Gets a unique read-only string that changes whenever the resource is updated
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="frontendIPConfigurations")
    def frontend_ip_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayFrontendIPConfigurationResponse']]]:
        """
        Gets or sets frontend IP addresses of application gateway resource
        """
        return pulumi.get(self, "frontend_ip_configurations")

    @property
    @pulumi.getter(name="frontendPorts")
    def frontend_ports(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayFrontendPortResponse']]]:
        """
        Gets or sets frontend ports of application gateway resource
        """
        return pulumi.get(self, "frontend_ports")

    @property
    @pulumi.getter(name="gatewayIPConfigurations")
    def gateway_ip_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayIPConfigurationResponse']]]:
        """
        Gets or sets subnets of application gateway resource
        """
        return pulumi.get(self, "gateway_ip_configurations")

    @property
    @pulumi.getter(name="httpListeners")
    def http_listeners(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayHttpListenerResponse']]]:
        """
        Gets or sets HTTP listeners of application gateway resource
        """
        return pulumi.get(self, "http_listeners")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="operationalState")
    def operational_state(self) -> pulumi.Output[str]:
        """
        Gets operational state of application gateway resource
        """
        return pulumi.get(self, "operational_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets Provisioning state of the ApplicationGateway resource Updating/Deleting/Failed
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="requestRoutingRules")
    def request_routing_rules(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayRequestRoutingRuleResponse']]]:
        """
        Gets or sets request routing rules of application gateway resource
        """
        return pulumi.get(self, "request_routing_rules")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets resource guid property of the ApplicationGateway resource
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.ApplicationGatewaySkuResponse']]:
        """
        Gets or sets sku of application gateway resource
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="sslCertificates")
    def ssl_certificates(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewaySslCertificateResponse']]]:
        """
        Gets or sets ssl certificates of application gateway resource
        """
        return pulumi.get(self, "ssl_certificates")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

