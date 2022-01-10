# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEdgeApplicationVersionDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'description': 'str',
        'deploy_type': 'str',
        'container_settings': 'ContainerSettingsDTO',
        'liveness_probe': 'ProbeDTO',
        'readiness_probe': 'ProbeDTO',
        'arch': 'object',
        'command': 'object',
        'args': 'object',
        'outputs': 'object',
        'inputs': 'object',
        'services': 'object'
    }

    attribute_map = {
        'version': 'version',
        'description': 'description',
        'deploy_type': 'deploy_type',
        'container_settings': 'container_settings',
        'liveness_probe': 'liveness_probe',
        'readiness_probe': 'readiness_probe',
        'arch': 'arch',
        'command': 'command',
        'args': 'args',
        'outputs': 'outputs',
        'inputs': 'inputs',
        'services': 'services'
    }

    def __init__(self, version=None, description=None, deploy_type=None, container_settings=None, liveness_probe=None, readiness_probe=None, arch=None, command=None, args=None, outputs=None, inputs=None, services=None):
        """CreateEdgeApplicationVersionDTO - a model defined in huaweicloud sdk"""
        
        

        self._version = None
        self._description = None
        self._deploy_type = None
        self._container_settings = None
        self._liveness_probe = None
        self._readiness_probe = None
        self._arch = None
        self._command = None
        self._args = None
        self._outputs = None
        self._inputs = None
        self._services = None
        self.discriminator = None

        self.version = version
        if description is not None:
            self.description = description
        if deploy_type is not None:
            self.deploy_type = deploy_type
        self.container_settings = container_settings
        if liveness_probe is not None:
            self.liveness_probe = liveness_probe
        if readiness_probe is not None:
            self.readiness_probe = readiness_probe
        self.arch = arch
        if command is not None:
            self.command = command
        if args is not None:
            self.args = args
        if outputs is not None:
            self.outputs = outputs
        if inputs is not None:
            self.inputs = inputs
        if services is not None:
            self.services = services

    @property
    def version(self):
        """Gets the version of this CreateEdgeApplicationVersionDTO.

        应用版本

        :return: The version of this CreateEdgeApplicationVersionDTO.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CreateEdgeApplicationVersionDTO.

        应用版本

        :param version: The version of this CreateEdgeApplicationVersionDTO.
        :type: str
        """
        self._version = version

    @property
    def description(self):
        """Gets the description of this CreateEdgeApplicationVersionDTO.

        应用描述

        :return: The description of this CreateEdgeApplicationVersionDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateEdgeApplicationVersionDTO.

        应用描述

        :param description: The description of this CreateEdgeApplicationVersionDTO.
        :type: str
        """
        self._description = description

    @property
    def deploy_type(self):
        """Gets the deploy_type of this CreateEdgeApplicationVersionDTO.

        应用部署类型，分为docker容器部署类型和process进程部署类型，兼容之前数据，此字段可以为空，为空情况为docker类型

        :return: The deploy_type of this CreateEdgeApplicationVersionDTO.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        """Sets the deploy_type of this CreateEdgeApplicationVersionDTO.

        应用部署类型，分为docker容器部署类型和process进程部署类型，兼容之前数据，此字段可以为空，为空情况为docker类型

        :param deploy_type: The deploy_type of this CreateEdgeApplicationVersionDTO.
        :type: str
        """
        self._deploy_type = deploy_type

    @property
    def container_settings(self):
        """Gets the container_settings of this CreateEdgeApplicationVersionDTO.


        :return: The container_settings of this CreateEdgeApplicationVersionDTO.
        :rtype: ContainerSettingsDTO
        """
        return self._container_settings

    @container_settings.setter
    def container_settings(self, container_settings):
        """Sets the container_settings of this CreateEdgeApplicationVersionDTO.


        :param container_settings: The container_settings of this CreateEdgeApplicationVersionDTO.
        :type: ContainerSettingsDTO
        """
        self._container_settings = container_settings

    @property
    def liveness_probe(self):
        """Gets the liveness_probe of this CreateEdgeApplicationVersionDTO.


        :return: The liveness_probe of this CreateEdgeApplicationVersionDTO.
        :rtype: ProbeDTO
        """
        return self._liveness_probe

    @liveness_probe.setter
    def liveness_probe(self, liveness_probe):
        """Sets the liveness_probe of this CreateEdgeApplicationVersionDTO.


        :param liveness_probe: The liveness_probe of this CreateEdgeApplicationVersionDTO.
        :type: ProbeDTO
        """
        self._liveness_probe = liveness_probe

    @property
    def readiness_probe(self):
        """Gets the readiness_probe of this CreateEdgeApplicationVersionDTO.


        :return: The readiness_probe of this CreateEdgeApplicationVersionDTO.
        :rtype: ProbeDTO
        """
        return self._readiness_probe

    @readiness_probe.setter
    def readiness_probe(self, readiness_probe):
        """Sets the readiness_probe of this CreateEdgeApplicationVersionDTO.


        :param readiness_probe: The readiness_probe of this CreateEdgeApplicationVersionDTO.
        :type: ProbeDTO
        """
        self._readiness_probe = readiness_probe

    @property
    def arch(self):
        """Gets the arch of this CreateEdgeApplicationVersionDTO.

        架构

        :return: The arch of this CreateEdgeApplicationVersionDTO.
        :rtype: object
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this CreateEdgeApplicationVersionDTO.

        架构

        :param arch: The arch of this CreateEdgeApplicationVersionDTO.
        :type: object
        """
        self._arch = arch

    @property
    def command(self):
        """Gets the command of this CreateEdgeApplicationVersionDTO.

        启动命令

        :return: The command of this CreateEdgeApplicationVersionDTO.
        :rtype: object
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this CreateEdgeApplicationVersionDTO.

        启动命令

        :param command: The command of this CreateEdgeApplicationVersionDTO.
        :type: object
        """
        self._command = command

    @property
    def args(self):
        """Gets the args of this CreateEdgeApplicationVersionDTO.

        启动参数

        :return: The args of this CreateEdgeApplicationVersionDTO.
        :rtype: object
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this CreateEdgeApplicationVersionDTO.

        启动参数

        :param args: The args of this CreateEdgeApplicationVersionDTO.
        :type: object
        """
        self._args = args

    @property
    def outputs(self):
        """Gets the outputs of this CreateEdgeApplicationVersionDTO.

        应用输出路由端点

        :return: The outputs of this CreateEdgeApplicationVersionDTO.
        :rtype: object
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this CreateEdgeApplicationVersionDTO.

        应用输出路由端点

        :param outputs: The outputs of this CreateEdgeApplicationVersionDTO.
        :type: object
        """
        self._outputs = outputs

    @property
    def inputs(self):
        """Gets the inputs of this CreateEdgeApplicationVersionDTO.

        应用输入路由

        :return: The inputs of this CreateEdgeApplicationVersionDTO.
        :rtype: object
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this CreateEdgeApplicationVersionDTO.

        应用输入路由

        :param inputs: The inputs of this CreateEdgeApplicationVersionDTO.
        :type: object
        """
        self._inputs = inputs

    @property
    def services(self):
        """Gets the services of this CreateEdgeApplicationVersionDTO.

        应用实现的服务列表

        :return: The services of this CreateEdgeApplicationVersionDTO.
        :rtype: object
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this CreateEdgeApplicationVersionDTO.

        应用实现的服务列表

        :param services: The services of this CreateEdgeApplicationVersionDTO.
        :type: object
        """
        self._services = services

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateEdgeApplicationVersionDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
