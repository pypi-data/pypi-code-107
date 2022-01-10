# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServiceDescribeDetailsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'endpoint_service_name': 'str',
        'id': 'str'
    }

    attribute_map = {
        'endpoint_service_name': 'endpoint_service_name',
        'id': 'id'
    }

    def __init__(self, endpoint_service_name=None, id=None):
        """ListServiceDescribeDetailsRequest - a model defined in huaweicloud sdk"""
        
        

        self._endpoint_service_name = None
        self._id = None
        self.discriminator = None

        if endpoint_service_name is not None:
            self.endpoint_service_name = endpoint_service_name
        if id is not None:
            self.id = id

    @property
    def endpoint_service_name(self):
        """Gets the endpoint_service_name of this ListServiceDescribeDetailsRequest.

        终端节点服务的名称。说明：该字段和id字段必须二选一，否则会出现错误。

        :return: The endpoint_service_name of this ListServiceDescribeDetailsRequest.
        :rtype: str
        """
        return self._endpoint_service_name

    @endpoint_service_name.setter
    def endpoint_service_name(self, endpoint_service_name):
        """Sets the endpoint_service_name of this ListServiceDescribeDetailsRequest.

        终端节点服务的名称。说明：该字段和id字段必须二选一，否则会出现错误。

        :param endpoint_service_name: The endpoint_service_name of this ListServiceDescribeDetailsRequest.
        :type: str
        """
        self._endpoint_service_name = endpoint_service_name

    @property
    def id(self):
        """Gets the id of this ListServiceDescribeDetailsRequest.

        终端节点服务的ID，唯一标识。说明：该字段必须和endpoint_service_name字段二选一，否则会出现错误。

        :return: The id of this ListServiceDescribeDetailsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListServiceDescribeDetailsRequest.

        终端节点服务的ID，唯一标识。说明：该字段必须和endpoint_service_name字段二选一，否则会出现错误。

        :param id: The id of this ListServiceDescribeDetailsRequest.
        :type: str
        """
        self._id = id

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
        if not isinstance(other, ListServiceDescribeDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
