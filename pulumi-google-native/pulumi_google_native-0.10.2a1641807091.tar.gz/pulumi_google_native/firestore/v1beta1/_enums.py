# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'GoogleFirestoreAdminV1beta1IndexFieldMode',
    'IndexState',
]


class GoogleFirestoreAdminV1beta1IndexFieldMode(str, Enum):
    """
    The field's mode.
    """
    MODE_UNSPECIFIED = "MODE_UNSPECIFIED"
    """
    The mode is unspecified.
    """
    ASCENDING = "ASCENDING"
    """
    The field's values are indexed so as to support sequencing in ascending order and also query by <, >, <=, >=, and =.
    """
    DESCENDING = "DESCENDING"
    """
    The field's values are indexed so as to support sequencing in descending order and also query by <, >, <=, >=, and =.
    """
    ARRAY_CONTAINS = "ARRAY_CONTAINS"
    """
    The field's array values are indexed so as to support membership using ARRAY_CONTAINS queries.
    """


class IndexState(str, Enum):
    """
    The state of the index. Output only.
    """
    STATE_UNSPECIFIED = "STATE_UNSPECIFIED"
    """
    The state is unspecified.
    """
    CREATING = "CREATING"
    """
    The index is being created. There is an active long-running operation for the index. The index is updated when writing a document. Some index data may exist.
    """
    READY = "READY"
    """
    The index is ready to be used. The index is updated when writing a document. The index is fully populated from all stored documents it applies to.
    """
    ERROR = "ERROR"
    """
    The index was being created, but something went wrong. There is no active long-running operation for the index, and the most recently finished long-running operation failed. The index is not updated when writing a document. Some index data may exist.
    """
