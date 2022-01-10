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

__all__ = ['ManagementLockAtResourceLevelArgs', 'ManagementLockAtResourceLevel']

@pulumi.input_type
class ManagementLockAtResourceLevelArgs:
    def __init__(__self__, *,
                 level: pulumi.Input[Union[str, 'LockLevel']],
                 parent_resource_path: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 resource_name: pulumi.Input[str],
                 resource_provider_namespace: pulumi.Input[str],
                 resource_type: pulumi.Input[str],
                 lock_name: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 owners: Optional[pulumi.Input[Sequence[pulumi.Input['ManagementLockOwnerArgs']]]] = None):
        """
        The set of arguments for constructing a ManagementLockAtResourceLevel resource.
        :param pulumi.Input[Union[str, 'LockLevel']] level: The level of the lock. Possible values are: NotSpecified, CanNotDelete, ReadOnly. CanNotDelete means authorized users are able to read and modify the resources, but not delete. ReadOnly means authorized users can only read from a resource, but they can't modify or delete it.
        :param pulumi.Input[str] parent_resource_path: The parent resource identity.
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing the resource to lock. 
        :param pulumi.Input[str] resource_name: The name of the resource to lock.
        :param pulumi.Input[str] resource_provider_namespace: The resource provider namespace of the resource to lock.
        :param pulumi.Input[str] resource_type: The resource type of the resource to lock.
        :param pulumi.Input[str] lock_name: The name of lock. The lock name can be a maximum of 260 characters. It cannot contain <, > %, &, :, \, ?, /, or any control characters.
        :param pulumi.Input[str] notes: Notes about the lock. Maximum of 512 characters.
        :param pulumi.Input[Sequence[pulumi.Input['ManagementLockOwnerArgs']]] owners: The owners of the lock.
        """
        pulumi.set(__self__, "level", level)
        pulumi.set(__self__, "parent_resource_path", parent_resource_path)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_name", resource_name)
        pulumi.set(__self__, "resource_provider_namespace", resource_provider_namespace)
        pulumi.set(__self__, "resource_type", resource_type)
        if lock_name is not None:
            pulumi.set(__self__, "lock_name", lock_name)
        if notes is not None:
            pulumi.set(__self__, "notes", notes)
        if owners is not None:
            pulumi.set(__self__, "owners", owners)

    @property
    @pulumi.getter
    def level(self) -> pulumi.Input[Union[str, 'LockLevel']]:
        """
        The level of the lock. Possible values are: NotSpecified, CanNotDelete, ReadOnly. CanNotDelete means authorized users are able to read and modify the resources, but not delete. ReadOnly means authorized users can only read from a resource, but they can't modify or delete it.
        """
        return pulumi.get(self, "level")

    @level.setter
    def level(self, value: pulumi.Input[Union[str, 'LockLevel']]):
        pulumi.set(self, "level", value)

    @property
    @pulumi.getter(name="parentResourcePath")
    def parent_resource_path(self) -> pulumi.Input[str]:
        """
        The parent resource identity.
        """
        return pulumi.get(self, "parent_resource_path")

    @parent_resource_path.setter
    def parent_resource_path(self, value: pulumi.Input[str]):
        pulumi.set(self, "parent_resource_path", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group containing the resource to lock. 
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[str]:
        """
        The name of the resource to lock.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="resourceProviderNamespace")
    def resource_provider_namespace(self) -> pulumi.Input[str]:
        """
        The resource provider namespace of the resource to lock.
        """
        return pulumi.get(self, "resource_provider_namespace")

    @resource_provider_namespace.setter
    def resource_provider_namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_provider_namespace", value)

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> pulumi.Input[str]:
        """
        The resource type of the resource to lock.
        """
        return pulumi.get(self, "resource_type")

    @resource_type.setter
    def resource_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_type", value)

    @property
    @pulumi.getter(name="lockName")
    def lock_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of lock. The lock name can be a maximum of 260 characters. It cannot contain <, > %, &, :, \, ?, /, or any control characters.
        """
        return pulumi.get(self, "lock_name")

    @lock_name.setter
    def lock_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lock_name", value)

    @property
    @pulumi.getter
    def notes(self) -> Optional[pulumi.Input[str]]:
        """
        Notes about the lock. Maximum of 512 characters.
        """
        return pulumi.get(self, "notes")

    @notes.setter
    def notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "notes", value)

    @property
    @pulumi.getter
    def owners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ManagementLockOwnerArgs']]]]:
        """
        The owners of the lock.
        """
        return pulumi.get(self, "owners")

    @owners.setter
    def owners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ManagementLockOwnerArgs']]]]):
        pulumi.set(self, "owners", value)


class ManagementLockAtResourceLevel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 level: Optional[pulumi.Input[Union[str, 'LockLevel']]] = None,
                 lock_name: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 owners: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ManagementLockOwnerArgs']]]]] = None,
                 parent_resource_path: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 resource_provider_namespace: Optional[pulumi.Input[str]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The lock information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'LockLevel']] level: The level of the lock. Possible values are: NotSpecified, CanNotDelete, ReadOnly. CanNotDelete means authorized users are able to read and modify the resources, but not delete. ReadOnly means authorized users can only read from a resource, but they can't modify or delete it.
        :param pulumi.Input[str] lock_name: The name of lock. The lock name can be a maximum of 260 characters. It cannot contain <, > %, &, :, \, ?, /, or any control characters.
        :param pulumi.Input[str] notes: Notes about the lock. Maximum of 512 characters.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ManagementLockOwnerArgs']]]] owners: The owners of the lock.
        :param pulumi.Input[str] parent_resource_path: The parent resource identity.
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing the resource to lock. 
        :param pulumi.Input[str] resource_name_: The name of the resource to lock.
        :param pulumi.Input[str] resource_provider_namespace: The resource provider namespace of the resource to lock.
        :param pulumi.Input[str] resource_type: The resource type of the resource to lock.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagementLockAtResourceLevelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The lock information.

        :param str resource_name: The name of the resource.
        :param ManagementLockAtResourceLevelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagementLockAtResourceLevelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 level: Optional[pulumi.Input[Union[str, 'LockLevel']]] = None,
                 lock_name: Optional[pulumi.Input[str]] = None,
                 notes: Optional[pulumi.Input[str]] = None,
                 owners: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ManagementLockOwnerArgs']]]]] = None,
                 parent_resource_path: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 resource_provider_namespace: Optional[pulumi.Input[str]] = None,
                 resource_type: Optional[pulumi.Input[str]] = None,
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
            __props__ = ManagementLockAtResourceLevelArgs.__new__(ManagementLockAtResourceLevelArgs)

            if level is None and not opts.urn:
                raise TypeError("Missing required property 'level'")
            __props__.__dict__["level"] = level
            __props__.__dict__["lock_name"] = lock_name
            __props__.__dict__["notes"] = notes
            __props__.__dict__["owners"] = owners
            if parent_resource_path is None and not opts.urn:
                raise TypeError("Missing required property 'parent_resource_path'")
            __props__.__dict__["parent_resource_path"] = parent_resource_path
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if resource_name_ is None and not opts.urn:
                raise TypeError("Missing required property 'resource_name_'")
            __props__.__dict__["resource_name"] = resource_name_
            if resource_provider_namespace is None and not opts.urn:
                raise TypeError("Missing required property 'resource_provider_namespace'")
            __props__.__dict__["resource_provider_namespace"] = resource_provider_namespace
            if resource_type is None and not opts.urn:
                raise TypeError("Missing required property 'resource_type'")
            __props__.__dict__["resource_type"] = resource_type
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:authorization:ManagementLockAtResourceLevel"), pulumi.Alias(type_="azure-native:authorization/v20160901:ManagementLockAtResourceLevel"), pulumi.Alias(type_="azure-native:authorization/v20200501:ManagementLockAtResourceLevel")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ManagementLockAtResourceLevel, __self__).__init__(
            'azure-native:authorization/v20170401:ManagementLockAtResourceLevel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ManagementLockAtResourceLevel':
        """
        Get an existing ManagementLockAtResourceLevel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ManagementLockAtResourceLevelArgs.__new__(ManagementLockAtResourceLevelArgs)

        __props__.__dict__["level"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["notes"] = None
        __props__.__dict__["owners"] = None
        __props__.__dict__["type"] = None
        return ManagementLockAtResourceLevel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def level(self) -> pulumi.Output[str]:
        """
        The level of the lock. Possible values are: NotSpecified, CanNotDelete, ReadOnly. CanNotDelete means authorized users are able to read and modify the resources, but not delete. ReadOnly means authorized users can only read from a resource, but they can't modify or delete it.
        """
        return pulumi.get(self, "level")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the lock.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def notes(self) -> pulumi.Output[Optional[str]]:
        """
        Notes about the lock. Maximum of 512 characters.
        """
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter
    def owners(self) -> pulumi.Output[Optional[Sequence['outputs.ManagementLockOwnerResponse']]]:
        """
        The owners of the lock.
        """
        return pulumi.get(self, "owners")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The resource type of the lock - Microsoft.Authorization/locks.
        """
        return pulumi.get(self, "type")

