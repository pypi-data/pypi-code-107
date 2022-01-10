# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDeviceGroupResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'permissions': 'list[str]',
        'parent_id': 'int',
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'app_id': 'str',
        'created_user': 'CreatedUser',
        'last_updated_user': 'LastUpdatedUser',
        'created_datetime': 'str',
        'last_updated_datetime': 'str',
        'app_name': 'str'
    }

    attribute_map = {
        'permissions': 'permissions',
        'parent_id': 'parent_id',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'app_id': 'app_id',
        'created_user': 'created_user',
        'last_updated_user': 'last_updated_user',
        'created_datetime': 'created_datetime',
        'last_updated_datetime': 'last_updated_datetime',
        'app_name': 'app_name'
    }

    def __init__(self, permissions=None, parent_id=None, id=None, name=None, description=None, app_id=None, created_user=None, last_updated_user=None, created_datetime=None, last_updated_datetime=None, app_name=None):
        """CreateDeviceGroupResponse - a model defined in huaweicloud sdk"""
        
        super(CreateDeviceGroupResponse, self).__init__()

        self._permissions = None
        self._parent_id = None
        self._id = None
        self._name = None
        self._description = None
        self._app_id = None
        self._created_user = None
        self._last_updated_user = None
        self._created_datetime = None
        self._last_updated_datetime = None
        self._app_name = None
        self.discriminator = None

        if permissions is not None:
            self.permissions = permissions
        if parent_id is not None:
            self.parent_id = parent_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if app_id is not None:
            self.app_id = app_id
        if created_user is not None:
            self.created_user = created_user
        if last_updated_user is not None:
            self.last_updated_user = last_updated_user
        if created_datetime is not None:
            self.created_datetime = created_datetime
        if last_updated_datetime is not None:
            self.last_updated_datetime = last_updated_datetime
        if app_name is not None:
            self.app_name = app_name

    @property
    def permissions(self):
        """Gets the permissions of this CreateDeviceGroupResponse.

        权限

        :return: The permissions of this CreateDeviceGroupResponse.
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this CreateDeviceGroupResponse.

        权限

        :param permissions: The permissions of this CreateDeviceGroupResponse.
        :type: list[str]
        """
        self._permissions = permissions

    @property
    def parent_id(self):
        """Gets the parent_id of this CreateDeviceGroupResponse.

        父分组ID

        :return: The parent_id of this CreateDeviceGroupResponse.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this CreateDeviceGroupResponse.

        父分组ID

        :param parent_id: The parent_id of this CreateDeviceGroupResponse.
        :type: int
        """
        self._parent_id = parent_id

    @property
    def id(self):
        """Gets the id of this CreateDeviceGroupResponse.

        分组ID

        :return: The id of this CreateDeviceGroupResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateDeviceGroupResponse.

        分组ID

        :param id: The id of this CreateDeviceGroupResponse.
        :type: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateDeviceGroupResponse.

        分组名称，支持中文，英文大小写，数字，下划线和中划线,长度2-64

        :return: The name of this CreateDeviceGroupResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateDeviceGroupResponse.

        分组名称，支持中文，英文大小写，数字，下划线和中划线,长度2-64

        :param name: The name of this CreateDeviceGroupResponse.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateDeviceGroupResponse.

        分组描述，长度0-200

        :return: The description of this CreateDeviceGroupResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDeviceGroupResponse.

        分组描述，长度0-200

        :param description: The description of this CreateDeviceGroupResponse.
        :type: str
        """
        self._description = description

    @property
    def app_id(self):
        """Gets the app_id of this CreateDeviceGroupResponse.

        分组归属应用ID

        :return: The app_id of this CreateDeviceGroupResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this CreateDeviceGroupResponse.

        分组归属应用ID

        :param app_id: The app_id of this CreateDeviceGroupResponse.
        :type: str
        """
        self._app_id = app_id

    @property
    def created_user(self):
        """Gets the created_user of this CreateDeviceGroupResponse.


        :return: The created_user of this CreateDeviceGroupResponse.
        :rtype: CreatedUser
        """
        return self._created_user

    @created_user.setter
    def created_user(self, created_user):
        """Sets the created_user of this CreateDeviceGroupResponse.


        :param created_user: The created_user of this CreateDeviceGroupResponse.
        :type: CreatedUser
        """
        self._created_user = created_user

    @property
    def last_updated_user(self):
        """Gets the last_updated_user of this CreateDeviceGroupResponse.


        :return: The last_updated_user of this CreateDeviceGroupResponse.
        :rtype: LastUpdatedUser
        """
        return self._last_updated_user

    @last_updated_user.setter
    def last_updated_user(self, last_updated_user):
        """Sets the last_updated_user of this CreateDeviceGroupResponse.


        :param last_updated_user: The last_updated_user of this CreateDeviceGroupResponse.
        :type: LastUpdatedUser
        """
        self._last_updated_user = last_updated_user

    @property
    def created_datetime(self):
        """Gets the created_datetime of this CreateDeviceGroupResponse.

        创建时间

        :return: The created_datetime of this CreateDeviceGroupResponse.
        :rtype: str
        """
        return self._created_datetime

    @created_datetime.setter
    def created_datetime(self, created_datetime):
        """Sets the created_datetime of this CreateDeviceGroupResponse.

        创建时间

        :param created_datetime: The created_datetime of this CreateDeviceGroupResponse.
        :type: str
        """
        self._created_datetime = created_datetime

    @property
    def last_updated_datetime(self):
        """Gets the last_updated_datetime of this CreateDeviceGroupResponse.

        最后修改时间

        :return: The last_updated_datetime of this CreateDeviceGroupResponse.
        :rtype: str
        """
        return self._last_updated_datetime

    @last_updated_datetime.setter
    def last_updated_datetime(self, last_updated_datetime):
        """Sets the last_updated_datetime of this CreateDeviceGroupResponse.

        最后修改时间

        :param last_updated_datetime: The last_updated_datetime of this CreateDeviceGroupResponse.
        :type: str
        """
        self._last_updated_datetime = last_updated_datetime

    @property
    def app_name(self):
        """Gets the app_name of this CreateDeviceGroupResponse.

        应用名称

        :return: The app_name of this CreateDeviceGroupResponse.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this CreateDeviceGroupResponse.

        应用名称

        :param app_name: The app_name of this CreateDeviceGroupResponse.
        :type: str
        """
        self._app_name = app_name

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
        if not isinstance(other, CreateDeviceGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
