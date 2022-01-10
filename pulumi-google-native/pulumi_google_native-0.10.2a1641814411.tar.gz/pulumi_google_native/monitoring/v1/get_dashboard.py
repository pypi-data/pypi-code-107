# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetDashboardResult',
    'AwaitableGetDashboardResult',
    'get_dashboard',
    'get_dashboard_output',
]

@pulumi.output_type
class GetDashboardResult:
    def __init__(__self__, column_layout=None, display_name=None, etag=None, grid_layout=None, labels=None, mosaic_layout=None, name=None, row_layout=None):
        if column_layout and not isinstance(column_layout, dict):
            raise TypeError("Expected argument 'column_layout' to be a dict")
        pulumi.set(__self__, "column_layout", column_layout)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if grid_layout and not isinstance(grid_layout, dict):
            raise TypeError("Expected argument 'grid_layout' to be a dict")
        pulumi.set(__self__, "grid_layout", grid_layout)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if mosaic_layout and not isinstance(mosaic_layout, dict):
            raise TypeError("Expected argument 'mosaic_layout' to be a dict")
        pulumi.set(__self__, "mosaic_layout", mosaic_layout)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if row_layout and not isinstance(row_layout, dict):
            raise TypeError("Expected argument 'row_layout' to be a dict")
        pulumi.set(__self__, "row_layout", row_layout)

    @property
    @pulumi.getter(name="columnLayout")
    def column_layout(self) -> 'outputs.ColumnLayoutResponse':
        """
        The content is divided into equally spaced columns and the widgets are arranged vertically.
        """
        return pulumi.get(self, "column_layout")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The mutable, human-readable name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        etag is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. An etag is returned in the response to GetDashboard, and users are expected to put that etag in the request to UpdateDashboard to ensure that their change will be applied to the same version of the Dashboard configuration. The field should not be passed during dashboard creation.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="gridLayout")
    def grid_layout(self) -> 'outputs.GridLayoutResponse':
        """
        Content is arranged with a basic layout that re-flows a simple list of informational elements like widgets or tiles.
        """
        return pulumi.get(self, "grid_layout")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Labels applied to the dashboard
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="mosaicLayout")
    def mosaic_layout(self) -> 'outputs.MosaicLayoutResponse':
        """
        The content is arranged as a grid of tiles, with each content widget occupying one or more grid blocks.
        """
        return pulumi.get(self, "mosaic_layout")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Immutable. The resource name of the dashboard.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="rowLayout")
    def row_layout(self) -> 'outputs.RowLayoutResponse':
        """
        The content is divided into equally spaced rows and the widgets are arranged horizontally.
        """
        return pulumi.get(self, "row_layout")


class AwaitableGetDashboardResult(GetDashboardResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDashboardResult(
            column_layout=self.column_layout,
            display_name=self.display_name,
            etag=self.etag,
            grid_layout=self.grid_layout,
            labels=self.labels,
            mosaic_layout=self.mosaic_layout,
            name=self.name,
            row_layout=self.row_layout)


def get_dashboard(dashboard_id: Optional[str] = None,
                  project: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDashboardResult:
    """
    Fetches a specific dashboard.This method requires the monitoring.dashboards.get permission on the specified dashboard. For more information, see Cloud Identity and Access Management (https://cloud.google.com/iam).
    """
    __args__ = dict()
    __args__['dashboardId'] = dashboard_id
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:monitoring/v1:getDashboard', __args__, opts=opts, typ=GetDashboardResult).value

    return AwaitableGetDashboardResult(
        column_layout=__ret__.column_layout,
        display_name=__ret__.display_name,
        etag=__ret__.etag,
        grid_layout=__ret__.grid_layout,
        labels=__ret__.labels,
        mosaic_layout=__ret__.mosaic_layout,
        name=__ret__.name,
        row_layout=__ret__.row_layout)


@_utilities.lift_output_func(get_dashboard)
def get_dashboard_output(dashboard_id: Optional[pulumi.Input[str]] = None,
                         project: Optional[pulumi.Input[Optional[str]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDashboardResult]:
    """
    Fetches a specific dashboard.This method requires the monitoring.dashboards.get permission on the specified dashboard. For more information, see Cloud Identity and Access Management (https://cloud.google.com/iam).
    """
    ...
