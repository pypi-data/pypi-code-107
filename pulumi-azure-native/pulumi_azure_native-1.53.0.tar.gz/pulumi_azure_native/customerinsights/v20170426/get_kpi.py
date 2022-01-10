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
    'GetKpiResult',
    'AwaitableGetKpiResult',
    'get_kpi',
    'get_kpi_output',
]

@pulumi.output_type
class GetKpiResult:
    """
    The KPI resource format.
    """
    def __init__(__self__, aliases=None, calculation_window=None, calculation_window_field_name=None, description=None, display_name=None, entity_type=None, entity_type_name=None, expression=None, extracts=None, filter=None, function=None, group_by=None, group_by_metadata=None, id=None, kpi_name=None, name=None, participant_profiles_metadata=None, provisioning_state=None, tenant_id=None, thres_holds=None, type=None, unit=None):
        if aliases and not isinstance(aliases, list):
            raise TypeError("Expected argument 'aliases' to be a list")
        pulumi.set(__self__, "aliases", aliases)
        if calculation_window and not isinstance(calculation_window, str):
            raise TypeError("Expected argument 'calculation_window' to be a str")
        pulumi.set(__self__, "calculation_window", calculation_window)
        if calculation_window_field_name and not isinstance(calculation_window_field_name, str):
            raise TypeError("Expected argument 'calculation_window_field_name' to be a str")
        pulumi.set(__self__, "calculation_window_field_name", calculation_window_field_name)
        if description and not isinstance(description, dict):
            raise TypeError("Expected argument 'description' to be a dict")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, dict):
            raise TypeError("Expected argument 'display_name' to be a dict")
        pulumi.set(__self__, "display_name", display_name)
        if entity_type and not isinstance(entity_type, str):
            raise TypeError("Expected argument 'entity_type' to be a str")
        pulumi.set(__self__, "entity_type", entity_type)
        if entity_type_name and not isinstance(entity_type_name, str):
            raise TypeError("Expected argument 'entity_type_name' to be a str")
        pulumi.set(__self__, "entity_type_name", entity_type_name)
        if expression and not isinstance(expression, str):
            raise TypeError("Expected argument 'expression' to be a str")
        pulumi.set(__self__, "expression", expression)
        if extracts and not isinstance(extracts, list):
            raise TypeError("Expected argument 'extracts' to be a list")
        pulumi.set(__self__, "extracts", extracts)
        if filter and not isinstance(filter, str):
            raise TypeError("Expected argument 'filter' to be a str")
        pulumi.set(__self__, "filter", filter)
        if function and not isinstance(function, str):
            raise TypeError("Expected argument 'function' to be a str")
        pulumi.set(__self__, "function", function)
        if group_by and not isinstance(group_by, list):
            raise TypeError("Expected argument 'group_by' to be a list")
        pulumi.set(__self__, "group_by", group_by)
        if group_by_metadata and not isinstance(group_by_metadata, list):
            raise TypeError("Expected argument 'group_by_metadata' to be a list")
        pulumi.set(__self__, "group_by_metadata", group_by_metadata)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kpi_name and not isinstance(kpi_name, str):
            raise TypeError("Expected argument 'kpi_name' to be a str")
        pulumi.set(__self__, "kpi_name", kpi_name)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if participant_profiles_metadata and not isinstance(participant_profiles_metadata, list):
            raise TypeError("Expected argument 'participant_profiles_metadata' to be a list")
        pulumi.set(__self__, "participant_profiles_metadata", participant_profiles_metadata)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if thres_holds and not isinstance(thres_holds, dict):
            raise TypeError("Expected argument 'thres_holds' to be a dict")
        pulumi.set(__self__, "thres_holds", thres_holds)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if unit and not isinstance(unit, str):
            raise TypeError("Expected argument 'unit' to be a str")
        pulumi.set(__self__, "unit", unit)

    @property
    @pulumi.getter
    def aliases(self) -> Optional[Sequence['outputs.KpiAliasResponse']]:
        """
        The aliases.
        """
        return pulumi.get(self, "aliases")

    @property
    @pulumi.getter(name="calculationWindow")
    def calculation_window(self) -> str:
        """
        The calculation window.
        """
        return pulumi.get(self, "calculation_window")

    @property
    @pulumi.getter(name="calculationWindowFieldName")
    def calculation_window_field_name(self) -> Optional[str]:
        """
        Name of calculation window field.
        """
        return pulumi.get(self, "calculation_window_field_name")

    @property
    @pulumi.getter
    def description(self) -> Optional[Mapping[str, str]]:
        """
        Localized description for the KPI.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[Mapping[str, str]]:
        """
        Localized display name for the KPI.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> str:
        """
        The mapping entity type.
        """
        return pulumi.get(self, "entity_type")

    @property
    @pulumi.getter(name="entityTypeName")
    def entity_type_name(self) -> str:
        """
        The mapping entity name.
        """
        return pulumi.get(self, "entity_type_name")

    @property
    @pulumi.getter
    def expression(self) -> str:
        """
        The computation expression for the KPI.
        """
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def extracts(self) -> Optional[Sequence['outputs.KpiExtractResponse']]:
        """
        The KPI extracts.
        """
        return pulumi.get(self, "extracts")

    @property
    @pulumi.getter
    def filter(self) -> Optional[str]:
        """
        The filter expression for the KPI.
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def function(self) -> str:
        """
        The computation function for the KPI.
        """
        return pulumi.get(self, "function")

    @property
    @pulumi.getter(name="groupBy")
    def group_by(self) -> Optional[Sequence[str]]:
        """
        the group by properties for the KPI.
        """
        return pulumi.get(self, "group_by")

    @property
    @pulumi.getter(name="groupByMetadata")
    def group_by_metadata(self) -> Sequence['outputs.KpiGroupByMetadataResponse']:
        """
        The KPI GroupByMetadata.
        """
        return pulumi.get(self, "group_by_metadata")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="kpiName")
    def kpi_name(self) -> str:
        """
        The KPI name.
        """
        return pulumi.get(self, "kpi_name")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="participantProfilesMetadata")
    def participant_profiles_metadata(self) -> Sequence['outputs.KpiParticipantProfilesMetadataResponse']:
        """
        The participant profiles.
        """
        return pulumi.get(self, "participant_profiles_metadata")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The hub name.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="thresHolds")
    def thres_holds(self) -> Optional['outputs.KpiThresholdsResponse']:
        """
        The KPI thresholds.
        """
        return pulumi.get(self, "thres_holds")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def unit(self) -> Optional[str]:
        """
        The unit of measurement for the KPI.
        """
        return pulumi.get(self, "unit")


class AwaitableGetKpiResult(GetKpiResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKpiResult(
            aliases=self.aliases,
            calculation_window=self.calculation_window,
            calculation_window_field_name=self.calculation_window_field_name,
            description=self.description,
            display_name=self.display_name,
            entity_type=self.entity_type,
            entity_type_name=self.entity_type_name,
            expression=self.expression,
            extracts=self.extracts,
            filter=self.filter,
            function=self.function,
            group_by=self.group_by,
            group_by_metadata=self.group_by_metadata,
            id=self.id,
            kpi_name=self.kpi_name,
            name=self.name,
            participant_profiles_metadata=self.participant_profiles_metadata,
            provisioning_state=self.provisioning_state,
            tenant_id=self.tenant_id,
            thres_holds=self.thres_holds,
            type=self.type,
            unit=self.unit)


def get_kpi(hub_name: Optional[str] = None,
            kpi_name: Optional[str] = None,
            resource_group_name: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKpiResult:
    """
    The KPI resource format.


    :param str hub_name: The name of the hub.
    :param str kpi_name: The name of the KPI.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['hubName'] = hub_name
    __args__['kpiName'] = kpi_name
    __args__['resourceGroupName'] = resource_group_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:customerinsights/v20170426:getKpi', __args__, opts=opts, typ=GetKpiResult).value

    return AwaitableGetKpiResult(
        aliases=__ret__.aliases,
        calculation_window=__ret__.calculation_window,
        calculation_window_field_name=__ret__.calculation_window_field_name,
        description=__ret__.description,
        display_name=__ret__.display_name,
        entity_type=__ret__.entity_type,
        entity_type_name=__ret__.entity_type_name,
        expression=__ret__.expression,
        extracts=__ret__.extracts,
        filter=__ret__.filter,
        function=__ret__.function,
        group_by=__ret__.group_by,
        group_by_metadata=__ret__.group_by_metadata,
        id=__ret__.id,
        kpi_name=__ret__.kpi_name,
        name=__ret__.name,
        participant_profiles_metadata=__ret__.participant_profiles_metadata,
        provisioning_state=__ret__.provisioning_state,
        tenant_id=__ret__.tenant_id,
        thres_holds=__ret__.thres_holds,
        type=__ret__.type,
        unit=__ret__.unit)


@_utilities.lift_output_func(get_kpi)
def get_kpi_output(hub_name: Optional[pulumi.Input[str]] = None,
                   kpi_name: Optional[pulumi.Input[str]] = None,
                   resource_group_name: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKpiResult]:
    """
    The KPI resource format.


    :param str hub_name: The name of the hub.
    :param str kpi_name: The name of the KPI.
    :param str resource_group_name: The name of the resource group.
    """
    ...
