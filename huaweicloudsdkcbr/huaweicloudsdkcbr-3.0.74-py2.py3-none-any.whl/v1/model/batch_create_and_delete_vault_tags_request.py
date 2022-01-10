# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateAndDeleteVaultTagsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'vault_id': 'str',
        'body': 'BulkCreateAndDeleteVaultTagsReq'
    }

    attribute_map = {
        'vault_id': 'vault_id',
        'body': 'body'
    }

    def __init__(self, vault_id=None, body=None):
        """BatchCreateAndDeleteVaultTagsRequest - a model defined in huaweicloud sdk"""
        
        

        self._vault_id = None
        self._body = None
        self.discriminator = None

        self.vault_id = vault_id
        if body is not None:
            self.body = body

    @property
    def vault_id(self):
        """Gets the vault_id of this BatchCreateAndDeleteVaultTagsRequest.

        资源id

        :return: The vault_id of this BatchCreateAndDeleteVaultTagsRequest.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """Sets the vault_id of this BatchCreateAndDeleteVaultTagsRequest.

        资源id

        :param vault_id: The vault_id of this BatchCreateAndDeleteVaultTagsRequest.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def body(self):
        """Gets the body of this BatchCreateAndDeleteVaultTagsRequest.


        :return: The body of this BatchCreateAndDeleteVaultTagsRequest.
        :rtype: BulkCreateAndDeleteVaultTagsReq
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchCreateAndDeleteVaultTagsRequest.


        :param body: The body of this BatchCreateAndDeleteVaultTagsRequest.
        :type: BulkCreateAndDeleteVaultTagsReq
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
        if not isinstance(other, BatchCreateAndDeleteVaultTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
