# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['WorkloadClassifierArgs', 'WorkloadClassifier']

@pulumi.input_type
class WorkloadClassifierArgs:
    def __init__(__self__, *,
                 database_name: pulumi.Input[str],
                 member_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 server_name: pulumi.Input[str],
                 workload_group_name: pulumi.Input[str],
                 context: Optional[pulumi.Input[str]] = None,
                 end_time: Optional[pulumi.Input[str]] = None,
                 importance: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 workload_classifier_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a WorkloadClassifier resource.
        :param pulumi.Input[str] database_name: The name of the database.
        :param pulumi.Input[str] member_name: The workload classifier member name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[str] workload_group_name: The name of the workload group from which to receive the classifier from.
        :param pulumi.Input[str] context: The workload classifier context.
        :param pulumi.Input[str] end_time: The workload classifier end time for classification.
        :param pulumi.Input[str] importance: The workload classifier importance.
        :param pulumi.Input[str] label: The workload classifier label.
        :param pulumi.Input[str] start_time: The workload classifier start time for classification.
        :param pulumi.Input[str] workload_classifier_name: The name of the workload classifier to create/update.
        """
        pulumi.set(__self__, "database_name", database_name)
        pulumi.set(__self__, "member_name", member_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "server_name", server_name)
        pulumi.set(__self__, "workload_group_name", workload_group_name)
        if context is not None:
            pulumi.set(__self__, "context", context)
        if end_time is not None:
            pulumi.set(__self__, "end_time", end_time)
        if importance is not None:
            pulumi.set(__self__, "importance", importance)
        if label is not None:
            pulumi.set(__self__, "label", label)
        if start_time is not None:
            pulumi.set(__self__, "start_time", start_time)
        if workload_classifier_name is not None:
            pulumi.set(__self__, "workload_classifier_name", workload_classifier_name)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[str]:
        """
        The name of the database.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter(name="memberName")
    def member_name(self) -> pulumi.Input[str]:
        """
        The workload classifier member name.
        """
        return pulumi.get(self, "member_name")

    @member_name.setter
    def member_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "member_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[str]:
        """
        The name of the server.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter(name="workloadGroupName")
    def workload_group_name(self) -> pulumi.Input[str]:
        """
        The name of the workload group from which to receive the classifier from.
        """
        return pulumi.get(self, "workload_group_name")

    @workload_group_name.setter
    def workload_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workload_group_name", value)

    @property
    @pulumi.getter
    def context(self) -> Optional[pulumi.Input[str]]:
        """
        The workload classifier context.
        """
        return pulumi.get(self, "context")

    @context.setter
    def context(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "context", value)

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[str]]:
        """
        The workload classifier end time for classification.
        """
        return pulumi.get(self, "end_time")

    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_time", value)

    @property
    @pulumi.getter
    def importance(self) -> Optional[pulumi.Input[str]]:
        """
        The workload classifier importance.
        """
        return pulumi.get(self, "importance")

    @importance.setter
    def importance(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "importance", value)

    @property
    @pulumi.getter
    def label(self) -> Optional[pulumi.Input[str]]:
        """
        The workload classifier label.
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[str]]:
        """
        The workload classifier start time for classification.
        """
        return pulumi.get(self, "start_time")

    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_time", value)

    @property
    @pulumi.getter(name="workloadClassifierName")
    def workload_classifier_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the workload classifier to create/update.
        """
        return pulumi.get(self, "workload_classifier_name")

    @workload_classifier_name.setter
    def workload_classifier_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workload_classifier_name", value)


class WorkloadClassifier(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 context: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 end_time: Optional[pulumi.Input[str]] = None,
                 importance: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 member_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 workload_classifier_name: Optional[pulumi.Input[str]] = None,
                 workload_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Workload classifier operations for a data warehouse

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] context: The workload classifier context.
        :param pulumi.Input[str] database_name: The name of the database.
        :param pulumi.Input[str] end_time: The workload classifier end time for classification.
        :param pulumi.Input[str] importance: The workload classifier importance.
        :param pulumi.Input[str] label: The workload classifier label.
        :param pulumi.Input[str] member_name: The workload classifier member name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[str] start_time: The workload classifier start time for classification.
        :param pulumi.Input[str] workload_classifier_name: The name of the workload classifier to create/update.
        :param pulumi.Input[str] workload_group_name: The name of the workload group from which to receive the classifier from.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkloadClassifierArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Workload classifier operations for a data warehouse

        :param str resource_name: The name of the resource.
        :param WorkloadClassifierArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkloadClassifierArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 context: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 end_time: Optional[pulumi.Input[str]] = None,
                 importance: Optional[pulumi.Input[str]] = None,
                 label: Optional[pulumi.Input[str]] = None,
                 member_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 start_time: Optional[pulumi.Input[str]] = None,
                 workload_classifier_name: Optional[pulumi.Input[str]] = None,
                 workload_group_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = WorkloadClassifierArgs.__new__(WorkloadClassifierArgs)

            __props__.__dict__["context"] = context
            if database_name is None and not opts.urn:
                raise TypeError("Missing required property 'database_name'")
            __props__.__dict__["database_name"] = database_name
            __props__.__dict__["end_time"] = end_time
            __props__.__dict__["importance"] = importance
            __props__.__dict__["label"] = label
            if member_name is None and not opts.urn:
                raise TypeError("Missing required property 'member_name'")
            __props__.__dict__["member_name"] = member_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if server_name is None and not opts.urn:
                raise TypeError("Missing required property 'server_name'")
            __props__.__dict__["server_name"] = server_name
            __props__.__dict__["start_time"] = start_time
            __props__.__dict__["workload_classifier_name"] = workload_classifier_name
            if workload_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'workload_group_name'")
            __props__.__dict__["workload_group_name"] = workload_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sql:WorkloadClassifier"), pulumi.Alias(type_="azure-native:sql/v20190601preview:WorkloadClassifier"), pulumi.Alias(type_="azure-native:sql/v20200202preview:WorkloadClassifier"), pulumi.Alias(type_="azure-native:sql/v20200801preview:WorkloadClassifier"), pulumi.Alias(type_="azure-native:sql/v20201101preview:WorkloadClassifier"), pulumi.Alias(type_="azure-native:sql/v20210201preview:WorkloadClassifier"), pulumi.Alias(type_="azure-native:sql/v20210501preview:WorkloadClassifier")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WorkloadClassifier, __self__).__init__(
            'azure-native:sql/v20210801preview:WorkloadClassifier',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkloadClassifier':
        """
        Get an existing WorkloadClassifier resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkloadClassifierArgs.__new__(WorkloadClassifierArgs)

        __props__.__dict__["context"] = None
        __props__.__dict__["end_time"] = None
        __props__.__dict__["importance"] = None
        __props__.__dict__["label"] = None
        __props__.__dict__["member_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["start_time"] = None
        __props__.__dict__["type"] = None
        return WorkloadClassifier(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def context(self) -> pulumi.Output[Optional[str]]:
        """
        The workload classifier context.
        """
        return pulumi.get(self, "context")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> pulumi.Output[Optional[str]]:
        """
        The workload classifier end time for classification.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter
    def importance(self) -> pulumi.Output[Optional[str]]:
        """
        The workload classifier importance.
        """
        return pulumi.get(self, "importance")

    @property
    @pulumi.getter
    def label(self) -> pulumi.Output[Optional[str]]:
        """
        The workload classifier label.
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter(name="memberName")
    def member_name(self) -> pulumi.Output[str]:
        """
        The workload classifier member name.
        """
        return pulumi.get(self, "member_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="startTime")
    def start_time(self) -> pulumi.Output[Optional[str]]:
        """
        The workload classifier start time for classification.
        """
        return pulumi.get(self, "start_time")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

