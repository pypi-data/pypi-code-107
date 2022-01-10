# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePrivateBucketAccessRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'domain_id': 'str',
        'body': 'UpdatePrivateBucketAccessBody'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'domain_id': 'domain_id',
        'body': 'body'
    }

    def __init__(self, enterprise_project_id=None, domain_id=None, body=None):
        """UpdatePrivateBucketAccessRequest - a model defined in huaweicloud sdk"""
        
        

        self._enterprise_project_id = None
        self._domain_id = None
        self._body = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.domain_id = domain_id
        if body is not None:
            self.body = body

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this UpdatePrivateBucketAccessRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，不传表示查询默认项目。注意：当使用子账号调用接口时，该参数必传。

        :return: The enterprise_project_id of this UpdatePrivateBucketAccessRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this UpdatePrivateBucketAccessRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，不传表示查询默认项目。注意：当使用子账号调用接口时，该参数必传。

        :param enterprise_project_id: The enterprise_project_id of this UpdatePrivateBucketAccessRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def domain_id(self):
        """Gets the domain_id of this UpdatePrivateBucketAccessRequest.

        加速域名id。获取方法请参见查询加速域名。

        :return: The domain_id of this UpdatePrivateBucketAccessRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this UpdatePrivateBucketAccessRequest.

        加速域名id。获取方法请参见查询加速域名。

        :param domain_id: The domain_id of this UpdatePrivateBucketAccessRequest.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def body(self):
        """Gets the body of this UpdatePrivateBucketAccessRequest.


        :return: The body of this UpdatePrivateBucketAccessRequest.
        :rtype: UpdatePrivateBucketAccessBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdatePrivateBucketAccessRequest.


        :param body: The body of this UpdatePrivateBucketAccessRequest.
        :type: UpdatePrivateBucketAccessBody
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
        if not isinstance(other, UpdatePrivateBucketAccessRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
