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

__all__ = ['AKSServiceArgs', 'AKSService']

@pulumi.input_type
class AKSServiceArgs:
    def __init__(__self__, *,
                 compute_type: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 aad_auth_enabled: Optional[pulumi.Input[bool]] = None,
                 app_insights_enabled: Optional[pulumi.Input[bool]] = None,
                 auth_enabled: Optional[pulumi.Input[bool]] = None,
                 auto_scaler: Optional[pulumi.Input['AKSServiceCreateRequestAutoScalerArgs']] = None,
                 compute_name: Optional[pulumi.Input[str]] = None,
                 container_resource_requirements: Optional[pulumi.Input['ContainerResourceRequirementsArgs']] = None,
                 data_collection: Optional[pulumi.Input['AKSServiceCreateRequestDataCollectionArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment_image_request: Optional[pulumi.Input['CreateServiceRequestEnvironmentImageRequestArgs']] = None,
                 is_default: Optional[pulumi.Input[bool]] = None,
                 keys: Optional[pulumi.Input['CreateServiceRequestKeysArgs']] = None,
                 kv_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 liveness_probe_requirements: Optional[pulumi.Input['AKSServiceCreateRequestLivenessProbeRequirementsArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 max_concurrent_requests_per_container: Optional[pulumi.Input[int]] = None,
                 max_queue_wait_ms: Optional[pulumi.Input[int]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 num_replicas: Optional[pulumi.Input[int]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 scoring_timeout_ms: Optional[pulumi.Input[int]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 traffic_percentile: Optional[pulumi.Input[float]] = None,
                 type: Optional[pulumi.Input[Union[str, 'VariantType']]] = None):
        """
        The set of arguments for constructing a AKSService resource.
        :param pulumi.Input[str] compute_type: The compute environment type for the service.
               Expected value is 'AKS'.
        :param pulumi.Input[str] resource_group_name: Name of the resource group in which workspace is located.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        :param pulumi.Input[bool] aad_auth_enabled: Whether or not AAD authentication is enabled.
        :param pulumi.Input[bool] app_insights_enabled: Whether or not Application Insights is enabled.
        :param pulumi.Input[bool] auth_enabled: Whether or not authentication is enabled.
        :param pulumi.Input['AKSServiceCreateRequestAutoScalerArgs'] auto_scaler: The auto scaler properties.
        :param pulumi.Input[str] compute_name: The name of the compute resource.
        :param pulumi.Input['ContainerResourceRequirementsArgs'] container_resource_requirements: The container resource requirements.
        :param pulumi.Input['AKSServiceCreateRequestDataCollectionArgs'] data_collection: Details of the data collection options specified.
        :param pulumi.Input[str] description: The description of the service.
        :param pulumi.Input['CreateServiceRequestEnvironmentImageRequestArgs'] environment_image_request: The Environment, models and assets needed for inferencing.
        :param pulumi.Input[bool] is_default: Is this the default variant.
        :param pulumi.Input['CreateServiceRequestKeysArgs'] keys: The authentication keys.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] kv_tags: The service tag dictionary. Tags are mutable.
        :param pulumi.Input['AKSServiceCreateRequestLivenessProbeRequirementsArgs'] liveness_probe_requirements: The liveness probe requirements.
        :param pulumi.Input[str] location: The name of the Azure location/region.
        :param pulumi.Input[int] max_concurrent_requests_per_container: The maximum number of concurrent requests per container.
        :param pulumi.Input[int] max_queue_wait_ms: Maximum time a request will wait in the queue (in milliseconds). After this time, the service will return 503 (Service Unavailable)
        :param pulumi.Input[str] namespace: Kubernetes namespace for the service.
        :param pulumi.Input[int] num_replicas: The number of replicas on the cluster.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] properties: The service properties dictionary. Properties are immutable.
        :param pulumi.Input[int] scoring_timeout_ms: The scoring timeout in milliseconds.
        :param pulumi.Input[str] service_name: Name of the Azure Machine Learning service.
        :param pulumi.Input[float] traffic_percentile: The amount of traffic variant receives.
        :param pulumi.Input[Union[str, 'VariantType']] type: The type of the variant.
        """
        pulumi.set(__self__, "compute_type", 'AKS')
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if aad_auth_enabled is not None:
            pulumi.set(__self__, "aad_auth_enabled", aad_auth_enabled)
        if app_insights_enabled is not None:
            pulumi.set(__self__, "app_insights_enabled", app_insights_enabled)
        if auth_enabled is not None:
            pulumi.set(__self__, "auth_enabled", auth_enabled)
        if auto_scaler is not None:
            pulumi.set(__self__, "auto_scaler", auto_scaler)
        if compute_name is not None:
            pulumi.set(__self__, "compute_name", compute_name)
        if container_resource_requirements is not None:
            pulumi.set(__self__, "container_resource_requirements", container_resource_requirements)
        if data_collection is not None:
            pulumi.set(__self__, "data_collection", data_collection)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if environment_image_request is not None:
            pulumi.set(__self__, "environment_image_request", environment_image_request)
        if is_default is not None:
            pulumi.set(__self__, "is_default", is_default)
        if keys is not None:
            pulumi.set(__self__, "keys", keys)
        if kv_tags is not None:
            pulumi.set(__self__, "kv_tags", kv_tags)
        if liveness_probe_requirements is not None:
            pulumi.set(__self__, "liveness_probe_requirements", liveness_probe_requirements)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if max_concurrent_requests_per_container is not None:
            pulumi.set(__self__, "max_concurrent_requests_per_container", max_concurrent_requests_per_container)
        if max_queue_wait_ms is not None:
            pulumi.set(__self__, "max_queue_wait_ms", max_queue_wait_ms)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if num_replicas is not None:
            pulumi.set(__self__, "num_replicas", num_replicas)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if scoring_timeout_ms is not None:
            pulumi.set(__self__, "scoring_timeout_ms", scoring_timeout_ms)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)
        if traffic_percentile is not None:
            pulumi.set(__self__, "traffic_percentile", traffic_percentile)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> pulumi.Input[str]:
        """
        The compute environment type for the service.
        Expected value is 'AKS'.
        """
        return pulumi.get(self, "compute_type")

    @compute_type.setter
    def compute_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "compute_type", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group in which workspace is located.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        Name of Azure Machine Learning workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="aadAuthEnabled")
    def aad_auth_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not AAD authentication is enabled.
        """
        return pulumi.get(self, "aad_auth_enabled")

    @aad_auth_enabled.setter
    def aad_auth_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "aad_auth_enabled", value)

    @property
    @pulumi.getter(name="appInsightsEnabled")
    def app_insights_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not Application Insights is enabled.
        """
        return pulumi.get(self, "app_insights_enabled")

    @app_insights_enabled.setter
    def app_insights_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "app_insights_enabled", value)

    @property
    @pulumi.getter(name="authEnabled")
    def auth_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether or not authentication is enabled.
        """
        return pulumi.get(self, "auth_enabled")

    @auth_enabled.setter
    def auth_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auth_enabled", value)

    @property
    @pulumi.getter(name="autoScaler")
    def auto_scaler(self) -> Optional[pulumi.Input['AKSServiceCreateRequestAutoScalerArgs']]:
        """
        The auto scaler properties.
        """
        return pulumi.get(self, "auto_scaler")

    @auto_scaler.setter
    def auto_scaler(self, value: Optional[pulumi.Input['AKSServiceCreateRequestAutoScalerArgs']]):
        pulumi.set(self, "auto_scaler", value)

    @property
    @pulumi.getter(name="computeName")
    def compute_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the compute resource.
        """
        return pulumi.get(self, "compute_name")

    @compute_name.setter
    def compute_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compute_name", value)

    @property
    @pulumi.getter(name="containerResourceRequirements")
    def container_resource_requirements(self) -> Optional[pulumi.Input['ContainerResourceRequirementsArgs']]:
        """
        The container resource requirements.
        """
        return pulumi.get(self, "container_resource_requirements")

    @container_resource_requirements.setter
    def container_resource_requirements(self, value: Optional[pulumi.Input['ContainerResourceRequirementsArgs']]):
        pulumi.set(self, "container_resource_requirements", value)

    @property
    @pulumi.getter(name="dataCollection")
    def data_collection(self) -> Optional[pulumi.Input['AKSServiceCreateRequestDataCollectionArgs']]:
        """
        Details of the data collection options specified.
        """
        return pulumi.get(self, "data_collection")

    @data_collection.setter
    def data_collection(self, value: Optional[pulumi.Input['AKSServiceCreateRequestDataCollectionArgs']]):
        pulumi.set(self, "data_collection", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the service.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="environmentImageRequest")
    def environment_image_request(self) -> Optional[pulumi.Input['CreateServiceRequestEnvironmentImageRequestArgs']]:
        """
        The Environment, models and assets needed for inferencing.
        """
        return pulumi.get(self, "environment_image_request")

    @environment_image_request.setter
    def environment_image_request(self, value: Optional[pulumi.Input['CreateServiceRequestEnvironmentImageRequestArgs']]):
        pulumi.set(self, "environment_image_request", value)

    @property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> Optional[pulumi.Input[bool]]:
        """
        Is this the default variant.
        """
        return pulumi.get(self, "is_default")

    @is_default.setter
    def is_default(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_default", value)

    @property
    @pulumi.getter
    def keys(self) -> Optional[pulumi.Input['CreateServiceRequestKeysArgs']]:
        """
        The authentication keys.
        """
        return pulumi.get(self, "keys")

    @keys.setter
    def keys(self, value: Optional[pulumi.Input['CreateServiceRequestKeysArgs']]):
        pulumi.set(self, "keys", value)

    @property
    @pulumi.getter(name="kvTags")
    def kv_tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The service tag dictionary. Tags are mutable.
        """
        return pulumi.get(self, "kv_tags")

    @kv_tags.setter
    def kv_tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "kv_tags", value)

    @property
    @pulumi.getter(name="livenessProbeRequirements")
    def liveness_probe_requirements(self) -> Optional[pulumi.Input['AKSServiceCreateRequestLivenessProbeRequirementsArgs']]:
        """
        The liveness probe requirements.
        """
        return pulumi.get(self, "liveness_probe_requirements")

    @liveness_probe_requirements.setter
    def liveness_probe_requirements(self, value: Optional[pulumi.Input['AKSServiceCreateRequestLivenessProbeRequirementsArgs']]):
        pulumi.set(self, "liveness_probe_requirements", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Azure location/region.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="maxConcurrentRequestsPerContainer")
    def max_concurrent_requests_per_container(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum number of concurrent requests per container.
        """
        return pulumi.get(self, "max_concurrent_requests_per_container")

    @max_concurrent_requests_per_container.setter
    def max_concurrent_requests_per_container(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_concurrent_requests_per_container", value)

    @property
    @pulumi.getter(name="maxQueueWaitMs")
    def max_queue_wait_ms(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum time a request will wait in the queue (in milliseconds). After this time, the service will return 503 (Service Unavailable)
        """
        return pulumi.get(self, "max_queue_wait_ms")

    @max_queue_wait_ms.setter
    def max_queue_wait_ms(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_queue_wait_ms", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        Kubernetes namespace for the service.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter(name="numReplicas")
    def num_replicas(self) -> Optional[pulumi.Input[int]]:
        """
        The number of replicas on the cluster.
        """
        return pulumi.get(self, "num_replicas")

    @num_replicas.setter
    def num_replicas(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "num_replicas", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The service properties dictionary. Properties are immutable.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="scoringTimeoutMs")
    def scoring_timeout_ms(self) -> Optional[pulumi.Input[int]]:
        """
        The scoring timeout in milliseconds.
        """
        return pulumi.get(self, "scoring_timeout_ms")

    @scoring_timeout_ms.setter
    def scoring_timeout_ms(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "scoring_timeout_ms", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Azure Machine Learning service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="trafficPercentile")
    def traffic_percentile(self) -> Optional[pulumi.Input[float]]:
        """
        The amount of traffic variant receives.
        """
        return pulumi.get(self, "traffic_percentile")

    @traffic_percentile.setter
    def traffic_percentile(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "traffic_percentile", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[Union[str, 'VariantType']]]:
        """
        The type of the variant.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[Union[str, 'VariantType']]]):
        pulumi.set(self, "type", value)


class AKSService(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aad_auth_enabled: Optional[pulumi.Input[bool]] = None,
                 app_insights_enabled: Optional[pulumi.Input[bool]] = None,
                 auth_enabled: Optional[pulumi.Input[bool]] = None,
                 auto_scaler: Optional[pulumi.Input[pulumi.InputType['AKSServiceCreateRequestAutoScalerArgs']]] = None,
                 compute_name: Optional[pulumi.Input[str]] = None,
                 compute_type: Optional[pulumi.Input[str]] = None,
                 container_resource_requirements: Optional[pulumi.Input[pulumi.InputType['ContainerResourceRequirementsArgs']]] = None,
                 data_collection: Optional[pulumi.Input[pulumi.InputType['AKSServiceCreateRequestDataCollectionArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment_image_request: Optional[pulumi.Input[pulumi.InputType['CreateServiceRequestEnvironmentImageRequestArgs']]] = None,
                 is_default: Optional[pulumi.Input[bool]] = None,
                 keys: Optional[pulumi.Input[pulumi.InputType['CreateServiceRequestKeysArgs']]] = None,
                 kv_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 liveness_probe_requirements: Optional[pulumi.Input[pulumi.InputType['AKSServiceCreateRequestLivenessProbeRequirementsArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 max_concurrent_requests_per_container: Optional[pulumi.Input[int]] = None,
                 max_queue_wait_ms: Optional[pulumi.Input[int]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 num_replicas: Optional[pulumi.Input[int]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scoring_timeout_ms: Optional[pulumi.Input[int]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 traffic_percentile: Optional[pulumi.Input[float]] = None,
                 type: Optional[pulumi.Input[Union[str, 'VariantType']]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Machine Learning service object wrapped into ARM resource envelope.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] aad_auth_enabled: Whether or not AAD authentication is enabled.
        :param pulumi.Input[bool] app_insights_enabled: Whether or not Application Insights is enabled.
        :param pulumi.Input[bool] auth_enabled: Whether or not authentication is enabled.
        :param pulumi.Input[pulumi.InputType['AKSServiceCreateRequestAutoScalerArgs']] auto_scaler: The auto scaler properties.
        :param pulumi.Input[str] compute_name: The name of the compute resource.
        :param pulumi.Input[str] compute_type: The compute environment type for the service.
               Expected value is 'AKS'.
        :param pulumi.Input[pulumi.InputType['ContainerResourceRequirementsArgs']] container_resource_requirements: The container resource requirements.
        :param pulumi.Input[pulumi.InputType['AKSServiceCreateRequestDataCollectionArgs']] data_collection: Details of the data collection options specified.
        :param pulumi.Input[str] description: The description of the service.
        :param pulumi.Input[pulumi.InputType['CreateServiceRequestEnvironmentImageRequestArgs']] environment_image_request: The Environment, models and assets needed for inferencing.
        :param pulumi.Input[bool] is_default: Is this the default variant.
        :param pulumi.Input[pulumi.InputType['CreateServiceRequestKeysArgs']] keys: The authentication keys.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] kv_tags: The service tag dictionary. Tags are mutable.
        :param pulumi.Input[pulumi.InputType['AKSServiceCreateRequestLivenessProbeRequirementsArgs']] liveness_probe_requirements: The liveness probe requirements.
        :param pulumi.Input[str] location: The name of the Azure location/region.
        :param pulumi.Input[int] max_concurrent_requests_per_container: The maximum number of concurrent requests per container.
        :param pulumi.Input[int] max_queue_wait_ms: Maximum time a request will wait in the queue (in milliseconds). After this time, the service will return 503 (Service Unavailable)
        :param pulumi.Input[str] namespace: Kubernetes namespace for the service.
        :param pulumi.Input[int] num_replicas: The number of replicas on the cluster.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] properties: The service properties dictionary. Properties are immutable.
        :param pulumi.Input[str] resource_group_name: Name of the resource group in which workspace is located.
        :param pulumi.Input[int] scoring_timeout_ms: The scoring timeout in milliseconds.
        :param pulumi.Input[str] service_name: Name of the Azure Machine Learning service.
        :param pulumi.Input[float] traffic_percentile: The amount of traffic variant receives.
        :param pulumi.Input[Union[str, 'VariantType']] type: The type of the variant.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AKSServiceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Machine Learning service object wrapped into ARM resource envelope.

        :param str resource_name: The name of the resource.
        :param AKSServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AKSServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aad_auth_enabled: Optional[pulumi.Input[bool]] = None,
                 app_insights_enabled: Optional[pulumi.Input[bool]] = None,
                 auth_enabled: Optional[pulumi.Input[bool]] = None,
                 auto_scaler: Optional[pulumi.Input[pulumi.InputType['AKSServiceCreateRequestAutoScalerArgs']]] = None,
                 compute_name: Optional[pulumi.Input[str]] = None,
                 compute_type: Optional[pulumi.Input[str]] = None,
                 container_resource_requirements: Optional[pulumi.Input[pulumi.InputType['ContainerResourceRequirementsArgs']]] = None,
                 data_collection: Optional[pulumi.Input[pulumi.InputType['AKSServiceCreateRequestDataCollectionArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 environment_image_request: Optional[pulumi.Input[pulumi.InputType['CreateServiceRequestEnvironmentImageRequestArgs']]] = None,
                 is_default: Optional[pulumi.Input[bool]] = None,
                 keys: Optional[pulumi.Input[pulumi.InputType['CreateServiceRequestKeysArgs']]] = None,
                 kv_tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 liveness_probe_requirements: Optional[pulumi.Input[pulumi.InputType['AKSServiceCreateRequestLivenessProbeRequirementsArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 max_concurrent_requests_per_container: Optional[pulumi.Input[int]] = None,
                 max_queue_wait_ms: Optional[pulumi.Input[int]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 num_replicas: Optional[pulumi.Input[int]] = None,
                 properties: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 scoring_timeout_ms: Optional[pulumi.Input[int]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 traffic_percentile: Optional[pulumi.Input[float]] = None,
                 type: Optional[pulumi.Input[Union[str, 'VariantType']]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = AKSServiceArgs.__new__(AKSServiceArgs)

            __props__.__dict__["aad_auth_enabled"] = aad_auth_enabled
            __props__.__dict__["app_insights_enabled"] = app_insights_enabled
            __props__.__dict__["auth_enabled"] = auth_enabled
            __props__.__dict__["auto_scaler"] = auto_scaler
            __props__.__dict__["compute_name"] = compute_name
            if compute_type is None and not opts.urn:
                raise TypeError("Missing required property 'compute_type'")
            __props__.__dict__["compute_type"] = 'AKS'
            __props__.__dict__["container_resource_requirements"] = container_resource_requirements
            __props__.__dict__["data_collection"] = data_collection
            __props__.__dict__["description"] = description
            __props__.__dict__["environment_image_request"] = environment_image_request
            __props__.__dict__["is_default"] = is_default
            __props__.__dict__["keys"] = keys
            __props__.__dict__["kv_tags"] = kv_tags
            __props__.__dict__["liveness_probe_requirements"] = liveness_probe_requirements
            __props__.__dict__["location"] = location
            __props__.__dict__["max_concurrent_requests_per_container"] = max_concurrent_requests_per_container
            __props__.__dict__["max_queue_wait_ms"] = max_queue_wait_ms
            __props__.__dict__["namespace"] = namespace
            __props__.__dict__["num_replicas"] = num_replicas
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["scoring_timeout_ms"] = scoring_timeout_ms
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["traffic_percentile"] = traffic_percentile
            __props__.__dict__["type"] = type
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["identity"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["sku"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["tags"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:machinelearningservices:AKSService"), pulumi.Alias(type_="azure-native:machinelearningservices/v20200501preview:AKSService"), pulumi.Alias(type_="azure-native:machinelearningservices/v20200515preview:AKSService"), pulumi.Alias(type_="azure-native:machinelearningservices/v20200901preview:AKSService"), pulumi.Alias(type_="azure-native:machinelearningservices/v20210101:AKSService")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AKSService, __self__).__init__(
            'azure-native:machinelearningservices/v20210401:AKSService',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AKSService':
        """
        Get an existing AKSService resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AKSServiceArgs.__new__(AKSServiceArgs)

        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return AKSService(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.IdentityResponse']]:
        """
        The identity of the resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Any]:
        """
        Service properties
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        The sku of the workspace.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Read only system data
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Contains resource tags defined as key/value pairs.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Specifies the type of the resource.
        """
        return pulumi.get(self, "type")

