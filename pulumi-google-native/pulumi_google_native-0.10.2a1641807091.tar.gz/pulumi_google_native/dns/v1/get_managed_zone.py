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
    'GetManagedZoneResult',
    'AwaitableGetManagedZoneResult',
    'get_managed_zone',
    'get_managed_zone_output',
]

@pulumi.output_type
class GetManagedZoneResult:
    def __init__(__self__, cloud_logging_config=None, creation_time=None, description=None, dns_name=None, dnssec_config=None, forwarding_config=None, kind=None, labels=None, name=None, name_server_set=None, name_servers=None, peering_config=None, private_visibility_config=None, reverse_lookup_config=None, service_directory_config=None, visibility=None):
        if cloud_logging_config and not isinstance(cloud_logging_config, dict):
            raise TypeError("Expected argument 'cloud_logging_config' to be a dict")
        pulumi.set(__self__, "cloud_logging_config", cloud_logging_config)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if dns_name and not isinstance(dns_name, str):
            raise TypeError("Expected argument 'dns_name' to be a str")
        pulumi.set(__self__, "dns_name", dns_name)
        if dnssec_config and not isinstance(dnssec_config, dict):
            raise TypeError("Expected argument 'dnssec_config' to be a dict")
        pulumi.set(__self__, "dnssec_config", dnssec_config)
        if forwarding_config and not isinstance(forwarding_config, dict):
            raise TypeError("Expected argument 'forwarding_config' to be a dict")
        pulumi.set(__self__, "forwarding_config", forwarding_config)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if name_server_set and not isinstance(name_server_set, str):
            raise TypeError("Expected argument 'name_server_set' to be a str")
        pulumi.set(__self__, "name_server_set", name_server_set)
        if name_servers and not isinstance(name_servers, list):
            raise TypeError("Expected argument 'name_servers' to be a list")
        pulumi.set(__self__, "name_servers", name_servers)
        if peering_config and not isinstance(peering_config, dict):
            raise TypeError("Expected argument 'peering_config' to be a dict")
        pulumi.set(__self__, "peering_config", peering_config)
        if private_visibility_config and not isinstance(private_visibility_config, dict):
            raise TypeError("Expected argument 'private_visibility_config' to be a dict")
        pulumi.set(__self__, "private_visibility_config", private_visibility_config)
        if reverse_lookup_config and not isinstance(reverse_lookup_config, dict):
            raise TypeError("Expected argument 'reverse_lookup_config' to be a dict")
        pulumi.set(__self__, "reverse_lookup_config", reverse_lookup_config)
        if service_directory_config and not isinstance(service_directory_config, dict):
            raise TypeError("Expected argument 'service_directory_config' to be a dict")
        pulumi.set(__self__, "service_directory_config", service_directory_config)
        if visibility and not isinstance(visibility, str):
            raise TypeError("Expected argument 'visibility' to be a str")
        pulumi.set(__self__, "visibility", visibility)

    @property
    @pulumi.getter(name="cloudLoggingConfig")
    def cloud_logging_config(self) -> 'outputs.ManagedZoneCloudLoggingConfigResponse':
        return pulumi.get(self, "cloud_logging_config")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        """
        The time that this resource was created on the server. This is in RFC3339 text format. Output only.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A mutable string of at most 1024 characters associated with this resource for the user's convenience. Has no effect on the managed zone's function.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> str:
        """
        The DNS name of this managed zone, for instance "example.com.".
        """
        return pulumi.get(self, "dns_name")

    @property
    @pulumi.getter(name="dnssecConfig")
    def dnssec_config(self) -> 'outputs.ManagedZoneDnsSecConfigResponse':
        """
        DNSSEC configuration.
        """
        return pulumi.get(self, "dnssec_config")

    @property
    @pulumi.getter(name="forwardingConfig")
    def forwarding_config(self) -> 'outputs.ManagedZoneForwardingConfigResponse':
        """
        The presence for this field indicates that outbound forwarding is enabled for this zone. The value of this field contains the set of destinations to forward to.
        """
        return pulumi.get(self, "forwarding_config")

    @property
    @pulumi.getter
    def kind(self) -> str:
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        User labels.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        User assigned name for this resource. Must be unique within the project. The name must be 1-63 characters long, must begin with a letter, end with a letter or digit, and only contain lowercase letters, digits or dashes.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nameServerSet")
    def name_server_set(self) -> str:
        """
        Optionally specifies the NameServerSet for this ManagedZone. A NameServerSet is a set of DNS name servers that all host the same ManagedZones. Most users leave this field unset. If you need to use this field, contact your account team.
        """
        return pulumi.get(self, "name_server_set")

    @property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> Sequence[str]:
        """
        Delegate your managed_zone to these virtual name servers; defined by the server (output only)
        """
        return pulumi.get(self, "name_servers")

    @property
    @pulumi.getter(name="peeringConfig")
    def peering_config(self) -> 'outputs.ManagedZonePeeringConfigResponse':
        """
        The presence of this field indicates that DNS Peering is enabled for this zone. The value of this field contains the network to peer with.
        """
        return pulumi.get(self, "peering_config")

    @property
    @pulumi.getter(name="privateVisibilityConfig")
    def private_visibility_config(self) -> 'outputs.ManagedZonePrivateVisibilityConfigResponse':
        """
        For privately visible zones, the set of Virtual Private Cloud resources that the zone is visible from.
        """
        return pulumi.get(self, "private_visibility_config")

    @property
    @pulumi.getter(name="reverseLookupConfig")
    def reverse_lookup_config(self) -> 'outputs.ManagedZoneReverseLookupConfigResponse':
        """
        The presence of this field indicates that this is a managed reverse lookup zone and Cloud DNS resolves reverse lookup queries using automatically configured records for VPC resources. This only applies to networks listed under private_visibility_config.
        """
        return pulumi.get(self, "reverse_lookup_config")

    @property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(self) -> 'outputs.ManagedZoneServiceDirectoryConfigResponse':
        """
        This field links to the associated service directory namespace. Do not set this field for public zones or forwarding zones.
        """
        return pulumi.get(self, "service_directory_config")

    @property
    @pulumi.getter
    def visibility(self) -> str:
        """
        The zone's visibility: public zones are exposed to the Internet, while private zones are visible only to Virtual Private Cloud resources.
        """
        return pulumi.get(self, "visibility")


class AwaitableGetManagedZoneResult(GetManagedZoneResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedZoneResult(
            cloud_logging_config=self.cloud_logging_config,
            creation_time=self.creation_time,
            description=self.description,
            dns_name=self.dns_name,
            dnssec_config=self.dnssec_config,
            forwarding_config=self.forwarding_config,
            kind=self.kind,
            labels=self.labels,
            name=self.name,
            name_server_set=self.name_server_set,
            name_servers=self.name_servers,
            peering_config=self.peering_config,
            private_visibility_config=self.private_visibility_config,
            reverse_lookup_config=self.reverse_lookup_config,
            service_directory_config=self.service_directory_config,
            visibility=self.visibility)


def get_managed_zone(client_operation_id: Optional[str] = None,
                     managed_zone: Optional[str] = None,
                     project: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedZoneResult:
    """
    Fetches the representation of an existing ManagedZone.
    """
    __args__ = dict()
    __args__['clientOperationId'] = client_operation_id
    __args__['managedZone'] = managed_zone
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:dns/v1:getManagedZone', __args__, opts=opts, typ=GetManagedZoneResult).value

    return AwaitableGetManagedZoneResult(
        cloud_logging_config=__ret__.cloud_logging_config,
        creation_time=__ret__.creation_time,
        description=__ret__.description,
        dns_name=__ret__.dns_name,
        dnssec_config=__ret__.dnssec_config,
        forwarding_config=__ret__.forwarding_config,
        kind=__ret__.kind,
        labels=__ret__.labels,
        name=__ret__.name,
        name_server_set=__ret__.name_server_set,
        name_servers=__ret__.name_servers,
        peering_config=__ret__.peering_config,
        private_visibility_config=__ret__.private_visibility_config,
        reverse_lookup_config=__ret__.reverse_lookup_config,
        service_directory_config=__ret__.service_directory_config,
        visibility=__ret__.visibility)


@_utilities.lift_output_func(get_managed_zone)
def get_managed_zone_output(client_operation_id: Optional[pulumi.Input[Optional[str]]] = None,
                            managed_zone: Optional[pulumi.Input[str]] = None,
                            project: Optional[pulumi.Input[Optional[str]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedZoneResult]:
    """
    Fetches the representation of an existing ManagedZone.
    """
    ...
