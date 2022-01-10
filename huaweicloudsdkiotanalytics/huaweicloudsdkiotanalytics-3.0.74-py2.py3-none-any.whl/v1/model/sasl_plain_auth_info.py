# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SaslPlainAuthInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'username': 'str',
        'password': 'str'
    }

    attribute_map = {
        'username': 'username',
        'password': 'password'
    }

    def __init__(self, username=None, password=None):
        """SaslPlainAuthInfo - a model defined in huaweicloud sdk"""
        
        

        self._username = None
        self._password = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if password is not None:
            self.password = password

    @property
    def username(self):
        """Gets the username of this SaslPlainAuthInfo.

        用户名。支持大小写字母、数字、“.”、“-” 、“_”

        :return: The username of this SaslPlainAuthInfo.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SaslPlainAuthInfo.

        用户名。支持大小写字母、数字、“.”、“-” 、“_”

        :param username: The username of this SaslPlainAuthInfo.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """Gets the password of this SaslPlainAuthInfo.

        密码

        :return: The password of this SaslPlainAuthInfo.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SaslPlainAuthInfo.

        密码

        :param password: The password of this SaslPlainAuthInfo.
        :type: str
        """
        self._password = password

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
        if not isinstance(other, SaslPlainAuthInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
