# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MixJobReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'mix_param': 'MixParam',
        'publish_param': 'PublishParam',
        'record_param': 'RecordParam'
    }

    attribute_map = {
        'mix_param': 'mix_param',
        'publish_param': 'publish_param',
        'record_param': 'record_param'
    }

    def __init__(self, mix_param=None, publish_param=None, record_param=None):
        """MixJobReq - a model defined in huaweicloud sdk"""
        
        

        self._mix_param = None
        self._publish_param = None
        self._record_param = None
        self.discriminator = None

        self.mix_param = mix_param
        if publish_param is not None:
            self.publish_param = publish_param
        if record_param is not None:
            self.record_param = record_param

    @property
    def mix_param(self):
        """Gets the mix_param of this MixJobReq.


        :return: The mix_param of this MixJobReq.
        :rtype: MixParam
        """
        return self._mix_param

    @mix_param.setter
    def mix_param(self, mix_param):
        """Sets the mix_param of this MixJobReq.


        :param mix_param: The mix_param of this MixJobReq.
        :type: MixParam
        """
        self._mix_param = mix_param

    @property
    def publish_param(self):
        """Gets the publish_param of this MixJobReq.


        :return: The publish_param of this MixJobReq.
        :rtype: PublishParam
        """
        return self._publish_param

    @publish_param.setter
    def publish_param(self, publish_param):
        """Sets the publish_param of this MixJobReq.


        :param publish_param: The publish_param of this MixJobReq.
        :type: PublishParam
        """
        self._publish_param = publish_param

    @property
    def record_param(self):
        """Gets the record_param of this MixJobReq.


        :return: The record_param of this MixJobReq.
        :rtype: RecordParam
        """
        return self._record_param

    @record_param.setter
    def record_param(self, record_param):
        """Sets the record_param of this MixJobReq.


        :param record_param: The record_param of this MixJobReq.
        :type: RecordParam
        """
        self._record_param = record_param

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
        if not isinstance(other, MixJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
