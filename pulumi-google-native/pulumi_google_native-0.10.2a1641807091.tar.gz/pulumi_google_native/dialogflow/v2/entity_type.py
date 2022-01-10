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

__all__ = ['EntityTypeArgs', 'EntityType']

@pulumi.input_type
class EntityTypeArgs:
    def __init__(__self__, *,
                 display_name: pulumi.Input[str],
                 kind: pulumi.Input['EntityTypeKind'],
                 auto_expansion_mode: Optional[pulumi.Input['EntityTypeAutoExpansionMode']] = None,
                 enable_fuzzy_extraction: Optional[pulumi.Input[bool]] = None,
                 entities: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowV2EntityTypeEntityArgs']]]] = None,
                 language_code: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a EntityType resource.
        :param pulumi.Input[str] display_name: The name of the entity type.
        :param pulumi.Input['EntityTypeKind'] kind: Indicates the kind of entity type.
        :param pulumi.Input['EntityTypeAutoExpansionMode'] auto_expansion_mode: Optional. Indicates whether the entity type can be automatically expanded.
        :param pulumi.Input[bool] enable_fuzzy_extraction: Optional. Enables fuzzy entity extraction during classification.
        :param pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowV2EntityTypeEntityArgs']]] entities: Optional. The collection of entity entries associated with the entity type.
        :param pulumi.Input[str] name: The unique identifier of the entity type. Required for EntityTypes.UpdateEntityType and EntityTypes.BatchUpdateEntityTypes methods. Format: `projects//agent/entityTypes/`.
        """
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "kind", kind)
        if auto_expansion_mode is not None:
            pulumi.set(__self__, "auto_expansion_mode", auto_expansion_mode)
        if enable_fuzzy_extraction is not None:
            pulumi.set(__self__, "enable_fuzzy_extraction", enable_fuzzy_extraction)
        if entities is not None:
            pulumi.set(__self__, "entities", entities)
        if language_code is not None:
            pulumi.set(__self__, "language_code", language_code)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The name of the entity type.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input['EntityTypeKind']:
        """
        Indicates the kind of entity type.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input['EntityTypeKind']):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="autoExpansionMode")
    def auto_expansion_mode(self) -> Optional[pulumi.Input['EntityTypeAutoExpansionMode']]:
        """
        Optional. Indicates whether the entity type can be automatically expanded.
        """
        return pulumi.get(self, "auto_expansion_mode")

    @auto_expansion_mode.setter
    def auto_expansion_mode(self, value: Optional[pulumi.Input['EntityTypeAutoExpansionMode']]):
        pulumi.set(self, "auto_expansion_mode", value)

    @property
    @pulumi.getter(name="enableFuzzyExtraction")
    def enable_fuzzy_extraction(self) -> Optional[pulumi.Input[bool]]:
        """
        Optional. Enables fuzzy entity extraction during classification.
        """
        return pulumi.get(self, "enable_fuzzy_extraction")

    @enable_fuzzy_extraction.setter
    def enable_fuzzy_extraction(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_fuzzy_extraction", value)

    @property
    @pulumi.getter
    def entities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowV2EntityTypeEntityArgs']]]]:
        """
        Optional. The collection of entity entries associated with the entity type.
        """
        return pulumi.get(self, "entities")

    @entities.setter
    def entities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowV2EntityTypeEntityArgs']]]]):
        pulumi.set(self, "entities", value)

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "language_code")

    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "language_code", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identifier of the entity type. Required for EntityTypes.UpdateEntityType and EntityTypes.BatchUpdateEntityTypes methods. Format: `projects//agent/entityTypes/`.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


class EntityType(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_expansion_mode: Optional[pulumi.Input['EntityTypeAutoExpansionMode']] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enable_fuzzy_extraction: Optional[pulumi.Input[bool]] = None,
                 entities: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2EntityTypeEntityArgs']]]]] = None,
                 kind: Optional[pulumi.Input['EntityTypeKind']] = None,
                 language_code: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates an entity type in the specified agent. Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input['EntityTypeAutoExpansionMode'] auto_expansion_mode: Optional. Indicates whether the entity type can be automatically expanded.
        :param pulumi.Input[str] display_name: The name of the entity type.
        :param pulumi.Input[bool] enable_fuzzy_extraction: Optional. Enables fuzzy entity extraction during classification.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2EntityTypeEntityArgs']]]] entities: Optional. The collection of entity entries associated with the entity type.
        :param pulumi.Input['EntityTypeKind'] kind: Indicates the kind of entity type.
        :param pulumi.Input[str] name: The unique identifier of the entity type. Required for EntityTypes.UpdateEntityType and EntityTypes.BatchUpdateEntityTypes methods. Format: `projects//agent/entityTypes/`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EntityTypeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an entity type in the specified agent. Note: You should always train an agent prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/es/docs/training).
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param EntityTypeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EntityTypeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_expansion_mode: Optional[pulumi.Input['EntityTypeAutoExpansionMode']] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enable_fuzzy_extraction: Optional[pulumi.Input[bool]] = None,
                 entities: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowV2EntityTypeEntityArgs']]]]] = None,
                 kind: Optional[pulumi.Input['EntityTypeKind']] = None,
                 language_code: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
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
            __props__ = EntityTypeArgs.__new__(EntityTypeArgs)

            __props__.__dict__["auto_expansion_mode"] = auto_expansion_mode
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["enable_fuzzy_extraction"] = enable_fuzzy_extraction
            __props__.__dict__["entities"] = entities
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = kind
            __props__.__dict__["language_code"] = language_code
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
        super(EntityType, __self__).__init__(
            'google-native:dialogflow/v2:EntityType',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'EntityType':
        """
        Get an existing EntityType resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EntityTypeArgs.__new__(EntityTypeArgs)

        __props__.__dict__["auto_expansion_mode"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["enable_fuzzy_extraction"] = None
        __props__.__dict__["entities"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        return EntityType(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="autoExpansionMode")
    def auto_expansion_mode(self) -> pulumi.Output[str]:
        """
        Optional. Indicates whether the entity type can be automatically expanded.
        """
        return pulumi.get(self, "auto_expansion_mode")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The name of the entity type.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="enableFuzzyExtraction")
    def enable_fuzzy_extraction(self) -> pulumi.Output[bool]:
        """
        Optional. Enables fuzzy entity extraction during classification.
        """
        return pulumi.get(self, "enable_fuzzy_extraction")

    @property
    @pulumi.getter
    def entities(self) -> pulumi.Output[Sequence['outputs.GoogleCloudDialogflowV2EntityTypeEntityResponse']]:
        """
        Optional. The collection of entity entries associated with the entity type.
        """
        return pulumi.get(self, "entities")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Indicates the kind of entity type.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The unique identifier of the entity type. Required for EntityTypes.UpdateEntityType and EntityTypes.BatchUpdateEntityTypes methods. Format: `projects//agent/entityTypes/`.
        """
        return pulumi.get(self, "name")

