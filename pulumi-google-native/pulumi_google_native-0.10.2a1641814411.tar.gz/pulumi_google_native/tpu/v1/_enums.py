# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'NodeHealth',
]


class NodeHealth(str, Enum):
    """
    The health status of the TPU node.
    """
    HEALTH_UNSPECIFIED = "HEALTH_UNSPECIFIED"
    """
    Health status is unknown: not initialized or failed to retrieve.
    """
    HEALTHY = "HEALTHY"
    """
    The resource is healthy.
    """
    DEPRECATED_UNHEALTHY = "DEPRECATED_UNHEALTHY"
    """
    The resource is unhealthy.
    """
    TIMEOUT = "TIMEOUT"
    """
    The resource is unresponsive.
    """
    UNHEALTHY_TENSORFLOW = "UNHEALTHY_TENSORFLOW"
    """
    The in-guest ML stack is unhealthy.
    """
    UNHEALTHY_MAINTENANCE = "UNHEALTHY_MAINTENANCE"
    """
    The node is under maintenance/priority boost caused rescheduling and will resume running once rescheduled.
    """
