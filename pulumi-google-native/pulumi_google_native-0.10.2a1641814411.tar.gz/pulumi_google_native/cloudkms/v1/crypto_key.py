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

__all__ = ['CryptoKeyArgs', 'CryptoKey']

@pulumi.input_type
class CryptoKeyArgs:
    def __init__(__self__, *,
                 crypto_key_id: pulumi.Input[str],
                 key_ring_id: pulumi.Input[str],
                 destroy_scheduled_duration: Optional[pulumi.Input[str]] = None,
                 import_only: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 next_rotation_time: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 purpose: Optional[pulumi.Input['CryptoKeyPurpose']] = None,
                 rotation_period: Optional[pulumi.Input[str]] = None,
                 skip_initial_version_creation: Optional[pulumi.Input[str]] = None,
                 version_template: Optional[pulumi.Input['CryptoKeyVersionTemplateArgs']] = None):
        """
        The set of arguments for constructing a CryptoKey resource.
        :param pulumi.Input[str] destroy_scheduled_duration: Immutable. The period of time that versions of this key spend in the DESTROY_SCHEDULED state before transitioning to DESTROYED. If not specified at creation time, the default duration is 24 hours.
        :param pulumi.Input[bool] import_only: Immutable. Whether this key may contain imported versions only.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels with user-defined metadata. For more information, see [Labeling Keys](https://cloud.google.com/kms/docs/labeling-keys).
        :param pulumi.Input[str] next_rotation_time: At next_rotation_time, the Key Management Service will automatically: 1. Create a new version of this CryptoKey. 2. Mark the new version as primary. Key rotations performed manually via CreateCryptoKeyVersion and UpdateCryptoKeyPrimaryVersion do not affect next_rotation_time. Keys with purpose ENCRYPT_DECRYPT support automatic rotation. For other keys, this field must be omitted.
        :param pulumi.Input['CryptoKeyPurpose'] purpose: Immutable. The immutable purpose of this CryptoKey.
        :param pulumi.Input[str] rotation_period: next_rotation_time will be advanced by this period when the service automatically rotates a key. Must be at least 24 hours and at most 876,000 hours. If rotation_period is set, next_rotation_time must also be set. Keys with purpose ENCRYPT_DECRYPT support automatic rotation. For other keys, this field must be omitted.
        :param pulumi.Input['CryptoKeyVersionTemplateArgs'] version_template: A template describing settings for new CryptoKeyVersion instances. The properties of new CryptoKeyVersion instances created by either CreateCryptoKeyVersion or auto-rotation are controlled by this template.
        """
        pulumi.set(__self__, "crypto_key_id", crypto_key_id)
        pulumi.set(__self__, "key_ring_id", key_ring_id)
        if destroy_scheduled_duration is not None:
            pulumi.set(__self__, "destroy_scheduled_duration", destroy_scheduled_duration)
        if import_only is not None:
            pulumi.set(__self__, "import_only", import_only)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if next_rotation_time is not None:
            pulumi.set(__self__, "next_rotation_time", next_rotation_time)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if purpose is not None:
            pulumi.set(__self__, "purpose", purpose)
        if rotation_period is not None:
            pulumi.set(__self__, "rotation_period", rotation_period)
        if skip_initial_version_creation is not None:
            pulumi.set(__self__, "skip_initial_version_creation", skip_initial_version_creation)
        if version_template is not None:
            pulumi.set(__self__, "version_template", version_template)

    @property
    @pulumi.getter(name="cryptoKeyId")
    def crypto_key_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "crypto_key_id")

    @crypto_key_id.setter
    def crypto_key_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "crypto_key_id", value)

    @property
    @pulumi.getter(name="keyRingId")
    def key_ring_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key_ring_id")

    @key_ring_id.setter
    def key_ring_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_ring_id", value)

    @property
    @pulumi.getter(name="destroyScheduledDuration")
    def destroy_scheduled_duration(self) -> Optional[pulumi.Input[str]]:
        """
        Immutable. The period of time that versions of this key spend in the DESTROY_SCHEDULED state before transitioning to DESTROYED. If not specified at creation time, the default duration is 24 hours.
        """
        return pulumi.get(self, "destroy_scheduled_duration")

    @destroy_scheduled_duration.setter
    def destroy_scheduled_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destroy_scheduled_duration", value)

    @property
    @pulumi.getter(name="importOnly")
    def import_only(self) -> Optional[pulumi.Input[bool]]:
        """
        Immutable. Whether this key may contain imported versions only.
        """
        return pulumi.get(self, "import_only")

    @import_only.setter
    def import_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "import_only", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Labels with user-defined metadata. For more information, see [Labeling Keys](https://cloud.google.com/kms/docs/labeling-keys).
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="nextRotationTime")
    def next_rotation_time(self) -> Optional[pulumi.Input[str]]:
        """
        At next_rotation_time, the Key Management Service will automatically: 1. Create a new version of this CryptoKey. 2. Mark the new version as primary. Key rotations performed manually via CreateCryptoKeyVersion and UpdateCryptoKeyPrimaryVersion do not affect next_rotation_time. Keys with purpose ENCRYPT_DECRYPT support automatic rotation. For other keys, this field must be omitted.
        """
        return pulumi.get(self, "next_rotation_time")

    @next_rotation_time.setter
    def next_rotation_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "next_rotation_time", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def purpose(self) -> Optional[pulumi.Input['CryptoKeyPurpose']]:
        """
        Immutable. The immutable purpose of this CryptoKey.
        """
        return pulumi.get(self, "purpose")

    @purpose.setter
    def purpose(self, value: Optional[pulumi.Input['CryptoKeyPurpose']]):
        pulumi.set(self, "purpose", value)

    @property
    @pulumi.getter(name="rotationPeriod")
    def rotation_period(self) -> Optional[pulumi.Input[str]]:
        """
        next_rotation_time will be advanced by this period when the service automatically rotates a key. Must be at least 24 hours and at most 876,000 hours. If rotation_period is set, next_rotation_time must also be set. Keys with purpose ENCRYPT_DECRYPT support automatic rotation. For other keys, this field must be omitted.
        """
        return pulumi.get(self, "rotation_period")

    @rotation_period.setter
    def rotation_period(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rotation_period", value)

    @property
    @pulumi.getter(name="skipInitialVersionCreation")
    def skip_initial_version_creation(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "skip_initial_version_creation")

    @skip_initial_version_creation.setter
    def skip_initial_version_creation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "skip_initial_version_creation", value)

    @property
    @pulumi.getter(name="versionTemplate")
    def version_template(self) -> Optional[pulumi.Input['CryptoKeyVersionTemplateArgs']]:
        """
        A template describing settings for new CryptoKeyVersion instances. The properties of new CryptoKeyVersion instances created by either CreateCryptoKeyVersion or auto-rotation are controlled by this template.
        """
        return pulumi.get(self, "version_template")

    @version_template.setter
    def version_template(self, value: Optional[pulumi.Input['CryptoKeyVersionTemplateArgs']]):
        pulumi.set(self, "version_template", value)


class CryptoKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 crypto_key_id: Optional[pulumi.Input[str]] = None,
                 destroy_scheduled_duration: Optional[pulumi.Input[str]] = None,
                 import_only: Optional[pulumi.Input[bool]] = None,
                 key_ring_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 next_rotation_time: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 purpose: Optional[pulumi.Input['CryptoKeyPurpose']] = None,
                 rotation_period: Optional[pulumi.Input[str]] = None,
                 skip_initial_version_creation: Optional[pulumi.Input[str]] = None,
                 version_template: Optional[pulumi.Input[pulumi.InputType['CryptoKeyVersionTemplateArgs']]] = None,
                 __props__=None):
        """
        Create a new CryptoKey within a KeyRing. CryptoKey.purpose and CryptoKey.version_template.algorithm are required.
        Auto-naming is currently not supported for this resource.
        Note - this resource's API doesn't support deletion. When deleted, the resource will persist
        on Google Cloud even though it will be deleted from Pulumi state.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] destroy_scheduled_duration: Immutable. The period of time that versions of this key spend in the DESTROY_SCHEDULED state before transitioning to DESTROYED. If not specified at creation time, the default duration is 24 hours.
        :param pulumi.Input[bool] import_only: Immutable. Whether this key may contain imported versions only.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Labels with user-defined metadata. For more information, see [Labeling Keys](https://cloud.google.com/kms/docs/labeling-keys).
        :param pulumi.Input[str] next_rotation_time: At next_rotation_time, the Key Management Service will automatically: 1. Create a new version of this CryptoKey. 2. Mark the new version as primary. Key rotations performed manually via CreateCryptoKeyVersion and UpdateCryptoKeyPrimaryVersion do not affect next_rotation_time. Keys with purpose ENCRYPT_DECRYPT support automatic rotation. For other keys, this field must be omitted.
        :param pulumi.Input['CryptoKeyPurpose'] purpose: Immutable. The immutable purpose of this CryptoKey.
        :param pulumi.Input[str] rotation_period: next_rotation_time will be advanced by this period when the service automatically rotates a key. Must be at least 24 hours and at most 876,000 hours. If rotation_period is set, next_rotation_time must also be set. Keys with purpose ENCRYPT_DECRYPT support automatic rotation. For other keys, this field must be omitted.
        :param pulumi.Input[pulumi.InputType['CryptoKeyVersionTemplateArgs']] version_template: A template describing settings for new CryptoKeyVersion instances. The properties of new CryptoKeyVersion instances created by either CreateCryptoKeyVersion or auto-rotation are controlled by this template.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CryptoKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a new CryptoKey within a KeyRing. CryptoKey.purpose and CryptoKey.version_template.algorithm are required.
        Auto-naming is currently not supported for this resource.
        Note - this resource's API doesn't support deletion. When deleted, the resource will persist
        on Google Cloud even though it will be deleted from Pulumi state.

        :param str resource_name: The name of the resource.
        :param CryptoKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CryptoKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 crypto_key_id: Optional[pulumi.Input[str]] = None,
                 destroy_scheduled_duration: Optional[pulumi.Input[str]] = None,
                 import_only: Optional[pulumi.Input[bool]] = None,
                 key_ring_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 next_rotation_time: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 purpose: Optional[pulumi.Input['CryptoKeyPurpose']] = None,
                 rotation_period: Optional[pulumi.Input[str]] = None,
                 skip_initial_version_creation: Optional[pulumi.Input[str]] = None,
                 version_template: Optional[pulumi.Input[pulumi.InputType['CryptoKeyVersionTemplateArgs']]] = None,
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
            __props__ = CryptoKeyArgs.__new__(CryptoKeyArgs)

            if crypto_key_id is None and not opts.urn:
                raise TypeError("Missing required property 'crypto_key_id'")
            __props__.__dict__["crypto_key_id"] = crypto_key_id
            __props__.__dict__["destroy_scheduled_duration"] = destroy_scheduled_duration
            __props__.__dict__["import_only"] = import_only
            if key_ring_id is None and not opts.urn:
                raise TypeError("Missing required property 'key_ring_id'")
            __props__.__dict__["key_ring_id"] = key_ring_id
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            __props__.__dict__["next_rotation_time"] = next_rotation_time
            __props__.__dict__["project"] = project
            __props__.__dict__["purpose"] = purpose
            __props__.__dict__["rotation_period"] = rotation_period
            __props__.__dict__["skip_initial_version_creation"] = skip_initial_version_creation
            __props__.__dict__["version_template"] = version_template
            __props__.__dict__["create_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["primary"] = None
        super(CryptoKey, __self__).__init__(
            'google-native:cloudkms/v1:CryptoKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CryptoKey':
        """
        Get an existing CryptoKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CryptoKeyArgs.__new__(CryptoKeyArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["destroy_scheduled_duration"] = None
        __props__.__dict__["import_only"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["next_rotation_time"] = None
        __props__.__dict__["primary"] = None
        __props__.__dict__["purpose"] = None
        __props__.__dict__["rotation_period"] = None
        __props__.__dict__["version_template"] = None
        return CryptoKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time at which this CryptoKey was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="destroyScheduledDuration")
    def destroy_scheduled_duration(self) -> pulumi.Output[str]:
        """
        Immutable. The period of time that versions of this key spend in the DESTROY_SCHEDULED state before transitioning to DESTROYED. If not specified at creation time, the default duration is 24 hours.
        """
        return pulumi.get(self, "destroy_scheduled_duration")

    @property
    @pulumi.getter(name="importOnly")
    def import_only(self) -> pulumi.Output[bool]:
        """
        Immutable. Whether this key may contain imported versions only.
        """
        return pulumi.get(self, "import_only")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Labels with user-defined metadata. For more information, see [Labeling Keys](https://cloud.google.com/kms/docs/labeling-keys).
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name for this CryptoKey in the format `projects/*/locations/*/keyRings/*/cryptoKeys/*`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nextRotationTime")
    def next_rotation_time(self) -> pulumi.Output[str]:
        """
        At next_rotation_time, the Key Management Service will automatically: 1. Create a new version of this CryptoKey. 2. Mark the new version as primary. Key rotations performed manually via CreateCryptoKeyVersion and UpdateCryptoKeyPrimaryVersion do not affect next_rotation_time. Keys with purpose ENCRYPT_DECRYPT support automatic rotation. For other keys, this field must be omitted.
        """
        return pulumi.get(self, "next_rotation_time")

    @property
    @pulumi.getter
    def primary(self) -> pulumi.Output['outputs.CryptoKeyVersionResponse']:
        """
        A copy of the "primary" CryptoKeyVersion that will be used by Encrypt when this CryptoKey is given in EncryptRequest.name. The CryptoKey's primary version can be updated via UpdateCryptoKeyPrimaryVersion. Keys with purpose ENCRYPT_DECRYPT may have a primary. For other keys, this field will be omitted.
        """
        return pulumi.get(self, "primary")

    @property
    @pulumi.getter
    def purpose(self) -> pulumi.Output[str]:
        """
        Immutable. The immutable purpose of this CryptoKey.
        """
        return pulumi.get(self, "purpose")

    @property
    @pulumi.getter(name="rotationPeriod")
    def rotation_period(self) -> pulumi.Output[str]:
        """
        next_rotation_time will be advanced by this period when the service automatically rotates a key. Must be at least 24 hours and at most 876,000 hours. If rotation_period is set, next_rotation_time must also be set. Keys with purpose ENCRYPT_DECRYPT support automatic rotation. For other keys, this field must be omitted.
        """
        return pulumi.get(self, "rotation_period")

    @property
    @pulumi.getter(name="versionTemplate")
    def version_template(self) -> pulumi.Output['outputs.CryptoKeyVersionTemplateResponse']:
        """
        A template describing settings for new CryptoKeyVersion instances. The properties of new CryptoKeyVersion instances created by either CreateCryptoKeyVersion or auto-rotation are controlled by this template.
        """
        return pulumi.get(self, "version_template")

