# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryRoleDetailResp:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'role': 'str',
        'comment': 'str',
        'is_transfer': 'bool',
        'privileges': 'str',
        'inherits_roles': 'list[str]',
        'selected': 'bool'
    }

    attribute_map = {
        'role': 'role',
        'comment': 'comment',
        'is_transfer': 'is_transfer',
        'privileges': 'privileges',
        'inherits_roles': 'inherits_roles',
        'selected': 'selected'
    }

    def __init__(self, role=None, comment=None, is_transfer=None, privileges=None, inherits_roles=None, selected=None):
        """QueryRoleDetailResp - a model defined in huaweicloud sdk"""
        
        

        self._role = None
        self._comment = None
        self._is_transfer = None
        self._privileges = None
        self._inherits_roles = None
        self._selected = None
        self.discriminator = None

        if role is not None:
            self.role = role
        if comment is not None:
            self.comment = comment
        if is_transfer is not None:
            self.is_transfer = is_transfer
        if privileges is not None:
            self.privileges = privileges
        if inherits_roles is not None:
            self.inherits_roles = inherits_roles
        if selected is not None:
            self.selected = selected

    @property
    def role(self):
        """Gets the role of this QueryRoleDetailResp.

        角色。

        :return: The role of this QueryRoleDetailResp.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this QueryRoleDetailResp.

        角色。

        :param role: The role of this QueryRoleDetailResp.
        :type: str
        """
        self._role = role

    @property
    def comment(self):
        """Gets the comment of this QueryRoleDetailResp.

        说明。

        :return: The comment of this QueryRoleDetailResp.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this QueryRoleDetailResp.

        说明。

        :param comment: The comment of this QueryRoleDetailResp.
        :type: str
        """
        self._comment = comment

    @property
    def is_transfer(self):
        """Gets the is_transfer of this QueryRoleDetailResp.

        是否支持迁移。

        :return: The is_transfer of this QueryRoleDetailResp.
        :rtype: bool
        """
        return self._is_transfer

    @is_transfer.setter
    def is_transfer(self, is_transfer):
        """Sets the is_transfer of this QueryRoleDetailResp.

        是否支持迁移。

        :param is_transfer: The is_transfer of this QueryRoleDetailResp.
        :type: bool
        """
        self._is_transfer = is_transfer

    @property
    def privileges(self):
        """Gets the privileges of this QueryRoleDetailResp.

        角色权限。

        :return: The privileges of this QueryRoleDetailResp.
        :rtype: str
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this QueryRoleDetailResp.

        角色权限。

        :param privileges: The privileges of this QueryRoleDetailResp.
        :type: str
        """
        self._privileges = privileges

    @property
    def inherits_roles(self):
        """Gets the inherits_roles of this QueryRoleDetailResp.

        继承的角色。

        :return: The inherits_roles of this QueryRoleDetailResp.
        :rtype: list[str]
        """
        return self._inherits_roles

    @inherits_roles.setter
    def inherits_roles(self, inherits_roles):
        """Sets the inherits_roles of this QueryRoleDetailResp.

        继承的角色。

        :param inherits_roles: The inherits_roles of this QueryRoleDetailResp.
        :type: list[str]
        """
        self._inherits_roles = inherits_roles

    @property
    def selected(self):
        """Gets the selected of this QueryRoleDetailResp.

        是否选择。

        :return: The selected of this QueryRoleDetailResp.
        :rtype: bool
        """
        return self._selected

    @selected.setter
    def selected(self, selected):
        """Sets the selected of this QueryRoleDetailResp.

        是否选择。

        :param selected: The selected of this QueryRoleDetailResp.
        :type: bool
        """
        self._selected = selected

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
        if not isinstance(other, QueryRoleDetailResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
