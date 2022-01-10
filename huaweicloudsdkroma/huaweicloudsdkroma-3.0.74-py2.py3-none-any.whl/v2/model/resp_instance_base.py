# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RespInstanceBase:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'project_id': 'str',
        'instance_name': 'str',
        'status': 'str',
        'instance_status': 'int',
        'type': 'str',
        'spec': 'str',
        'create_time': 'int',
        'enterprise_project_id': 'str',
        'eip_address': 'str',
        'charging_mode': 'int',
        'cbc_metadata': 'str'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'instance_name': 'instance_name',
        'status': 'status',
        'instance_status': 'instance_status',
        'type': 'type',
        'spec': 'spec',
        'create_time': 'create_time',
        'enterprise_project_id': 'enterprise_project_id',
        'eip_address': 'eip_address',
        'charging_mode': 'charging_mode',
        'cbc_metadata': 'cbc_metadata'
    }

    def __init__(self, id=None, project_id=None, instance_name=None, status=None, instance_status=None, type=None, spec=None, create_time=None, enterprise_project_id=None, eip_address=None, charging_mode=None, cbc_metadata=None):
        """RespInstanceBase - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._project_id = None
        self._instance_name = None
        self._status = None
        self._instance_status = None
        self._type = None
        self._spec = None
        self._create_time = None
        self._enterprise_project_id = None
        self._eip_address = None
        self._charging_mode = None
        self._cbc_metadata = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if instance_name is not None:
            self.instance_name = instance_name
        if status is not None:
            self.status = status
        if instance_status is not None:
            self.instance_status = instance_status
        if type is not None:
            self.type = type
        if spec is not None:
            self.spec = spec
        if create_time is not None:
            self.create_time = create_time
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if eip_address is not None:
            self.eip_address = eip_address
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if cbc_metadata is not None:
            self.cbc_metadata = cbc_metadata

    @property
    def id(self):
        """Gets the id of this RespInstanceBase.

        实例编号

        :return: The id of this RespInstanceBase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RespInstanceBase.

        实例编号

        :param id: The id of this RespInstanceBase.
        :type: str
        """
        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this RespInstanceBase.

        实例所属项目编号

        :return: The project_id of this RespInstanceBase.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this RespInstanceBase.

        实例所属项目编号

        :param project_id: The project_id of this RespInstanceBase.
        :type: str
        """
        self._project_id = project_id

    @property
    def instance_name(self):
        """Gets the instance_name of this RespInstanceBase.

        实例名称

        :return: The instance_name of this RespInstanceBase.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this RespInstanceBase.

        实例名称

        :param instance_name: The instance_name of this RespInstanceBase.
        :type: str
        """
        self._instance_name = instance_name

    @property
    def status(self):
        """Gets the status of this RespInstanceBase.

        实例状态： - Creating：创建中 - CreateSuccess：创建成功 - CreateFail：创建失败 - Initing：初始化中 - Registering：注册中 - Running：运行中 - InitingFailed：初始化失败 - RegisterFailed：注册失败 - Installing：安装中 - InstallFailed：安装失败 - Updating：升级中 - UpdateFailed：升级失败 - Rollbacking：回滚中 - RollbackSuccess：回滚成功 - RollbackFailed：回滚失败 - Deleting：删除中 - DeleteFailed：删除失败 - Unregistering：注销中 - UnRegisterFailed：注销失败 - CreateTimeout：创建超时 - InitTimeout：初始化超时 - RegisterTimeout：注册超时 - InstallTimeout：安装超时 - UpdateTimeout：升级超时 - RollbackTimeout：回滚超时 - DeleteTimeout：删除超时 - UnregisterTimeout：注销超时 - Starting：启动中 - Freezing：冻结中 - Frozen：已冻结 - Restarting：重启中 - RestartFail：重启失败 - Unhealthy：实例异常 - RestartTimeout：重启超时

        :return: The status of this RespInstanceBase.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RespInstanceBase.

        实例状态： - Creating：创建中 - CreateSuccess：创建成功 - CreateFail：创建失败 - Initing：初始化中 - Registering：注册中 - Running：运行中 - InitingFailed：初始化失败 - RegisterFailed：注册失败 - Installing：安装中 - InstallFailed：安装失败 - Updating：升级中 - UpdateFailed：升级失败 - Rollbacking：回滚中 - RollbackSuccess：回滚成功 - RollbackFailed：回滚失败 - Deleting：删除中 - DeleteFailed：删除失败 - Unregistering：注销中 - UnRegisterFailed：注销失败 - CreateTimeout：创建超时 - InitTimeout：初始化超时 - RegisterTimeout：注册超时 - InstallTimeout：安装超时 - UpdateTimeout：升级超时 - RollbackTimeout：回滚超时 - DeleteTimeout：删除超时 - UnregisterTimeout：注销超时 - Starting：启动中 - Freezing：冻结中 - Frozen：已冻结 - Restarting：重启中 - RestartFail：重启失败 - Unhealthy：实例异常 - RestartTimeout：重启超时

        :param status: The status of this RespInstanceBase.
        :type: str
        """
        self._status = status

    @property
    def instance_status(self):
        """Gets the instance_status of this RespInstanceBase.

        实例状态对应编号 - 1：创建中 - 2：创建成功 - 3：创建失败 - 4：初始化中 - 5：注册中 - 6：运行中 - 7：初始化失败 - 8：注册失败 - 10：安装中 - 11：安装失败 - 12：升级中 - 13：升级失败 - 20：回滚中 - 21：回滚成功 - 22：回滚失败 - 23：删除中 - 24：删除失败 - 25：注销中 - 26：注销失败 - 27：创建超时 - 28：初始化超时 - 29：注册超时 - 30：安装超时 - 31：升级超时 - 32：回滚超时 - 33：删除超时 - 34：注销超时 - 35：启动中 - 36：冻结中 - 37：已冻结 - 38：重启中 - 39：重启失败 - 40：实例异常 - 41：重启超时

        :return: The instance_status of this RespInstanceBase.
        :rtype: int
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        """Sets the instance_status of this RespInstanceBase.

        实例状态对应编号 - 1：创建中 - 2：创建成功 - 3：创建失败 - 4：初始化中 - 5：注册中 - 6：运行中 - 7：初始化失败 - 8：注册失败 - 10：安装中 - 11：安装失败 - 12：升级中 - 13：升级失败 - 20：回滚中 - 21：回滚成功 - 22：回滚失败 - 23：删除中 - 24：删除失败 - 25：注销中 - 26：注销失败 - 27：创建超时 - 28：初始化超时 - 29：注册超时 - 30：安装超时 - 31：升级超时 - 32：回滚超时 - 33：删除超时 - 34：注销超时 - 35：启动中 - 36：冻结中 - 37：已冻结 - 38：重启中 - 39：重启失败 - 40：实例异常 - 41：重启超时

        :param instance_status: The instance_status of this RespInstanceBase.
        :type: int
        """
        self._instance_status = instance_status

    @property
    def type(self):
        """Gets the type of this RespInstanceBase.

        实例类型  暂不支持

        :return: The type of this RespInstanceBase.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RespInstanceBase.

        实例类型  暂不支持

        :param type: The type of this RespInstanceBase.
        :type: str
        """
        self._type = type

    @property
    def spec(self):
        """Gets the spec of this RespInstanceBase.

        实例规格： - ROMA_BASIC：基础版实例 - ROMA_PROFESSIONAL：专业版实例 - ROMA_ENTERPRISE：企业版实例 - ROMA_PLATINUM：铂金版实例 [- ROMA_BASIC_IPV6：基础版IPV6实例](tag:hcs) [- ROMA_PROFESSIONAL_IPV6：专业版IPV6实例](tag:hcs) [- ROMA_ENTERPRISE_IPV6：企业版IPV6实例](tag:hcs) [- ROMA_PLATINUM_IPV6：铂金版IPV6实例](tag:hcs)

        :return: The spec of this RespInstanceBase.
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this RespInstanceBase.

        实例规格： - ROMA_BASIC：基础版实例 - ROMA_PROFESSIONAL：专业版实例 - ROMA_ENTERPRISE：企业版实例 - ROMA_PLATINUM：铂金版实例 [- ROMA_BASIC_IPV6：基础版IPV6实例](tag:hcs) [- ROMA_PROFESSIONAL_IPV6：专业版IPV6实例](tag:hcs) [- ROMA_ENTERPRISE_IPV6：企业版IPV6实例](tag:hcs) [- ROMA_PLATINUM_IPV6：铂金版IPV6实例](tag:hcs)

        :param spec: The spec of this RespInstanceBase.
        :type: str
        """
        self._spec = spec

    @property
    def create_time(self):
        """Gets the create_time of this RespInstanceBase.

        实例创建时间。unix时间戳格式。

        :return: The create_time of this RespInstanceBase.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this RespInstanceBase.

        实例创建时间。unix时间戳格式。

        :param create_time: The create_time of this RespInstanceBase.
        :type: int
        """
        self._create_time = create_time

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this RespInstanceBase.

        企业项目ID，企业帐号必填

        :return: The enterprise_project_id of this RespInstanceBase.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this RespInstanceBase.

        企业项目ID，企业帐号必填

        :param enterprise_project_id: The enterprise_project_id of this RespInstanceBase.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def eip_address(self):
        """Gets the eip_address of this RespInstanceBase.

        实例绑定的弹性IP地址

        :return: The eip_address of this RespInstanceBase.
        :rtype: str
        """
        return self._eip_address

    @eip_address.setter
    def eip_address(self, eip_address):
        """Sets the eip_address of this RespInstanceBase.

        实例绑定的弹性IP地址

        :param eip_address: The eip_address of this RespInstanceBase.
        :type: str
        """
        self._eip_address = eip_address

    @property
    def charging_mode(self):
        """Gets the charging_mode of this RespInstanceBase.

        实例计费方式： - 0：按需计费 - 1：包周期计费

        :return: The charging_mode of this RespInstanceBase.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this RespInstanceBase.

        实例计费方式： - 0：按需计费 - 1：包周期计费

        :param charging_mode: The charging_mode of this RespInstanceBase.
        :type: int
        """
        self._charging_mode = charging_mode

    @property
    def cbc_metadata(self):
        """Gets the cbc_metadata of this RespInstanceBase.

        包周期计费订单编号

        :return: The cbc_metadata of this RespInstanceBase.
        :rtype: str
        """
        return self._cbc_metadata

    @cbc_metadata.setter
    def cbc_metadata(self, cbc_metadata):
        """Sets the cbc_metadata of this RespInstanceBase.

        包周期计费订单编号

        :param cbc_metadata: The cbc_metadata of this RespInstanceBase.
        :type: str
        """
        self._cbc_metadata = cbc_metadata

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
        if not isinstance(other, RespInstanceBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
