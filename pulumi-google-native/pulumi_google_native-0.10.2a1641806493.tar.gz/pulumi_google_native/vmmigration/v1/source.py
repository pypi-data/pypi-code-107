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

__all__ = ['SourceArgs', 'Source']

@pulumi.input_type
class SourceArgs:
    def __init__(__self__, *,
                 source_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 vmware: Optional[pulumi.Input['VmwareSourceDetailsArgs']] = None):
        """
        The set of arguments for constructing a Source resource.
        :param pulumi.Input[str] description: User-provided description of the source.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels of the source.
        :param pulumi.Input['VmwareSourceDetailsArgs'] vmware: Vmware type source details.
        """
        pulumi.set(__self__, "source_id", source_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if request_id is not None:
            pulumi.set(__self__, "request_id", request_id)
        if vmware is not None:
            pulumi.set(__self__, "vmware", vmware)

    @property
    @pulumi.getter(name="sourceId")
    def source_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "source_id")

    @source_id.setter
    def source_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        User-provided description of the source.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The labels of the source.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

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
    def vmware(self) -> Optional[pulumi.Input['VmwareSourceDetailsArgs']]:
        """
        Vmware type source details.
        """
        return pulumi.get(self, "vmware")

    @vmware.setter
    def vmware(self, value: Optional[pulumi.Input['VmwareSourceDetailsArgs']]):
        pulumi.set(self, "vmware", value)


class Source(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 source_id: Optional[pulumi.Input[str]] = None,
                 vmware: Optional[pulumi.Input[pulumi.InputType['VmwareSourceDetailsArgs']]] = None,
                 __props__=None):
        """
        Creates a new Source in a given project and location.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: User-provided description of the source.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: The labels of the source.
        :param pulumi.Input[pulumi.InputType['VmwareSourceDetailsArgs']] vmware: Vmware type source details.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new Source in a given project and location.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param SourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 source_id: Optional[pulumi.Input[str]] = None,
                 vmware: Optional[pulumi.Input[pulumi.InputType['VmwareSourceDetailsArgs']]] = None,
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
            __props__ = SourceArgs.__new__(SourceArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            __props__.__dict__["project"] = project
            __props__.__dict__["request_id"] = request_id
            if source_id is None and not opts.urn:
                raise TypeError("Missing required property 'source_id'")
            __props__.__dict__["source_id"] = source_id
            __props__.__dict__["vmware"] = vmware
            __props__.__dict__["create_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["update_time"] = None
        super(Source, __self__).__init__(
            'google-native:vmmigration/v1:Source',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Source':
        """
        Get an existing Source resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SourceArgs.__new__(SourceArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["update_time"] = None
        __props__.__dict__["vmware"] = None
        return Source(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The create time timestamp.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        User-provided description of the source.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        The labels of the source.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The Source name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The update time timestamp.
        """
        return pulumi.get(self, "update_time")

    @property
    @pulumi.getter
    def vmware(self) -> pulumi.Output['outputs.VmwareSourceDetailsResponse']:
        """
        Vmware type source details.
        """
        return pulumi.get(self, "vmware")

