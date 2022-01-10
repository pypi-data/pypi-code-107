# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneUserResult:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'pwd_status': 'bool',
        'domain_id': 'str',
        'last_project_id': 'str',
        'name': 'str',
        'description': 'str',
        'password_expires_at': 'str',
        'links': 'Links',
        'id': 'str',
        'enabled': 'bool',
        'pwd_strength': 'str',
        'extra': 'KeystoneUserResultExtra'
    }

    attribute_map = {
        'pwd_status': 'pwd_status',
        'domain_id': 'domain_id',
        'last_project_id': 'last_project_id',
        'name': 'name',
        'description': 'description',
        'password_expires_at': 'password_expires_at',
        'links': 'links',
        'id': 'id',
        'enabled': 'enabled',
        'pwd_strength': 'pwd_strength',
        'extra': 'extra'
    }

    def __init__(self, pwd_status=None, domain_id=None, last_project_id=None, name=None, description=None, password_expires_at=None, links=None, id=None, enabled=None, pwd_strength=None, extra=None):
        """KeystoneUserResult - a model defined in huaweicloud sdk"""
        
        

        self._pwd_status = None
        self._domain_id = None
        self._last_project_id = None
        self._name = None
        self._description = None
        self._password_expires_at = None
        self._links = None
        self._id = None
        self._enabled = None
        self._pwd_strength = None
        self._extra = None
        self.discriminator = None

        if pwd_status is not None:
            self.pwd_status = pwd_status
        self.domain_id = domain_id
        if last_project_id is not None:
            self.last_project_id = last_project_id
        self.name = name
        if description is not None:
            self.description = description
        self.password_expires_at = password_expires_at
        self.links = links
        self.id = id
        self.enabled = enabled
        if pwd_strength is not None:
            self.pwd_strength = pwd_strength
        if extra is not None:
            self.extra = extra

    @property
    def pwd_status(self):
        """Gets the pwd_status of this KeystoneUserResult.

        IAM用户密码状态。true：需要修改密码，false：正常。

        :return: The pwd_status of this KeystoneUserResult.
        :rtype: bool
        """
        return self._pwd_status

    @pwd_status.setter
    def pwd_status(self, pwd_status):
        """Sets the pwd_status of this KeystoneUserResult.

        IAM用户密码状态。true：需要修改密码，false：正常。

        :param pwd_status: The pwd_status of this KeystoneUserResult.
        :type: bool
        """
        self._pwd_status = pwd_status

    @property
    def domain_id(self):
        """Gets the domain_id of this KeystoneUserResult.

        IAM用户所属账号ID。

        :return: The domain_id of this KeystoneUserResult.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this KeystoneUserResult.

        IAM用户所属账号ID。

        :param domain_id: The domain_id of this KeystoneUserResult.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def last_project_id(self):
        """Gets the last_project_id of this KeystoneUserResult.

        IAM用户退出系统前，在控制台最后访问的项目ID。

        :return: The last_project_id of this KeystoneUserResult.
        :rtype: str
        """
        return self._last_project_id

    @last_project_id.setter
    def last_project_id(self, last_project_id):
        """Sets the last_project_id of this KeystoneUserResult.

        IAM用户退出系统前，在控制台最后访问的项目ID。

        :param last_project_id: The last_project_id of this KeystoneUserResult.
        :type: str
        """
        self._last_project_id = last_project_id

    @property
    def name(self):
        """Gets the name of this KeystoneUserResult.

        IAM用户名。

        :return: The name of this KeystoneUserResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KeystoneUserResult.

        IAM用户名。

        :param name: The name of this KeystoneUserResult.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this KeystoneUserResult.

        IAM用户描述信息。

        :return: The description of this KeystoneUserResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this KeystoneUserResult.

        IAM用户描述信息。

        :param description: The description of this KeystoneUserResult.
        :type: str
        """
        self._description = description

    @property
    def password_expires_at(self):
        """Gets the password_expires_at of this KeystoneUserResult.

        IAM用户密码过期时间（UTC时间），“null”表示密码不过期。

        :return: The password_expires_at of this KeystoneUserResult.
        :rtype: str
        """
        return self._password_expires_at

    @password_expires_at.setter
    def password_expires_at(self, password_expires_at):
        """Sets the password_expires_at of this KeystoneUserResult.

        IAM用户密码过期时间（UTC时间），“null”表示密码不过期。

        :param password_expires_at: The password_expires_at of this KeystoneUserResult.
        :type: str
        """
        self._password_expires_at = password_expires_at

    @property
    def links(self):
        """Gets the links of this KeystoneUserResult.


        :return: The links of this KeystoneUserResult.
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this KeystoneUserResult.


        :param links: The links of this KeystoneUserResult.
        :type: Links
        """
        self._links = links

    @property
    def id(self):
        """Gets the id of this KeystoneUserResult.

        IAM用户ID。

        :return: The id of this KeystoneUserResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this KeystoneUserResult.

        IAM用户ID。

        :param id: The id of this KeystoneUserResult.
        :type: str
        """
        self._id = id

    @property
    def enabled(self):
        """Gets the enabled of this KeystoneUserResult.

        IAM用户是否启用。true表示启用，false表示停用，默认为true。

        :return: The enabled of this KeystoneUserResult.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this KeystoneUserResult.

        IAM用户是否启用。true表示启用，false表示停用，默认为true。

        :param enabled: The enabled of this KeystoneUserResult.
        :type: bool
        """
        self._enabled = enabled

    @property
    def pwd_strength(self):
        """Gets the pwd_strength of this KeystoneUserResult.

        IAM用户的密码强度。high：密码强度高；mid：密码强度中等；low：密码强度低。

        :return: The pwd_strength of this KeystoneUserResult.
        :rtype: str
        """
        return self._pwd_strength

    @pwd_strength.setter
    def pwd_strength(self, pwd_strength):
        """Sets the pwd_strength of this KeystoneUserResult.

        IAM用户的密码强度。high：密码强度高；mid：密码强度中等；low：密码强度低。

        :param pwd_strength: The pwd_strength of this KeystoneUserResult.
        :type: str
        """
        self._pwd_strength = pwd_strength

    @property
    def extra(self):
        """Gets the extra of this KeystoneUserResult.


        :return: The extra of this KeystoneUserResult.
        :rtype: KeystoneUserResultExtra
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this KeystoneUserResult.


        :param extra: The extra of this KeystoneUserResult.
        :type: KeystoneUserResultExtra
        """
        self._extra = extra

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
        if not isinstance(other, KeystoneUserResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
