# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetExposureControlFeatureValueByFactoryResult',
    'AwaitableGetExposureControlFeatureValueByFactoryResult',
    'get_exposure_control_feature_value_by_factory',
    'get_exposure_control_feature_value_by_factory_output',
]

@pulumi.output_type
class GetExposureControlFeatureValueByFactoryResult:
    """
    The exposure control response.
    """
    def __init__(__self__, feature_name=None, value=None):
        if feature_name and not isinstance(feature_name, str):
            raise TypeError("Expected argument 'feature_name' to be a str")
        pulumi.set(__self__, "feature_name", feature_name)
        if value and not isinstance(value, str):
            raise TypeError("Expected argument 'value' to be a str")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="featureName")
    def feature_name(self) -> str:
        """
        The feature name.
        """
        return pulumi.get(self, "feature_name")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The feature value.
        """
        return pulumi.get(self, "value")


class AwaitableGetExposureControlFeatureValueByFactoryResult(GetExposureControlFeatureValueByFactoryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExposureControlFeatureValueByFactoryResult(
            feature_name=self.feature_name,
            value=self.value)


def get_exposure_control_feature_value_by_factory(factory_name: Optional[str] = None,
                                                  feature_name: Optional[str] = None,
                                                  feature_type: Optional[str] = None,
                                                  resource_group_name: Optional[str] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExposureControlFeatureValueByFactoryResult:
    """
    The exposure control response.


    :param str factory_name: The factory name.
    :param str feature_name: The feature name.
    :param str feature_type: The feature type.
    :param str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['factoryName'] = factory_name
    __args__['featureName'] = feature_name
    __args__['featureType'] = feature_type
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:datafactory/v20180601:getExposureControlFeatureValueByFactory', __args__, opts=opts, typ=GetExposureControlFeatureValueByFactoryResult).value

    return AwaitableGetExposureControlFeatureValueByFactoryResult(
        feature_name=__ret__.feature_name,
        value=__ret__.value)


@_utilities.lift_output_func(get_exposure_control_feature_value_by_factory)
def get_exposure_control_feature_value_by_factory_output(factory_name: Optional[pulumi.Input[str]] = None,
                                                         feature_name: Optional[pulumi.Input[Optional[str]]] = None,
                                                         feature_type: Optional[pulumi.Input[Optional[str]]] = None,
                                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExposureControlFeatureValueByFactoryResult]:
    """
    The exposure control response.


    :param str factory_name: The factory name.
    :param str feature_name: The feature name.
    :param str feature_type: The feature type.
    :param str resource_group_name: The resource group name.
    """
    ...
