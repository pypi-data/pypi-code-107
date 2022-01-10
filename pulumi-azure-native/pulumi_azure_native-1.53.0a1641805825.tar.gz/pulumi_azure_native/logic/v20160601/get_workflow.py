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
    'GetWorkflowResult',
    'AwaitableGetWorkflowResult',
    'get_workflow',
    'get_workflow_output',
]

@pulumi.output_type
class GetWorkflowResult:
    """
    The workflow type.
    """
    def __init__(__self__, access_endpoint=None, changed_time=None, created_time=None, definition=None, id=None, integration_account=None, location=None, name=None, parameters=None, provisioning_state=None, sku=None, state=None, tags=None, type=None, version=None):
        if access_endpoint and not isinstance(access_endpoint, str):
            raise TypeError("Expected argument 'access_endpoint' to be a str")
        pulumi.set(__self__, "access_endpoint", access_endpoint)
        if changed_time and not isinstance(changed_time, str):
            raise TypeError("Expected argument 'changed_time' to be a str")
        pulumi.set(__self__, "changed_time", changed_time)
        if created_time and not isinstance(created_time, str):
            raise TypeError("Expected argument 'created_time' to be a str")
        pulumi.set(__self__, "created_time", created_time)
        if definition and not isinstance(definition, dict):
            raise TypeError("Expected argument 'definition' to be a dict")
        pulumi.set(__self__, "definition", definition)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if integration_account and not isinstance(integration_account, dict):
            raise TypeError("Expected argument 'integration_account' to be a dict")
        pulumi.set(__self__, "integration_account", integration_account)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if parameters and not isinstance(parameters, dict):
            raise TypeError("Expected argument 'parameters' to be a dict")
        pulumi.set(__self__, "parameters", parameters)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="accessEndpoint")
    def access_endpoint(self) -> str:
        """
        Gets the access endpoint.
        """
        return pulumi.get(self, "access_endpoint")

    @property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> str:
        """
        Gets the changed time.
        """
        return pulumi.get(self, "changed_time")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> str:
        """
        Gets the created time.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def definition(self) -> Optional[Any]:
        """
        The definition. See [Schema reference for Workflow Definition Language in Azure Logic Apps](https://aka.ms/logic-apps-workflow-definition-language).
        """
        return pulumi.get(self, "definition")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="integrationAccount")
    def integration_account(self) -> Optional['outputs.ResourceReferenceResponse']:
        """
        The integration account.
        """
        return pulumi.get(self, "integration_account")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Gets the resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, 'outputs.WorkflowParameterResponse']]:
        """
        The parameters.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Gets the provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        The sku.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The state.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Gets the resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Gets the version.
        """
        return pulumi.get(self, "version")


class AwaitableGetWorkflowResult(GetWorkflowResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWorkflowResult(
            access_endpoint=self.access_endpoint,
            changed_time=self.changed_time,
            created_time=self.created_time,
            definition=self.definition,
            id=self.id,
            integration_account=self.integration_account,
            location=self.location,
            name=self.name,
            parameters=self.parameters,
            provisioning_state=self.provisioning_state,
            sku=self.sku,
            state=self.state,
            tags=self.tags,
            type=self.type,
            version=self.version)


def get_workflow(resource_group_name: Optional[str] = None,
                 workflow_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWorkflowResult:
    """
    The workflow type.


    :param str resource_group_name: The resource group name.
    :param str workflow_name: The workflow name.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['workflowName'] = workflow_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azure-native:logic/v20160601:getWorkflow', __args__, opts=opts, typ=GetWorkflowResult).value

    return AwaitableGetWorkflowResult(
        access_endpoint=__ret__.access_endpoint,
        changed_time=__ret__.changed_time,
        created_time=__ret__.created_time,
        definition=__ret__.definition,
        id=__ret__.id,
        integration_account=__ret__.integration_account,
        location=__ret__.location,
        name=__ret__.name,
        parameters=__ret__.parameters,
        provisioning_state=__ret__.provisioning_state,
        sku=__ret__.sku,
        state=__ret__.state,
        tags=__ret__.tags,
        type=__ret__.type,
        version=__ret__.version)


@_utilities.lift_output_func(get_workflow)
def get_workflow_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                        workflow_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWorkflowResult]:
    """
    The workflow type.


    :param str resource_group_name: The resource group name.
    :param str workflow_name: The workflow name.
    """
    ...
