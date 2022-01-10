# coding: utf-8

"""
    AssistedInstall

    Assisted installation  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ClusterCreateParams(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'high_availability_mode': 'str',
        'openshift_version': 'str',
        'ocp_release_image': 'str',
        'base_dns_domain': 'str',
        'cluster_network_cidr': 'str',
        'cluster_network_host_prefix': 'int',
        'service_network_cidr': 'str',
        'ingress_vip': 'str',
        'pull_secret': 'str',
        'ssh_public_key': 'str',
        'vip_dhcp_allocation': 'bool',
        'http_proxy': 'str',
        'https_proxy': 'str',
        'no_proxy': 'str',
        'user_managed_networking': 'bool',
        'additional_ntp_source': 'str',
        'olm_operators': 'list[OperatorCreateParams]',
        'hyperthreading': 'str',
        'network_type': 'str',
        'schedulable_masters': 'bool',
        'cluster_networks': 'list[ClusterNetwork]',
        'service_networks': 'list[ServiceNetwork]',
        'machine_networks': 'list[MachineNetwork]',
        'platform': 'Platform',
        'cpu_architecture': 'str',
        'disk_encryption': 'DiskEncryption',
        'ignition_endpoint': 'IgnitionEndpoint'
    }

    attribute_map = {
        'name': 'name',
        'high_availability_mode': 'high_availability_mode',
        'openshift_version': 'openshift_version',
        'ocp_release_image': 'ocp_release_image',
        'base_dns_domain': 'base_dns_domain',
        'cluster_network_cidr': 'cluster_network_cidr',
        'cluster_network_host_prefix': 'cluster_network_host_prefix',
        'service_network_cidr': 'service_network_cidr',
        'ingress_vip': 'ingress_vip',
        'pull_secret': 'pull_secret',
        'ssh_public_key': 'ssh_public_key',
        'vip_dhcp_allocation': 'vip_dhcp_allocation',
        'http_proxy': 'http_proxy',
        'https_proxy': 'https_proxy',
        'no_proxy': 'no_proxy',
        'user_managed_networking': 'user_managed_networking',
        'additional_ntp_source': 'additional_ntp_source',
        'olm_operators': 'olm_operators',
        'hyperthreading': 'hyperthreading',
        'network_type': 'network_type',
        'schedulable_masters': 'schedulable_masters',
        'cluster_networks': 'cluster_networks',
        'service_networks': 'service_networks',
        'machine_networks': 'machine_networks',
        'platform': 'platform',
        'cpu_architecture': 'cpu_architecture',
        'disk_encryption': 'disk_encryption',
        'ignition_endpoint': 'ignition_endpoint'
    }

    def __init__(self, name=None, high_availability_mode='Full', openshift_version=None, ocp_release_image=None, base_dns_domain=None, cluster_network_cidr='10.128.0.0/14', cluster_network_host_prefix=None, service_network_cidr='172.30.0.0/16', ingress_vip=None, pull_secret=None, ssh_public_key=None, vip_dhcp_allocation=True, http_proxy=None, https_proxy=None, no_proxy=None, user_managed_networking=False, additional_ntp_source=None, olm_operators=None, hyperthreading='all', network_type='OpenShiftSDN', schedulable_masters=False, cluster_networks=None, service_networks=None, machine_networks=None, platform=None, cpu_architecture='x86_64', disk_encryption=None, ignition_endpoint=None):  # noqa: E501
        """ClusterCreateParams - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._high_availability_mode = None
        self._openshift_version = None
        self._ocp_release_image = None
        self._base_dns_domain = None
        self._cluster_network_cidr = None
        self._cluster_network_host_prefix = None
        self._service_network_cidr = None
        self._ingress_vip = None
        self._pull_secret = None
        self._ssh_public_key = None
        self._vip_dhcp_allocation = None
        self._http_proxy = None
        self._https_proxy = None
        self._no_proxy = None
        self._user_managed_networking = None
        self._additional_ntp_source = None
        self._olm_operators = None
        self._hyperthreading = None
        self._network_type = None
        self._schedulable_masters = None
        self._cluster_networks = None
        self._service_networks = None
        self._machine_networks = None
        self._platform = None
        self._cpu_architecture = None
        self._disk_encryption = None
        self._ignition_endpoint = None
        self.discriminator = None

        self.name = name
        if high_availability_mode is not None:
            self.high_availability_mode = high_availability_mode
        self.openshift_version = openshift_version
        if ocp_release_image is not None:
            self.ocp_release_image = ocp_release_image
        if base_dns_domain is not None:
            self.base_dns_domain = base_dns_domain
        if cluster_network_cidr is not None:
            self.cluster_network_cidr = cluster_network_cidr
        if cluster_network_host_prefix is not None:
            self.cluster_network_host_prefix = cluster_network_host_prefix
        if service_network_cidr is not None:
            self.service_network_cidr = service_network_cidr
        if ingress_vip is not None:
            self.ingress_vip = ingress_vip
        self.pull_secret = pull_secret
        if ssh_public_key is not None:
            self.ssh_public_key = ssh_public_key
        if vip_dhcp_allocation is not None:
            self.vip_dhcp_allocation = vip_dhcp_allocation
        if http_proxy is not None:
            self.http_proxy = http_proxy
        if https_proxy is not None:
            self.https_proxy = https_proxy
        if no_proxy is not None:
            self.no_proxy = no_proxy
        if user_managed_networking is not None:
            self.user_managed_networking = user_managed_networking
        if additional_ntp_source is not None:
            self.additional_ntp_source = additional_ntp_source
        if olm_operators is not None:
            self.olm_operators = olm_operators
        if hyperthreading is not None:
            self.hyperthreading = hyperthreading
        if network_type is not None:
            self.network_type = network_type
        if schedulable_masters is not None:
            self.schedulable_masters = schedulable_masters
        if cluster_networks is not None:
            self.cluster_networks = cluster_networks
        if service_networks is not None:
            self.service_networks = service_networks
        if machine_networks is not None:
            self.machine_networks = machine_networks
        if platform is not None:
            self.platform = platform
        if cpu_architecture is not None:
            self.cpu_architecture = cpu_architecture
        if disk_encryption is not None:
            self.disk_encryption = disk_encryption
        if ignition_endpoint is not None:
            self.ignition_endpoint = ignition_endpoint

    @property
    def name(self):
        """Gets the name of this ClusterCreateParams.  # noqa: E501

        Name of the OpenShift cluster.  # noqa: E501

        :return: The name of this ClusterCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterCreateParams.

        Name of the OpenShift cluster.  # noqa: E501

        :param name: The name of this ClusterCreateParams.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 54:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `54`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def high_availability_mode(self):
        """Gets the high_availability_mode of this ClusterCreateParams.  # noqa: E501

        Guaranteed availability of the installed cluster. 'Full' installs a Highly-Available cluster over multiple master nodes whereas 'None' installs a full cluster over one node.   # noqa: E501

        :return: The high_availability_mode of this ClusterCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._high_availability_mode

    @high_availability_mode.setter
    def high_availability_mode(self, high_availability_mode):
        """Sets the high_availability_mode of this ClusterCreateParams.

        Guaranteed availability of the installed cluster. 'Full' installs a Highly-Available cluster over multiple master nodes whereas 'None' installs a full cluster over one node.   # noqa: E501

        :param high_availability_mode: The high_availability_mode of this ClusterCreateParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["Full", "None"]  # noqa: E501
        if high_availability_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `high_availability_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(high_availability_mode, allowed_values)
            )

        self._high_availability_mode = high_availability_mode

    @property
    def openshift_version(self):
        """Gets the openshift_version of this ClusterCreateParams.  # noqa: E501

        Version of the OpenShift cluster.  # noqa: E501

        :return: The openshift_version of this ClusterCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._openshift_version

    @openshift_version.setter
    def openshift_version(self, openshift_version):
        """Sets the openshift_version of this ClusterCreateParams.

        Version of the OpenShift cluster.  # noqa: E501

        :param openshift_version: The openshift_version of this ClusterCreateParams.  # noqa: E501
        :type: str
        """
        if openshift_version is None:
            raise ValueError("Invalid value for `openshift_version`, must not be `None`")  # noqa: E501

        self._openshift_version = openshift_version

    @property
    def ocp_release_image(self):
        """Gets the ocp_release_image of this ClusterCreateParams.  # noqa: E501

        OpenShift release image URI.  # noqa: E501

        :return: The ocp_release_image of this ClusterCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._ocp_release_image

    @ocp_release_image.setter
    def ocp_release_image(self, ocp_release_image):
        """Sets the ocp_release_image of this ClusterCreateParams.

        OpenShift release image URI.  # noqa: E501

        :param ocp_release_image: The ocp_release_image of this ClusterCreateParams.  # noqa: E501
        :type: str
        """

        self._ocp_release_image = ocp_release_image

    @property
    def base_dns_domain(self):
        """Gets the base_dns_domain of this ClusterCreateParams.  # noqa: E501

        Base domain of the cluster. All DNS records must be sub-domains of this base and include the cluster name.  # noqa: E501

        :return: The base_dns_domain of this ClusterCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._base_dns_domain

    @base_dns_domain.setter
    def base_dns_domain(self, base_dns_domain):
        """Sets the base_dns_domain of this ClusterCreateParams.

        Base domain of the cluster. All DNS records must be sub-domains of this base and include the cluster name.  # noqa: E501

        :param base_dns_domain: The base_dns_domain of this ClusterCreateParams.  # noqa: E501
        :type: str
        """

        self._base_dns_domain = base_dns_domain

    @property
    def cluster_network_cidr(self):
        """Gets the cluster_network_cidr of this ClusterCreateParams.  # noqa: E501

        IP address block from which Pod IPs are allocated. This block must not overlap with existing physical networks. These IP addresses are used for the Pod network, and if you need to access the Pods from an external network, configure load balancers and routers to manage the traffic.  # noqa: E501

        :return: The cluster_network_cidr of this ClusterCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._cluster_network_cidr

    @cluster_network_cidr.setter
    def cluster_network_cidr(self, cluster_network_cidr):
        """Sets the cluster_network_cidr of this ClusterCreateParams.

        IP address block from which Pod IPs are allocated. This block must not overlap with existing physical networks. These IP addresses are used for the Pod network, and if you need to access the Pods from an external network, configure load balancers and routers to manage the traffic.  # noqa: E501

        :param cluster_network_cidr: The cluster_network_cidr of this ClusterCreateParams.  # noqa: E501
        :type: str
        """

        self._cluster_network_cidr = cluster_network_cidr

    @property
    def cluster_network_host_prefix(self):
        """Gets the cluster_network_host_prefix of this ClusterCreateParams.  # noqa: E501

        The subnet prefix length to assign to each individual node. For example, if clusterNetworkHostPrefix is set to 23, then each node is assigned a /23 subnet out of the given cidr (clusterNetworkCIDR), which allows for 510 (2^(32 - 23) - 2) pod IPs addresses. If you are required to provide access to nodes from an external network, configure load balancers and routers to manage the traffic.  # noqa: E501

        :return: The cluster_network_host_prefix of this ClusterCreateParams.  # noqa: E501
        :rtype: int
        """
        return self._cluster_network_host_prefix

    @cluster_network_host_prefix.setter
    def cluster_network_host_prefix(self, cluster_network_host_prefix):
        """Sets the cluster_network_host_prefix of this ClusterCreateParams.

        The subnet prefix length to assign to each individual node. For example, if clusterNetworkHostPrefix is set to 23, then each node is assigned a /23 subnet out of the given cidr (clusterNetworkCIDR), which allows for 510 (2^(32 - 23) - 2) pod IPs addresses. If you are required to provide access to nodes from an external network, configure load balancers and routers to manage the traffic.  # noqa: E501

        :param cluster_network_host_prefix: The cluster_network_host_prefix of this ClusterCreateParams.  # noqa: E501
        :type: int
        """
        if cluster_network_host_prefix is not None and cluster_network_host_prefix > 128:  # noqa: E501
            raise ValueError("Invalid value for `cluster_network_host_prefix`, must be a value less than or equal to `128`")  # noqa: E501
        if cluster_network_host_prefix is not None and cluster_network_host_prefix < 1:  # noqa: E501
            raise ValueError("Invalid value for `cluster_network_host_prefix`, must be a value greater than or equal to `1`")  # noqa: E501

        self._cluster_network_host_prefix = cluster_network_host_prefix

    @property
    def service_network_cidr(self):
        """Gets the service_network_cidr of this ClusterCreateParams.  # noqa: E501

        The IP address pool to use for service IP addresses. You can enter only one IP address pool. If you need to access the services from an external network, configure load balancers and routers to manage the traffic.  # noqa: E501

        :return: The service_network_cidr of this ClusterCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._service_network_cidr

    @service_network_cidr.setter
    def service_network_cidr(self, service_network_cidr):
        """Sets the service_network_cidr of this ClusterCreateParams.

        The IP address pool to use for service IP addresses. You can enter only one IP address pool. If you need to access the services from an external network, configure load balancers and routers to manage the traffic.  # noqa: E501

        :param service_network_cidr: The service_network_cidr of this ClusterCreateParams.  # noqa: E501
        :type: str
        """

        self._service_network_cidr = service_network_cidr

    @property
    def ingress_vip(self):
        """Gets the ingress_vip of this ClusterCreateParams.  # noqa: E501

        The virtual IP used for cluster ingress traffic.  # noqa: E501

        :return: The ingress_vip of this ClusterCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._ingress_vip

    @ingress_vip.setter
    def ingress_vip(self, ingress_vip):
        """Sets the ingress_vip of this ClusterCreateParams.

        The virtual IP used for cluster ingress traffic.  # noqa: E501

        :param ingress_vip: The ingress_vip of this ClusterCreateParams.  # noqa: E501
        :type: str
        """

        self._ingress_vip = ingress_vip

    @property
    def pull_secret(self):
        """Gets the pull_secret of this ClusterCreateParams.  # noqa: E501

        The pull secret obtained from Red Hat OpenShift Cluster Manager at console.redhat.com/openshift/install/pull-secret.  # noqa: E501

        :return: The pull_secret of this ClusterCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._pull_secret

    @pull_secret.setter
    def pull_secret(self, pull_secret):
        """Sets the pull_secret of this ClusterCreateParams.

        The pull secret obtained from Red Hat OpenShift Cluster Manager at console.redhat.com/openshift/install/pull-secret.  # noqa: E501

        :param pull_secret: The pull_secret of this ClusterCreateParams.  # noqa: E501
        :type: str
        """
        if pull_secret is None:
            raise ValueError("Invalid value for `pull_secret`, must not be `None`")  # noqa: E501

        self._pull_secret = pull_secret

    @property
    def ssh_public_key(self):
        """Gets the ssh_public_key of this ClusterCreateParams.  # noqa: E501

        SSH public key for debugging OpenShift nodes.  # noqa: E501

        :return: The ssh_public_key of this ClusterCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._ssh_public_key

    @ssh_public_key.setter
    def ssh_public_key(self, ssh_public_key):
        """Sets the ssh_public_key of this ClusterCreateParams.

        SSH public key for debugging OpenShift nodes.  # noqa: E501

        :param ssh_public_key: The ssh_public_key of this ClusterCreateParams.  # noqa: E501
        :type: str
        """

        self._ssh_public_key = ssh_public_key

    @property
    def vip_dhcp_allocation(self):
        """Gets the vip_dhcp_allocation of this ClusterCreateParams.  # noqa: E501

        Indicate if virtual IP DHCP allocation mode is enabled.  # noqa: E501

        :return: The vip_dhcp_allocation of this ClusterCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._vip_dhcp_allocation

    @vip_dhcp_allocation.setter
    def vip_dhcp_allocation(self, vip_dhcp_allocation):
        """Sets the vip_dhcp_allocation of this ClusterCreateParams.

        Indicate if virtual IP DHCP allocation mode is enabled.  # noqa: E501

        :param vip_dhcp_allocation: The vip_dhcp_allocation of this ClusterCreateParams.  # noqa: E501
        :type: bool
        """

        self._vip_dhcp_allocation = vip_dhcp_allocation

    @property
    def http_proxy(self):
        """Gets the http_proxy of this ClusterCreateParams.  # noqa: E501

        A proxy URL to use for creating HTTP connections outside the cluster. http://\\<username\\>:\\<pswd\\>@\\<ip\\>:\\<port\\>   # noqa: E501

        :return: The http_proxy of this ClusterCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._http_proxy

    @http_proxy.setter
    def http_proxy(self, http_proxy):
        """Sets the http_proxy of this ClusterCreateParams.

        A proxy URL to use for creating HTTP connections outside the cluster. http://\\<username\\>:\\<pswd\\>@\\<ip\\>:\\<port\\>   # noqa: E501

        :param http_proxy: The http_proxy of this ClusterCreateParams.  # noqa: E501
        :type: str
        """

        self._http_proxy = http_proxy

    @property
    def https_proxy(self):
        """Gets the https_proxy of this ClusterCreateParams.  # noqa: E501

        A proxy URL to use for creating HTTPS connections outside the cluster. http://\\<username\\>:\\<pswd\\>@\\<ip\\>:\\<port\\>   # noqa: E501

        :return: The https_proxy of this ClusterCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._https_proxy

    @https_proxy.setter
    def https_proxy(self, https_proxy):
        """Sets the https_proxy of this ClusterCreateParams.

        A proxy URL to use for creating HTTPS connections outside the cluster. http://\\<username\\>:\\<pswd\\>@\\<ip\\>:\\<port\\>   # noqa: E501

        :param https_proxy: The https_proxy of this ClusterCreateParams.  # noqa: E501
        :type: str
        """

        self._https_proxy = https_proxy

    @property
    def no_proxy(self):
        """Gets the no_proxy of this ClusterCreateParams.  # noqa: E501

        An \"*\" or a comma-separated list of destination domain names, domains, IP addresses, or other network CIDRs to exclude from proxying.  # noqa: E501

        :return: The no_proxy of this ClusterCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._no_proxy

    @no_proxy.setter
    def no_proxy(self, no_proxy):
        """Sets the no_proxy of this ClusterCreateParams.

        An \"*\" or a comma-separated list of destination domain names, domains, IP addresses, or other network CIDRs to exclude from proxying.  # noqa: E501

        :param no_proxy: The no_proxy of this ClusterCreateParams.  # noqa: E501
        :type: str
        """

        self._no_proxy = no_proxy

    @property
    def user_managed_networking(self):
        """Gets the user_managed_networking of this ClusterCreateParams.  # noqa: E501

        Indicate if the networking is managed by the user.  # noqa: E501

        :return: The user_managed_networking of this ClusterCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._user_managed_networking

    @user_managed_networking.setter
    def user_managed_networking(self, user_managed_networking):
        """Sets the user_managed_networking of this ClusterCreateParams.

        Indicate if the networking is managed by the user.  # noqa: E501

        :param user_managed_networking: The user_managed_networking of this ClusterCreateParams.  # noqa: E501
        :type: bool
        """

        self._user_managed_networking = user_managed_networking

    @property
    def additional_ntp_source(self):
        """Gets the additional_ntp_source of this ClusterCreateParams.  # noqa: E501

        A comma-separated list of NTP sources (name or IP) going to be added to all the hosts.  # noqa: E501

        :return: The additional_ntp_source of this ClusterCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._additional_ntp_source

    @additional_ntp_source.setter
    def additional_ntp_source(self, additional_ntp_source):
        """Sets the additional_ntp_source of this ClusterCreateParams.

        A comma-separated list of NTP sources (name or IP) going to be added to all the hosts.  # noqa: E501

        :param additional_ntp_source: The additional_ntp_source of this ClusterCreateParams.  # noqa: E501
        :type: str
        """

        self._additional_ntp_source = additional_ntp_source

    @property
    def olm_operators(self):
        """Gets the olm_operators of this ClusterCreateParams.  # noqa: E501

        List of OLM operators to be installed.  # noqa: E501

        :return: The olm_operators of this ClusterCreateParams.  # noqa: E501
        :rtype: list[OperatorCreateParams]
        """
        return self._olm_operators

    @olm_operators.setter
    def olm_operators(self, olm_operators):
        """Sets the olm_operators of this ClusterCreateParams.

        List of OLM operators to be installed.  # noqa: E501

        :param olm_operators: The olm_operators of this ClusterCreateParams.  # noqa: E501
        :type: list[OperatorCreateParams]
        """

        self._olm_operators = olm_operators

    @property
    def hyperthreading(self):
        """Gets the hyperthreading of this ClusterCreateParams.  # noqa: E501

        Enable/disable hyperthreading on master nodes, worker nodes, or all nodes.  # noqa: E501

        :return: The hyperthreading of this ClusterCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._hyperthreading

    @hyperthreading.setter
    def hyperthreading(self, hyperthreading):
        """Sets the hyperthreading of this ClusterCreateParams.

        Enable/disable hyperthreading on master nodes, worker nodes, or all nodes.  # noqa: E501

        :param hyperthreading: The hyperthreading of this ClusterCreateParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["masters", "workers", "none", "all"]  # noqa: E501
        if hyperthreading not in allowed_values:
            raise ValueError(
                "Invalid value for `hyperthreading` ({0}), must be one of {1}"  # noqa: E501
                .format(hyperthreading, allowed_values)
            )

        self._hyperthreading = hyperthreading

    @property
    def network_type(self):
        """Gets the network_type of this ClusterCreateParams.  # noqa: E501

        The desired network type used.  # noqa: E501

        :return: The network_type of this ClusterCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._network_type

    @network_type.setter
    def network_type(self, network_type):
        """Sets the network_type of this ClusterCreateParams.

        The desired network type used.  # noqa: E501

        :param network_type: The network_type of this ClusterCreateParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["OpenShiftSDN", "OVNKubernetes"]  # noqa: E501
        if network_type not in allowed_values:
            raise ValueError(
                "Invalid value for `network_type` ({0}), must be one of {1}"  # noqa: E501
                .format(network_type, allowed_values)
            )

        self._network_type = network_type

    @property
    def schedulable_masters(self):
        """Gets the schedulable_masters of this ClusterCreateParams.  # noqa: E501

        Schedule workloads on masters  # noqa: E501

        :return: The schedulable_masters of this ClusterCreateParams.  # noqa: E501
        :rtype: bool
        """
        return self._schedulable_masters

    @schedulable_masters.setter
    def schedulable_masters(self, schedulable_masters):
        """Sets the schedulable_masters of this ClusterCreateParams.

        Schedule workloads on masters  # noqa: E501

        :param schedulable_masters: The schedulable_masters of this ClusterCreateParams.  # noqa: E501
        :type: bool
        """

        self._schedulable_masters = schedulable_masters

    @property
    def cluster_networks(self):
        """Gets the cluster_networks of this ClusterCreateParams.  # noqa: E501

        Cluster networks that are associated with this cluster.  # noqa: E501

        :return: The cluster_networks of this ClusterCreateParams.  # noqa: E501
        :rtype: list[ClusterNetwork]
        """
        return self._cluster_networks

    @cluster_networks.setter
    def cluster_networks(self, cluster_networks):
        """Sets the cluster_networks of this ClusterCreateParams.

        Cluster networks that are associated with this cluster.  # noqa: E501

        :param cluster_networks: The cluster_networks of this ClusterCreateParams.  # noqa: E501
        :type: list[ClusterNetwork]
        """

        self._cluster_networks = cluster_networks

    @property
    def service_networks(self):
        """Gets the service_networks of this ClusterCreateParams.  # noqa: E501

        Service networks that are associated with this cluster.  # noqa: E501

        :return: The service_networks of this ClusterCreateParams.  # noqa: E501
        :rtype: list[ServiceNetwork]
        """
        return self._service_networks

    @service_networks.setter
    def service_networks(self, service_networks):
        """Sets the service_networks of this ClusterCreateParams.

        Service networks that are associated with this cluster.  # noqa: E501

        :param service_networks: The service_networks of this ClusterCreateParams.  # noqa: E501
        :type: list[ServiceNetwork]
        """

        self._service_networks = service_networks

    @property
    def machine_networks(self):
        """Gets the machine_networks of this ClusterCreateParams.  # noqa: E501

        Machine networks that are associated with this cluster.  # noqa: E501

        :return: The machine_networks of this ClusterCreateParams.  # noqa: E501
        :rtype: list[MachineNetwork]
        """
        return self._machine_networks

    @machine_networks.setter
    def machine_networks(self, machine_networks):
        """Sets the machine_networks of this ClusterCreateParams.

        Machine networks that are associated with this cluster.  # noqa: E501

        :param machine_networks: The machine_networks of this ClusterCreateParams.  # noqa: E501
        :type: list[MachineNetwork]
        """

        self._machine_networks = machine_networks

    @property
    def platform(self):
        """Gets the platform of this ClusterCreateParams.  # noqa: E501


        :return: The platform of this ClusterCreateParams.  # noqa: E501
        :rtype: Platform
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this ClusterCreateParams.


        :param platform: The platform of this ClusterCreateParams.  # noqa: E501
        :type: Platform
        """

        self._platform = platform

    @property
    def cpu_architecture(self):
        """Gets the cpu_architecture of this ClusterCreateParams.  # noqa: E501

        The CPU architecture of the image (x86_64/arm64/etc).  # noqa: E501

        :return: The cpu_architecture of this ClusterCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._cpu_architecture

    @cpu_architecture.setter
    def cpu_architecture(self, cpu_architecture):
        """Sets the cpu_architecture of this ClusterCreateParams.

        The CPU architecture of the image (x86_64/arm64/etc).  # noqa: E501

        :param cpu_architecture: The cpu_architecture of this ClusterCreateParams.  # noqa: E501
        :type: str
        """

        self._cpu_architecture = cpu_architecture

    @property
    def disk_encryption(self):
        """Gets the disk_encryption of this ClusterCreateParams.  # noqa: E501

        Installation disks encryption mode and host roles to be applied.  # noqa: E501

        :return: The disk_encryption of this ClusterCreateParams.  # noqa: E501
        :rtype: DiskEncryption
        """
        return self._disk_encryption

    @disk_encryption.setter
    def disk_encryption(self, disk_encryption):
        """Sets the disk_encryption of this ClusterCreateParams.

        Installation disks encryption mode and host roles to be applied.  # noqa: E501

        :param disk_encryption: The disk_encryption of this ClusterCreateParams.  # noqa: E501
        :type: DiskEncryption
        """

        self._disk_encryption = disk_encryption

    @property
    def ignition_endpoint(self):
        """Gets the ignition_endpoint of this ClusterCreateParams.  # noqa: E501

        Explicit ignition endpoint overrides the default ignition endpoint.  # noqa: E501

        :return: The ignition_endpoint of this ClusterCreateParams.  # noqa: E501
        :rtype: IgnitionEndpoint
        """
        return self._ignition_endpoint

    @ignition_endpoint.setter
    def ignition_endpoint(self, ignition_endpoint):
        """Sets the ignition_endpoint of this ClusterCreateParams.

        Explicit ignition endpoint overrides the default ignition endpoint.  # noqa: E501

        :param ignition_endpoint: The ignition_endpoint of this ClusterCreateParams.  # noqa: E501
        :type: IgnitionEndpoint
        """

        self._ignition_endpoint = ignition_endpoint

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ClusterCreateParams, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClusterCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
