# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUsersResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'job_id': 'str',
        'is_global_password': 'str',
        'message': 'str',
        'user_list': 'list[QueryUserDetailResp]',
        'roles_list': 'list[QueryRoleDetailResp]',
        'is_success': 'bool'
    }

    attribute_map = {
        'job_id': 'job_id',
        'is_global_password': 'is_global_password',
        'message': 'message',
        'user_list': 'user_list',
        'roles_list': 'roles_list',
        'is_success': 'is_success'
    }

    def __init__(self, job_id=None, is_global_password=None, message=None, user_list=None, roles_list=None, is_success=None):
        """ListUsersResponse - a model defined in huaweicloud sdk"""
        
        super(ListUsersResponse, self).__init__()

        self._job_id = None
        self._is_global_password = None
        self._message = None
        self._user_list = None
        self._roles_list = None
        self._is_success = None
        self.discriminator = None

        if job_id is not None:
            self.job_id = job_id
        if is_global_password is not None:
            self.is_global_password = is_global_password
        if message is not None:
            self.message = message
        if user_list is not None:
            self.user_list = user_list
        if roles_list is not None:
            self.roles_list = roles_list
        if is_success is not None:
            self.is_success = is_success

    @property
    def job_id(self):
        """Gets the job_id of this ListUsersResponse.

        任务id

        :return: The job_id of this ListUsersResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ListUsersResponse.

        任务id

        :param job_id: The job_id of this ListUsersResponse.
        :type: str
        """
        self._job_id = job_id

    @property
    def is_global_password(self):
        """Gets the is_global_password of this ListUsersResponse.

        是否使用全局密码

        :return: The is_global_password of this ListUsersResponse.
        :rtype: str
        """
        return self._is_global_password

    @is_global_password.setter
    def is_global_password(self, is_global_password):
        """Sets the is_global_password of this ListUsersResponse.

        是否使用全局密码

        :param is_global_password: The is_global_password of this ListUsersResponse.
        :type: str
        """
        self._is_global_password = is_global_password

    @property
    def message(self):
        """Gets the message of this ListUsersResponse.

        错误码

        :return: The message of this ListUsersResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListUsersResponse.

        错误码

        :param message: The message of this ListUsersResponse.
        :type: str
        """
        self._message = message

    @property
    def user_list(self):
        """Gets the user_list of this ListUsersResponse.

        用户列表数据

        :return: The user_list of this ListUsersResponse.
        :rtype: list[QueryUserDetailResp]
        """
        return self._user_list

    @user_list.setter
    def user_list(self, user_list):
        """Sets the user_list of this ListUsersResponse.

        用户列表数据

        :param user_list: The user_list of this ListUsersResponse.
        :type: list[QueryUserDetailResp]
        """
        self._user_list = user_list

    @property
    def roles_list(self):
        """Gets the roles_list of this ListUsersResponse.

        角色列表数据

        :return: The roles_list of this ListUsersResponse.
        :rtype: list[QueryRoleDetailResp]
        """
        return self._roles_list

    @roles_list.setter
    def roles_list(self, roles_list):
        """Sets the roles_list of this ListUsersResponse.

        角色列表数据

        :param roles_list: The roles_list of this ListUsersResponse.
        :type: list[QueryRoleDetailResp]
        """
        self._roles_list = roles_list

    @property
    def is_success(self):
        """Gets the is_success of this ListUsersResponse.

        是否成功

        :return: The is_success of this ListUsersResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ListUsersResponse.

        是否成功

        :param is_success: The is_success of this ListUsersResponse.
        :type: bool
        """
        self._is_success = is_success

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
        if not isinstance(other, ListUsersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
