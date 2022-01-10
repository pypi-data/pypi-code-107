# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSinkTaskQuotaRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'connector_id': 'str',
        'body': 'UpdateSinkTaskQuotaReq'
    }

    attribute_map = {
        'connector_id': 'connector_id',
        'body': 'body'
    }

    def __init__(self, connector_id=None, body=None):
        """UpdateSinkTaskQuotaRequest - a model defined in huaweicloud sdk"""
        
        

        self._connector_id = None
        self._body = None
        self.discriminator = None

        self.connector_id = connector_id
        if body is not None:
            self.body = body

    @property
    def connector_id(self):
        """Gets the connector_id of this UpdateSinkTaskQuotaRequest.

        实例转储ID。 请参考[实例生命周期][查询实例]接口返回的数据。

        :return: The connector_id of this UpdateSinkTaskQuotaRequest.
        :rtype: str
        """
        return self._connector_id

    @connector_id.setter
    def connector_id(self, connector_id):
        """Sets the connector_id of this UpdateSinkTaskQuotaRequest.

        实例转储ID。 请参考[实例生命周期][查询实例]接口返回的数据。

        :param connector_id: The connector_id of this UpdateSinkTaskQuotaRequest.
        :type: str
        """
        self._connector_id = connector_id

    @property
    def body(self):
        """Gets the body of this UpdateSinkTaskQuotaRequest.


        :return: The body of this UpdateSinkTaskQuotaRequest.
        :rtype: UpdateSinkTaskQuotaReq
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateSinkTaskQuotaRequest.


        :param body: The body of this UpdateSinkTaskQuotaRequest.
        :type: UpdateSinkTaskQuotaReq
        """
        self._body = body

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
        if not isinstance(other, UpdateSinkTaskQuotaRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
