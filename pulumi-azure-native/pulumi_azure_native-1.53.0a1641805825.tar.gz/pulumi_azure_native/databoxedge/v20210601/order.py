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

__all__ = ['OrderArgs', 'Order']

@pulumi.input_type
class OrderArgs:
    def __init__(__self__, *,
                 contact_information: pulumi.Input['ContactDetailsArgs'],
                 device_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 shipment_type: Optional[pulumi.Input[Union[str, 'ShipmentType']]] = None,
                 shipping_address: Optional[pulumi.Input['AddressArgs']] = None):
        """
        The set of arguments for constructing a Order resource.
        :param pulumi.Input['ContactDetailsArgs'] contact_information: The contact details.
        :param pulumi.Input[str] device_name: The order details of a device.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[Union[str, 'ShipmentType']] shipment_type: ShipmentType of the order
        :param pulumi.Input['AddressArgs'] shipping_address: The shipping address.
        """
        pulumi.set(__self__, "contact_information", contact_information)
        pulumi.set(__self__, "device_name", device_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if shipment_type is not None:
            pulumi.set(__self__, "shipment_type", shipment_type)
        if shipping_address is not None:
            pulumi.set(__self__, "shipping_address", shipping_address)

    @property
    @pulumi.getter(name="contactInformation")
    def contact_information(self) -> pulumi.Input['ContactDetailsArgs']:
        """
        The contact details.
        """
        return pulumi.get(self, "contact_information")

    @contact_information.setter
    def contact_information(self, value: pulumi.Input['ContactDetailsArgs']):
        pulumi.set(self, "contact_information", value)

    @property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[str]:
        """
        The order details of a device.
        """
        return pulumi.get(self, "device_name")

    @device_name.setter
    def device_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "device_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="shipmentType")
    def shipment_type(self) -> Optional[pulumi.Input[Union[str, 'ShipmentType']]]:
        """
        ShipmentType of the order
        """
        return pulumi.get(self, "shipment_type")

    @shipment_type.setter
    def shipment_type(self, value: Optional[pulumi.Input[Union[str, 'ShipmentType']]]):
        pulumi.set(self, "shipment_type", value)

    @property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> Optional[pulumi.Input['AddressArgs']]:
        """
        The shipping address.
        """
        return pulumi.get(self, "shipping_address")

    @shipping_address.setter
    def shipping_address(self, value: Optional[pulumi.Input['AddressArgs']]):
        pulumi.set(self, "shipping_address", value)


class Order(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 contact_information: Optional[pulumi.Input[pulumi.InputType['ContactDetailsArgs']]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 shipment_type: Optional[pulumi.Input[Union[str, 'ShipmentType']]] = None,
                 shipping_address: Optional[pulumi.Input[pulumi.InputType['AddressArgs']]] = None,
                 __props__=None):
        """
        The order details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ContactDetailsArgs']] contact_information: The contact details.
        :param pulumi.Input[str] device_name: The order details of a device.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[Union[str, 'ShipmentType']] shipment_type: ShipmentType of the order
        :param pulumi.Input[pulumi.InputType['AddressArgs']] shipping_address: The shipping address.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OrderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The order details.

        :param str resource_name: The name of the resource.
        :param OrderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OrderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 contact_information: Optional[pulumi.Input[pulumi.InputType['ContactDetailsArgs']]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 shipment_type: Optional[pulumi.Input[Union[str, 'ShipmentType']]] = None,
                 shipping_address: Optional[pulumi.Input[pulumi.InputType['AddressArgs']]] = None,
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
            __props__ = OrderArgs.__new__(OrderArgs)

            if contact_information is None and not opts.urn:
                raise TypeError("Missing required property 'contact_information'")
            __props__.__dict__["contact_information"] = contact_information
            if device_name is None and not opts.urn:
                raise TypeError("Missing required property 'device_name'")
            __props__.__dict__["device_name"] = device_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["shipment_type"] = shipment_type
            __props__.__dict__["shipping_address"] = shipping_address
            __props__.__dict__["current_status"] = None
            __props__.__dict__["delivery_tracking_info"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["order_history"] = None
            __props__.__dict__["return_tracking_info"] = None
            __props__.__dict__["serial_number"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:databoxedge:Order"), pulumi.Alias(type_="azure-native:databoxedge/v20190301:Order"), pulumi.Alias(type_="azure-native:databoxedge/v20190701:Order"), pulumi.Alias(type_="azure-native:databoxedge/v20190801:Order"), pulumi.Alias(type_="azure-native:databoxedge/v20200501preview:Order"), pulumi.Alias(type_="azure-native:databoxedge/v20200901:Order"), pulumi.Alias(type_="azure-native:databoxedge/v20200901preview:Order"), pulumi.Alias(type_="azure-native:databoxedge/v20201201:Order"), pulumi.Alias(type_="azure-native:databoxedge/v20210201:Order"), pulumi.Alias(type_="azure-native:databoxedge/v20210201preview:Order"), pulumi.Alias(type_="azure-native:databoxedge/v20210601preview:Order")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Order, __self__).__init__(
            'azure-native:databoxedge/v20210601:Order',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Order':
        """
        Get an existing Order resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = OrderArgs.__new__(OrderArgs)

        __props__.__dict__["contact_information"] = None
        __props__.__dict__["current_status"] = None
        __props__.__dict__["delivery_tracking_info"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["order_history"] = None
        __props__.__dict__["return_tracking_info"] = None
        __props__.__dict__["serial_number"] = None
        __props__.__dict__["shipment_type"] = None
        __props__.__dict__["shipping_address"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return Order(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="contactInformation")
    def contact_information(self) -> pulumi.Output['outputs.ContactDetailsResponse']:
        """
        The contact details.
        """
        return pulumi.get(self, "contact_information")

    @property
    @pulumi.getter(name="currentStatus")
    def current_status(self) -> pulumi.Output['outputs.OrderStatusResponse']:
        """
        Current status of the order.
        """
        return pulumi.get(self, "current_status")

    @property
    @pulumi.getter(name="deliveryTrackingInfo")
    def delivery_tracking_info(self) -> pulumi.Output[Sequence['outputs.TrackingInfoResponse']]:
        """
        Tracking information for the package delivered to the customer whether it has an original or a replacement device.
        """
        return pulumi.get(self, "delivery_tracking_info")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The object name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="orderHistory")
    def order_history(self) -> pulumi.Output[Sequence['outputs.OrderStatusResponse']]:
        """
        List of status changes in the order.
        """
        return pulumi.get(self, "order_history")

    @property
    @pulumi.getter(name="returnTrackingInfo")
    def return_tracking_info(self) -> pulumi.Output[Sequence['outputs.TrackingInfoResponse']]:
        """
        Tracking information for the package returned from the customer whether it has an original or a replacement device.
        """
        return pulumi.get(self, "return_tracking_info")

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> pulumi.Output[str]:
        """
        Serial number of the device.
        """
        return pulumi.get(self, "serial_number")

    @property
    @pulumi.getter(name="shipmentType")
    def shipment_type(self) -> pulumi.Output[Optional[str]]:
        """
        ShipmentType of the order
        """
        return pulumi.get(self, "shipment_type")

    @property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> pulumi.Output[Optional['outputs.AddressResponse']]:
        """
        The shipping address.
        """
        return pulumi.get(self, "shipping_address")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Order configured on ASE resource
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")

