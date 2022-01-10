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
    'GetLabResult',
    'AwaitableGetLabResult',
    'get_lab',
    'get_lab_output',
]

@pulumi.output_type
class GetLabResult:
    """
    A lab.
    """
    def __init__(__self__, announcement=None, artifacts_storage_account=None, created_date=None, default_premium_storage_account=None, default_storage_account=None, environment_permission=None, extended_properties=None, id=None, lab_storage_type=None, load_balancer_id=None, location=None, mandatory_artifacts_resource_ids_linux=None, mandatory_artifacts_resource_ids_windows=None, name=None, network_security_group_id=None, premium_data_disk_storage_account=None, premium_data_disks=None, provisioning_state=None, public_ip_id=None, support=None, tags=None, type=None, unique_identifier=None, vault_name=None, vm_creation_resource_group=None):
        if announcement and not isinstance(announcement, dict):
            raise TypeError("Expected argument 'announcement' to be a dict")
        pulumi.set(__self__, "announcement", announcement)
        if artifacts_storage_account and not isinstance(artifacts_storage_account, str):
            raise TypeError("Expected argument 'artifacts_storage_account' to be a str")
        pulumi.set(__self__, "artifacts_storage_account", artifacts_storage_account)
        if created_date and not isinstance(created_date, str):
            raise TypeError("Expected argument 'created_date' to be a str")
        pulumi.set(__self__, "created_date", created_date)
        if default_premium_storage_account and not isinstance(default_premium_storage_account, str):
            raise TypeError("Expected argument 'default_premium_storage_account' to be a str")
        pulumi.set(__self__, "default_premium_storage_account", default_premium_storage_account)
        if default_storage_account and not isinstance(default_storage_account, str):
            raise TypeError("Expected argument 'default_storage_account' to be a str")
        pulumi.set(__self__, "default_storage_account", default_storage_account)
        if environment_permission and not isinstance(environment_permission, str):
            raise TypeError("Expected argument 'environment_permission' to be a str")
        pulumi.set(__self__, "environment_permission", environment_permission)
        if extended_properties and not isinstance(extended_properties, dict):
            raise TypeError("Expected argument 'extended_properties' to be a dict")
        pulumi.set(__self__, "extended_properties", extended_properties)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lab_storage_type and not isinstance(lab_storage_type, str):
            raise TypeError("Expected argument 'lab_storage_type' to be a str")
        pulumi.set(__self__, "lab_storage_type", lab_storage_type)
        if load_balancer_id and not isinstance(load_balancer_id, str):
            raise TypeError("Expected argument 'load_balancer_id' to be a str")
        pulumi.set(__self__, "load_balancer_id", load_balancer_id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if mandatory_artifacts_resource_ids_linux and not isinstance(mandatory_artifacts_resource_ids_linux, list):
            raise TypeError("Expected argument 'mandatory_artifacts_resource_ids_linux' to be a list")
        pulumi.set(__self__, "mandatory_artifacts_resource_ids_linux", mandatory_artifacts_resource_ids_linux)
        if mandatory_artifacts_resource_ids_windows and not isinstance(mandatory_artifacts_resource_ids_windows, list):
            raise TypeError("Expected argument 'mandatory_artifacts_resource_ids_windows' to be a list")
        pulumi.set(__self__, "mandatory_artifacts_resource_ids_windows", mandatory_artifacts_resource_ids_windows)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_security_group_id and not isinstance(network_security_group_id, str):
            raise TypeError("Expected argument 'network_security_group_id' to be a str")
        pulumi.set(__self__, "network_security_group_id", network_security_group_id)
        if premium_data_disk_storage_account and not isinstance(premium_data_disk_storage_account, str):
            raise TypeError("Expected argument 'premium_data_disk_storage_account' to be a str")
        pulumi.set(__self__, "premium_data_disk_storage_account", premium_data_disk_storage_account)
        if premium_data_disks and not isinstance(premium_data_disks, str):
            raise TypeError("Expected argument 'premium_data_disks' to be a str")
        pulumi.set(__self__, "premium_data_disks", premium_data_disks)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_ip_id and not isinstance(public_ip_id, str):
            raise TypeError("Expected argument 'public_ip_id' to be a str")
        pulumi.set(__self__, "public_ip_id", public_ip_id)
        if support and not isinstance(support, dict):
            raise TypeError("Expected argument 'support' to be a dict")
        pulumi.set(__self__, "support", support)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if unique_identifier and not isinstance(unique_identifier, str):
            raise TypeError("Expected argument 'unique_identifier' to be a str")
        pulumi.set(__self__, "unique_identifier", unique_identifier)
        if vault_name and not isinstance(vault_name, str):
            raise TypeError("Expected argument 'vault_name' to be a str")
        pulumi.set(__self__, "vault_name", vault_name)
        if vm_creation_resource_group and not isinstance(vm_creation_resource_group, str):
            raise TypeError("Expected argument 'vm_creation_resource_group' to be a str")
        pulumi.set(__self__, "vm_creation_resource_group", vm_creation_resource_group)

    @property
    @pulumi.getter
    def announcement(self) -> Optional['outputs.LabAnnouncementPropertiesResponse']:
        """
        The properties of any lab announcement associated with this lab
        """
        return pulumi.get(self, "announcement")

    @property
    @pulumi.getter(name="artifactsStorageAccount")
    def artifacts_storage_account(self) -> str:
        """
        The lab's artifact storage account.
        """
        return pulumi.get(self, "artifacts_storage_account")

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> str:
        """
        The creation date of the lab.
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter(name="defaultPremiumStorageAccount")
    def default_premium_storage_account(self) -> str:
        """
        The lab's default premium storage account.
        """
        return pulumi.get(self, "default_premium_storage_account")

    @property
    @pulumi.getter(name="defaultStorageAccount")
    def default_storage_account(self) -> str:
        """
        The lab's default storage account.
        """
        return pulumi.get(self, "default_storage_account")

    @property
    @pulumi.getter(name="environmentPermission")
    def environment_permission(self) -> Optional[str]:
        """
        The access rights to be granted to the user when provisioning an environment
        """
        return pulumi.get(self, "environment_permission")

    @property
    @pulumi.getter(name="extendedProperties")
    def extended_properties(self) -> Optional[Mapping[str, str]]:
        """
        Extended properties of the lab used for experimental features
        """
        return pulumi.get(self, "extended_properties")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The identifier of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="labStorageType")
    def lab_storage_type(self) -> Optional[str]:
        """
        Type of storage used by the lab. It can be either Premium or Standard. Default is Premium.
        """
        return pulumi.get(self, "lab_storage_type")

    @property
    @pulumi.getter(name="loadBalancerId")
    def load_balancer_id(self) -> str:
        """
        The load balancer used to for lab VMs that use shared IP address.
        """
        return pulumi.get(self, "load_balancer_id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="mandatoryArtifactsResourceIdsLinux")
    def mandatory_artifacts_resource_ids_linux(self) -> Optional[Sequence[str]]:
        """
        The ordered list of artifact resource IDs that should be applied on all Linux VM creations by default, prior to the artifacts specified by the user.
        """
        return pulumi.get(self, "mandatory_artifacts_resource_ids_linux")

    @property
    @pulumi.getter(name="mandatoryArtifactsResourceIdsWindows")
    def mandatory_artifacts_resource_ids_windows(self) -> Optional[Sequence[str]]:
        """
        The ordered list of artifact resource IDs that should be applied on all Windows VM creations by default, prior to the artifacts specified by the user.
        """
        return pulumi.get(self, "mandatory_artifacts_resource_ids_windows")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkSecurityGroupId")
    def network_security_group_id(self) -> str:
        """
        The Network Security Group attached to the lab VMs Network interfaces to restrict open ports.
        """
        return pulumi.get(self, "network_security_group_id")

    @property
    @pulumi.getter(name="premiumDataDiskStorageAccount")
    def premium_data_disk_storage_account(self) -> str:
        """
        The lab's premium data disk storage account.
        """
        return pulumi.get(self, "premium_data_disk_storage_account")

    @property
    @pulumi.getter(name="premiumDataDisks")
    def premium_data_disks(self) -> Optional[str]:
        """
        The setting to enable usage of premium data disks.
        When its value is 'Enabled', creation of standard or premium data disks is allowed.
        When its value is 'Disabled', only creation of standard data disks is allowed.
        """
        return pulumi.get(self, "premium_data_disks")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning status of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicIpId")
    def public_ip_id(self) -> str:
        """
        The public IP address for the lab's load balancer.
        """
        return pulumi.get(self, "public_ip_id")

    @property
    @pulumi.getter
    def support(self) -> Optional['outputs.LabSupportPropertiesResponse']:
        """
        The properties of any lab support message associated with this lab
        """
        return pulumi.get(self, "support")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> str:
        """
        The unique immutable identifier of a resource (Guid).
        """
        return pulumi.get(self, "unique_identifier")

    @property
    @pulumi.getter(name="vaultName")
    def vault_name(self) -> str:
        """
        The lab's Key vault.
        """
        return pulumi.get(self, "vault_name")

    @property
    @pulumi.getter(name="vmCreationResourceGroup")
    def vm_creation_resource_group(self) -> str:
        """
        The resource group in which all new lab virtual machines will be created. To let DevTest Labs manage resource group creation, set this value to null.
        """
        return pulumi.get(self, "vm_creation_resource_group")


class AwaitableGetLabResult(GetLabResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLabResult(
            announcement=self.announcement,
            artifacts_storage_account=self.artifacts_storage_account,
            created_date=self.created_date,
            default_premium_storage_account=self.default_premium_storage_account,
            default_storage_account=self.default_storage_account,
            environment_permission=self.environment_permission,
            extended_properties=self.extended_properties,
            id=self.id,
            lab_storage_type=self.lab_storage_type,
            load_balancer_id=self.load_balancer_id,
            location=self.location,
            mandatory_artifacts_resource_ids_linux=self.mandatory_artifacts_resource_ids_linux,
            mandatory_artifacts_resource_ids_windows=self.mandatory_artifacts_resource_ids_windows,
            name=self.name,
            network_security_group_id=self.network_security_group_id,
            premium_data_disk_storage_account=self.premium_data_disk_storage_account,
            premium_data_disks=self.premium_data_disks,
            provisioning_state=self.provisioning_state,
            public_ip_id=self.public_ip_id,
            support=self.support,
            tags=self.tags,
            type=self.type,
            unique_identifier=self.unique_identifier,
            vault_name=self.vault_name,
            vm_creation_resource_group=self.vm_creation_resource_group)


def get_lab(expand: Optional[str] = None,
            name: Optional[str] = None,
            resource_group_name: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLabResult:
    """
    A lab.


    :param str expand: Specify the $expand query. Example: 'properties($select=defaultStorageAccount)'
    :param str name: The name of the lab.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:devtestlab/v20180915:getLab', __args__, opts=opts, typ=GetLabResult).value

    return AwaitableGetLabResult(
        announcement=__ret__.announcement,
        artifacts_storage_account=__ret__.artifacts_storage_account,
        created_date=__ret__.created_date,
        default_premium_storage_account=__ret__.default_premium_storage_account,
        default_storage_account=__ret__.default_storage_account,
        environment_permission=__ret__.environment_permission,
        extended_properties=__ret__.extended_properties,
        id=__ret__.id,
        lab_storage_type=__ret__.lab_storage_type,
        load_balancer_id=__ret__.load_balancer_id,
        location=__ret__.location,
        mandatory_artifacts_resource_ids_linux=__ret__.mandatory_artifacts_resource_ids_linux,
        mandatory_artifacts_resource_ids_windows=__ret__.mandatory_artifacts_resource_ids_windows,
        name=__ret__.name,
        network_security_group_id=__ret__.network_security_group_id,
        premium_data_disk_storage_account=__ret__.premium_data_disk_storage_account,
        premium_data_disks=__ret__.premium_data_disks,
        provisioning_state=__ret__.provisioning_state,
        public_ip_id=__ret__.public_ip_id,
        support=__ret__.support,
        tags=__ret__.tags,
        type=__ret__.type,
        unique_identifier=__ret__.unique_identifier,
        vault_name=__ret__.vault_name,
        vm_creation_resource_group=__ret__.vm_creation_resource_group)


@_utilities.lift_output_func(get_lab)
def get_lab_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                   name: Optional[pulumi.Input[str]] = None,
                   resource_group_name: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLabResult]:
    """
    A lab.


    :param str expand: Specify the $expand query. Example: 'properties($select=defaultStorageAccount)'
    :param str name: The name of the lab.
    :param str resource_group_name: The name of the resource group.
    """
    ...
