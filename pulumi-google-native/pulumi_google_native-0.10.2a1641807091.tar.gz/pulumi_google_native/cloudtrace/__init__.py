# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_google_native.cloudtrace.v2beta1 as __v2beta1
    v2beta1 = __v2beta1
else:
    v2beta1 = _utilities.lazy_import('pulumi_google_native.cloudtrace.v2beta1')

