# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AccessRights',
    'NamespaceType',
]


class AccessRights(str, Enum):
    MANAGE = "Manage"
    SEND = "Send"
    LISTEN = "Listen"


class NamespaceType(str, Enum):
    """
    Gets or sets the namespace type.
    """
    MESSAGING = "Messaging"
    NOTIFICATION_HUB = "NotificationHub"
