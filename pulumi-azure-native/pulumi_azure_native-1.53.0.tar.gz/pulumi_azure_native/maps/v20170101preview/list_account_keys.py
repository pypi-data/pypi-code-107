# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'ListAccountKeysResult',
    'AwaitableListAccountKeysResult',
    'list_account_keys',
    'list_account_keys_output',
]

@pulumi.output_type
class ListAccountKeysResult:
    """
    The set of keys which can be used to access the Maps REST APIs. Two keys are provided for key rotation without interruption.
    """
    def __init__(__self__, id=None, primary_key=None, secondary_key=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if primary_key and not isinstance(primary_key, str):
            raise TypeError("Expected argument 'primary_key' to be a str")
        pulumi.set(__self__, "primary_key", primary_key)
        if secondary_key and not isinstance(secondary_key, str):
            raise TypeError("Expected argument 'secondary_key' to be a str")
        pulumi.set(__self__, "secondary_key", secondary_key)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The full Azure resource identifier of the Maps Account.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> str:
        """
        The primary key for accessing the Maps REST APIs.
        """
        return pulumi.get(self, "primary_key")

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> str:
        """
        The secondary key for accessing the Maps REST APIs.
        """
        return pulumi.get(self, "secondary_key")


class AwaitableListAccountKeysResult(ListAccountKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListAccountKeysResult(
            id=self.id,
            primary_key=self.primary_key,
            secondary_key=self.secondary_key)


def list_account_keys(account_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListAccountKeysResult:
    """
    The set of keys which can be used to access the Maps REST APIs. Two keys are provided for key rotation without interruption.


    :param str account_name: The name of the Maps Account.
    :param str resource_group_name: The name of the Azure Resource Group.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:maps/v20170101preview:listAccountKeys', __args__, opts=opts, typ=ListAccountKeysResult).value

    return AwaitableListAccountKeysResult(
        id=__ret__.id,
        primary_key=__ret__.primary_key,
        secondary_key=__ret__.secondary_key)


@_utilities.lift_output_func(list_account_keys)
def list_account_keys_output(account_name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListAccountKeysResult]:
    """
    The set of keys which can be used to access the Maps REST APIs. Two keys are provided for key rotation without interruption.


    :param str account_name: The name of the Maps Account.
    :param str resource_group_name: The name of the Azure Resource Group.
    """
    ...
