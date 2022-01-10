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

__all__ = ['ExpressRouteCircuitArgs', 'ExpressRouteCircuit']

@pulumi.input_type
class ExpressRouteCircuitArgs:
    def __init__(__self__, *,
                 circuit_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 authorizations: Optional[pulumi.Input[Sequence[pulumi.Input['ExpressRouteCircuitAuthorizationArgs']]]] = None,
                 circuit_provisioning_state: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 peerings: Optional[pulumi.Input[Sequence[pulumi.Input['ExpressRouteCircuitPeeringArgs']]]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 service_key: Optional[pulumi.Input[str]] = None,
                 service_provider_notes: Optional[pulumi.Input[str]] = None,
                 service_provider_properties: Optional[pulumi.Input['ExpressRouteCircuitServiceProviderPropertiesArgs']] = None,
                 service_provider_provisioning_state: Optional[pulumi.Input[Union[str, 'ServiceProviderProvisioningState']]] = None,
                 sku: Optional[pulumi.Input['ExpressRouteCircuitSkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ExpressRouteCircuit resource.
        :param pulumi.Input[str] circuit_name: The name of the circuit.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Sequence[pulumi.Input['ExpressRouteCircuitAuthorizationArgs']]] authorizations: Gets or sets list of authorizations
        :param pulumi.Input[str] circuit_provisioning_state: Gets or sets CircuitProvisioningState state of the resource 
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[Sequence[pulumi.Input['ExpressRouteCircuitPeeringArgs']]] peerings: Gets or sets list of peerings
        :param pulumi.Input[str] provisioning_state: Gets or sets Provisioning state of the PublicIP resource Updating/Deleting/Failed
        :param pulumi.Input[str] service_key: Gets or sets ServiceKey
        :param pulumi.Input[str] service_provider_notes: Gets or sets ServiceProviderNotes
        :param pulumi.Input['ExpressRouteCircuitServiceProviderPropertiesArgs'] service_provider_properties: Gets or sets ServiceProviderProperties
        :param pulumi.Input[Union[str, 'ServiceProviderProvisioningState']] service_provider_provisioning_state: Gets or sets ServiceProviderProvisioningState state of the resource 
        :param pulumi.Input['ExpressRouteCircuitSkuArgs'] sku: Gets or sets sku
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "circuit_name", circuit_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if authorizations is not None:
            pulumi.set(__self__, "authorizations", authorizations)
        if circuit_provisioning_state is not None:
            pulumi.set(__self__, "circuit_provisioning_state", circuit_provisioning_state)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if peerings is not None:
            pulumi.set(__self__, "peerings", peerings)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if service_key is not None:
            pulumi.set(__self__, "service_key", service_key)
        if service_provider_notes is not None:
            pulumi.set(__self__, "service_provider_notes", service_provider_notes)
        if service_provider_properties is not None:
            pulumi.set(__self__, "service_provider_properties", service_provider_properties)
        if service_provider_provisioning_state is not None:
            pulumi.set(__self__, "service_provider_provisioning_state", service_provider_provisioning_state)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="circuitName")
    def circuit_name(self) -> pulumi.Input[str]:
        """
        The name of the circuit.
        """
        return pulumi.get(self, "circuit_name")

    @circuit_name.setter
    def circuit_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "circuit_name", value)

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
    @pulumi.getter
    def authorizations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ExpressRouteCircuitAuthorizationArgs']]]]:
        """
        Gets or sets list of authorizations
        """
        return pulumi.get(self, "authorizations")

    @authorizations.setter
    def authorizations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ExpressRouteCircuitAuthorizationArgs']]]]):
        pulumi.set(self, "authorizations", value)

    @property
    @pulumi.getter(name="circuitProvisioningState")
    def circuit_provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets CircuitProvisioningState state of the resource 
        """
        return pulumi.get(self, "circuit_provisioning_state")

    @circuit_provisioning_state.setter
    def circuit_provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "circuit_provisioning_state", value)

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
    @pulumi.getter
    def peerings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ExpressRouteCircuitPeeringArgs']]]]:
        """
        Gets or sets list of peerings
        """
        return pulumi.get(self, "peerings")

    @peerings.setter
    def peerings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ExpressRouteCircuitPeeringArgs']]]]):
        pulumi.set(self, "peerings", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets Provisioning state of the PublicIP resource Updating/Deleting/Failed
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="serviceKey")
    def service_key(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets ServiceKey
        """
        return pulumi.get(self, "service_key")

    @service_key.setter
    def service_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_key", value)

    @property
    @pulumi.getter(name="serviceProviderNotes")
    def service_provider_notes(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets ServiceProviderNotes
        """
        return pulumi.get(self, "service_provider_notes")

    @service_provider_notes.setter
    def service_provider_notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_provider_notes", value)

    @property
    @pulumi.getter(name="serviceProviderProperties")
    def service_provider_properties(self) -> Optional[pulumi.Input['ExpressRouteCircuitServiceProviderPropertiesArgs']]:
        """
        Gets or sets ServiceProviderProperties
        """
        return pulumi.get(self, "service_provider_properties")

    @service_provider_properties.setter
    def service_provider_properties(self, value: Optional[pulumi.Input['ExpressRouteCircuitServiceProviderPropertiesArgs']]):
        pulumi.set(self, "service_provider_properties", value)

    @property
    @pulumi.getter(name="serviceProviderProvisioningState")
    def service_provider_provisioning_state(self) -> Optional[pulumi.Input[Union[str, 'ServiceProviderProvisioningState']]]:
        """
        Gets or sets ServiceProviderProvisioningState state of the resource 
        """
        return pulumi.get(self, "service_provider_provisioning_state")

    @service_provider_provisioning_state.setter
    def service_provider_provisioning_state(self, value: Optional[pulumi.Input[Union[str, 'ServiceProviderProvisioningState']]]):
        pulumi.set(self, "service_provider_provisioning_state", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['ExpressRouteCircuitSkuArgs']]:
        """
        Gets or sets sku
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['ExpressRouteCircuitSkuArgs']]):
        pulumi.set(self, "sku", value)

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


class ExpressRouteCircuit(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorizations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExpressRouteCircuitAuthorizationArgs']]]]] = None,
                 circuit_name: Optional[pulumi.Input[str]] = None,
                 circuit_provisioning_state: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 peerings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExpressRouteCircuitPeeringArgs']]]]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_key: Optional[pulumi.Input[str]] = None,
                 service_provider_notes: Optional[pulumi.Input[str]] = None,
                 service_provider_properties: Optional[pulumi.Input[pulumi.InputType['ExpressRouteCircuitServiceProviderPropertiesArgs']]] = None,
                 service_provider_provisioning_state: Optional[pulumi.Input[Union[str, 'ServiceProviderProvisioningState']]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['ExpressRouteCircuitSkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        ExpressRouteCircuit resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExpressRouteCircuitAuthorizationArgs']]]] authorizations: Gets or sets list of authorizations
        :param pulumi.Input[str] circuit_name: The name of the circuit.
        :param pulumi.Input[str] circuit_provisioning_state: Gets or sets CircuitProvisioningState state of the resource 
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExpressRouteCircuitPeeringArgs']]]] peerings: Gets or sets list of peerings
        :param pulumi.Input[str] provisioning_state: Gets or sets Provisioning state of the PublicIP resource Updating/Deleting/Failed
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_key: Gets or sets ServiceKey
        :param pulumi.Input[str] service_provider_notes: Gets or sets ServiceProviderNotes
        :param pulumi.Input[pulumi.InputType['ExpressRouteCircuitServiceProviderPropertiesArgs']] service_provider_properties: Gets or sets ServiceProviderProperties
        :param pulumi.Input[Union[str, 'ServiceProviderProvisioningState']] service_provider_provisioning_state: Gets or sets ServiceProviderProvisioningState state of the resource 
        :param pulumi.Input[pulumi.InputType['ExpressRouteCircuitSkuArgs']] sku: Gets or sets sku
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExpressRouteCircuitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ExpressRouteCircuit resource

        :param str resource_name: The name of the resource.
        :param ExpressRouteCircuitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExpressRouteCircuitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorizations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExpressRouteCircuitAuthorizationArgs']]]]] = None,
                 circuit_name: Optional[pulumi.Input[str]] = None,
                 circuit_provisioning_state: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 peerings: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExpressRouteCircuitPeeringArgs']]]]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_key: Optional[pulumi.Input[str]] = None,
                 service_provider_notes: Optional[pulumi.Input[str]] = None,
                 service_provider_properties: Optional[pulumi.Input[pulumi.InputType['ExpressRouteCircuitServiceProviderPropertiesArgs']]] = None,
                 service_provider_provisioning_state: Optional[pulumi.Input[Union[str, 'ServiceProviderProvisioningState']]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['ExpressRouteCircuitSkuArgs']]] = None,
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
            __props__ = ExpressRouteCircuitArgs.__new__(ExpressRouteCircuitArgs)

            __props__.__dict__["authorizations"] = authorizations
            if circuit_name is None and not opts.urn:
                raise TypeError("Missing required property 'circuit_name'")
            __props__.__dict__["circuit_name"] = circuit_name
            __props__.__dict__["circuit_provisioning_state"] = circuit_provisioning_state
            __props__.__dict__["location"] = location
            __props__.__dict__["peerings"] = peerings
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["service_key"] = service_key
            __props__.__dict__["service_provider_notes"] = service_provider_notes
            __props__.__dict__["service_provider_properties"] = service_provider_properties
            __props__.__dict__["service_provider_provisioning_state"] = service_provider_provisioning_state
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20150615:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20160330:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20160601:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20160901:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20161201:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20170301:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20170601:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20170801:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20170901:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20171001:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20171101:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20180101:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20180201:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20180401:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20180601:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20180701:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20180801:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20181001:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20181101:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20181201:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20190201:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20190401:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20190601:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20190701:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20190801:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20190901:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20191101:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20191201:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20200301:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20200401:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20200501:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20200601:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20200701:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20200801:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20201101:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20210201:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20210301:ExpressRouteCircuit"), pulumi.Alias(type_="azure-native:network/v20210501:ExpressRouteCircuit")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ExpressRouteCircuit, __self__).__init__(
            'azure-native:network/v20150501preview:ExpressRouteCircuit',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ExpressRouteCircuit':
        """
        Get an existing ExpressRouteCircuit resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ExpressRouteCircuitArgs.__new__(ExpressRouteCircuitArgs)

        __props__.__dict__["authorizations"] = None
        __props__.__dict__["circuit_provisioning_state"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["peerings"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["service_key"] = None
        __props__.__dict__["service_provider_notes"] = None
        __props__.__dict__["service_provider_properties"] = None
        __props__.__dict__["service_provider_provisioning_state"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return ExpressRouteCircuit(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def authorizations(self) -> pulumi.Output[Optional[Sequence['outputs.ExpressRouteCircuitAuthorizationResponse']]]:
        """
        Gets or sets list of authorizations
        """
        return pulumi.get(self, "authorizations")

    @property
    @pulumi.getter(name="circuitProvisioningState")
    def circuit_provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets CircuitProvisioningState state of the resource 
        """
        return pulumi.get(self, "circuit_provisioning_state")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Gets a unique read-only string that changes whenever the resource is updated
        """
        return pulumi.get(self, "etag")

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
    @pulumi.getter
    def peerings(self) -> pulumi.Output[Optional[Sequence['outputs.ExpressRouteCircuitPeeringResponse']]]:
        """
        Gets or sets list of peerings
        """
        return pulumi.get(self, "peerings")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets Provisioning state of the PublicIP resource Updating/Deleting/Failed
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serviceKey")
    def service_key(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets ServiceKey
        """
        return pulumi.get(self, "service_key")

    @property
    @pulumi.getter(name="serviceProviderNotes")
    def service_provider_notes(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets ServiceProviderNotes
        """
        return pulumi.get(self, "service_provider_notes")

    @property
    @pulumi.getter(name="serviceProviderProperties")
    def service_provider_properties(self) -> pulumi.Output[Optional['outputs.ExpressRouteCircuitServiceProviderPropertiesResponse']]:
        """
        Gets or sets ServiceProviderProperties
        """
        return pulumi.get(self, "service_provider_properties")

    @property
    @pulumi.getter(name="serviceProviderProvisioningState")
    def service_provider_provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets ServiceProviderProvisioningState state of the resource 
        """
        return pulumi.get(self, "service_provider_provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.ExpressRouteCircuitSkuResponse']]:
        """
        Gets or sets sku
        """
        return pulumi.get(self, "sku")

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

