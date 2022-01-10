# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['ReservationArgs', 'Reservation']

@pulumi.input_type
class ReservationArgs:
    def __init__(__self__, *,
                 reservation_id: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 throughput_capacity: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Reservation resource.
        :param pulumi.Input[str] name: The name of the reservation. Structured like: projects/{project_number}/locations/{location}/reservations/{reservation_id}
        :param pulumi.Input[str] throughput_capacity: The reserved throughput capacity. Every unit of throughput capacity is equivalent to 1 MiB/s of published messages or 2 MiB/s of subscribed messages. Any topics which are declared as using capacity from a Reservation will consume resources from this reservation instead of being charged individually.
        """
        pulumi.set(__self__, "reservation_id", reservation_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if throughput_capacity is not None:
            pulumi.set(__self__, "throughput_capacity", throughput_capacity)

    @property
    @pulumi.getter(name="reservationId")
    def reservation_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "reservation_id")

    @reservation_id.setter
    def reservation_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "reservation_id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the reservation. Structured like: projects/{project_number}/locations/{location}/reservations/{reservation_id}
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="throughputCapacity")
    def throughput_capacity(self) -> Optional[pulumi.Input[str]]:
        """
        The reserved throughput capacity. Every unit of throughput capacity is equivalent to 1 MiB/s of published messages or 2 MiB/s of subscribed messages. Any topics which are declared as using capacity from a Reservation will consume resources from this reservation instead of being charged individually.
        """
        return pulumi.get(self, "throughput_capacity")

    @throughput_capacity.setter
    def throughput_capacity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "throughput_capacity", value)


class Reservation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 reservation_id: Optional[pulumi.Input[str]] = None,
                 throughput_capacity: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new reservation.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the reservation. Structured like: projects/{project_number}/locations/{location}/reservations/{reservation_id}
        :param pulumi.Input[str] throughput_capacity: The reserved throughput capacity. Every unit of throughput capacity is equivalent to 1 MiB/s of published messages or 2 MiB/s of subscribed messages. Any topics which are declared as using capacity from a Reservation will consume resources from this reservation instead of being charged individually.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ReservationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new reservation.

        :param str resource_name: The name of the resource.
        :param ReservationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReservationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 reservation_id: Optional[pulumi.Input[str]] = None,
                 throughput_capacity: Optional[pulumi.Input[str]] = None,
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
            __props__ = ReservationArgs.__new__(ReservationArgs)

            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            if reservation_id is None and not opts.urn:
                raise TypeError("Missing required property 'reservation_id'")
            __props__.__dict__["reservation_id"] = reservation_id
            __props__.__dict__["throughput_capacity"] = throughput_capacity
        super(Reservation, __self__).__init__(
            'google-native:pubsublite/v1:Reservation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Reservation':
        """
        Get an existing Reservation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ReservationArgs.__new__(ReservationArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["throughput_capacity"] = None
        return Reservation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the reservation. Structured like: projects/{project_number}/locations/{location}/reservations/{reservation_id}
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="throughputCapacity")
    def throughput_capacity(self) -> pulumi.Output[str]:
        """
        The reserved throughput capacity. Every unit of throughput capacity is equivalent to 1 MiB/s of published messages or 2 MiB/s of subscribed messages. Any topics which are declared as using capacity from a Reservation will consume resources from this reservation instead of being charged individually.
        """
        return pulumi.get(self, "throughput_capacity")

