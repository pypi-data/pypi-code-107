# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRecurringSubMeetingRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_authorization_type': 'str',
        'user_uuid': 'str',
        'x_site_id': 'str',
        'conference_id': 'str',
        'body': 'RestScheduleCycleConfDTO'
    }

    attribute_map = {
        'x_authorization_type': 'X-Authorization-Type',
        'user_uuid': 'userUUID',
        'x_site_id': 'X-Site-Id',
        'conference_id': 'conferenceID',
        'body': 'body'
    }

    def __init__(self, x_authorization_type=None, user_uuid=None, x_site_id=None, conference_id=None, body=None):
        """UpdateRecurringSubMeetingRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_authorization_type = None
        self._user_uuid = None
        self._x_site_id = None
        self._conference_id = None
        self._body = None
        self.discriminator = None

        if x_authorization_type is not None:
            self.x_authorization_type = x_authorization_type
        if user_uuid is not None:
            self.user_uuid = user_uuid
        if x_site_id is not None:
            self.x_site_id = x_site_id
        self.conference_id = conference_id
        if body is not None:
            self.body = body

    @property
    def x_authorization_type(self):
        """Gets the x_authorization_type of this UpdateRecurringSubMeetingRequest.

        标识是否为第三方portal过来的请求

        :return: The x_authorization_type of this UpdateRecurringSubMeetingRequest.
        :rtype: str
        """
        return self._x_authorization_type

    @x_authorization_type.setter
    def x_authorization_type(self, x_authorization_type):
        """Sets the x_authorization_type of this UpdateRecurringSubMeetingRequest.

        标识是否为第三方portal过来的请求

        :param x_authorization_type: The x_authorization_type of this UpdateRecurringSubMeetingRequest.
        :type: str
        """
        self._x_authorization_type = x_authorization_type

    @property
    def user_uuid(self):
        """Gets the user_uuid of this UpdateRecurringSubMeetingRequest.

        用户的uuid（已在USG注册过的）

        :return: The user_uuid of this UpdateRecurringSubMeetingRequest.
        :rtype: str
        """
        return self._user_uuid

    @user_uuid.setter
    def user_uuid(self, user_uuid):
        """Sets the user_uuid of this UpdateRecurringSubMeetingRequest.

        用户的uuid（已在USG注册过的）

        :param user_uuid: The user_uuid of this UpdateRecurringSubMeetingRequest.
        :type: str
        """
        self._user_uuid = user_uuid

    @property
    def x_site_id(self):
        """Gets the x_site_id of this UpdateRecurringSubMeetingRequest.

        用于区分到哪个HCSO站点鉴权。

        :return: The x_site_id of this UpdateRecurringSubMeetingRequest.
        :rtype: str
        """
        return self._x_site_id

    @x_site_id.setter
    def x_site_id(self, x_site_id):
        """Sets the x_site_id of this UpdateRecurringSubMeetingRequest.

        用于区分到哪个HCSO站点鉴权。

        :param x_site_id: The x_site_id of this UpdateRecurringSubMeetingRequest.
        :type: str
        """
        self._x_site_id = x_site_id

    @property
    def conference_id(self):
        """Gets the conference_id of this UpdateRecurringSubMeetingRequest.

        会议标识

        :return: The conference_id of this UpdateRecurringSubMeetingRequest.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this UpdateRecurringSubMeetingRequest.

        会议标识

        :param conference_id: The conference_id of this UpdateRecurringSubMeetingRequest.
        :type: str
        """
        self._conference_id = conference_id

    @property
    def body(self):
        """Gets the body of this UpdateRecurringSubMeetingRequest.


        :return: The body of this UpdateRecurringSubMeetingRequest.
        :rtype: RestScheduleCycleConfDTO
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateRecurringSubMeetingRequest.


        :param body: The body of this UpdateRecurringSubMeetingRequest.
        :type: RestScheduleCycleConfDTO
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
        if not isinstance(other, UpdateRecurringSubMeetingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
