# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'BasicPerfSampleSeriesPerfMetricType',
    'BasicPerfSampleSeriesPerfUnit',
    'BasicPerfSampleSeriesSampleSeriesLabel',
    'ExecutionState',
    'HistoryTestPlatform',
    'IndividualOutcomeOutcomeSummary',
    'OutcomeSummary',
    'PrimaryStepRollUp',
    'StepState',
    'TestIssueCategory',
    'TestIssueSeverity',
    'TestIssueType',
]


class BasicPerfSampleSeriesPerfMetricType(str, Enum):
    PERF_METRIC_TYPE_UNSPECIFIED = "perfMetricTypeUnspecified"
    MEMORY = "memory"
    CPU = "cpu"
    NETWORK = "network"
    GRAPHICS = "graphics"


class BasicPerfSampleSeriesPerfUnit(str, Enum):
    PERF_UNIT_UNSPECIFIED = "perfUnitUnspecified"
    KIBIBYTE = "kibibyte"
    PERCENT = "percent"
    BYTES_PER_SECOND = "bytesPerSecond"
    FRAMES_PER_SECOND = "framesPerSecond"
    BYTE = "byte"


class BasicPerfSampleSeriesSampleSeriesLabel(str, Enum):
    SAMPLE_SERIES_TYPE_UNSPECIFIED = "sampleSeriesTypeUnspecified"
    MEMORY_RSS_PRIVATE = "memoryRssPrivate"
    """
    Memory sample series
    """
    MEMORY_RSS_SHARED = "memoryRssShared"
    MEMORY_RSS_TOTAL = "memoryRssTotal"
    MEMORY_TOTAL = "memoryTotal"
    CPU_USER = "cpuUser"
    """
    CPU sample series
    """
    CPU_KERNEL = "cpuKernel"
    CPU_TOTAL = "cpuTotal"
    NT_BYTES_TRANSFERRED = "ntBytesTransferred"
    """
    Network sample series
    """
    NT_BYTES_RECEIVED = "ntBytesReceived"
    NETWORK_SENT = "networkSent"
    NETWORK_RECEIVED = "networkReceived"
    GRAPHICS_FRAME_RATE = "graphicsFrameRate"
    """
    Graphics sample series
    """


class ExecutionState(str, Enum):
    """
    The initial state is IN_PROGRESS. The only legal state transitions is from IN_PROGRESS to COMPLETE. A PRECONDITION_FAILED will be returned if an invalid transition is requested. The state can only be set to COMPLETE once. A FAILED_PRECONDITION will be returned if the state is set to COMPLETE multiple times. If the state is set to COMPLETE, all the in-progress steps within the execution will be set as COMPLETE. If the outcome of the step is not set, the outcome will be set to INCONCLUSIVE. - In response always set - In create/update request: optional
    """
    UNKNOWN_STATE = "unknownState"
    """
    Should never be in this state. Exists for proto deserialization backward compatibility.
    """
    PENDING = "pending"
    """
    The Execution/Step is created, ready to run, but not running yet. If an Execution/Step is created without initial state, it is assumed that the Execution/Step is in PENDING state.
    """
    IN_PROGRESS = "inProgress"
    """
    The Execution/Step is in progress.
    """
    COMPLETE = "complete"
    """
    The finalized, immutable state. Steps/Executions in this state cannot be modified.
    """


class HistoryTestPlatform(str, Enum):
    """
    The platform of the test history. - In response: always set. Returns the platform of the last execution if unknown.
    """
    UNKNOWN_PLATFORM = "unknownPlatform"
    ANDROID = "android"
    IOS = "ios"


class IndividualOutcomeOutcomeSummary(str, Enum):
    UNSET = "unset"
    """
    Do not use. For proto versioning only.
    """
    SUCCESS = "success"
    """
    The test matrix run was successful, for instance: - All the test cases passed. - Robo did not detect a crash of the application under test.
    """
    FAILURE = "failure"
    """
    A run failed, for instance: - One or more test case failed. - A test timed out. - The application under test crashed.
    """
    INCONCLUSIVE = "inconclusive"
    """
    Something unexpected happened. The run should still be considered unsuccessful but this is likely a transient problem and re-running the test might be successful.
    """
    SKIPPED = "skipped"
    """
    All tests were skipped, for instance: - All device configurations were incompatible.
    """
    FLAKY = "flaky"
    """
    A group of steps that were run with the same configuration had both failure and success outcomes.
    """


class OutcomeSummary(str, Enum):
    """
    The simplest way to interpret a result. Required
    """
    UNSET = "unset"
    """
    Do not use. For proto versioning only.
    """
    SUCCESS = "success"
    """
    The test matrix run was successful, for instance: - All the test cases passed. - Robo did not detect a crash of the application under test.
    """
    FAILURE = "failure"
    """
    A run failed, for instance: - One or more test case failed. - A test timed out. - The application under test crashed.
    """
    INCONCLUSIVE = "inconclusive"
    """
    Something unexpected happened. The run should still be considered unsuccessful but this is likely a transient problem and re-running the test might be successful.
    """
    SKIPPED = "skipped"
    """
    All tests were skipped, for instance: - All device configurations were incompatible.
    """
    FLAKY = "flaky"
    """
    A group of steps that were run with the same configuration had both failure and success outcomes.
    """


class PrimaryStepRollUp(str, Enum):
    """
    Rollup test status of multiple steps that were run with the same configuration as a group.
    """
    UNSET = "unset"
    """
    Do not use. For proto versioning only.
    """
    SUCCESS = "success"
    """
    The test matrix run was successful, for instance: - All the test cases passed. - Robo did not detect a crash of the application under test.
    """
    FAILURE = "failure"
    """
    A run failed, for instance: - One or more test case failed. - A test timed out. - The application under test crashed.
    """
    INCONCLUSIVE = "inconclusive"
    """
    Something unexpected happened. The run should still be considered unsuccessful but this is likely a transient problem and re-running the test might be successful.
    """
    SKIPPED = "skipped"
    """
    All tests were skipped, for instance: - All device configurations were incompatible.
    """
    FLAKY = "flaky"
    """
    A group of steps that were run with the same configuration had both failure and success outcomes.
    """


class StepState(str, Enum):
    """
    The initial state is IN_PROGRESS. The only legal state transitions are * IN_PROGRESS -> COMPLETE A PRECONDITION_FAILED will be returned if an invalid transition is requested. It is valid to create Step with a state set to COMPLETE. The state can only be set to COMPLETE once. A PRECONDITION_FAILED will be returned if the state is set to COMPLETE multiple times. - In response: always set - In create/update request: optional
    """
    UNKNOWN_STATE = "unknownState"
    """
    Should never be in this state. Exists for proto deserialization backward compatibility.
    """
    PENDING = "pending"
    """
    The Execution/Step is created, ready to run, but not running yet. If an Execution/Step is created without initial state, it is assumed that the Execution/Step is in PENDING state.
    """
    IN_PROGRESS = "inProgress"
    """
    The Execution/Step is in progress.
    """
    COMPLETE = "complete"
    """
    The finalized, immutable state. Steps/Executions in this state cannot be modified.
    """


class TestIssueCategory(str, Enum):
    """
    Category of issue. Required.
    """
    UNSPECIFIED_CATEGORY = "unspecifiedCategory"
    """
    Default unspecified category. Do not use. For versioning only.
    """
    COMMON = "common"
    """
    Issue is not specific to a particular test kind (e.g., a native crash).
    """
    ROBO = "robo"
    """
    Issue is specific to Robo run.
    """


class TestIssueSeverity(str, Enum):
    """
    Severity of issue. Required.
    """
    UNSPECIFIED_SEVERITY = "unspecifiedSeverity"
    """
    Default unspecified severity. Do not use. For versioning only.
    """
    INFO = "info"
    """
    Non critical issue, providing users with some info about the test run.
    """
    SUGGESTION = "suggestion"
    """
    Non critical issue, providing users with some hints on improving their testing experience, e.g., suggesting to use Game Loops.
    """
    WARNING = "warning"
    """
    Potentially critical issue.
    """
    SEVERE = "severe"
    """
    Critical issue.
    """


class TestIssueType(str, Enum):
    """
    Type of issue. Required.
    """
    UNSPECIFIED_TYPE = "unspecifiedType"
    """
    Default unspecified type. Do not use. For versioning only.
    """
    FATAL_EXCEPTION = "fatalException"
    """
    Issue is a fatal exception.
    """
    NATIVE_CRASH = "nativeCrash"
    """
    Issue is a native crash.
    """
    ANR = "anr"
    """
    Issue is an ANR crash.
    """
    UNUSED_ROBO_DIRECTIVE = "unusedRoboDirective"
    """
    Issue is an unused robo directive.
    """
    COMPATIBLE_WITH_ORCHESTRATOR = "compatibleWithOrchestrator"
    """
    Issue is a suggestion to use orchestrator.
    """
    LAUNCHER_ACTIVITY_NOT_FOUND = "launcherActivityNotFound"
    """
    Issue with finding a launcher activity
    """
    START_ACTIVITY_NOT_FOUND = "startActivityNotFound"
    """
    Issue with resolving a user-provided intent to start an activity
    """
    INCOMPLETE_ROBO_SCRIPT_EXECUTION = "incompleteRoboScriptExecution"
    """
    A Robo script was not fully executed.
    """
    COMPLETE_ROBO_SCRIPT_EXECUTION = "completeRoboScriptExecution"
    """
    A Robo script was fully and successfully executed.
    """
    FAILED_TO_INSTALL = "failedToInstall"
    """
    The APK failed to install.
    """
    AVAILABLE_DEEP_LINKS = "availableDeepLinks"
    """
    The app-under-test has deep links, but none were provided to Robo.
    """
    NON_SDK_API_USAGE_VIOLATION = "nonSdkApiUsageViolation"
    """
    App accessed a non-sdk Api.
    """
    NON_SDK_API_USAGE_REPORT = "nonSdkApiUsageReport"
    """
    App accessed a non-sdk Api (new detailed report)
    """
    ENCOUNTERED_NON_ANDROID_UI_WIDGET_SCREEN = "encounteredNonAndroidUiWidgetScreen"
    """
    Robo crawl encountered at least one screen with elements that are not Android UI widgets.
    """
    ENCOUNTERED_LOGIN_SCREEN = "encounteredLoginScreen"
    """
    Robo crawl encountered at least one probable login screen.
    """
    PERFORMED_GOOGLE_LOGIN = "performedGoogleLogin"
    """
    Robo signed in with Google.
    """
    IOS_EXCEPTION = "iosException"
    """
    iOS App crashed with an exception.
    """
    IOS_CRASH = "iosCrash"
    """
    iOS App crashed without an exception (e.g. killed).
    """
    PERFORMED_MONKEY_ACTIONS = "performedMonkeyActions"
    """
    Robo crawl involved performing some monkey actions.
    """
    USED_ROBO_DIRECTIVE = "usedRoboDirective"
    """
    Robo crawl used a Robo directive.
    """
    USED_ROBO_IGNORE_DIRECTIVE = "usedRoboIgnoreDirective"
    """
    Robo crawl used a Robo directive to ignore an UI element.
    """
    INSUFFICIENT_COVERAGE = "insufficientCoverage"
    """
    Robo did not crawl some potentially important parts of the app.
    """
    IN_APP_PURCHASES = "inAppPurchases"
    """
    Robo crawl involved some in-app purchases.
    """
    CRASH_DIALOG_ERROR = "crashDialogError"
    """
    Crash dialog was detected during the test execution
    """
    UI_ELEMENTS_TOO_DEEP = "uiElementsTooDeep"
    """
    UI element depth is greater than the threshold
    """
    BLANK_SCREEN = "blankScreen"
    """
    Blank screen is found in the Robo crawl
    """
    OVERLAPPING_UI_ELEMENTS = "overlappingUiElements"
    """
    Overlapping UI elements are found in the Robo crawl
    """
    UNITY_EXCEPTION = "unityException"
    """
    An uncaught Unity exception was detected (these don't crash apps).
    """
    DEVICE_OUT_OF_MEMORY = "deviceOutOfMemory"
    """
    Device running out of memory was detected
    """
    LOGCAT_COLLECTION_ERROR = "logcatCollectionError"
    """
    Problems detected while collecting logcat
    """
