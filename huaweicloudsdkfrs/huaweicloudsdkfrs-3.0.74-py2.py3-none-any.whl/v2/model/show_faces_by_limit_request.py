# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFacesByLimitRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'face_set_name': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'face_set_name': 'face_set_name',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, face_set_name=None, offset=None, limit=None):
        """ShowFacesByLimitRequest - a model defined in huaweicloud sdk"""
        
        

        self._face_set_name = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.face_set_name = face_set_name
        self.offset = offset
        self.limit = limit

    @property
    def face_set_name(self):
        """Gets the face_set_name of this ShowFacesByLimitRequest.

        人脸库名称。

        :return: The face_set_name of this ShowFacesByLimitRequest.
        :rtype: str
        """
        return self._face_set_name

    @face_set_name.setter
    def face_set_name(self, face_set_name):
        """Sets the face_set_name of this ShowFacesByLimitRequest.

        人脸库名称。

        :param face_set_name: The face_set_name of this ShowFacesByLimitRequest.
        :type: str
        """
        self._face_set_name = face_set_name

    @property
    def offset(self):
        """Gets the offset of this ShowFacesByLimitRequest.

        从第几条数据读起，默认为0。

        :return: The offset of this ShowFacesByLimitRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowFacesByLimitRequest.

        从第几条数据读起，默认为0。

        :param offset: The offset of this ShowFacesByLimitRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowFacesByLimitRequest.

        读取多少条，默认为5。

        :return: The limit of this ShowFacesByLimitRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowFacesByLimitRequest.

        读取多少条，默认为5。

        :param limit: The limit of this ShowFacesByLimitRequest.
        :type: int
        """
        self._limit = limit

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
        if not isinstance(other, ShowFacesByLimitRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
