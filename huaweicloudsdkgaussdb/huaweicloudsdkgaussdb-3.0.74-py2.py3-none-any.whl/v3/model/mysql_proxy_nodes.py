# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlProxyNodes:


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
        'status': 'str',
        'name': 'str',
        'role': 'str',
        'az_code': 'str',
        'frozen_flag': 'int'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'name': 'name',
        'role': 'role',
        'az_code': 'az_code',
        'frozen_flag': 'frozen_flag'
    }

    def __init__(self, id=None, status=None, name=None, role=None, az_code=None, frozen_flag=None):
        """MysqlProxyNodes - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._status = None
        self._name = None
        self._role = None
        self._az_code = None
        self._frozen_flag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if role is not None:
            self.role = role
        if az_code is not None:
            self.az_code = az_code
        if frozen_flag is not None:
            self.frozen_flag = frozen_flag

    @property
    def id(self):
        """Gets the id of this MysqlProxyNodes.

        Proxy节点id。

        :return: The id of this MysqlProxyNodes.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MysqlProxyNodes.

        Proxy节点id。

        :param id: The id of this MysqlProxyNodes.
        :type: str
        """
        self._id = id

    @property
    def status(self):
        """Gets the status of this MysqlProxyNodes.

        Proxy节点状态。 取值范围：normal、abnormal、creating和deleted。

        :return: The status of this MysqlProxyNodes.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MysqlProxyNodes.

        Proxy节点状态。 取值范围：normal、abnormal、creating和deleted。

        :param status: The status of this MysqlProxyNodes.
        :type: str
        """
        self._status = status

    @property
    def name(self):
        """Gets the name of this MysqlProxyNodes.

        Proxy节点名称。

        :return: The name of this MysqlProxyNodes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MysqlProxyNodes.

        Proxy节点名称。

        :param name: The name of this MysqlProxyNodes.
        :type: str
        """
        self._name = name

    @property
    def role(self):
        """Gets the role of this MysqlProxyNodes.

        Proxy节点角色：master和slave。

        :return: The role of this MysqlProxyNodes.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this MysqlProxyNodes.

        Proxy节点角色：master和slave。

        :param role: The role of this MysqlProxyNodes.
        :type: str
        """
        self._role = role

    @property
    def az_code(self):
        """Gets the az_code of this MysqlProxyNodes.

        可用区。

        :return: The az_code of this MysqlProxyNodes.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        """Sets the az_code of this MysqlProxyNodes.

        可用区。

        :param az_code: The az_code of this MysqlProxyNodes.
        :type: str
        """
        self._az_code = az_code

    @property
    def frozen_flag(self):
        """Gets the frozen_flag of this MysqlProxyNodes.

        Proxy节点是否被冻结：0-未冻结；1-冻结；2-冻结删除。

        :return: The frozen_flag of this MysqlProxyNodes.
        :rtype: int
        """
        return self._frozen_flag

    @frozen_flag.setter
    def frozen_flag(self, frozen_flag):
        """Sets the frozen_flag of this MysqlProxyNodes.

        Proxy节点是否被冻结：0-未冻结；1-冻结；2-冻结删除。

        :param frozen_flag: The frozen_flag of this MysqlProxyNodes.
        :type: int
        """
        self._frozen_flag = frozen_flag

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
        if not isinstance(other, MysqlProxyNodes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
