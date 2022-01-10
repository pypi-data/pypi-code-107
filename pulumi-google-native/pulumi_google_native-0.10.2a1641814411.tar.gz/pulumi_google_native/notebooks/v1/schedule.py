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

__all__ = ['ScheduleArgs', 'Schedule']

@pulumi.input_type
class ScheduleArgs:
    def __init__(__self__, *,
                 schedule_id: pulumi.Input[str],
                 cron_schedule: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 execution_template: Optional[pulumi.Input['ExecutionTemplateArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input['ScheduleState']] = None,
                 time_zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Schedule resource.
        :param pulumi.Input[str] cron_schedule: Cron-tab formatted schedule by which the job will execute. Format: minute, hour, day of month, month, day of week, e.g. 0 0 * * WED = every Wednesday More examples: https://crontab.guru/examples.html
        :param pulumi.Input[str] description: A brief description of this environment.
        :param pulumi.Input['ExecutionTemplateArgs'] execution_template: Notebook Execution Template corresponding to this schedule.
        :param pulumi.Input[str] time_zone: Timezone on which the cron_schedule. The value of this field must be a time zone name from the tz database. TZ Database: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones Note that some time zones include a provision for daylight savings time. The rules for daylight saving time are determined by the chosen tz. For UTC use the string "utc". If a time zone is not specified, the default will be in UTC (also known as GMT).
        """
        pulumi.set(__self__, "schedule_id", schedule_id)
        if cron_schedule is not None:
            pulumi.set(__self__, "cron_schedule", cron_schedule)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if execution_template is not None:
            pulumi.set(__self__, "execution_template", execution_template)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if time_zone is not None:
            pulumi.set(__self__, "time_zone", time_zone)

    @property
    @pulumi.getter(name="scheduleId")
    def schedule_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "schedule_id")

    @schedule_id.setter
    def schedule_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "schedule_id", value)

    @property
    @pulumi.getter(name="cronSchedule")
    def cron_schedule(self) -> Optional[pulumi.Input[str]]:
        """
        Cron-tab formatted schedule by which the job will execute. Format: minute, hour, day of month, month, day of week, e.g. 0 0 * * WED = every Wednesday More examples: https://crontab.guru/examples.html
        """
        return pulumi.get(self, "cron_schedule")

    @cron_schedule.setter
    def cron_schedule(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cron_schedule", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A brief description of this environment.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="executionTemplate")
    def execution_template(self) -> Optional[pulumi.Input['ExecutionTemplateArgs']]:
        """
        Notebook Execution Template corresponding to this schedule.
        """
        return pulumi.get(self, "execution_template")

    @execution_template.setter
    def execution_template(self, value: Optional[pulumi.Input['ExecutionTemplateArgs']]):
        pulumi.set(self, "execution_template", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input['ScheduleState']]:
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input['ScheduleState']]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[str]]:
        """
        Timezone on which the cron_schedule. The value of this field must be a time zone name from the tz database. TZ Database: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones Note that some time zones include a provision for daylight savings time. The rules for daylight saving time are determined by the chosen tz. For UTC use the string "utc". If a time zone is not specified, the default will be in UTC (also known as GMT).
        """
        return pulumi.get(self, "time_zone")

    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_zone", value)


class Schedule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cron_schedule: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 execution_template: Optional[pulumi.Input[pulumi.InputType['ExecutionTemplateArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 schedule_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input['ScheduleState']] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new Scheduled Notebook in a given project and location.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cron_schedule: Cron-tab formatted schedule by which the job will execute. Format: minute, hour, day of month, month, day of week, e.g. 0 0 * * WED = every Wednesday More examples: https://crontab.guru/examples.html
        :param pulumi.Input[str] description: A brief description of this environment.
        :param pulumi.Input[pulumi.InputType['ExecutionTemplateArgs']] execution_template: Notebook Execution Template corresponding to this schedule.
        :param pulumi.Input[str] time_zone: Timezone on which the cron_schedule. The value of this field must be a time zone name from the tz database. TZ Database: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones Note that some time zones include a provision for daylight savings time. The rules for daylight saving time are determined by the chosen tz. For UTC use the string "utc". If a time zone is not specified, the default will be in UTC (also known as GMT).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScheduleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new Scheduled Notebook in a given project and location.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param ScheduleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScheduleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cron_schedule: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 execution_template: Optional[pulumi.Input[pulumi.InputType['ExecutionTemplateArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 schedule_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input['ScheduleState']] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
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
            __props__ = ScheduleArgs.__new__(ScheduleArgs)

            __props__.__dict__["cron_schedule"] = cron_schedule
            __props__.__dict__["description"] = description
            __props__.__dict__["execution_template"] = execution_template
            __props__.__dict__["location"] = location
            __props__.__dict__["project"] = project
            if schedule_id is None and not opts.urn:
                raise TypeError("Missing required property 'schedule_id'")
            __props__.__dict__["schedule_id"] = schedule_id
            __props__.__dict__["state"] = state
            __props__.__dict__["time_zone"] = time_zone
            __props__.__dict__["create_time"] = None
            __props__.__dict__["display_name"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["recent_executions"] = None
            __props__.__dict__["update_time"] = None
        super(Schedule, __self__).__init__(
            'google-native:notebooks/v1:Schedule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Schedule':
        """
        Get an existing Schedule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ScheduleArgs.__new__(ScheduleArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["cron_schedule"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["execution_template"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["recent_executions"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["time_zone"] = None
        __props__.__dict__["update_time"] = None
        return Schedule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        Time the schedule was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="cronSchedule")
    def cron_schedule(self) -> pulumi.Output[str]:
        """
        Cron-tab formatted schedule by which the job will execute. Format: minute, hour, day of month, month, day of week, e.g. 0 0 * * WED = every Wednesday More examples: https://crontab.guru/examples.html
        """
        return pulumi.get(self, "cron_schedule")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        A brief description of this environment.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Display name used for UI purposes. Name can only contain alphanumeric characters, hyphens '-', and underscores '_'.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="executionTemplate")
    def execution_template(self) -> pulumi.Output['outputs.ExecutionTemplateResponse']:
        """
        Notebook Execution Template corresponding to this schedule.
        """
        return pulumi.get(self, "execution_template")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of this schedule. Format: `projects/{project_id}/locations/{location}/schedules/{schedule_id}`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="recentExecutions")
    def recent_executions(self) -> pulumi.Output[Sequence['outputs.ExecutionResponse']]:
        """
        The most recent execution names triggered from this schedule and their corresponding states.
        """
        return pulumi.get(self, "recent_executions")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[str]:
        """
        Timezone on which the cron_schedule. The value of this field must be a time zone name from the tz database. TZ Database: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones Note that some time zones include a provision for daylight savings time. The rules for daylight saving time are determined by the chosen tz. For UTC use the string "utc". If a time zone is not specified, the default will be in UTC (also known as GMT).
        """
        return pulumi.get(self, "time_zone")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        Time the schedule was last updated.
        """
        return pulumi.get(self, "update_time")

