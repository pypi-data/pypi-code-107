# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._inputs import *

__all__ = ['PageArgs', 'Page']

@pulumi.input_type
class PageArgs:
    def __init__(__self__, *,
                 agent_id: pulumi.Input[str],
                 display_name: pulumi.Input[str],
                 flow_id: pulumi.Input[str],
                 entry_fulfillment: Optional[pulumi.Input['GoogleCloudDialogflowCxV3beta1FulfillmentArgs']] = None,
                 event_handlers: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowCxV3beta1EventHandlerArgs']]]] = None,
                 form: Optional[pulumi.Input['GoogleCloudDialogflowCxV3beta1FormArgs']] = None,
                 language_code: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 transition_route_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 transition_routes: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowCxV3beta1TransitionRouteArgs']]]] = None):
        """
        The set of arguments for constructing a Page resource.
        :param pulumi.Input[str] display_name: The human-readable name of the page, unique within the agent.
        :param pulumi.Input['GoogleCloudDialogflowCxV3beta1FulfillmentArgs'] entry_fulfillment: The fulfillment to call when the session is entering the page.
        :param pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowCxV3beta1EventHandlerArgs']]] event_handlers: Handlers associated with the page to handle events such as webhook errors, no match or no input.
        :param pulumi.Input['GoogleCloudDialogflowCxV3beta1FormArgs'] form: The form associated with the page, used for collecting parameters relevant to the page.
        :param pulumi.Input[str] name: The unique identifier of the page. Required for the Pages.UpdatePage method. Pages.CreatePage populates the name automatically. Format: `projects//locations//agents//flows//pages/`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] transition_route_groups: Ordered list of `TransitionRouteGroups` associated with the page. Transition route groups must be unique within a page. * If multiple transition routes within a page scope refer to the same intent, then the precedence order is: page's transition route -> page's transition route group -> flow's transition routes. * If multiple transition route groups within a page contain the same intent, then the first group in the ordered list takes precedence. Format:`projects//locations//agents//flows//transitionRouteGroups/`.
        :param pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowCxV3beta1TransitionRouteArgs']]] transition_routes: A list of transitions for the transition rules of this page. They route the conversation to another page in the same flow, or another flow. When we are in a certain page, the TransitionRoutes are evalauted in the following order: * TransitionRoutes defined in the page with intent specified. * TransitionRoutes defined in the transition route groups with intent specified. * TransitionRoutes defined in flow with intent specified. * TransitionRoutes defined in the transition route groups with intent specified. * TransitionRoutes defined in the page with only condition specified. * TransitionRoutes defined in the transition route groups with only condition specified.
        """
        pulumi.set(__self__, "agent_id", agent_id)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "flow_id", flow_id)
        if entry_fulfillment is not None:
            pulumi.set(__self__, "entry_fulfillment", entry_fulfillment)
        if event_handlers is not None:
            pulumi.set(__self__, "event_handlers", event_handlers)
        if form is not None:
            pulumi.set(__self__, "form", form)
        if language_code is not None:
            pulumi.set(__self__, "language_code", language_code)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if transition_route_groups is not None:
            pulumi.set(__self__, "transition_route_groups", transition_route_groups)
        if transition_routes is not None:
            pulumi.set(__self__, "transition_routes", transition_routes)

    @property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "agent_id")

    @agent_id.setter
    def agent_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "agent_id", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The human-readable name of the page, unique within the agent.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="flowId")
    def flow_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "flow_id")

    @flow_id.setter
    def flow_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "flow_id", value)

    @property
    @pulumi.getter(name="entryFulfillment")
    def entry_fulfillment(self) -> Optional[pulumi.Input['GoogleCloudDialogflowCxV3beta1FulfillmentArgs']]:
        """
        The fulfillment to call when the session is entering the page.
        """
        return pulumi.get(self, "entry_fulfillment")

    @entry_fulfillment.setter
    def entry_fulfillment(self, value: Optional[pulumi.Input['GoogleCloudDialogflowCxV3beta1FulfillmentArgs']]):
        pulumi.set(self, "entry_fulfillment", value)

    @property
    @pulumi.getter(name="eventHandlers")
    def event_handlers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowCxV3beta1EventHandlerArgs']]]]:
        """
        Handlers associated with the page to handle events such as webhook errors, no match or no input.
        """
        return pulumi.get(self, "event_handlers")

    @event_handlers.setter
    def event_handlers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowCxV3beta1EventHandlerArgs']]]]):
        pulumi.set(self, "event_handlers", value)

    @property
    @pulumi.getter
    def form(self) -> Optional[pulumi.Input['GoogleCloudDialogflowCxV3beta1FormArgs']]:
        """
        The form associated with the page, used for collecting parameters relevant to the page.
        """
        return pulumi.get(self, "form")

    @form.setter
    def form(self, value: Optional[pulumi.Input['GoogleCloudDialogflowCxV3beta1FormArgs']]):
        pulumi.set(self, "form", value)

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
        The unique identifier of the page. Required for the Pages.UpdatePage method. Pages.CreatePage populates the name automatically. Format: `projects//locations//agents//flows//pages/`.
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

    @property
    @pulumi.getter(name="transitionRouteGroups")
    def transition_route_groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Ordered list of `TransitionRouteGroups` associated with the page. Transition route groups must be unique within a page. * If multiple transition routes within a page scope refer to the same intent, then the precedence order is: page's transition route -> page's transition route group -> flow's transition routes. * If multiple transition route groups within a page contain the same intent, then the first group in the ordered list takes precedence. Format:`projects//locations//agents//flows//transitionRouteGroups/`.
        """
        return pulumi.get(self, "transition_route_groups")

    @transition_route_groups.setter
    def transition_route_groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "transition_route_groups", value)

    @property
    @pulumi.getter(name="transitionRoutes")
    def transition_routes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowCxV3beta1TransitionRouteArgs']]]]:
        """
        A list of transitions for the transition rules of this page. They route the conversation to another page in the same flow, or another flow. When we are in a certain page, the TransitionRoutes are evalauted in the following order: * TransitionRoutes defined in the page with intent specified. * TransitionRoutes defined in the transition route groups with intent specified. * TransitionRoutes defined in flow with intent specified. * TransitionRoutes defined in the transition route groups with intent specified. * TransitionRoutes defined in the page with only condition specified. * TransitionRoutes defined in the transition route groups with only condition specified.
        """
        return pulumi.get(self, "transition_routes")

    @transition_routes.setter
    def transition_routes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudDialogflowCxV3beta1TransitionRouteArgs']]]]):
        pulumi.set(self, "transition_routes", value)


class Page(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_id: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 entry_fulfillment: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1FulfillmentArgs']]] = None,
                 event_handlers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1EventHandlerArgs']]]]] = None,
                 flow_id: Optional[pulumi.Input[str]] = None,
                 form: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1FormArgs']]] = None,
                 language_code: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 transition_route_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 transition_routes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1TransitionRouteArgs']]]]] = None,
                 __props__=None):
        """
        Creates a page in the specified flow.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] display_name: The human-readable name of the page, unique within the agent.
        :param pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1FulfillmentArgs']] entry_fulfillment: The fulfillment to call when the session is entering the page.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1EventHandlerArgs']]]] event_handlers: Handlers associated with the page to handle events such as webhook errors, no match or no input.
        :param pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1FormArgs']] form: The form associated with the page, used for collecting parameters relevant to the page.
        :param pulumi.Input[str] name: The unique identifier of the page. Required for the Pages.UpdatePage method. Pages.CreatePage populates the name automatically. Format: `projects//locations//agents//flows//pages/`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] transition_route_groups: Ordered list of `TransitionRouteGroups` associated with the page. Transition route groups must be unique within a page. * If multiple transition routes within a page scope refer to the same intent, then the precedence order is: page's transition route -> page's transition route group -> flow's transition routes. * If multiple transition route groups within a page contain the same intent, then the first group in the ordered list takes precedence. Format:`projects//locations//agents//flows//transitionRouteGroups/`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1TransitionRouteArgs']]]] transition_routes: A list of transitions for the transition rules of this page. They route the conversation to another page in the same flow, or another flow. When we are in a certain page, the TransitionRoutes are evalauted in the following order: * TransitionRoutes defined in the page with intent specified. * TransitionRoutes defined in the transition route groups with intent specified. * TransitionRoutes defined in flow with intent specified. * TransitionRoutes defined in the transition route groups with intent specified. * TransitionRoutes defined in the page with only condition specified. * TransitionRoutes defined in the transition route groups with only condition specified.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PageArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a page in the specified flow.

        :param str resource_name: The name of the resource.
        :param PageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 agent_id: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 entry_fulfillment: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1FulfillmentArgs']]] = None,
                 event_handlers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1EventHandlerArgs']]]]] = None,
                 flow_id: Optional[pulumi.Input[str]] = None,
                 form: Optional[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1FormArgs']]] = None,
                 language_code: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 transition_route_groups: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 transition_routes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudDialogflowCxV3beta1TransitionRouteArgs']]]]] = None,
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
            __props__ = PageArgs.__new__(PageArgs)

            if agent_id is None and not opts.urn:
                raise TypeError("Missing required property 'agent_id'")
            __props__.__dict__["agent_id"] = agent_id
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["entry_fulfillment"] = entry_fulfillment
            __props__.__dict__["event_handlers"] = event_handlers
            if flow_id is None and not opts.urn:
                raise TypeError("Missing required property 'flow_id'")
            __props__.__dict__["flow_id"] = flow_id
            __props__.__dict__["form"] = form
            __props__.__dict__["language_code"] = language_code
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            __props__.__dict__["transition_route_groups"] = transition_route_groups
            __props__.__dict__["transition_routes"] = transition_routes
        super(Page, __self__).__init__(
            'google-native:dialogflow/v3beta1:Page',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Page':
        """
        Get an existing Page resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PageArgs.__new__(PageArgs)

        __props__.__dict__["display_name"] = None
        __props__.__dict__["entry_fulfillment"] = None
        __props__.__dict__["event_handlers"] = None
        __props__.__dict__["form"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["transition_route_groups"] = None
        __props__.__dict__["transition_routes"] = None
        return Page(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The human-readable name of the page, unique within the agent.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="entryFulfillment")
    def entry_fulfillment(self) -> pulumi.Output['outputs.GoogleCloudDialogflowCxV3beta1FulfillmentResponse']:
        """
        The fulfillment to call when the session is entering the page.
        """
        return pulumi.get(self, "entry_fulfillment")

    @property
    @pulumi.getter(name="eventHandlers")
    def event_handlers(self) -> pulumi.Output[Sequence['outputs.GoogleCloudDialogflowCxV3beta1EventHandlerResponse']]:
        """
        Handlers associated with the page to handle events such as webhook errors, no match or no input.
        """
        return pulumi.get(self, "event_handlers")

    @property
    @pulumi.getter
    def form(self) -> pulumi.Output['outputs.GoogleCloudDialogflowCxV3beta1FormResponse']:
        """
        The form associated with the page, used for collecting parameters relevant to the page.
        """
        return pulumi.get(self, "form")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The unique identifier of the page. Required for the Pages.UpdatePage method. Pages.CreatePage populates the name automatically. Format: `projects//locations//agents//flows//pages/`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="transitionRouteGroups")
    def transition_route_groups(self) -> pulumi.Output[Sequence[str]]:
        """
        Ordered list of `TransitionRouteGroups` associated with the page. Transition route groups must be unique within a page. * If multiple transition routes within a page scope refer to the same intent, then the precedence order is: page's transition route -> page's transition route group -> flow's transition routes. * If multiple transition route groups within a page contain the same intent, then the first group in the ordered list takes precedence. Format:`projects//locations//agents//flows//transitionRouteGroups/`.
        """
        return pulumi.get(self, "transition_route_groups")

    @property
    @pulumi.getter(name="transitionRoutes")
    def transition_routes(self) -> pulumi.Output[Sequence['outputs.GoogleCloudDialogflowCxV3beta1TransitionRouteResponse']]:
        """
        A list of transitions for the transition rules of this page. They route the conversation to another page in the same flow, or another flow. When we are in a certain page, the TransitionRoutes are evalauted in the following order: * TransitionRoutes defined in the page with intent specified. * TransitionRoutes defined in the transition route groups with intent specified. * TransitionRoutes defined in flow with intent specified. * TransitionRoutes defined in the transition route groups with intent specified. * TransitionRoutes defined in the page with only condition specified. * TransitionRoutes defined in the transition route groups with only condition specified.
        """
        return pulumi.get(self, "transition_routes")

