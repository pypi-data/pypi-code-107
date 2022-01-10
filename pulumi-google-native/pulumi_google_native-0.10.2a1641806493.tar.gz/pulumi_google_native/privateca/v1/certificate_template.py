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

__all__ = ['CertificateTemplateArgs', 'CertificateTemplate']

@pulumi.input_type
class CertificateTemplateArgs:
    def __init__(__self__, *,
                 certificate_template_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 identity_constraints: Optional[pulumi.Input['CertificateIdentityConstraintsArgs']] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 passthrough_extensions: Optional[pulumi.Input['CertificateExtensionConstraintsArgs']] = None,
                 predefined_values: Optional[pulumi.Input['X509ParametersArgs']] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CertificateTemplate resource.
        :param pulumi.Input[str] description: Optional. A human-readable description of scenarios this template is intended for.
        :param pulumi.Input['CertificateIdentityConstraintsArgs'] identity_constraints: Optional. Describes constraints on identities that may be appear in Certificates issued using this template. If this is omitted, then this template will not add restrictions on a certificate's identity.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. Labels with user-defined metadata.
        :param pulumi.Input['CertificateExtensionConstraintsArgs'] passthrough_extensions: Optional. Describes the set of X.509 extensions that may appear in a Certificate issued using this CertificateTemplate. If a certificate request sets extensions that don't appear in the passthrough_extensions, those extensions will be dropped. If the issuing CaPool's IssuancePolicy defines baseline_values that don't appear here, the certificate issuance request will fail. If this is omitted, then this template will not add restrictions on a certificate's X.509 extensions. These constraints do not apply to X.509 extensions set in this CertificateTemplate's predefined_values.
        :param pulumi.Input['X509ParametersArgs'] predefined_values: Optional. A set of X.509 values that will be applied to all issued certificates that use this template. If the certificate request includes conflicting values for the same properties, they will be overwritten by the values defined here. If the issuing CaPool's IssuancePolicy defines conflicting baseline_values for the same properties, the certificate issuance request will fail.
        """
        pulumi.set(__self__, "certificate_template_id", certificate_template_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if identity_constraints is not None:
            pulumi.set(__self__, "identity_constraints", identity_constraints)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if passthrough_extensions is not None:
            pulumi.set(__self__, "passthrough_extensions", passthrough_extensions)
        if predefined_values is not None:
            pulumi.set(__self__, "predefined_values", predefined_values)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if request_id is not None:
            pulumi.set(__self__, "request_id", request_id)

    @property
    @pulumi.getter(name="certificateTemplateId")
    def certificate_template_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "certificate_template_id")

    @certificate_template_id.setter
    def certificate_template_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "certificate_template_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. A human-readable description of scenarios this template is intended for.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="identityConstraints")
    def identity_constraints(self) -> Optional[pulumi.Input['CertificateIdentityConstraintsArgs']]:
        """
        Optional. Describes constraints on identities that may be appear in Certificates issued using this template. If this is omitted, then this template will not add restrictions on a certificate's identity.
        """
        return pulumi.get(self, "identity_constraints")

    @identity_constraints.setter
    def identity_constraints(self, value: Optional[pulumi.Input['CertificateIdentityConstraintsArgs']]):
        pulumi.set(self, "identity_constraints", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Optional. Labels with user-defined metadata.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="passthroughExtensions")
    def passthrough_extensions(self) -> Optional[pulumi.Input['CertificateExtensionConstraintsArgs']]:
        """
        Optional. Describes the set of X.509 extensions that may appear in a Certificate issued using this CertificateTemplate. If a certificate request sets extensions that don't appear in the passthrough_extensions, those extensions will be dropped. If the issuing CaPool's IssuancePolicy defines baseline_values that don't appear here, the certificate issuance request will fail. If this is omitted, then this template will not add restrictions on a certificate's X.509 extensions. These constraints do not apply to X.509 extensions set in this CertificateTemplate's predefined_values.
        """
        return pulumi.get(self, "passthrough_extensions")

    @passthrough_extensions.setter
    def passthrough_extensions(self, value: Optional[pulumi.Input['CertificateExtensionConstraintsArgs']]):
        pulumi.set(self, "passthrough_extensions", value)

    @property
    @pulumi.getter(name="predefinedValues")
    def predefined_values(self) -> Optional[pulumi.Input['X509ParametersArgs']]:
        """
        Optional. A set of X.509 values that will be applied to all issued certificates that use this template. If the certificate request includes conflicting values for the same properties, they will be overwritten by the values defined here. If the issuing CaPool's IssuancePolicy defines conflicting baseline_values for the same properties, the certificate issuance request will fail.
        """
        return pulumi.get(self, "predefined_values")

    @predefined_values.setter
    def predefined_values(self, value: Optional[pulumi.Input['X509ParametersArgs']]):
        pulumi.set(self, "predefined_values", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="requestId")
    def request_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "request_id")

    @request_id.setter
    def request_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_id", value)


class CertificateTemplate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_template_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 identity_constraints: Optional[pulumi.Input[pulumi.InputType['CertificateIdentityConstraintsArgs']]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 passthrough_extensions: Optional[pulumi.Input[pulumi.InputType['CertificateExtensionConstraintsArgs']]] = None,
                 predefined_values: Optional[pulumi.Input[pulumi.InputType['X509ParametersArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a new CertificateTemplate in a given Project and Location.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Optional. A human-readable description of scenarios this template is intended for.
        :param pulumi.Input[pulumi.InputType['CertificateIdentityConstraintsArgs']] identity_constraints: Optional. Describes constraints on identities that may be appear in Certificates issued using this template. If this is omitted, then this template will not add restrictions on a certificate's identity.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: Optional. Labels with user-defined metadata.
        :param pulumi.Input[pulumi.InputType['CertificateExtensionConstraintsArgs']] passthrough_extensions: Optional. Describes the set of X.509 extensions that may appear in a Certificate issued using this CertificateTemplate. If a certificate request sets extensions that don't appear in the passthrough_extensions, those extensions will be dropped. If the issuing CaPool's IssuancePolicy defines baseline_values that don't appear here, the certificate issuance request will fail. If this is omitted, then this template will not add restrictions on a certificate's X.509 extensions. These constraints do not apply to X.509 extensions set in this CertificateTemplate's predefined_values.
        :param pulumi.Input[pulumi.InputType['X509ParametersArgs']] predefined_values: Optional. A set of X.509 values that will be applied to all issued certificates that use this template. If the certificate request includes conflicting values for the same properties, they will be overwritten by the values defined here. If the issuing CaPool's IssuancePolicy defines conflicting baseline_values for the same properties, the certificate issuance request will fail.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CertificateTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a new CertificateTemplate in a given Project and Location.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param CertificateTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CertificateTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_template_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 identity_constraints: Optional[pulumi.Input[pulumi.InputType['CertificateIdentityConstraintsArgs']]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 passthrough_extensions: Optional[pulumi.Input[pulumi.InputType['CertificateExtensionConstraintsArgs']]] = None,
                 predefined_values: Optional[pulumi.Input[pulumi.InputType['X509ParametersArgs']]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = CertificateTemplateArgs.__new__(CertificateTemplateArgs)

            if certificate_template_id is None and not opts.urn:
                raise TypeError("Missing required property 'certificate_template_id'")
            __props__.__dict__["certificate_template_id"] = certificate_template_id
            __props__.__dict__["description"] = description
            __props__.__dict__["identity_constraints"] = identity_constraints
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            __props__.__dict__["passthrough_extensions"] = passthrough_extensions
            __props__.__dict__["predefined_values"] = predefined_values
            __props__.__dict__["project"] = project
            __props__.__dict__["request_id"] = request_id
            __props__.__dict__["create_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["update_time"] = None
        super(CertificateTemplate, __self__).__init__(
            'google-native:privateca/v1:CertificateTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CertificateTemplate':
        """
        Get an existing CertificateTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CertificateTemplateArgs.__new__(CertificateTemplateArgs)

        __props__.__dict__["create_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["identity_constraints"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["passthrough_extensions"] = None
        __props__.__dict__["predefined_values"] = None
        __props__.__dict__["update_time"] = None
        return CertificateTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        The time at which this CertificateTemplate was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Optional. A human-readable description of scenarios this template is intended for.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="identityConstraints")
    def identity_constraints(self) -> pulumi.Output['outputs.CertificateIdentityConstraintsResponse']:
        """
        Optional. Describes constraints on identities that may be appear in Certificates issued using this template. If this is omitted, then this template will not add restrictions on a certificate's identity.
        """
        return pulumi.get(self, "identity_constraints")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Optional. Labels with user-defined metadata.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The resource name for this CertificateTemplate in the format `projects/*/locations/*/certificateTemplates/*`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="passthroughExtensions")
    def passthrough_extensions(self) -> pulumi.Output['outputs.CertificateExtensionConstraintsResponse']:
        """
        Optional. Describes the set of X.509 extensions that may appear in a Certificate issued using this CertificateTemplate. If a certificate request sets extensions that don't appear in the passthrough_extensions, those extensions will be dropped. If the issuing CaPool's IssuancePolicy defines baseline_values that don't appear here, the certificate issuance request will fail. If this is omitted, then this template will not add restrictions on a certificate's X.509 extensions. These constraints do not apply to X.509 extensions set in this CertificateTemplate's predefined_values.
        """
        return pulumi.get(self, "passthrough_extensions")

    @property
    @pulumi.getter(name="predefinedValues")
    def predefined_values(self) -> pulumi.Output['outputs.X509ParametersResponse']:
        """
        Optional. A set of X.509 values that will be applied to all issued certificates that use this template. If the certificate request includes conflicting values for the same properties, they will be overwritten by the values defined here. If the issuing CaPool's IssuancePolicy defines conflicting baseline_values for the same properties, the certificate issuance request will fail.
        """
        return pulumi.get(self, "predefined_values")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[str]:
        """
        The time at which this CertificateTemplate was updated.
        """
        return pulumi.get(self, "update_time")

