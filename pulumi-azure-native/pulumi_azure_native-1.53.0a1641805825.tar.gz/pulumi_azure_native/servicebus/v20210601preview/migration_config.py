# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = ['MigrationConfigArgs', 'MigrationConfig']

@pulumi.input_type
class MigrationConfigArgs:
    def __init__(__self__, *,
                 namespace_name: pulumi.Input[str],
                 post_migration_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 target_namespace: pulumi.Input[str],
                 config_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a MigrationConfig resource.
        :param pulumi.Input[str] namespace_name: The namespace name
        :param pulumi.Input[str] post_migration_name: Name to access Standard Namespace after migration
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[str] target_namespace: Existing premium Namespace ARM Id name which has no entities, will be used for migration
        :param pulumi.Input[str] config_name: The configuration name. Should always be "$default".
        """
        pulumi.set(__self__, "namespace_name", namespace_name)
        pulumi.set(__self__, "post_migration_name", post_migration_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "target_namespace", target_namespace)
        if config_name is not None:
            pulumi.set(__self__, "config_name", config_name)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[str]:
        """
        The namespace name
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter(name="postMigrationName")
    def post_migration_name(self) -> pulumi.Input[str]:
        """
        Name to access Standard Namespace after migration
        """
        return pulumi.get(self, "post_migration_name")

    @post_migration_name.setter
    def post_migration_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "post_migration_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the Resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="targetNamespace")
    def target_namespace(self) -> pulumi.Input[str]:
        """
        Existing premium Namespace ARM Id name which has no entities, will be used for migration
        """
        return pulumi.get(self, "target_namespace")

    @target_namespace.setter
    def target_namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_namespace", value)

    @property
    @pulumi.getter(name="configName")
    def config_name(self) -> Optional[pulumi.Input[str]]:
        """
        The configuration name. Should always be "$default".
        """
        return pulumi.get(self, "config_name")

    @config_name.setter
    def config_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "config_name", value)


class MigrationConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config_name: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 post_migration_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 target_namespace: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Single item in List or Get Migration Config operation

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] config_name: The configuration name. Should always be "$default".
        :param pulumi.Input[str] namespace_name: The namespace name
        :param pulumi.Input[str] post_migration_name: Name to access Standard Namespace after migration
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[str] target_namespace: Existing premium Namespace ARM Id name which has no entities, will be used for migration
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MigrationConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Single item in List or Get Migration Config operation

        :param str resource_name: The name of the resource.
        :param MigrationConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MigrationConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config_name: Optional[pulumi.Input[str]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 post_migration_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 target_namespace: Optional[pulumi.Input[str]] = None,
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
            __props__ = MigrationConfigArgs.__new__(MigrationConfigArgs)

            __props__.__dict__["config_name"] = config_name
            if namespace_name is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_name'")
            __props__.__dict__["namespace_name"] = namespace_name
            if post_migration_name is None and not opts.urn:
                raise TypeError("Missing required property 'post_migration_name'")
            __props__.__dict__["post_migration_name"] = post_migration_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if target_namespace is None and not opts.urn:
                raise TypeError("Missing required property 'target_namespace'")
            __props__.__dict__["target_namespace"] = target_namespace
            __props__.__dict__["migration_state"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["pending_replication_operations_count"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:servicebus:MigrationConfig"), pulumi.Alias(type_="azure-native:servicebus/v20170401:MigrationConfig"), pulumi.Alias(type_="azure-native:servicebus/v20180101preview:MigrationConfig"), pulumi.Alias(type_="azure-native:servicebus/v20210101preview:MigrationConfig"), pulumi.Alias(type_="azure-native:servicebus/v20211101:MigrationConfig")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(MigrationConfig, __self__).__init__(
            'azure-native:servicebus/v20210601preview:MigrationConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'MigrationConfig':
        """
        Get an existing MigrationConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = MigrationConfigArgs.__new__(MigrationConfigArgs)

        __props__.__dict__["migration_state"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["pending_replication_operations_count"] = None
        __props__.__dict__["post_migration_name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["target_namespace"] = None
        __props__.__dict__["type"] = None
        return MigrationConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="migrationState")
    def migration_state(self) -> pulumi.Output[str]:
        """
        State in which Standard to Premium Migration is, possible values : Unknown, Reverting, Completing, Initiating, Syncing, Active
        """
        return pulumi.get(self, "migration_state")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pendingReplicationOperationsCount")
    def pending_replication_operations_count(self) -> pulumi.Output[float]:
        """
        Number of entities pending to be replicated.
        """
        return pulumi.get(self, "pending_replication_operations_count")

    @property
    @pulumi.getter(name="postMigrationName")
    def post_migration_name(self) -> pulumi.Output[str]:
        """
        Name to access Standard Namespace after migration
        """
        return pulumi.get(self, "post_migration_name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of Migration Configuration 
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system meta data relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="targetNamespace")
    def target_namespace(self) -> pulumi.Output[str]:
        """
        Existing premium Namespace ARM Id name which has no entities, will be used for migration
        """
        return pulumi.get(self, "target_namespace")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

