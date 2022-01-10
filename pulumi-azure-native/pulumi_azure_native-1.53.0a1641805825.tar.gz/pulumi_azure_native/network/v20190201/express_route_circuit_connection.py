# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ExpressRouteCircuitConnectionInitArgs', 'ExpressRouteCircuitConnection']

@pulumi.input_type
class ExpressRouteCircuitConnectionInitArgs:
    def __init__(__self__, *,
                 circuit_name: pulumi.Input[str],
                 peering_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 address_prefix: Optional[pulumi.Input[str]] = None,
                 authorization_key: Optional[pulumi.Input[str]] = None,
                 connection_name: Optional[pulumi.Input[str]] = None,
                 express_route_circuit_peering: Optional[pulumi.Input['SubResourceArgs']] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peer_express_route_circuit_peering: Optional[pulumi.Input['SubResourceArgs']] = None):
        """
        The set of arguments for constructing a ExpressRouteCircuitConnection resource.
        :param pulumi.Input[str] circuit_name: The name of the express route circuit.
        :param pulumi.Input[str] peering_name: The name of the peering.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] address_prefix: /29 IP address space to carve out Customer addresses for tunnels.
        :param pulumi.Input[str] authorization_key: The authorization key.
        :param pulumi.Input[str] connection_name: The name of the express route circuit connection.
        :param pulumi.Input['SubResourceArgs'] express_route_circuit_peering: Reference to Express Route Circuit Private Peering Resource of the circuit initiating connection.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
        :param pulumi.Input['SubResourceArgs'] peer_express_route_circuit_peering: Reference to Express Route Circuit Private Peering Resource of the peered circuit.
        """
        pulumi.set(__self__, "circuit_name", circuit_name)
        pulumi.set(__self__, "peering_name", peering_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if address_prefix is not None:
            pulumi.set(__self__, "address_prefix", address_prefix)
        if authorization_key is not None:
            pulumi.set(__self__, "authorization_key", authorization_key)
        if connection_name is not None:
            pulumi.set(__self__, "connection_name", connection_name)
        if express_route_circuit_peering is not None:
            pulumi.set(__self__, "express_route_circuit_peering", express_route_circuit_peering)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if peer_express_route_circuit_peering is not None:
            pulumi.set(__self__, "peer_express_route_circuit_peering", peer_express_route_circuit_peering)

    @property
    @pulumi.getter(name="circuitName")
    def circuit_name(self) -> pulumi.Input[str]:
        """
        The name of the express route circuit.
        """
        return pulumi.get(self, "circuit_name")

    @circuit_name.setter
    def circuit_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "circuit_name", value)

    @property
    @pulumi.getter(name="peeringName")
    def peering_name(self) -> pulumi.Input[str]:
        """
        The name of the peering.
        """
        return pulumi.get(self, "peering_name")

    @peering_name.setter
    def peering_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "peering_name", value)

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
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        /29 IP address space to carve out Customer addresses for tunnels.
        """
        return pulumi.get(self, "address_prefix")

    @address_prefix.setter
    def address_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address_prefix", value)

    @property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> Optional[pulumi.Input[str]]:
        """
        The authorization key.
        """
        return pulumi.get(self, "authorization_key")

    @authorization_key.setter
    def authorization_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorization_key", value)

    @property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the express route circuit connection.
        """
        return pulumi.get(self, "connection_name")

    @connection_name.setter
    def connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_name", value)

    @property
    @pulumi.getter(name="expressRouteCircuitPeering")
    def express_route_circuit_peering(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        Reference to Express Route Circuit Private Peering Resource of the circuit initiating connection.
        """
        return pulumi.get(self, "express_route_circuit_peering")

    @express_route_circuit_peering.setter
    def express_route_circuit_peering(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "express_route_circuit_peering", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="peerExpressRouteCircuitPeering")
    def peer_express_route_circuit_peering(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        Reference to Express Route Circuit Private Peering Resource of the peered circuit.
        """
        return pulumi.get(self, "peer_express_route_circuit_peering")

    @peer_express_route_circuit_peering.setter
    def peer_express_route_circuit_peering(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "peer_express_route_circuit_peering", value)


class ExpressRouteCircuitConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_prefix: Optional[pulumi.Input[str]] = None,
                 authorization_key: Optional[pulumi.Input[str]] = None,
                 circuit_name: Optional[pulumi.Input[str]] = None,
                 connection_name: Optional[pulumi.Input[str]] = None,
                 express_route_circuit_peering: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peer_express_route_circuit_peering: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 peering_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Express Route Circuit Connection in an ExpressRouteCircuitPeering resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address_prefix: /29 IP address space to carve out Customer addresses for tunnels.
        :param pulumi.Input[str] authorization_key: The authorization key.
        :param pulumi.Input[str] circuit_name: The name of the express route circuit.
        :param pulumi.Input[str] connection_name: The name of the express route circuit connection.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] express_route_circuit_peering: Reference to Express Route Circuit Private Peering Resource of the circuit initiating connection.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
        :param pulumi.Input[pulumi.InputType['SubResourceArgs']] peer_express_route_circuit_peering: Reference to Express Route Circuit Private Peering Resource of the peered circuit.
        :param pulumi.Input[str] peering_name: The name of the peering.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExpressRouteCircuitConnectionInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Express Route Circuit Connection in an ExpressRouteCircuitPeering resource.

        :param str resource_name: The name of the resource.
        :param ExpressRouteCircuitConnectionInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExpressRouteCircuitConnectionInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address_prefix: Optional[pulumi.Input[str]] = None,
                 authorization_key: Optional[pulumi.Input[str]] = None,
                 circuit_name: Optional[pulumi.Input[str]] = None,
                 connection_name: Optional[pulumi.Input[str]] = None,
                 express_route_circuit_peering: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peer_express_route_circuit_peering: Optional[pulumi.Input[pulumi.InputType['SubResourceArgs']]] = None,
                 peering_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ExpressRouteCircuitConnectionInitArgs.__new__(ExpressRouteCircuitConnectionInitArgs)

            __props__.__dict__["address_prefix"] = address_prefix
            __props__.__dict__["authorization_key"] = authorization_key
            if circuit_name is None and not opts.urn:
                raise TypeError("Missing required property 'circuit_name'")
            __props__.__dict__["circuit_name"] = circuit_name
            __props__.__dict__["connection_name"] = connection_name
            __props__.__dict__["express_route_circuit_peering"] = express_route_circuit_peering
            __props__.__dict__["id"] = id
            __props__.__dict__["name"] = name
            __props__.__dict__["peer_express_route_circuit_peering"] = peer_express_route_circuit_peering
            if peering_name is None and not opts.urn:
                raise TypeError("Missing required property 'peering_name'")
            __props__.__dict__["peering_name"] = peering_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["circuit_connection_status"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["provisioning_state"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20180201:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20180401:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20180601:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20180701:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20180801:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20181001:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20181101:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20181201:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20190401:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20190601:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20190701:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20190801:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20190901:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20191101:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20191201:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20200301:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20200401:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20200501:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20200601:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20200701:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20200801:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20201101:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20210201:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20210301:ExpressRouteCircuitConnection"), pulumi.Alias(type_="azure-native:network/v20210501:ExpressRouteCircuitConnection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ExpressRouteCircuitConnection, __self__).__init__(
            'azure-native:network/v20190201:ExpressRouteCircuitConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ExpressRouteCircuitConnection':
        """
        Get an existing ExpressRouteCircuitConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ExpressRouteCircuitConnectionInitArgs.__new__(ExpressRouteCircuitConnectionInitArgs)

        __props__.__dict__["address_prefix"] = None
        __props__.__dict__["authorization_key"] = None
        __props__.__dict__["circuit_connection_status"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["express_route_circuit_peering"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["peer_express_route_circuit_peering"] = None
        __props__.__dict__["provisioning_state"] = None
        return ExpressRouteCircuitConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        /29 IP address space to carve out Customer addresses for tunnels.
        """
        return pulumi.get(self, "address_prefix")

    @property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> pulumi.Output[Optional[str]]:
        """
        The authorization key.
        """
        return pulumi.get(self, "authorization_key")

    @property
    @pulumi.getter(name="circuitConnectionStatus")
    def circuit_connection_status(self) -> pulumi.Output[str]:
        """
        Express Route Circuit connection state.
        """
        return pulumi.get(self, "circuit_connection_status")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="expressRouteCircuitPeering")
    def express_route_circuit_peering(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        Reference to Express Route Circuit Private Peering Resource of the circuit initiating connection.
        """
        return pulumi.get(self, "express_route_circuit_peering")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Gets name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peerExpressRouteCircuitPeering")
    def peer_express_route_circuit_peering(self) -> pulumi.Output[Optional['outputs.SubResourceResponse']]:
        """
        Reference to Express Route Circuit Private Peering Resource of the peered circuit.
        """
        return pulumi.get(self, "peer_express_route_circuit_peering")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the circuit connection resource. Possible values are: 'Succeeded', 'Updating', 'Deleting', and 'Failed'.
        """
        return pulumi.get(self, "provisioning_state")

