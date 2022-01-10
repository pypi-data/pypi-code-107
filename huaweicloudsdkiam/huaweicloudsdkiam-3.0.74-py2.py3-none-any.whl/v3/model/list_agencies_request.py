# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAgenciesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'trust_domain_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'trust_domain_id': 'trust_domain_id',
        'name': 'name'
    }

    def __init__(self, domain_id=None, trust_domain_id=None, name=None):
        """ListAgenciesRequest - a model defined in huaweicloud sdk"""
        
        

        self._domain_id = None
        self._trust_domain_id = None
        self._name = None
        self.discriminator = None

        self.domain_id = domain_id
        if trust_domain_id is not None:
            self.trust_domain_id = trust_domain_id
        if name is not None:
            self.name = name

    @property
    def domain_id(self):
        """Gets the domain_id of this ListAgenciesRequest.

        委托方账号ID，获取方式请参见：[获取账号ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :return: The domain_id of this ListAgenciesRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ListAgenciesRequest.

        委托方账号ID，获取方式请参见：[获取账号ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :param domain_id: The domain_id of this ListAgenciesRequest.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def trust_domain_id(self):
        """Gets the trust_domain_id of this ListAgenciesRequest.

        被委托方账号ID，获取方式请参见：[获取账号ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :return: The trust_domain_id of this ListAgenciesRequest.
        :rtype: str
        """
        return self._trust_domain_id

    @trust_domain_id.setter
    def trust_domain_id(self, trust_domain_id):
        """Sets the trust_domain_id of this ListAgenciesRequest.

        被委托方账号ID，获取方式请参见：[获取账号ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :param trust_domain_id: The trust_domain_id of this ListAgenciesRequest.
        :type: str
        """
        self._trust_domain_id = trust_domain_id

    @property
    def name(self):
        """Gets the name of this ListAgenciesRequest.

        委托名，获取方式请参见：[获取委托名、委托ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :return: The name of this ListAgenciesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAgenciesRequest.

        委托名，获取方式请参见：[获取委托名、委托ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :param name: The name of this ListAgenciesRequest.
        :type: str
        """
        self._name = name

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
        if not isinstance(other, ListAgenciesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
