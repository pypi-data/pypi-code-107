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
    'GetAppServiceEnvironmentResult',
    'AwaitableGetAppServiceEnvironmentResult',
    'get_app_service_environment',
    'get_app_service_environment_output',
]

@pulumi.output_type
class GetAppServiceEnvironmentResult:
    """
    App Service Environment ARM resource.
    """
    def __init__(__self__, allowed_multi_sizes=None, allowed_worker_sizes=None, api_management_account_id=None, cluster_settings=None, database_edition=None, database_service_objective=None, default_front_end_scale_factor=None, dns_suffix=None, dynamic_cache_enabled=None, environment_capacities=None, environment_is_healthy=None, environment_status=None, front_end_scale_factor=None, has_linux_workers=None, id=None, internal_load_balancing_mode=None, ipssl_address_count=None, kind=None, last_action=None, last_action_result=None, location=None, maximum_number_of_machines=None, multi_role_count=None, multi_size=None, name=None, network_access_control_list=None, provisioning_state=None, resource_group=None, ssl_cert_key_vault_id=None, ssl_cert_key_vault_secret_name=None, status=None, subscription_id=None, suspended=None, system_data=None, tags=None, type=None, upgrade_domains=None, user_whitelisted_ip_ranges=None, vip_mappings=None, virtual_network=None, vnet_name=None, vnet_resource_group_name=None, vnet_subnet_name=None, worker_pools=None):
        if allowed_multi_sizes and not isinstance(allowed_multi_sizes, str):
            raise TypeError("Expected argument 'allowed_multi_sizes' to be a str")
        pulumi.set(__self__, "allowed_multi_sizes", allowed_multi_sizes)
        if allowed_worker_sizes and not isinstance(allowed_worker_sizes, str):
            raise TypeError("Expected argument 'allowed_worker_sizes' to be a str")
        pulumi.set(__self__, "allowed_worker_sizes", allowed_worker_sizes)
        if api_management_account_id and not isinstance(api_management_account_id, str):
            raise TypeError("Expected argument 'api_management_account_id' to be a str")
        pulumi.set(__self__, "api_management_account_id", api_management_account_id)
        if cluster_settings and not isinstance(cluster_settings, list):
            raise TypeError("Expected argument 'cluster_settings' to be a list")
        pulumi.set(__self__, "cluster_settings", cluster_settings)
        if database_edition and not isinstance(database_edition, str):
            raise TypeError("Expected argument 'database_edition' to be a str")
        pulumi.set(__self__, "database_edition", database_edition)
        if database_service_objective and not isinstance(database_service_objective, str):
            raise TypeError("Expected argument 'database_service_objective' to be a str")
        pulumi.set(__self__, "database_service_objective", database_service_objective)
        if default_front_end_scale_factor and not isinstance(default_front_end_scale_factor, int):
            raise TypeError("Expected argument 'default_front_end_scale_factor' to be a int")
        pulumi.set(__self__, "default_front_end_scale_factor", default_front_end_scale_factor)
        if dns_suffix and not isinstance(dns_suffix, str):
            raise TypeError("Expected argument 'dns_suffix' to be a str")
        pulumi.set(__self__, "dns_suffix", dns_suffix)
        if dynamic_cache_enabled and not isinstance(dynamic_cache_enabled, bool):
            raise TypeError("Expected argument 'dynamic_cache_enabled' to be a bool")
        pulumi.set(__self__, "dynamic_cache_enabled", dynamic_cache_enabled)
        if environment_capacities and not isinstance(environment_capacities, list):
            raise TypeError("Expected argument 'environment_capacities' to be a list")
        pulumi.set(__self__, "environment_capacities", environment_capacities)
        if environment_is_healthy and not isinstance(environment_is_healthy, bool):
            raise TypeError("Expected argument 'environment_is_healthy' to be a bool")
        pulumi.set(__self__, "environment_is_healthy", environment_is_healthy)
        if environment_status and not isinstance(environment_status, str):
            raise TypeError("Expected argument 'environment_status' to be a str")
        pulumi.set(__self__, "environment_status", environment_status)
        if front_end_scale_factor and not isinstance(front_end_scale_factor, int):
            raise TypeError("Expected argument 'front_end_scale_factor' to be a int")
        pulumi.set(__self__, "front_end_scale_factor", front_end_scale_factor)
        if has_linux_workers and not isinstance(has_linux_workers, bool):
            raise TypeError("Expected argument 'has_linux_workers' to be a bool")
        pulumi.set(__self__, "has_linux_workers", has_linux_workers)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if internal_load_balancing_mode and not isinstance(internal_load_balancing_mode, str):
            raise TypeError("Expected argument 'internal_load_balancing_mode' to be a str")
        pulumi.set(__self__, "internal_load_balancing_mode", internal_load_balancing_mode)
        if ipssl_address_count and not isinstance(ipssl_address_count, int):
            raise TypeError("Expected argument 'ipssl_address_count' to be a int")
        pulumi.set(__self__, "ipssl_address_count", ipssl_address_count)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if last_action and not isinstance(last_action, str):
            raise TypeError("Expected argument 'last_action' to be a str")
        pulumi.set(__self__, "last_action", last_action)
        if last_action_result and not isinstance(last_action_result, str):
            raise TypeError("Expected argument 'last_action_result' to be a str")
        pulumi.set(__self__, "last_action_result", last_action_result)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if maximum_number_of_machines and not isinstance(maximum_number_of_machines, int):
            raise TypeError("Expected argument 'maximum_number_of_machines' to be a int")
        pulumi.set(__self__, "maximum_number_of_machines", maximum_number_of_machines)
        if multi_role_count and not isinstance(multi_role_count, int):
            raise TypeError("Expected argument 'multi_role_count' to be a int")
        pulumi.set(__self__, "multi_role_count", multi_role_count)
        if multi_size and not isinstance(multi_size, str):
            raise TypeError("Expected argument 'multi_size' to be a str")
        pulumi.set(__self__, "multi_size", multi_size)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_access_control_list and not isinstance(network_access_control_list, list):
            raise TypeError("Expected argument 'network_access_control_list' to be a list")
        pulumi.set(__self__, "network_access_control_list", network_access_control_list)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_group and not isinstance(resource_group, str):
            raise TypeError("Expected argument 'resource_group' to be a str")
        pulumi.set(__self__, "resource_group", resource_group)
        if ssl_cert_key_vault_id and not isinstance(ssl_cert_key_vault_id, str):
            raise TypeError("Expected argument 'ssl_cert_key_vault_id' to be a str")
        pulumi.set(__self__, "ssl_cert_key_vault_id", ssl_cert_key_vault_id)
        if ssl_cert_key_vault_secret_name and not isinstance(ssl_cert_key_vault_secret_name, str):
            raise TypeError("Expected argument 'ssl_cert_key_vault_secret_name' to be a str")
        pulumi.set(__self__, "ssl_cert_key_vault_secret_name", ssl_cert_key_vault_secret_name)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if subscription_id and not isinstance(subscription_id, str):
            raise TypeError("Expected argument 'subscription_id' to be a str")
        pulumi.set(__self__, "subscription_id", subscription_id)
        if suspended and not isinstance(suspended, bool):
            raise TypeError("Expected argument 'suspended' to be a bool")
        pulumi.set(__self__, "suspended", suspended)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if upgrade_domains and not isinstance(upgrade_domains, int):
            raise TypeError("Expected argument 'upgrade_domains' to be a int")
        pulumi.set(__self__, "upgrade_domains", upgrade_domains)
        if user_whitelisted_ip_ranges and not isinstance(user_whitelisted_ip_ranges, list):
            raise TypeError("Expected argument 'user_whitelisted_ip_ranges' to be a list")
        pulumi.set(__self__, "user_whitelisted_ip_ranges", user_whitelisted_ip_ranges)
        if vip_mappings and not isinstance(vip_mappings, list):
            raise TypeError("Expected argument 'vip_mappings' to be a list")
        pulumi.set(__self__, "vip_mappings", vip_mappings)
        if virtual_network and not isinstance(virtual_network, dict):
            raise TypeError("Expected argument 'virtual_network' to be a dict")
        pulumi.set(__self__, "virtual_network", virtual_network)
        if vnet_name and not isinstance(vnet_name, str):
            raise TypeError("Expected argument 'vnet_name' to be a str")
        pulumi.set(__self__, "vnet_name", vnet_name)
        if vnet_resource_group_name and not isinstance(vnet_resource_group_name, str):
            raise TypeError("Expected argument 'vnet_resource_group_name' to be a str")
        pulumi.set(__self__, "vnet_resource_group_name", vnet_resource_group_name)
        if vnet_subnet_name and not isinstance(vnet_subnet_name, str):
            raise TypeError("Expected argument 'vnet_subnet_name' to be a str")
        pulumi.set(__self__, "vnet_subnet_name", vnet_subnet_name)
        if worker_pools and not isinstance(worker_pools, list):
            raise TypeError("Expected argument 'worker_pools' to be a list")
        pulumi.set(__self__, "worker_pools", worker_pools)

    @property
    @pulumi.getter(name="allowedMultiSizes")
    def allowed_multi_sizes(self) -> str:
        """
        List of comma separated strings describing which VM sizes are allowed for front-ends.
        """
        return pulumi.get(self, "allowed_multi_sizes")

    @property
    @pulumi.getter(name="allowedWorkerSizes")
    def allowed_worker_sizes(self) -> str:
        """
        List of comma separated strings describing which VM sizes are allowed for workers.
        """
        return pulumi.get(self, "allowed_worker_sizes")

    @property
    @pulumi.getter(name="apiManagementAccountId")
    def api_management_account_id(self) -> Optional[str]:
        """
        API Management Account associated with the App Service Environment.
        """
        return pulumi.get(self, "api_management_account_id")

    @property
    @pulumi.getter(name="clusterSettings")
    def cluster_settings(self) -> Optional[Sequence['outputs.NameValuePairResponse']]:
        """
        Custom settings for changing the behavior of the App Service Environment.
        """
        return pulumi.get(self, "cluster_settings")

    @property
    @pulumi.getter(name="databaseEdition")
    def database_edition(self) -> str:
        """
        Edition of the metadata database for the App Service Environment, e.g. "Standard".
        """
        return pulumi.get(self, "database_edition")

    @property
    @pulumi.getter(name="databaseServiceObjective")
    def database_service_objective(self) -> str:
        """
        Service objective of the metadata database for the App Service Environment, e.g. "S0".
        """
        return pulumi.get(self, "database_service_objective")

    @property
    @pulumi.getter(name="defaultFrontEndScaleFactor")
    def default_front_end_scale_factor(self) -> int:
        """
        Default Scale Factor for FrontEnds.
        """
        return pulumi.get(self, "default_front_end_scale_factor")

    @property
    @pulumi.getter(name="dnsSuffix")
    def dns_suffix(self) -> Optional[str]:
        """
        DNS suffix of the App Service Environment.
        """
        return pulumi.get(self, "dns_suffix")

    @property
    @pulumi.getter(name="dynamicCacheEnabled")
    def dynamic_cache_enabled(self) -> Optional[bool]:
        """
        True/false indicating whether the App Service Environment is suspended. The environment can be suspended e.g. when the management endpoint is no longer available
        (most likely because NSG blocked the incoming traffic).
        """
        return pulumi.get(self, "dynamic_cache_enabled")

    @property
    @pulumi.getter(name="environmentCapacities")
    def environment_capacities(self) -> Sequence['outputs.StampCapacityResponse']:
        """
        Current total, used, and available worker capacities.
        """
        return pulumi.get(self, "environment_capacities")

    @property
    @pulumi.getter(name="environmentIsHealthy")
    def environment_is_healthy(self) -> bool:
        """
        True/false indicating whether the App Service Environment is healthy.
        """
        return pulumi.get(self, "environment_is_healthy")

    @property
    @pulumi.getter(name="environmentStatus")
    def environment_status(self) -> str:
        """
        Detailed message about with results of the last check of the App Service Environment.
        """
        return pulumi.get(self, "environment_status")

    @property
    @pulumi.getter(name="frontEndScaleFactor")
    def front_end_scale_factor(self) -> Optional[int]:
        """
        Scale factor for front-ends.
        """
        return pulumi.get(self, "front_end_scale_factor")

    @property
    @pulumi.getter(name="hasLinuxWorkers")
    def has_linux_workers(self) -> Optional[bool]:
        """
        Flag that displays whether an ASE has linux workers or not
        """
        return pulumi.get(self, "has_linux_workers")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="internalLoadBalancingMode")
    def internal_load_balancing_mode(self) -> Optional[str]:
        """
        Specifies which endpoints to serve internally in the Virtual Network for the App Service Environment.
        """
        return pulumi.get(self, "internal_load_balancing_mode")

    @property
    @pulumi.getter(name="ipsslAddressCount")
    def ipssl_address_count(self) -> Optional[int]:
        """
        Number of IP SSL addresses reserved for the App Service Environment.
        """
        return pulumi.get(self, "ipssl_address_count")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="lastAction")
    def last_action(self) -> str:
        """
        Last deployment action on the App Service Environment.
        """
        return pulumi.get(self, "last_action")

    @property
    @pulumi.getter(name="lastActionResult")
    def last_action_result(self) -> str:
        """
        Result of the last deployment action on the App Service Environment.
        """
        return pulumi.get(self, "last_action_result")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource Location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maximumNumberOfMachines")
    def maximum_number_of_machines(self) -> int:
        """
        Maximum number of VMs in the App Service Environment.
        """
        return pulumi.get(self, "maximum_number_of_machines")

    @property
    @pulumi.getter(name="multiRoleCount")
    def multi_role_count(self) -> Optional[int]:
        """
        Number of front-end instances.
        """
        return pulumi.get(self, "multi_role_count")

    @property
    @pulumi.getter(name="multiSize")
    def multi_size(self) -> Optional[str]:
        """
        Front-end VM size, e.g. "Medium", "Large".
        """
        return pulumi.get(self, "multi_size")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkAccessControlList")
    def network_access_control_list(self) -> Optional[Sequence['outputs.NetworkAccessControlEntryResponse']]:
        """
        Access control list for controlling traffic to the App Service Environment.
        """
        return pulumi.get(self, "network_access_control_list")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the App Service Environment.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> str:
        """
        Resource group of the App Service Environment.
        """
        return pulumi.get(self, "resource_group")

    @property
    @pulumi.getter(name="sslCertKeyVaultId")
    def ssl_cert_key_vault_id(self) -> Optional[str]:
        """
        Key Vault ID for ILB App Service Environment default SSL certificate
        """
        return pulumi.get(self, "ssl_cert_key_vault_id")

    @property
    @pulumi.getter(name="sslCertKeyVaultSecretName")
    def ssl_cert_key_vault_secret_name(self) -> Optional[str]:
        """
        Key Vault Secret Name for ILB App Service Environment default SSL certificate
        """
        return pulumi.get(self, "ssl_cert_key_vault_secret_name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Current status of the App Service Environment.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> str:
        """
        Subscription of the App Service Environment.
        """
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter
    def suspended(self) -> Optional[bool]:
        """
        <code>true</code> if the App Service Environment is suspended; otherwise, <code>false</code>. The environment can be suspended, e.g. when the management endpoint is no longer available
         (most likely because NSG blocked the incoming traffic).
        """
        return pulumi.get(self, "suspended")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="upgradeDomains")
    def upgrade_domains(self) -> int:
        """
        Number of upgrade domains of the App Service Environment.
        """
        return pulumi.get(self, "upgrade_domains")

    @property
    @pulumi.getter(name="userWhitelistedIpRanges")
    def user_whitelisted_ip_ranges(self) -> Optional[Sequence[str]]:
        """
        User added ip ranges to whitelist on ASE db
        """
        return pulumi.get(self, "user_whitelisted_ip_ranges")

    @property
    @pulumi.getter(name="vipMappings")
    def vip_mappings(self) -> Sequence['outputs.VirtualIPMappingResponse']:
        """
        Description of IP SSL mapping for the App Service Environment.
        """
        return pulumi.get(self, "vip_mappings")

    @property
    @pulumi.getter(name="virtualNetwork")
    def virtual_network(self) -> 'outputs.VirtualNetworkProfileResponse':
        """
        Description of the Virtual Network.
        """
        return pulumi.get(self, "virtual_network")

    @property
    @pulumi.getter(name="vnetName")
    def vnet_name(self) -> Optional[str]:
        """
        Name of the Virtual Network for the App Service Environment.
        """
        return pulumi.get(self, "vnet_name")

    @property
    @pulumi.getter(name="vnetResourceGroupName")
    def vnet_resource_group_name(self) -> Optional[str]:
        """
        Resource group of the Virtual Network.
        """
        return pulumi.get(self, "vnet_resource_group_name")

    @property
    @pulumi.getter(name="vnetSubnetName")
    def vnet_subnet_name(self) -> Optional[str]:
        """
        Subnet of the Virtual Network.
        """
        return pulumi.get(self, "vnet_subnet_name")

    @property
    @pulumi.getter(name="workerPools")
    def worker_pools(self) -> Sequence['outputs.WorkerPoolResponse']:
        """
        Description of worker pools with worker size IDs, VM sizes, and number of workers in each pool.
        """
        return pulumi.get(self, "worker_pools")


class AwaitableGetAppServiceEnvironmentResult(GetAppServiceEnvironmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAppServiceEnvironmentResult(
            allowed_multi_sizes=self.allowed_multi_sizes,
            allowed_worker_sizes=self.allowed_worker_sizes,
            api_management_account_id=self.api_management_account_id,
            cluster_settings=self.cluster_settings,
            database_edition=self.database_edition,
            database_service_objective=self.database_service_objective,
            default_front_end_scale_factor=self.default_front_end_scale_factor,
            dns_suffix=self.dns_suffix,
            dynamic_cache_enabled=self.dynamic_cache_enabled,
            environment_capacities=self.environment_capacities,
            environment_is_healthy=self.environment_is_healthy,
            environment_status=self.environment_status,
            front_end_scale_factor=self.front_end_scale_factor,
            has_linux_workers=self.has_linux_workers,
            id=self.id,
            internal_load_balancing_mode=self.internal_load_balancing_mode,
            ipssl_address_count=self.ipssl_address_count,
            kind=self.kind,
            last_action=self.last_action,
            last_action_result=self.last_action_result,
            location=self.location,
            maximum_number_of_machines=self.maximum_number_of_machines,
            multi_role_count=self.multi_role_count,
            multi_size=self.multi_size,
            name=self.name,
            network_access_control_list=self.network_access_control_list,
            provisioning_state=self.provisioning_state,
            resource_group=self.resource_group,
            ssl_cert_key_vault_id=self.ssl_cert_key_vault_id,
            ssl_cert_key_vault_secret_name=self.ssl_cert_key_vault_secret_name,
            status=self.status,
            subscription_id=self.subscription_id,
            suspended=self.suspended,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            upgrade_domains=self.upgrade_domains,
            user_whitelisted_ip_ranges=self.user_whitelisted_ip_ranges,
            vip_mappings=self.vip_mappings,
            virtual_network=self.virtual_network,
            vnet_name=self.vnet_name,
            vnet_resource_group_name=self.vnet_resource_group_name,
            vnet_subnet_name=self.vnet_subnet_name,
            worker_pools=self.worker_pools)


def get_app_service_environment(name: Optional[str] = None,
                                resource_group_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAppServiceEnvironmentResult:
    """
    App Service Environment ARM resource.


    :param str name: Name of the App Service Environment.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20200901:getAppServiceEnvironment', __args__, opts=opts, typ=GetAppServiceEnvironmentResult).value

    return AwaitableGetAppServiceEnvironmentResult(
        allowed_multi_sizes=__ret__.allowed_multi_sizes,
        allowed_worker_sizes=__ret__.allowed_worker_sizes,
        api_management_account_id=__ret__.api_management_account_id,
        cluster_settings=__ret__.cluster_settings,
        database_edition=__ret__.database_edition,
        database_service_objective=__ret__.database_service_objective,
        default_front_end_scale_factor=__ret__.default_front_end_scale_factor,
        dns_suffix=__ret__.dns_suffix,
        dynamic_cache_enabled=__ret__.dynamic_cache_enabled,
        environment_capacities=__ret__.environment_capacities,
        environment_is_healthy=__ret__.environment_is_healthy,
        environment_status=__ret__.environment_status,
        front_end_scale_factor=__ret__.front_end_scale_factor,
        has_linux_workers=__ret__.has_linux_workers,
        id=__ret__.id,
        internal_load_balancing_mode=__ret__.internal_load_balancing_mode,
        ipssl_address_count=__ret__.ipssl_address_count,
        kind=__ret__.kind,
        last_action=__ret__.last_action,
        last_action_result=__ret__.last_action_result,
        location=__ret__.location,
        maximum_number_of_machines=__ret__.maximum_number_of_machines,
        multi_role_count=__ret__.multi_role_count,
        multi_size=__ret__.multi_size,
        name=__ret__.name,
        network_access_control_list=__ret__.network_access_control_list,
        provisioning_state=__ret__.provisioning_state,
        resource_group=__ret__.resource_group,
        ssl_cert_key_vault_id=__ret__.ssl_cert_key_vault_id,
        ssl_cert_key_vault_secret_name=__ret__.ssl_cert_key_vault_secret_name,
        status=__ret__.status,
        subscription_id=__ret__.subscription_id,
        suspended=__ret__.suspended,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type,
        upgrade_domains=__ret__.upgrade_domains,
        user_whitelisted_ip_ranges=__ret__.user_whitelisted_ip_ranges,
        vip_mappings=__ret__.vip_mappings,
        virtual_network=__ret__.virtual_network,
        vnet_name=__ret__.vnet_name,
        vnet_resource_group_name=__ret__.vnet_resource_group_name,
        vnet_subnet_name=__ret__.vnet_subnet_name,
        worker_pools=__ret__.worker_pools)


@_utilities.lift_output_func(get_app_service_environment)
def get_app_service_environment_output(name: Optional[pulumi.Input[str]] = None,
                                       resource_group_name: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAppServiceEnvironmentResult]:
    """
    App Service Environment ARM resource.


    :param str name: Name of the App Service Environment.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    ...
