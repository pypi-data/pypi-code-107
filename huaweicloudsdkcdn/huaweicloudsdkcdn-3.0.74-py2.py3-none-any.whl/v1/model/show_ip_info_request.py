# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIpInfoRequest:


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
        'ips': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'ips': 'ips'
    }

    def __init__(self, enterprise_project_id=None, ips=None):
        """ShowIpInfoRequest - a model defined in huaweicloud sdk"""
        
        

        self._enterprise_project_id = None
        self._ips = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.ips = ips

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowIpInfoRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，不传表示查询默认项目。注意：当使用子账号调用接口时，该参数必传。

        :return: The enterprise_project_id of this ShowIpInfoRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowIpInfoRequest.

        当用户开启企业项目功能时，该参数生效，表示查询资源所属项目，不传表示查询默认项目。注意：当使用子账号调用接口时，该参数必传。

        :param enterprise_project_id: The enterprise_project_id of this ShowIpInfoRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def ips(self):
        """Gets the ips of this ShowIpInfoRequest.

        IP地址列表，以“，”分割，最多20个。

        :return: The ips of this ShowIpInfoRequest.
        :rtype: str
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        """Sets the ips of this ShowIpInfoRequest.

        IP地址列表，以“，”分割，最多20个。

        :param ips: The ips of this ShowIpInfoRequest.
        :type: str
        """
        self._ips = ips

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
        if not isinstance(other, ShowIpInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
