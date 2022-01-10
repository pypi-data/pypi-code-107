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
    'GetDomainResult',
    'AwaitableGetDomainResult',
    'get_domain',
    'get_domain_output',
]

@pulumi.output_type
class GetDomainResult:
    def __init__(__self__, admin=None, audit_logs_enabled=None, authorized_networks=None, create_time=None, fqdn=None, labels=None, locations=None, name=None, reserved_ip_range=None, state=None, status_message=None, trusts=None, update_time=None):
        if admin and not isinstance(admin, str):
            raise TypeError("Expected argument 'admin' to be a str")
        pulumi.set(__self__, "admin", admin)
        if audit_logs_enabled and not isinstance(audit_logs_enabled, bool):
            raise TypeError("Expected argument 'audit_logs_enabled' to be a bool")
        pulumi.set(__self__, "audit_logs_enabled", audit_logs_enabled)
        if authorized_networks and not isinstance(authorized_networks, list):
            raise TypeError("Expected argument 'authorized_networks' to be a list")
        pulumi.set(__self__, "authorized_networks", authorized_networks)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if fqdn and not isinstance(fqdn, str):
            raise TypeError("Expected argument 'fqdn' to be a str")
        pulumi.set(__self__, "fqdn", fqdn)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if locations and not isinstance(locations, list):
            raise TypeError("Expected argument 'locations' to be a list")
        pulumi.set(__self__, "locations", locations)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if reserved_ip_range and not isinstance(reserved_ip_range, str):
            raise TypeError("Expected argument 'reserved_ip_range' to be a str")
        pulumi.set(__self__, "reserved_ip_range", reserved_ip_range)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if status_message and not isinstance(status_message, str):
            raise TypeError("Expected argument 'status_message' to be a str")
        pulumi.set(__self__, "status_message", status_message)
        if trusts and not isinstance(trusts, list):
            raise TypeError("Expected argument 'trusts' to be a list")
        pulumi.set(__self__, "trusts", trusts)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter
    def admin(self) -> str:
        """
        Optional. The name of delegated administrator account used to perform Active Directory operations. If not specified, `setupadmin` will be used.
        """
        return pulumi.get(self, "admin")

    @property
    @pulumi.getter(name="auditLogsEnabled")
    def audit_logs_enabled(self) -> bool:
        """
        Optional. Configuration for audit logs. True if audit logs are enabled, else false. Default is audit logs disabled.
        """
        return pulumi.get(self, "audit_logs_enabled")

    @property
    @pulumi.getter(name="authorizedNetworks")
    def authorized_networks(self) -> Sequence[str]:
        """
        Optional. The full names of the Google Compute Engine [networks](/compute/docs/networks-and-firewalls#networks) the domain instance is connected to. Networks can be added using UpdateDomain. The domain is only available on networks listed in `authorized_networks`. If CIDR subnets overlap between networks, domain creation will fail.
        """
        return pulumi.get(self, "authorized_networks")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The time the instance was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def fqdn(self) -> str:
        """
        The fully-qualified domain name of the exposed domain used by clients to connect to the service. Similar to what would be chosen for an Active Directory set up on an internal network.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Optional. Resource labels that can contain user-provided metadata.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def locations(self) -> Sequence[str]:
        """
        Locations where domain needs to be provisioned. regions e.g. us-west1 or us-east4 Service supports up to 4 locations at once. Each location will use a /26 block.
        """
        return pulumi.get(self, "locations")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The unique name of the domain using the form: `projects/{project_id}/locations/global/domains/{domain_name}`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="reservedIpRange")
    def reserved_ip_range(self) -> str:
        """
        The CIDR range of internal addresses that are reserved for this domain. Reserved networks must be /24 or larger. Ranges must be unique and non-overlapping with existing subnets in [Domain].[authorized_networks].
        """
        return pulumi.get(self, "reserved_ip_range")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of this domain.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="statusMessage")
    def status_message(self) -> str:
        """
        Additional information about the current status of this domain, if available.
        """
        return pulumi.get(self, "status_message")

    @property
    @pulumi.getter
    def trusts(self) -> Sequence['outputs.TrustResponse']:
        """
        The current trusts associated with the domain.
        """
        return pulumi.get(self, "trusts")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The last update time.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetDomainResult(GetDomainResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDomainResult(
            admin=self.admin,
            audit_logs_enabled=self.audit_logs_enabled,
            authorized_networks=self.authorized_networks,
            create_time=self.create_time,
            fqdn=self.fqdn,
            labels=self.labels,
            locations=self.locations,
            name=self.name,
            reserved_ip_range=self.reserved_ip_range,
            state=self.state,
            status_message=self.status_message,
            trusts=self.trusts,
            update_time=self.update_time)


def get_domain(domain_id: Optional[str] = None,
               project: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDomainResult:
    """
    Gets information about a domain.
    """
    __args__ = dict()
    __args__['domainId'] = domain_id
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:managedidentities/v1beta1:getDomain', __args__, opts=opts, typ=GetDomainResult).value

    return AwaitableGetDomainResult(
        admin=__ret__.admin,
        audit_logs_enabled=__ret__.audit_logs_enabled,
        authorized_networks=__ret__.authorized_networks,
        create_time=__ret__.create_time,
        fqdn=__ret__.fqdn,
        labels=__ret__.labels,
        locations=__ret__.locations,
        name=__ret__.name,
        reserved_ip_range=__ret__.reserved_ip_range,
        state=__ret__.state,
        status_message=__ret__.status_message,
        trusts=__ret__.trusts,
        update_time=__ret__.update_time)


@_utilities.lift_output_func(get_domain)
def get_domain_output(domain_id: Optional[pulumi.Input[str]] = None,
                      project: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDomainResult]:
    """
    Gets information about a domain.
    """
    ...
