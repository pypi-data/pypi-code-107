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

__all__ = ['ExtensionArgs', 'Extension']

@pulumi.input_type
class ExtensionArgs:
    def __init__(__self__, *,
                 cluster_name: pulumi.Input[str],
                 cluster_resource_name: pulumi.Input[str],
                 cluster_rp: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 aks_assigned_identity: Optional[pulumi.Input['ExtensionAksAssignedIdentityArgs']] = None,
                 auto_upgrade_minor_version: Optional[pulumi.Input[bool]] = None,
                 configuration_protected_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 configuration_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 extension_name: Optional[pulumi.Input[str]] = None,
                 extension_type: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['IdentityArgs']] = None,
                 release_train: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input['ScopeArgs']] = None,
                 statuses: Optional[pulumi.Input[Sequence[pulumi.Input['ExtensionStatusArgs']]]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Extension resource.
        :param pulumi.Input[str] cluster_name: The name of the kubernetes cluster.
        :param pulumi.Input[str] cluster_resource_name: The Kubernetes cluster resource name - either managedClusters (for AKS clusters) or connectedClusters (for OnPrem K8S clusters).
        :param pulumi.Input[str] cluster_rp: The Kubernetes cluster RP - either Microsoft.ContainerService (for AKS clusters) or Microsoft.Kubernetes (for OnPrem K8S clusters).
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['ExtensionAksAssignedIdentityArgs'] aks_assigned_identity: Identity of the Extension resource in an AKS cluster
        :param pulumi.Input[bool] auto_upgrade_minor_version: Flag to note if this extension participates in auto upgrade of minor version, or not.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] configuration_protected_settings: Configuration settings that are sensitive, as name-value pairs for configuring this extension.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] configuration_settings: Configuration settings, as name-value pairs for configuring this extension.
        :param pulumi.Input[str] extension_name: Name of the Extension.
        :param pulumi.Input[str] extension_type: Type of the Extension, of which this resource is an instance of.  It must be one of the Extension Types registered with Microsoft.KubernetesConfiguration by the Extension publisher.
        :param pulumi.Input['IdentityArgs'] identity: Identity of the Extension resource
        :param pulumi.Input[str] release_train: ReleaseTrain this extension participates in for auto-upgrade (e.g. Stable, Preview, etc.) - only if autoUpgradeMinorVersion is 'true'.
        :param pulumi.Input['ScopeArgs'] scope: Scope at which the extension is installed.
        :param pulumi.Input[Sequence[pulumi.Input['ExtensionStatusArgs']]] statuses: Status from this extension.
        :param pulumi.Input[str] version: Version of the extension for this extension, if it is 'pinned' to a specific version. autoUpgradeMinorVersion must be 'false'.
        """
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "cluster_resource_name", cluster_resource_name)
        pulumi.set(__self__, "cluster_rp", cluster_rp)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if aks_assigned_identity is not None:
            pulumi.set(__self__, "aks_assigned_identity", aks_assigned_identity)
        if auto_upgrade_minor_version is None:
            auto_upgrade_minor_version = True
        if auto_upgrade_minor_version is not None:
            pulumi.set(__self__, "auto_upgrade_minor_version", auto_upgrade_minor_version)
        if configuration_protected_settings is not None:
            pulumi.set(__self__, "configuration_protected_settings", configuration_protected_settings)
        if configuration_settings is not None:
            pulumi.set(__self__, "configuration_settings", configuration_settings)
        if extension_name is not None:
            pulumi.set(__self__, "extension_name", extension_name)
        if extension_type is not None:
            pulumi.set(__self__, "extension_type", extension_type)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if release_train is None:
            release_train = 'Stable'
        if release_train is not None:
            pulumi.set(__self__, "release_train", release_train)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if statuses is not None:
            pulumi.set(__self__, "statuses", statuses)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        The name of the kubernetes cluster.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="clusterResourceName")
    def cluster_resource_name(self) -> pulumi.Input[str]:
        """
        The Kubernetes cluster resource name - either managedClusters (for AKS clusters) or connectedClusters (for OnPrem K8S clusters).
        """
        return pulumi.get(self, "cluster_resource_name")

    @cluster_resource_name.setter
    def cluster_resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_resource_name", value)

    @property
    @pulumi.getter(name="clusterRp")
    def cluster_rp(self) -> pulumi.Input[str]:
        """
        The Kubernetes cluster RP - either Microsoft.ContainerService (for AKS clusters) or Microsoft.Kubernetes (for OnPrem K8S clusters).
        """
        return pulumi.get(self, "cluster_rp")

    @cluster_rp.setter
    def cluster_rp(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_rp", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="aksAssignedIdentity")
    def aks_assigned_identity(self) -> Optional[pulumi.Input['ExtensionAksAssignedIdentityArgs']]:
        """
        Identity of the Extension resource in an AKS cluster
        """
        return pulumi.get(self, "aks_assigned_identity")

    @aks_assigned_identity.setter
    def aks_assigned_identity(self, value: Optional[pulumi.Input['ExtensionAksAssignedIdentityArgs']]):
        pulumi.set(self, "aks_assigned_identity", value)

    @property
    @pulumi.getter(name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(self) -> Optional[pulumi.Input[bool]]:
        """
        Flag to note if this extension participates in auto upgrade of minor version, or not.
        """
        return pulumi.get(self, "auto_upgrade_minor_version")

    @auto_upgrade_minor_version.setter
    def auto_upgrade_minor_version(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_upgrade_minor_version", value)

    @property
    @pulumi.getter(name="configurationProtectedSettings")
    def configuration_protected_settings(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Configuration settings that are sensitive, as name-value pairs for configuring this extension.
        """
        return pulumi.get(self, "configuration_protected_settings")

    @configuration_protected_settings.setter
    def configuration_protected_settings(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "configuration_protected_settings", value)

    @property
    @pulumi.getter(name="configurationSettings")
    def configuration_settings(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Configuration settings, as name-value pairs for configuring this extension.
        """
        return pulumi.get(self, "configuration_settings")

    @configuration_settings.setter
    def configuration_settings(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "configuration_settings", value)

    @property
    @pulumi.getter(name="extensionName")
    def extension_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Extension.
        """
        return pulumi.get(self, "extension_name")

    @extension_name.setter
    def extension_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "extension_name", value)

    @property
    @pulumi.getter(name="extensionType")
    def extension_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of the Extension, of which this resource is an instance of.  It must be one of the Extension Types registered with Microsoft.KubernetesConfiguration by the Extension publisher.
        """
        return pulumi.get(self, "extension_type")

    @extension_type.setter
    def extension_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "extension_type", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['IdentityArgs']]:
        """
        Identity of the Extension resource
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['IdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="releaseTrain")
    def release_train(self) -> Optional[pulumi.Input[str]]:
        """
        ReleaseTrain this extension participates in for auto-upgrade (e.g. Stable, Preview, etc.) - only if autoUpgradeMinorVersion is 'true'.
        """
        return pulumi.get(self, "release_train")

    @release_train.setter
    def release_train(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "release_train", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input['ScopeArgs']]:
        """
        Scope at which the extension is installed.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input['ScopeArgs']]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def statuses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ExtensionStatusArgs']]]]:
        """
        Status from this extension.
        """
        return pulumi.get(self, "statuses")

    @statuses.setter
    def statuses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ExtensionStatusArgs']]]]):
        pulumi.set(self, "statuses", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        Version of the extension for this extension, if it is 'pinned' to a specific version. autoUpgradeMinorVersion must be 'false'.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class Extension(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aks_assigned_identity: Optional[pulumi.Input[pulumi.InputType['ExtensionAksAssignedIdentityArgs']]] = None,
                 auto_upgrade_minor_version: Optional[pulumi.Input[bool]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 cluster_resource_name: Optional[pulumi.Input[str]] = None,
                 cluster_rp: Optional[pulumi.Input[str]] = None,
                 configuration_protected_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 configuration_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 extension_name: Optional[pulumi.Input[str]] = None,
                 extension_type: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 release_train: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[pulumi.InputType['ScopeArgs']]] = None,
                 statuses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExtensionStatusArgs']]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The Extension object.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ExtensionAksAssignedIdentityArgs']] aks_assigned_identity: Identity of the Extension resource in an AKS cluster
        :param pulumi.Input[bool] auto_upgrade_minor_version: Flag to note if this extension participates in auto upgrade of minor version, or not.
        :param pulumi.Input[str] cluster_name: The name of the kubernetes cluster.
        :param pulumi.Input[str] cluster_resource_name: The Kubernetes cluster resource name - either managedClusters (for AKS clusters) or connectedClusters (for OnPrem K8S clusters).
        :param pulumi.Input[str] cluster_rp: The Kubernetes cluster RP - either Microsoft.ContainerService (for AKS clusters) or Microsoft.Kubernetes (for OnPrem K8S clusters).
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] configuration_protected_settings: Configuration settings that are sensitive, as name-value pairs for configuring this extension.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] configuration_settings: Configuration settings, as name-value pairs for configuring this extension.
        :param pulumi.Input[str] extension_name: Name of the Extension.
        :param pulumi.Input[str] extension_type: Type of the Extension, of which this resource is an instance of.  It must be one of the Extension Types registered with Microsoft.KubernetesConfiguration by the Extension publisher.
        :param pulumi.Input[pulumi.InputType['IdentityArgs']] identity: Identity of the Extension resource
        :param pulumi.Input[str] release_train: ReleaseTrain this extension participates in for auto-upgrade (e.g. Stable, Preview, etc.) - only if autoUpgradeMinorVersion is 'true'.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[pulumi.InputType['ScopeArgs']] scope: Scope at which the extension is installed.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExtensionStatusArgs']]]] statuses: Status from this extension.
        :param pulumi.Input[str] version: Version of the extension for this extension, if it is 'pinned' to a specific version. autoUpgradeMinorVersion must be 'false'.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ExtensionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Extension object.

        :param str resource_name: The name of the resource.
        :param ExtensionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExtensionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aks_assigned_identity: Optional[pulumi.Input[pulumi.InputType['ExtensionAksAssignedIdentityArgs']]] = None,
                 auto_upgrade_minor_version: Optional[pulumi.Input[bool]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 cluster_resource_name: Optional[pulumi.Input[str]] = None,
                 cluster_rp: Optional[pulumi.Input[str]] = None,
                 configuration_protected_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 configuration_settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 extension_name: Optional[pulumi.Input[str]] = None,
                 extension_type: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['IdentityArgs']]] = None,
                 release_train: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[pulumi.InputType['ScopeArgs']]] = None,
                 statuses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ExtensionStatusArgs']]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
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
            __props__ = ExtensionArgs.__new__(ExtensionArgs)

            __props__.__dict__["aks_assigned_identity"] = aks_assigned_identity
            if auto_upgrade_minor_version is None:
                auto_upgrade_minor_version = True
            __props__.__dict__["auto_upgrade_minor_version"] = auto_upgrade_minor_version
            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            if cluster_resource_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_resource_name'")
            __props__.__dict__["cluster_resource_name"] = cluster_resource_name
            if cluster_rp is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_rp'")
            __props__.__dict__["cluster_rp"] = cluster_rp
            __props__.__dict__["configuration_protected_settings"] = configuration_protected_settings
            __props__.__dict__["configuration_settings"] = configuration_settings
            __props__.__dict__["extension_name"] = extension_name
            __props__.__dict__["extension_type"] = extension_type
            __props__.__dict__["identity"] = identity
            if release_train is None:
                release_train = 'Stable'
            __props__.__dict__["release_train"] = release_train
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["scope"] = scope
            __props__.__dict__["statuses"] = statuses
            __props__.__dict__["version"] = version
            __props__.__dict__["custom_location_settings"] = None
            __props__.__dict__["error_info"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["package_uri"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:kubernetesconfiguration:Extension"), pulumi.Alias(type_="azure-native:kubernetesconfiguration/v20200701preview:Extension"), pulumi.Alias(type_="azure-native:kubernetesconfiguration/v20210501preview:Extension"), pulumi.Alias(type_="azure-native:kubernetesconfiguration/v20210901:Extension"), pulumi.Alias(type_="azure-native:kubernetesconfiguration/v20220101preview:Extension")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Extension, __self__).__init__(
            'azure-native:kubernetesconfiguration/v20211101preview:Extension',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Extension':
        """
        Get an existing Extension resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ExtensionArgs.__new__(ExtensionArgs)

        __props__.__dict__["aks_assigned_identity"] = None
        __props__.__dict__["auto_upgrade_minor_version"] = None
        __props__.__dict__["configuration_protected_settings"] = None
        __props__.__dict__["configuration_settings"] = None
        __props__.__dict__["custom_location_settings"] = None
        __props__.__dict__["error_info"] = None
        __props__.__dict__["extension_type"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["package_uri"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["release_train"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["statuses"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        return Extension(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aksAssignedIdentity")
    def aks_assigned_identity(self) -> pulumi.Output[Optional['outputs.ExtensionResponseAksAssignedIdentity']]:
        """
        Identity of the Extension resource in an AKS cluster
        """
        return pulumi.get(self, "aks_assigned_identity")

    @property
    @pulumi.getter(name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(self) -> pulumi.Output[Optional[bool]]:
        """
        Flag to note if this extension participates in auto upgrade of minor version, or not.
        """
        return pulumi.get(self, "auto_upgrade_minor_version")

    @property
    @pulumi.getter(name="configurationProtectedSettings")
    def configuration_protected_settings(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Configuration settings that are sensitive, as name-value pairs for configuring this extension.
        """
        return pulumi.get(self, "configuration_protected_settings")

    @property
    @pulumi.getter(name="configurationSettings")
    def configuration_settings(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Configuration settings, as name-value pairs for configuring this extension.
        """
        return pulumi.get(self, "configuration_settings")

    @property
    @pulumi.getter(name="customLocationSettings")
    def custom_location_settings(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Custom Location settings properties.
        """
        return pulumi.get(self, "custom_location_settings")

    @property
    @pulumi.getter(name="errorInfo")
    def error_info(self) -> pulumi.Output['outputs.ErrorDetailResponse']:
        """
        Error information from the Agent - e.g. errors during installation.
        """
        return pulumi.get(self, "error_info")

    @property
    @pulumi.getter(name="extensionType")
    def extension_type(self) -> pulumi.Output[Optional[str]]:
        """
        Type of the Extension, of which this resource is an instance of.  It must be one of the Extension Types registered with Microsoft.KubernetesConfiguration by the Extension publisher.
        """
        return pulumi.get(self, "extension_type")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityResponse']]:
        """
        Identity of the Extension resource
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="packageUri")
    def package_uri(self) -> pulumi.Output[str]:
        """
        Uri of the Helm package
        """
        return pulumi.get(self, "package_uri")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Status of installation of this extension.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="releaseTrain")
    def release_train(self) -> pulumi.Output[Optional[str]]:
        """
        ReleaseTrain this extension participates in for auto-upgrade (e.g. Stable, Preview, etc.) - only if autoUpgradeMinorVersion is 'true'.
        """
        return pulumi.get(self, "release_train")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional['outputs.ScopeResponse']]:
        """
        Scope at which the extension is installed.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def statuses(self) -> pulumi.Output[Optional[Sequence['outputs.ExtensionStatusResponse']]]:
        """
        Status from this extension.
        """
        return pulumi.get(self, "statuses")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Top level metadata https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/common-api-contracts.md#system-metadata-for-all-azure-resources
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        """
        Version of the extension for this extension, if it is 'pinned' to a specific version. autoUpgradeMinorVersion must be 'false'.
        """
        return pulumi.get(self, "version")

