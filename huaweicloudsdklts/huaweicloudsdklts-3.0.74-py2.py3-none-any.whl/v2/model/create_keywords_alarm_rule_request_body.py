# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateKeywordsAlarmRuleRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'keywords_alarm_rule_name': 'str',
        'keywords_alarm_rule_description': 'str',
        'keywords_requests': 'list[KeywordsRequest]',
        'frequency': 'Frequency',
        'keywords_alarm_level': 'str',
        'keywords_alarm_send': 'bool',
        'domain_id': 'str',
        'notification_save_rule': 'NotificationSaveRule',
        'language': 'str'
    }

    attribute_map = {
        'keywords_alarm_rule_name': 'keywords_alarm_rule_name',
        'keywords_alarm_rule_description': 'keywords_alarm_rule_description',
        'keywords_requests': 'keywords_requests',
        'frequency': 'frequency',
        'keywords_alarm_level': 'keywords_alarm_level',
        'keywords_alarm_send': 'keywords_alarm_send',
        'domain_id': 'domain_id',
        'notification_save_rule': 'notification_save_rule',
        'language': 'language'
    }

    def __init__(self, keywords_alarm_rule_name=None, keywords_alarm_rule_description=None, keywords_requests=None, frequency=None, keywords_alarm_level=None, keywords_alarm_send=None, domain_id=None, notification_save_rule=None, language=None):
        """CreateKeywordsAlarmRuleRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._keywords_alarm_rule_name = None
        self._keywords_alarm_rule_description = None
        self._keywords_requests = None
        self._frequency = None
        self._keywords_alarm_level = None
        self._keywords_alarm_send = None
        self._domain_id = None
        self._notification_save_rule = None
        self._language = None
        self.discriminator = None

        self.keywords_alarm_rule_name = keywords_alarm_rule_name
        if keywords_alarm_rule_description is not None:
            self.keywords_alarm_rule_description = keywords_alarm_rule_description
        self.keywords_requests = keywords_requests
        self.frequency = frequency
        self.keywords_alarm_level = keywords_alarm_level
        self.keywords_alarm_send = keywords_alarm_send
        self.domain_id = domain_id
        if notification_save_rule is not None:
            self.notification_save_rule = notification_save_rule
        self.language = language

    @property
    def keywords_alarm_rule_name(self):
        """Gets the keywords_alarm_rule_name of this CreateKeywordsAlarmRuleRequestBody.

        关键词告警名称

        :return: The keywords_alarm_rule_name of this CreateKeywordsAlarmRuleRequestBody.
        :rtype: str
        """
        return self._keywords_alarm_rule_name

    @keywords_alarm_rule_name.setter
    def keywords_alarm_rule_name(self, keywords_alarm_rule_name):
        """Sets the keywords_alarm_rule_name of this CreateKeywordsAlarmRuleRequestBody.

        关键词告警名称

        :param keywords_alarm_rule_name: The keywords_alarm_rule_name of this CreateKeywordsAlarmRuleRequestBody.
        :type: str
        """
        self._keywords_alarm_rule_name = keywords_alarm_rule_name

    @property
    def keywords_alarm_rule_description(self):
        """Gets the keywords_alarm_rule_description of this CreateKeywordsAlarmRuleRequestBody.

        关键词告警信息描述

        :return: The keywords_alarm_rule_description of this CreateKeywordsAlarmRuleRequestBody.
        :rtype: str
        """
        return self._keywords_alarm_rule_description

    @keywords_alarm_rule_description.setter
    def keywords_alarm_rule_description(self, keywords_alarm_rule_description):
        """Sets the keywords_alarm_rule_description of this CreateKeywordsAlarmRuleRequestBody.

        关键词告警信息描述

        :param keywords_alarm_rule_description: The keywords_alarm_rule_description of this CreateKeywordsAlarmRuleRequestBody.
        :type: str
        """
        self._keywords_alarm_rule_description = keywords_alarm_rule_description

    @property
    def keywords_requests(self):
        """Gets the keywords_requests of this CreateKeywordsAlarmRuleRequestBody.

        关键词详细信息

        :return: The keywords_requests of this CreateKeywordsAlarmRuleRequestBody.
        :rtype: list[KeywordsRequest]
        """
        return self._keywords_requests

    @keywords_requests.setter
    def keywords_requests(self, keywords_requests):
        """Sets the keywords_requests of this CreateKeywordsAlarmRuleRequestBody.

        关键词详细信息

        :param keywords_requests: The keywords_requests of this CreateKeywordsAlarmRuleRequestBody.
        :type: list[KeywordsRequest]
        """
        self._keywords_requests = keywords_requests

    @property
    def frequency(self):
        """Gets the frequency of this CreateKeywordsAlarmRuleRequestBody.


        :return: The frequency of this CreateKeywordsAlarmRuleRequestBody.
        :rtype: Frequency
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this CreateKeywordsAlarmRuleRequestBody.


        :param frequency: The frequency of this CreateKeywordsAlarmRuleRequestBody.
        :type: Frequency
        """
        self._frequency = frequency

    @property
    def keywords_alarm_level(self):
        """Gets the keywords_alarm_level of this CreateKeywordsAlarmRuleRequestBody.

        告警级别

        :return: The keywords_alarm_level of this CreateKeywordsAlarmRuleRequestBody.
        :rtype: str
        """
        return self._keywords_alarm_level

    @keywords_alarm_level.setter
    def keywords_alarm_level(self, keywords_alarm_level):
        """Sets the keywords_alarm_level of this CreateKeywordsAlarmRuleRequestBody.

        告警级别

        :param keywords_alarm_level: The keywords_alarm_level of this CreateKeywordsAlarmRuleRequestBody.
        :type: str
        """
        self._keywords_alarm_level = keywords_alarm_level

    @property
    def keywords_alarm_send(self):
        """Gets the keywords_alarm_send of this CreateKeywordsAlarmRuleRequestBody.

        是否发送

        :return: The keywords_alarm_send of this CreateKeywordsAlarmRuleRequestBody.
        :rtype: bool
        """
        return self._keywords_alarm_send

    @keywords_alarm_send.setter
    def keywords_alarm_send(self, keywords_alarm_send):
        """Sets the keywords_alarm_send of this CreateKeywordsAlarmRuleRequestBody.

        是否发送

        :param keywords_alarm_send: The keywords_alarm_send of this CreateKeywordsAlarmRuleRequestBody.
        :type: bool
        """
        self._keywords_alarm_send = keywords_alarm_send

    @property
    def domain_id(self):
        """Gets the domain_id of this CreateKeywordsAlarmRuleRequestBody.

        domainId

        :return: The domain_id of this CreateKeywordsAlarmRuleRequestBody.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this CreateKeywordsAlarmRuleRequestBody.

        domainId

        :param domain_id: The domain_id of this CreateKeywordsAlarmRuleRequestBody.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def notification_save_rule(self):
        """Gets the notification_save_rule of this CreateKeywordsAlarmRuleRequestBody.

        通知主题

        :return: The notification_save_rule of this CreateKeywordsAlarmRuleRequestBody.
        :rtype: NotificationSaveRule
        """
        return self._notification_save_rule

    @notification_save_rule.setter
    def notification_save_rule(self, notification_save_rule):
        """Sets the notification_save_rule of this CreateKeywordsAlarmRuleRequestBody.

        通知主题

        :param notification_save_rule: The notification_save_rule of this CreateKeywordsAlarmRuleRequestBody.
        :type: NotificationSaveRule
        """
        self._notification_save_rule = notification_save_rule

    @property
    def language(self):
        """Gets the language of this CreateKeywordsAlarmRuleRequestBody.

        邮件附加信息是否英文

        :return: The language of this CreateKeywordsAlarmRuleRequestBody.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this CreateKeywordsAlarmRuleRequestBody.

        邮件附加信息是否英文

        :param language: The language of this CreateKeywordsAlarmRuleRequestBody.
        :type: str
        """
        self._language = language

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
        if not isinstance(other, CreateKeywordsAlarmRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
