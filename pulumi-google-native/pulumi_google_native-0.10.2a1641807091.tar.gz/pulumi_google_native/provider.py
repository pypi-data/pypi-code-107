# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 append_user_agent: Optional[pulumi.Input[str]] = None,
                 disable_partner_name: Optional[pulumi.Input[bool]] = None,
                 partner_name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] append_user_agent: Additional user-agent string to append to the default one (<prod_name>/<ver>).
        :param pulumi.Input[bool] disable_partner_name: This will disable the Pulumi Partner Name which is used if a custom `partnerName` isn't specified.
        :param pulumi.Input[str] partner_name: A Google Partner Name to facilitate partner resource usage attribution.
        :param pulumi.Input[str] project: The default project to manage resources in. If another project is specified on a resource, it will take precedence.
        :param pulumi.Input[str] region: The default region to manage resources in. If another region is specified on a regional resource, it will take precedence.
        :param pulumi.Input[str] zone: The default zone to manage resources in. Generally, this zone should be within the default region you specified. If another zone is specified on a zonal resource, it will take precedence.
        """
        if append_user_agent is None:
            append_user_agent = _utilities.get_env('GOOGLE_APPEND_USER_AGENT')
        if append_user_agent is not None:
            pulumi.set(__self__, "append_user_agent", append_user_agent)
        if disable_partner_name is None:
            disable_partner_name = _utilities.get_env_bool('GOOGLE_DISABLE_PARTNER_NAME')
        if disable_partner_name is not None:
            pulumi.set(__self__, "disable_partner_name", disable_partner_name)
        if partner_name is None:
            partner_name = _utilities.get_env('GOOGLE_PARTNER_NAME')
        if partner_name is not None:
            pulumi.set(__self__, "partner_name", partner_name)
        if project is None:
            project = _utilities.get_env('GOOGLE_PROJECT', 'GOOGLE_CLOUD_PROJECT', 'GCLOUD_PROJECT', 'CLOUDSDK_CORE_PROJECT')
        if project is not None:
            pulumi.set(__self__, "project", project)
        if region is None:
            region = _utilities.get_env('GOOGLE_REGION', 'GCLOUD_REGION', 'CLOUDSDK_COMPUTE_REGION')
        if region is not None:
            pulumi.set(__self__, "region", region)
        if zone is None:
            zone = _utilities.get_env('GOOGLE_ZONE', 'GCLOUD_ZONE', 'CLOUDSDK_COMPUTE_ZONE')
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="appendUserAgent")
    def append_user_agent(self) -> Optional[pulumi.Input[str]]:
        """
        Additional user-agent string to append to the default one (<prod_name>/<ver>).
        """
        return pulumi.get(self, "append_user_agent")

    @append_user_agent.setter
    def append_user_agent(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "append_user_agent", value)

    @property
    @pulumi.getter(name="disablePartnerName")
    def disable_partner_name(self) -> Optional[pulumi.Input[bool]]:
        """
        This will disable the Pulumi Partner Name which is used if a custom `partnerName` isn't specified.
        """
        return pulumi.get(self, "disable_partner_name")

    @disable_partner_name.setter
    def disable_partner_name(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_partner_name", value)

    @property
    @pulumi.getter(name="partnerName")
    def partner_name(self) -> Optional[pulumi.Input[str]]:
        """
        A Google Partner Name to facilitate partner resource usage attribution.
        """
        return pulumi.get(self, "partner_name")

    @partner_name.setter
    def partner_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "partner_name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The default project to manage resources in. If another project is specified on a resource, it will take precedence.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The default region to manage resources in. If another region is specified on a regional resource, it will take precedence.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        The default zone to manage resources in. Generally, this zone should be within the default region you specified. If another zone is specified on a zonal resource, it will take precedence.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 append_user_agent: Optional[pulumi.Input[str]] = None,
                 disable_partner_name: Optional[pulumi.Input[bool]] = None,
                 partner_name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The provider type for the Google Cloud package.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] append_user_agent: Additional user-agent string to append to the default one (<prod_name>/<ver>).
        :param pulumi.Input[bool] disable_partner_name: This will disable the Pulumi Partner Name which is used if a custom `partnerName` isn't specified.
        :param pulumi.Input[str] partner_name: A Google Partner Name to facilitate partner resource usage attribution.
        :param pulumi.Input[str] project: The default project to manage resources in. If another project is specified on a resource, it will take precedence.
        :param pulumi.Input[str] region: The default region to manage resources in. If another region is specified on a regional resource, it will take precedence.
        :param pulumi.Input[str] zone: The default zone to manage resources in. Generally, this zone should be within the default region you specified. If another zone is specified on a zonal resource, it will take precedence.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ProviderArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the Google Cloud package.

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 append_user_agent: Optional[pulumi.Input[str]] = None,
                 disable_partner_name: Optional[pulumi.Input[bool]] = None,
                 partner_name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
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
            __props__ = ProviderArgs.__new__(ProviderArgs)

            if append_user_agent is None:
                append_user_agent = _utilities.get_env('GOOGLE_APPEND_USER_AGENT')
            __props__.__dict__["append_user_agent"] = append_user_agent
            if disable_partner_name is None:
                disable_partner_name = _utilities.get_env_bool('GOOGLE_DISABLE_PARTNER_NAME')
            __props__.__dict__["disable_partner_name"] = pulumi.Output.from_input(disable_partner_name).apply(pulumi.runtime.to_json) if disable_partner_name is not None else None
            if partner_name is None:
                partner_name = _utilities.get_env('GOOGLE_PARTNER_NAME')
            __props__.__dict__["partner_name"] = partner_name
            if project is None:
                project = _utilities.get_env('GOOGLE_PROJECT', 'GOOGLE_CLOUD_PROJECT', 'GCLOUD_PROJECT', 'CLOUDSDK_CORE_PROJECT')
            __props__.__dict__["project"] = project
            if region is None:
                region = _utilities.get_env('GOOGLE_REGION', 'GCLOUD_REGION', 'CLOUDSDK_COMPUTE_REGION')
            __props__.__dict__["region"] = region
            if zone is None:
                zone = _utilities.get_env('GOOGLE_ZONE', 'GCLOUD_ZONE', 'CLOUDSDK_COMPUTE_ZONE')
            __props__.__dict__["zone"] = zone
        super(Provider, __self__).__init__(
            'google-native',
            resource_name,
            __props__,
            opts)

