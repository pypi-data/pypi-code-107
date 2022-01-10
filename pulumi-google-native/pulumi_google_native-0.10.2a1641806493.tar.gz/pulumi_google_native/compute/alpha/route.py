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

__all__ = ['RouteArgs', 'Route']

@pulumi.input_type
class RouteArgs:
    def __init__(__self__, *,
                 allow_conflicting_subnetworks: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dest_range: Optional[pulumi.Input[str]] = None,
                 ilb_route_behavior_on_unhealthy: Optional[pulumi.Input['RouteIlbRouteBehaviorOnUnhealthy']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 next_hop_gateway: Optional[pulumi.Input[str]] = None,
                 next_hop_ilb: Optional[pulumi.Input[str]] = None,
                 next_hop_instance: Optional[pulumi.Input[str]] = None,
                 next_hop_ip: Optional[pulumi.Input[str]] = None,
                 next_hop_network: Optional[pulumi.Input[str]] = None,
                 next_hop_vpn_tunnel: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Route resource.
        :param pulumi.Input[bool] allow_conflicting_subnetworks: Whether this route can conflict with existing subnetworks. Setting this to true allows this route to conflict with subnetworks that have already been configured on the corresponding network.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this field when you create the resource.
        :param pulumi.Input[str] dest_range: The destination range of outgoing packets that this route applies to. Both IPv4 and IPv6 are supported.
        :param pulumi.Input['RouteIlbRouteBehaviorOnUnhealthy'] ilb_route_behavior_on_unhealthy: ILB route behavior when ILB is deemed unhealthy based on user specified threshold on the Backend Service of the internal load balancing.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`. The first character must be a lowercase letter, and all following characters (except for the last character) must be a dash, lowercase letter, or digit. The last character must be a lowercase letter or digit.
        :param pulumi.Input[str] network: Fully-qualified URL of the network that this route applies to.
        :param pulumi.Input[str] next_hop_gateway: The URL to a gateway that should handle matching packets. You can only specify the internet gateway using a full or partial valid URL: projects/ project/global/gateways/default-internet-gateway
        :param pulumi.Input[str] next_hop_ilb: The URL to a forwarding rule of type loadBalancingScheme=INTERNAL that should handle matching packets or the IP address of the forwarding Rule. For example, the following are all valid URLs: - 10.128.0.56 - https://www.googleapis.com/compute/v1/projects/project/regions/region /forwardingRules/forwardingRule - regions/region/forwardingRules/forwardingRule 
        :param pulumi.Input[str] next_hop_instance: The URL to an instance that should handle matching packets. You can specify this as a full or partial URL. For example: https://www.googleapis.com/compute/v1/projects/project/zones/zone/instances/
        :param pulumi.Input[str] next_hop_ip: The network IP address of an instance that should handle matching packets. Only IPv4 is supported.
        :param pulumi.Input[str] next_hop_network: The URL of the local network if it should handle matching packets.
        :param pulumi.Input[str] next_hop_vpn_tunnel: The URL to a VpnTunnel that should handle matching packets.
        :param pulumi.Input[int] priority: The priority of this route. Priority is used to break ties in cases where there is more than one matching route of equal prefix length. In cases where multiple routes have equal prefix length, the one with the lowest-numbered priority value wins. The default value is `1000`. The priority value must be from `0` to `65535`, inclusive.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A list of instance tags to which this route applies.
        """
        if allow_conflicting_subnetworks is not None:
            pulumi.set(__self__, "allow_conflicting_subnetworks", allow_conflicting_subnetworks)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if dest_range is not None:
            pulumi.set(__self__, "dest_range", dest_range)
        if ilb_route_behavior_on_unhealthy is not None:
            pulumi.set(__self__, "ilb_route_behavior_on_unhealthy", ilb_route_behavior_on_unhealthy)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if network is not None:
            pulumi.set(__self__, "network", network)
        if next_hop_gateway is not None:
            pulumi.set(__self__, "next_hop_gateway", next_hop_gateway)
        if next_hop_ilb is not None:
            pulumi.set(__self__, "next_hop_ilb", next_hop_ilb)
        if next_hop_instance is not None:
            pulumi.set(__self__, "next_hop_instance", next_hop_instance)
        if next_hop_ip is not None:
            pulumi.set(__self__, "next_hop_ip", next_hop_ip)
        if next_hop_network is not None:
            pulumi.set(__self__, "next_hop_network", next_hop_network)
        if next_hop_vpn_tunnel is not None:
            pulumi.set(__self__, "next_hop_vpn_tunnel", next_hop_vpn_tunnel)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if request_id is not None:
            pulumi.set(__self__, "request_id", request_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="allowConflictingSubnetworks")
    def allow_conflicting_subnetworks(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether this route can conflict with existing subnetworks. Setting this to true allows this route to conflict with subnetworks that have already been configured on the corresponding network.
        """
        return pulumi.get(self, "allow_conflicting_subnetworks")

    @allow_conflicting_subnetworks.setter
    def allow_conflicting_subnetworks(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_conflicting_subnetworks", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional description of this resource. Provide this field when you create the resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="destRange")
    def dest_range(self) -> Optional[pulumi.Input[str]]:
        """
        The destination range of outgoing packets that this route applies to. Both IPv4 and IPv6 are supported.
        """
        return pulumi.get(self, "dest_range")

    @dest_range.setter
    def dest_range(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dest_range", value)

    @property
    @pulumi.getter(name="ilbRouteBehaviorOnUnhealthy")
    def ilb_route_behavior_on_unhealthy(self) -> Optional[pulumi.Input['RouteIlbRouteBehaviorOnUnhealthy']]:
        """
        ILB route behavior when ILB is deemed unhealthy based on user specified threshold on the Backend Service of the internal load balancing.
        """
        return pulumi.get(self, "ilb_route_behavior_on_unhealthy")

    @ilb_route_behavior_on_unhealthy.setter
    def ilb_route_behavior_on_unhealthy(self, value: Optional[pulumi.Input['RouteIlbRouteBehaviorOnUnhealthy']]):
        pulumi.set(self, "ilb_route_behavior_on_unhealthy", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`. The first character must be a lowercase letter, and all following characters (except for the last character) must be a dash, lowercase letter, or digit. The last character must be a lowercase letter or digit.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[str]]:
        """
        Fully-qualified URL of the network that this route applies to.
        """
        return pulumi.get(self, "network")

    @network.setter
    def network(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network", value)

    @property
    @pulumi.getter(name="nextHopGateway")
    def next_hop_gateway(self) -> Optional[pulumi.Input[str]]:
        """
        The URL to a gateway that should handle matching packets. You can only specify the internet gateway using a full or partial valid URL: projects/ project/global/gateways/default-internet-gateway
        """
        return pulumi.get(self, "next_hop_gateway")

    @next_hop_gateway.setter
    def next_hop_gateway(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "next_hop_gateway", value)

    @property
    @pulumi.getter(name="nextHopIlb")
    def next_hop_ilb(self) -> Optional[pulumi.Input[str]]:
        """
        The URL to a forwarding rule of type loadBalancingScheme=INTERNAL that should handle matching packets or the IP address of the forwarding Rule. For example, the following are all valid URLs: - 10.128.0.56 - https://www.googleapis.com/compute/v1/projects/project/regions/region /forwardingRules/forwardingRule - regions/region/forwardingRules/forwardingRule 
        """
        return pulumi.get(self, "next_hop_ilb")

    @next_hop_ilb.setter
    def next_hop_ilb(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "next_hop_ilb", value)

    @property
    @pulumi.getter(name="nextHopInstance")
    def next_hop_instance(self) -> Optional[pulumi.Input[str]]:
        """
        The URL to an instance that should handle matching packets. You can specify this as a full or partial URL. For example: https://www.googleapis.com/compute/v1/projects/project/zones/zone/instances/
        """
        return pulumi.get(self, "next_hop_instance")

    @next_hop_instance.setter
    def next_hop_instance(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "next_hop_instance", value)

    @property
    @pulumi.getter(name="nextHopIp")
    def next_hop_ip(self) -> Optional[pulumi.Input[str]]:
        """
        The network IP address of an instance that should handle matching packets. Only IPv4 is supported.
        """
        return pulumi.get(self, "next_hop_ip")

    @next_hop_ip.setter
    def next_hop_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "next_hop_ip", value)

    @property
    @pulumi.getter(name="nextHopNetwork")
    def next_hop_network(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of the local network if it should handle matching packets.
        """
        return pulumi.get(self, "next_hop_network")

    @next_hop_network.setter
    def next_hop_network(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "next_hop_network", value)

    @property
    @pulumi.getter(name="nextHopVpnTunnel")
    def next_hop_vpn_tunnel(self) -> Optional[pulumi.Input[str]]:
        """
        The URL to a VpnTunnel that should handle matching packets.
        """
        return pulumi.get(self, "next_hop_vpn_tunnel")

    @next_hop_vpn_tunnel.setter
    def next_hop_vpn_tunnel(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "next_hop_vpn_tunnel", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        The priority of this route. Priority is used to break ties in cases where there is more than one matching route of equal prefix length. In cases where multiple routes have equal prefix length, the one with the lowest-numbered priority value wins. The default value is `1000`. The priority value must be from `0` to `65535`, inclusive.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="requestId")
    def request_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "request_id")

    @request_id.setter
    def request_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of instance tags to which this route applies.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Route(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 allow_conflicting_subnetworks: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dest_range: Optional[pulumi.Input[str]] = None,
                 ilb_route_behavior_on_unhealthy: Optional[pulumi.Input['RouteIlbRouteBehaviorOnUnhealthy']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 next_hop_gateway: Optional[pulumi.Input[str]] = None,
                 next_hop_ilb: Optional[pulumi.Input[str]] = None,
                 next_hop_instance: Optional[pulumi.Input[str]] = None,
                 next_hop_ip: Optional[pulumi.Input[str]] = None,
                 next_hop_network: Optional[pulumi.Input[str]] = None,
                 next_hop_vpn_tunnel: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Creates a Route resource in the specified project using the data included in the request.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] allow_conflicting_subnetworks: Whether this route can conflict with existing subnetworks. Setting this to true allows this route to conflict with subnetworks that have already been configured on the corresponding network.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this field when you create the resource.
        :param pulumi.Input[str] dest_range: The destination range of outgoing packets that this route applies to. Both IPv4 and IPv6 are supported.
        :param pulumi.Input['RouteIlbRouteBehaviorOnUnhealthy'] ilb_route_behavior_on_unhealthy: ILB route behavior when ILB is deemed unhealthy based on user specified threshold on the Backend Service of the internal load balancing.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`. The first character must be a lowercase letter, and all following characters (except for the last character) must be a dash, lowercase letter, or digit. The last character must be a lowercase letter or digit.
        :param pulumi.Input[str] network: Fully-qualified URL of the network that this route applies to.
        :param pulumi.Input[str] next_hop_gateway: The URL to a gateway that should handle matching packets. You can only specify the internet gateway using a full or partial valid URL: projects/ project/global/gateways/default-internet-gateway
        :param pulumi.Input[str] next_hop_ilb: The URL to a forwarding rule of type loadBalancingScheme=INTERNAL that should handle matching packets or the IP address of the forwarding Rule. For example, the following are all valid URLs: - 10.128.0.56 - https://www.googleapis.com/compute/v1/projects/project/regions/region /forwardingRules/forwardingRule - regions/region/forwardingRules/forwardingRule 
        :param pulumi.Input[str] next_hop_instance: The URL to an instance that should handle matching packets. You can specify this as a full or partial URL. For example: https://www.googleapis.com/compute/v1/projects/project/zones/zone/instances/
        :param pulumi.Input[str] next_hop_ip: The network IP address of an instance that should handle matching packets. Only IPv4 is supported.
        :param pulumi.Input[str] next_hop_network: The URL of the local network if it should handle matching packets.
        :param pulumi.Input[str] next_hop_vpn_tunnel: The URL to a VpnTunnel that should handle matching packets.
        :param pulumi.Input[int] priority: The priority of this route. Priority is used to break ties in cases where there is more than one matching route of equal prefix length. In cases where multiple routes have equal prefix length, the one with the lowest-numbered priority value wins. The default value is `1000`. The priority value must be from `0` to `65535`, inclusive.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A list of instance tags to which this route applies.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[RouteArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a Route resource in the specified project using the data included in the request.

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
                 allow_conflicting_subnetworks: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dest_range: Optional[pulumi.Input[str]] = None,
                 ilb_route_behavior_on_unhealthy: Optional[pulumi.Input['RouteIlbRouteBehaviorOnUnhealthy']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 network: Optional[pulumi.Input[str]] = None,
                 next_hop_gateway: Optional[pulumi.Input[str]] = None,
                 next_hop_ilb: Optional[pulumi.Input[str]] = None,
                 next_hop_instance: Optional[pulumi.Input[str]] = None,
                 next_hop_ip: Optional[pulumi.Input[str]] = None,
                 next_hop_network: Optional[pulumi.Input[str]] = None,
                 next_hop_vpn_tunnel: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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

            __props__.__dict__["allow_conflicting_subnetworks"] = allow_conflicting_subnetworks
            __props__.__dict__["description"] = description
            __props__.__dict__["dest_range"] = dest_range
            __props__.__dict__["ilb_route_behavior_on_unhealthy"] = ilb_route_behavior_on_unhealthy
            __props__.__dict__["name"] = name
            __props__.__dict__["network"] = network
            __props__.__dict__["next_hop_gateway"] = next_hop_gateway
            __props__.__dict__["next_hop_ilb"] = next_hop_ilb
            __props__.__dict__["next_hop_instance"] = next_hop_instance
            __props__.__dict__["next_hop_ip"] = next_hop_ip
            __props__.__dict__["next_hop_network"] = next_hop_network
            __props__.__dict__["next_hop_vpn_tunnel"] = next_hop_vpn_tunnel
            __props__.__dict__["priority"] = priority
            __props__.__dict__["project"] = project
            __props__.__dict__["request_id"] = request_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["as_paths"] = None
            __props__.__dict__["creation_timestamp"] = None
            __props__.__dict__["kind"] = None
            __props__.__dict__["next_hop_interconnect_attachment"] = None
            __props__.__dict__["next_hop_peering"] = None
            __props__.__dict__["route_status"] = None
            __props__.__dict__["route_type"] = None
            __props__.__dict__["self_link"] = None
            __props__.__dict__["self_link_with_id"] = None
            __props__.__dict__["warnings"] = None
        super(Route, __self__).__init__(
            'google-native:compute/alpha:Route',
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

        __props__.__dict__["allow_conflicting_subnetworks"] = None
        __props__.__dict__["as_paths"] = None
        __props__.__dict__["creation_timestamp"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["dest_range"] = None
        __props__.__dict__["ilb_route_behavior_on_unhealthy"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network"] = None
        __props__.__dict__["next_hop_gateway"] = None
        __props__.__dict__["next_hop_ilb"] = None
        __props__.__dict__["next_hop_instance"] = None
        __props__.__dict__["next_hop_interconnect_attachment"] = None
        __props__.__dict__["next_hop_ip"] = None
        __props__.__dict__["next_hop_network"] = None
        __props__.__dict__["next_hop_peering"] = None
        __props__.__dict__["next_hop_vpn_tunnel"] = None
        __props__.__dict__["priority"] = None
        __props__.__dict__["route_status"] = None
        __props__.__dict__["route_type"] = None
        __props__.__dict__["self_link"] = None
        __props__.__dict__["self_link_with_id"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["warnings"] = None
        return Route(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allowConflictingSubnetworks")
    def allow_conflicting_subnetworks(self) -> pulumi.Output[bool]:
        """
        Whether this route can conflict with existing subnetworks. Setting this to true allows this route to conflict with subnetworks that have already been configured on the corresponding network.
        """
        return pulumi.get(self, "allow_conflicting_subnetworks")

    @property
    @pulumi.getter(name="asPaths")
    def as_paths(self) -> pulumi.Output[Sequence['outputs.RouteAsPathResponse']]:
        """
        AS path.
        """
        return pulumi.get(self, "as_paths")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[str]:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        An optional description of this resource. Provide this field when you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="destRange")
    def dest_range(self) -> pulumi.Output[str]:
        """
        The destination range of outgoing packets that this route applies to. Both IPv4 and IPv6 are supported.
        """
        return pulumi.get(self, "dest_range")

    @property
    @pulumi.getter(name="ilbRouteBehaviorOnUnhealthy")
    def ilb_route_behavior_on_unhealthy(self) -> pulumi.Output[str]:
        """
        ILB route behavior when ILB is deemed unhealthy based on user specified threshold on the Backend Service of the internal load balancing.
        """
        return pulumi.get(self, "ilb_route_behavior_on_unhealthy")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Type of this resource. Always compute#routes for Route resources.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`. The first character must be a lowercase letter, and all following characters (except for the last character) must be a dash, lowercase letter, or digit. The last character must be a lowercase letter or digit.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> pulumi.Output[str]:
        """
        Fully-qualified URL of the network that this route applies to.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="nextHopGateway")
    def next_hop_gateway(self) -> pulumi.Output[str]:
        """
        The URL to a gateway that should handle matching packets. You can only specify the internet gateway using a full or partial valid URL: projects/ project/global/gateways/default-internet-gateway
        """
        return pulumi.get(self, "next_hop_gateway")

    @property
    @pulumi.getter(name="nextHopIlb")
    def next_hop_ilb(self) -> pulumi.Output[str]:
        """
        The URL to a forwarding rule of type loadBalancingScheme=INTERNAL that should handle matching packets or the IP address of the forwarding Rule. For example, the following are all valid URLs: - 10.128.0.56 - https://www.googleapis.com/compute/v1/projects/project/regions/region /forwardingRules/forwardingRule - regions/region/forwardingRules/forwardingRule 
        """
        return pulumi.get(self, "next_hop_ilb")

    @property
    @pulumi.getter(name="nextHopInstance")
    def next_hop_instance(self) -> pulumi.Output[str]:
        """
        The URL to an instance that should handle matching packets. You can specify this as a full or partial URL. For example: https://www.googleapis.com/compute/v1/projects/project/zones/zone/instances/
        """
        return pulumi.get(self, "next_hop_instance")

    @property
    @pulumi.getter(name="nextHopInterconnectAttachment")
    def next_hop_interconnect_attachment(self) -> pulumi.Output[str]:
        """
        The URL to an InterconnectAttachment which is the next hop for the route. This field will only be populated for the dynamic routes generated by Cloud Router with a linked interconnectAttachment.
        """
        return pulumi.get(self, "next_hop_interconnect_attachment")

    @property
    @pulumi.getter(name="nextHopIp")
    def next_hop_ip(self) -> pulumi.Output[str]:
        """
        The network IP address of an instance that should handle matching packets. Only IPv4 is supported.
        """
        return pulumi.get(self, "next_hop_ip")

    @property
    @pulumi.getter(name="nextHopNetwork")
    def next_hop_network(self) -> pulumi.Output[str]:
        """
        The URL of the local network if it should handle matching packets.
        """
        return pulumi.get(self, "next_hop_network")

    @property
    @pulumi.getter(name="nextHopPeering")
    def next_hop_peering(self) -> pulumi.Output[str]:
        """
        The network peering name that should handle matching packets, which should conform to RFC1035.
        """
        return pulumi.get(self, "next_hop_peering")

    @property
    @pulumi.getter(name="nextHopVpnTunnel")
    def next_hop_vpn_tunnel(self) -> pulumi.Output[str]:
        """
        The URL to a VpnTunnel that should handle matching packets.
        """
        return pulumi.get(self, "next_hop_vpn_tunnel")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        """
        The priority of this route. Priority is used to break ties in cases where there is more than one matching route of equal prefix length. In cases where multiple routes have equal prefix length, the one with the lowest-numbered priority value wins. The default value is `1000`. The priority value must be from `0` to `65535`, inclusive.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="routeStatus")
    def route_status(self) -> pulumi.Output[str]:
        """
        [Output only] The status of the route.
        """
        return pulumi.get(self, "route_status")

    @property
    @pulumi.getter(name="routeType")
    def route_type(self) -> pulumi.Output[str]:
        """
        The type of this route, which can be one of the following values: - 'TRANSIT' for a transit route that this router learned from another Cloud Router and will readvertise to one of its BGP peers - 'SUBNET' for a route from a subnet of the VPC - 'BGP' for a route learned from a BGP peer of this router - 'STATIC' for a static route
        """
        return pulumi.get(self, "route_type")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        Server-defined fully-qualified URL for this resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> pulumi.Output[str]:
        """
        Server-defined URL for this resource with the resource id.
        """
        return pulumi.get(self, "self_link_with_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of instance tags to which this route applies.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def warnings(self) -> pulumi.Output[Sequence['outputs.RouteWarningsItemResponse']]:
        """
        If potential misconfigurations are detected for this route, this field will be populated with warning messages.
        """
        return pulumi.get(self, "warnings")

