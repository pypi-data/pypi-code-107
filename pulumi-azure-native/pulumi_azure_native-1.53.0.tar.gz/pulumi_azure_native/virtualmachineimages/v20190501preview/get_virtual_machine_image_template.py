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
    'GetVirtualMachineImageTemplateResult',
    'AwaitableGetVirtualMachineImageTemplateResult',
    'get_virtual_machine_image_template',
    'get_virtual_machine_image_template_output',
]

@pulumi.output_type
class GetVirtualMachineImageTemplateResult:
    """
    Image template is an ARM resource managed by Microsoft.VirtualMachineImages provider
    """
    def __init__(__self__, build_timeout_in_minutes=None, customize=None, distribute=None, id=None, identity=None, last_run_status=None, location=None, name=None, provisioning_error=None, provisioning_state=None, source=None, tags=None, type=None, vm_profile=None):
        if build_timeout_in_minutes and not isinstance(build_timeout_in_minutes, int):
            raise TypeError("Expected argument 'build_timeout_in_minutes' to be a int")
        pulumi.set(__self__, "build_timeout_in_minutes", build_timeout_in_minutes)
        if customize and not isinstance(customize, list):
            raise TypeError("Expected argument 'customize' to be a list")
        pulumi.set(__self__, "customize", customize)
        if distribute and not isinstance(distribute, list):
            raise TypeError("Expected argument 'distribute' to be a list")
        pulumi.set(__self__, "distribute", distribute)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if last_run_status and not isinstance(last_run_status, dict):
            raise TypeError("Expected argument 'last_run_status' to be a dict")
        pulumi.set(__self__, "last_run_status", last_run_status)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_error and not isinstance(provisioning_error, dict):
            raise TypeError("Expected argument 'provisioning_error' to be a dict")
        pulumi.set(__self__, "provisioning_error", provisioning_error)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if source and not isinstance(source, dict):
            raise TypeError("Expected argument 'source' to be a dict")
        pulumi.set(__self__, "source", source)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if vm_profile and not isinstance(vm_profile, dict):
            raise TypeError("Expected argument 'vm_profile' to be a dict")
        pulumi.set(__self__, "vm_profile", vm_profile)

    @property
    @pulumi.getter(name="buildTimeoutInMinutes")
    def build_timeout_in_minutes(self) -> Optional[int]:
        """
        Maximum duration to wait while building the image template. Omit or specify 0 to use the default (4 hours).
        """
        return pulumi.get(self, "build_timeout_in_minutes")

    @property
    @pulumi.getter
    def customize(self) -> Optional[Sequence[Any]]:
        """
        Specifies the properties used to describe the customization steps of the image, like Image source etc
        """
        return pulumi.get(self, "customize")

    @property
    @pulumi.getter
    def distribute(self) -> Sequence[Any]:
        """
        The distribution targets where the image output needs to go to.
        """
        return pulumi.get(self, "distribute")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ImageTemplateIdentityResponse']:
        """
        The identity of the image template, if configured.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="lastRunStatus")
    def last_run_status(self) -> 'outputs.ImageTemplateLastRunStatusResponse':
        """
        State of 'run' that is currently executing or was last executed.
        """
        return pulumi.get(self, "last_run_status")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningError")
    def provisioning_error(self) -> 'outputs.ProvisioningErrorResponse':
        """
        Provisioning error, if any
        """
        return pulumi.get(self, "provisioning_error")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def source(self) -> Any:
        """
        Specifies the properties used to describe the source image.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vmProfile")
    def vm_profile(self) -> Optional['outputs.ImageTemplateVmProfileResponse']:
        """
        Describes how virtual machine is set up to build images
        """
        return pulumi.get(self, "vm_profile")


class AwaitableGetVirtualMachineImageTemplateResult(GetVirtualMachineImageTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualMachineImageTemplateResult(
            build_timeout_in_minutes=self.build_timeout_in_minutes,
            customize=self.customize,
            distribute=self.distribute,
            id=self.id,
            identity=self.identity,
            last_run_status=self.last_run_status,
            location=self.location,
            name=self.name,
            provisioning_error=self.provisioning_error,
            provisioning_state=self.provisioning_state,
            source=self.source,
            tags=self.tags,
            type=self.type,
            vm_profile=self.vm_profile)


def get_virtual_machine_image_template(image_template_name: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualMachineImageTemplateResult:
    """
    Image template is an ARM resource managed by Microsoft.VirtualMachineImages provider


    :param str image_template_name: The name of the image Template
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['imageTemplateName'] = image_template_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:virtualmachineimages/v20190501preview:getVirtualMachineImageTemplate', __args__, opts=opts, typ=GetVirtualMachineImageTemplateResult).value

    return AwaitableGetVirtualMachineImageTemplateResult(
        build_timeout_in_minutes=__ret__.build_timeout_in_minutes,
        customize=__ret__.customize,
        distribute=__ret__.distribute,
        id=__ret__.id,
        identity=__ret__.identity,
        last_run_status=__ret__.last_run_status,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_error=__ret__.provisioning_error,
        provisioning_state=__ret__.provisioning_state,
        source=__ret__.source,
        tags=__ret__.tags,
        type=__ret__.type,
        vm_profile=__ret__.vm_profile)


@_utilities.lift_output_func(get_virtual_machine_image_template)
def get_virtual_machine_image_template_output(image_template_name: Optional[pulumi.Input[str]] = None,
                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualMachineImageTemplateResult]:
    """
    Image template is an ARM resource managed by Microsoft.VirtualMachineImages provider


    :param str image_template_name: The name of the image Template
    :param str resource_group_name: The name of the resource group.
    """
    ...
