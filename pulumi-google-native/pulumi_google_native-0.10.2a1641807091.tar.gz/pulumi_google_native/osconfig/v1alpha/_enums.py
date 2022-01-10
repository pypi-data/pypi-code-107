# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'OSPolicyMode',
    'OSPolicyResourceExecResourceExecInterpreter',
    'OSPolicyResourceFileResourceState',
    'OSPolicyResourcePackageResourceDesiredState',
    'OSPolicyResourceRepositoryResourceAptRepositoryArchiveType',
]


class OSPolicyMode(str, Enum):
    """
    Required. Policy mode
    """
    MODE_UNSPECIFIED = "MODE_UNSPECIFIED"
    """
    Invalid mode
    """
    VALIDATION = "VALIDATION"
    """
    This mode checks if the configuration resources in the policy are in their desired state. No actions are performed if they are not in the desired state. This mode is used for reporting purposes.
    """
    ENFORCEMENT = "ENFORCEMENT"
    """
    This mode checks if the configuration resources in the policy are in their desired state, and if not, enforces the desired state.
    """


class OSPolicyResourceExecResourceExecInterpreter(str, Enum):
    """
    Required. The script interpreter to use.
    """
    INTERPRETER_UNSPECIFIED = "INTERPRETER_UNSPECIFIED"
    """
    Defaults to NONE.
    """
    NONE = "NONE"
    """
    If an interpreter is not specified, the source is executed directly. This execution, without an interpreter, only succeeds for executables and scripts that have shebang lines.
    """
    SHELL = "SHELL"
    """
    Indicates that the script runs with `/bin/sh` on Linux and `cmd.exe` on Windows.
    """
    POWERSHELL = "POWERSHELL"
    """
    Indicates that the script runs with PowerShell.
    """


class OSPolicyResourceFileResourceState(str, Enum):
    """
    Required. Desired state of the file.
    """
    DESIRED_STATE_UNSPECIFIED = "DESIRED_STATE_UNSPECIFIED"
    """
    Unspecified is invalid.
    """
    PRESENT = "PRESENT"
    """
    Ensure file at path is present.
    """
    ABSENT = "ABSENT"
    """
    Ensure file at path is absent.
    """
    CONTENTS_MATCH = "CONTENTS_MATCH"
    """
    Ensure the contents of the file at path matches. If the file does not exist it will be created.
    """


class OSPolicyResourcePackageResourceDesiredState(str, Enum):
    """
    Required. The desired state the agent should maintain for this package.
    """
    DESIRED_STATE_UNSPECIFIED = "DESIRED_STATE_UNSPECIFIED"
    """
    Unspecified is invalid.
    """
    INSTALLED = "INSTALLED"
    """
    Ensure that the package is installed.
    """
    REMOVED = "REMOVED"
    """
    The agent ensures that the package is not installed and uninstalls it if detected.
    """


class OSPolicyResourceRepositoryResourceAptRepositoryArchiveType(str, Enum):
    """
    Required. Type of archive files in this repository.
    """
    ARCHIVE_TYPE_UNSPECIFIED = "ARCHIVE_TYPE_UNSPECIFIED"
    """
    Unspecified is invalid.
    """
    DEB = "DEB"
    """
    Deb indicates that the archive contains binary files.
    """
    DEB_SRC = "DEB_SRC"
    """
    Deb-src indicates that the archive contains source files.
    """
