# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['SshPublicKeyArgs', 'SshPublicKey']

@pulumi.input_type
class SshPublicKeyArgs:
    def __init__(__self__, *,
                 user_id: pulumi.Input[str],
                 expiration_time_usec: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SshPublicKey resource.
        :param pulumi.Input[str] expiration_time_usec: An expiration time in microseconds since epoch.
        :param pulumi.Input[str] key: Public key text in SSH format, defined by RFC4253 section 6.6.
        """
        pulumi.set(__self__, "user_id", user_id)
        if expiration_time_usec is not None:
            pulumi.set(__self__, "expiration_time_usec", expiration_time_usec)
        if key is not None:
            pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_id", value)

    @property
    @pulumi.getter(name="expirationTimeUsec")
    def expiration_time_usec(self) -> Optional[pulumi.Input[str]]:
        """
        An expiration time in microseconds since epoch.
        """
        return pulumi.get(self, "expiration_time_usec")

    @expiration_time_usec.setter
    def expiration_time_usec(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiration_time_usec", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        Public key text in SSH format, defined by RFC4253 section 6.6.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)


class SshPublicKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 expiration_time_usec: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create an SSH public key
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] expiration_time_usec: An expiration time in microseconds since epoch.
        :param pulumi.Input[str] key: Public key text in SSH format, defined by RFC4253 section 6.6.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SshPublicKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create an SSH public key
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param SshPublicKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SshPublicKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 expiration_time_usec: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = SshPublicKeyArgs.__new__(SshPublicKeyArgs)

            __props__.__dict__["expiration_time_usec"] = expiration_time_usec
            __props__.__dict__["key"] = key
            if user_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_id'")
            __props__.__dict__["user_id"] = user_id
            __props__.__dict__["fingerprint"] = None
            __props__.__dict__["name"] = None
        super(SshPublicKey, __self__).__init__(
            'google-native:oslogin/v1:SshPublicKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SshPublicKey':
        """
        Get an existing SshPublicKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SshPublicKeyArgs.__new__(SshPublicKeyArgs)

        __props__.__dict__["expiration_time_usec"] = None
        __props__.__dict__["fingerprint"] = None
        __props__.__dict__["key"] = None
        __props__.__dict__["name"] = None
        return SshPublicKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="expirationTimeUsec")
    def expiration_time_usec(self) -> pulumi.Output[str]:
        """
        An expiration time in microseconds since epoch.
        """
        return pulumi.get(self, "expiration_time_usec")

    @property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[str]:
        """
        The SHA-256 fingerprint of the SSH public key.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        Public key text in SSH format, defined by RFC4253 section 6.6.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The canonical resource name.
        """
        return pulumi.get(self, "name")

