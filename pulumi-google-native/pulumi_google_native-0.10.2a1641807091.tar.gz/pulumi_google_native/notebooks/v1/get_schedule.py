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
    'GetScheduleResult',
    'AwaitableGetScheduleResult',
    'get_schedule',
    'get_schedule_output',
]

@pulumi.output_type
class GetScheduleResult:
    def __init__(__self__, create_time=None, cron_schedule=None, description=None, display_name=None, execution_template=None, name=None, recent_executions=None, state=None, time_zone=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if cron_schedule and not isinstance(cron_schedule, str):
            raise TypeError("Expected argument 'cron_schedule' to be a str")
        pulumi.set(__self__, "cron_schedule", cron_schedule)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if execution_template and not isinstance(execution_template, dict):
            raise TypeError("Expected argument 'execution_template' to be a dict")
        pulumi.set(__self__, "execution_template", execution_template)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if recent_executions and not isinstance(recent_executions, list):
            raise TypeError("Expected argument 'recent_executions' to be a list")
        pulumi.set(__self__, "recent_executions", recent_executions)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if time_zone and not isinstance(time_zone, str):
            raise TypeError("Expected argument 'time_zone' to be a str")
        pulumi.set(__self__, "time_zone", time_zone)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        Time the schedule was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="cronSchedule")
    def cron_schedule(self) -> str:
        """
        Cron-tab formatted schedule by which the job will execute. Format: minute, hour, day of month, month, day of week, e.g. 0 0 * * WED = every Wednesday More examples: https://crontab.guru/examples.html
        """
        return pulumi.get(self, "cron_schedule")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        A brief description of this environment.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        Display name used for UI purposes. Name can only contain alphanumeric characters, hyphens '-', and underscores '_'.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="executionTemplate")
    def execution_template(self) -> 'outputs.ExecutionTemplateResponse':
        """
        Notebook Execution Template corresponding to this schedule.
        """
        return pulumi.get(self, "execution_template")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of this schedule. Format: `projects/{project_id}/locations/{location}/schedules/{schedule_id}`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="recentExecutions")
    def recent_executions(self) -> Sequence['outputs.ExecutionResponse']:
        """
        The most recent execution names triggered from this schedule and their corresponding states.
        """
        return pulumi.get(self, "recent_executions")

    @property
    @pulumi.getter
    def state(self) -> str:
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> str:
        """
        Timezone on which the cron_schedule. The value of this field must be a time zone name from the tz database. TZ Database: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones Note that some time zones include a provision for daylight savings time. The rules for daylight saving time are determined by the chosen tz. For UTC use the string "utc". If a time zone is not specified, the default will be in UTC (also known as GMT).
        """
        return pulumi.get(self, "time_zone")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        Time the schedule was last updated.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetScheduleResult(GetScheduleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScheduleResult(
            create_time=self.create_time,
            cron_schedule=self.cron_schedule,
            description=self.description,
            display_name=self.display_name,
            execution_template=self.execution_template,
            name=self.name,
            recent_executions=self.recent_executions,
            state=self.state,
            time_zone=self.time_zone,
            update_time=self.update_time)


def get_schedule(location: Optional[str] = None,
                 project: Optional[str] = None,
                 schedule_id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScheduleResult:
    """
    Gets details of schedule
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['project'] = project
    __args__['scheduleId'] = schedule_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:notebooks/v1:getSchedule', __args__, opts=opts, typ=GetScheduleResult).value

    return AwaitableGetScheduleResult(
        create_time=__ret__.create_time,
        cron_schedule=__ret__.cron_schedule,
        description=__ret__.description,
        display_name=__ret__.display_name,
        execution_template=__ret__.execution_template,
        name=__ret__.name,
        recent_executions=__ret__.recent_executions,
        state=__ret__.state,
        time_zone=__ret__.time_zone,
        update_time=__ret__.update_time)


@_utilities.lift_output_func(get_schedule)
def get_schedule_output(location: Optional[pulumi.Input[str]] = None,
                        project: Optional[pulumi.Input[Optional[str]]] = None,
                        schedule_id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScheduleResult]:
    """
    Gets details of schedule
    """
    ...
