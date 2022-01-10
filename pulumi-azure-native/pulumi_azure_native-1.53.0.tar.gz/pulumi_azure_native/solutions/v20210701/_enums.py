# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ApplicationArtifactType',
    'ApplicationDefinitionArtifactName',
    'ApplicationLockLevel',
    'ApplicationManagementMode',
    'DeploymentMode',
    'JitApprovalMode',
    'JitApproverType',
    'JitSchedulingType',
    'ManagedServiceIdentityType',
]


class ApplicationArtifactType(str, Enum):
    """
    The managed application definition artifact type.
    """
    NOT_SPECIFIED = "NotSpecified"
    TEMPLATE = "Template"
    CUSTOM = "Custom"


class ApplicationDefinitionArtifactName(str, Enum):
    """
    The managed application definition artifact name.
    """
    NOT_SPECIFIED = "NotSpecified"
    APPLICATION_RESOURCE_TEMPLATE = "ApplicationResourceTemplate"
    CREATE_UI_DEFINITION = "CreateUiDefinition"
    MAIN_TEMPLATE_PARAMETERS = "MainTemplateParameters"


class ApplicationLockLevel(str, Enum):
    """
    The managed application lock level.
    """
    CAN_NOT_DELETE = "CanNotDelete"
    READ_ONLY = "ReadOnly"
    NONE = "None"


class ApplicationManagementMode(str, Enum):
    """
    The managed application management mode.
    """
    NOT_SPECIFIED = "NotSpecified"
    UNMANAGED = "Unmanaged"
    MANAGED = "Managed"


class DeploymentMode(str, Enum):
    """
    The managed application deployment mode.
    """
    NOT_SPECIFIED = "NotSpecified"
    INCREMENTAL = "Incremental"
    COMPLETE = "Complete"


class JitApprovalMode(str, Enum):
    """
    JIT approval mode.
    """
    NOT_SPECIFIED = "NotSpecified"
    AUTO_APPROVE = "AutoApprove"
    MANUAL_APPROVE = "ManualApprove"


class JitApproverType(str, Enum):
    """
    The approver type.
    """
    USER = "user"
    GROUP = "group"


class JitSchedulingType(str, Enum):
    """
    The type of JIT schedule.
    """
    NOT_SPECIFIED = "NotSpecified"
    ONCE = "Once"
    RECURRING = "Recurring"


class ManagedServiceIdentityType(str, Enum):
    """
    Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"
