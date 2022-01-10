# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimpleAccessoryV2:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'accessory_id': 'str',
        'file_actual_name': 'str'
    }

    attribute_map = {
        'accessory_id': 'accessory_id',
        'file_actual_name': 'file_actual_name'
    }

    def __init__(self, accessory_id=None, file_actual_name=None):
        """SimpleAccessoryV2 - a model defined in huaweicloud sdk"""
        
        

        self._accessory_id = None
        self._file_actual_name = None
        self.discriminator = None

        if accessory_id is not None:
            self.accessory_id = accessory_id
        if file_actual_name is not None:
            self.file_actual_name = file_actual_name

    @property
    def accessory_id(self):
        """Gets the accessory_id of this SimpleAccessoryV2.

        附件id

        :return: The accessory_id of this SimpleAccessoryV2.
        :rtype: str
        """
        return self._accessory_id

    @accessory_id.setter
    def accessory_id(self, accessory_id):
        """Sets the accessory_id of this SimpleAccessoryV2.

        附件id

        :param accessory_id: The accessory_id of this SimpleAccessoryV2.
        :type: str
        """
        self._accessory_id = accessory_id

    @property
    def file_actual_name(self):
        """Gets the file_actual_name of this SimpleAccessoryV2.

        附件实际名称

        :return: The file_actual_name of this SimpleAccessoryV2.
        :rtype: str
        """
        return self._file_actual_name

    @file_actual_name.setter
    def file_actual_name(self, file_actual_name):
        """Sets the file_actual_name of this SimpleAccessoryV2.

        附件实际名称

        :param file_actual_name: The file_actual_name of this SimpleAccessoryV2.
        :type: str
        """
        self._file_actual_name = file_actual_name

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
        if not isinstance(other, SimpleAccessoryV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
