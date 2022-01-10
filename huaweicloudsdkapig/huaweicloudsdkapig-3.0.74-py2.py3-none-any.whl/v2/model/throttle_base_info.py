# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ThrottleBaseInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'app_call_limits': 'int',
        'name': 'str',
        'time_unit': 'str',
        'remark': 'str',
        'api_call_limits': 'int',
        'type': 'int',
        'enable_adaptive_control': 'str',
        'user_call_limits': 'int',
        'time_interval': 'int',
        'ip_call_limits': 'int'
    }

    attribute_map = {
        'app_call_limits': 'app_call_limits',
        'name': 'name',
        'time_unit': 'time_unit',
        'remark': 'remark',
        'api_call_limits': 'api_call_limits',
        'type': 'type',
        'enable_adaptive_control': 'enable_adaptive_control',
        'user_call_limits': 'user_call_limits',
        'time_interval': 'time_interval',
        'ip_call_limits': 'ip_call_limits'
    }

    def __init__(self, app_call_limits=None, name=None, time_unit=None, remark=None, api_call_limits=None, type=None, enable_adaptive_control=None, user_call_limits=None, time_interval=None, ip_call_limits=None):
        """ThrottleBaseInfo - a model defined in huaweicloud sdk"""
        
        

        self._app_call_limits = None
        self._name = None
        self._time_unit = None
        self._remark = None
        self._api_call_limits = None
        self._type = None
        self._enable_adaptive_control = None
        self._user_call_limits = None
        self._time_interval = None
        self._ip_call_limits = None
        self.discriminator = None

        if app_call_limits is not None:
            self.app_call_limits = app_call_limits
        self.name = name
        self.time_unit = time_unit
        if remark is not None:
            self.remark = remark
        self.api_call_limits = api_call_limits
        if type is not None:
            self.type = type
        if enable_adaptive_control is not None:
            self.enable_adaptive_control = enable_adaptive_control
        if user_call_limits is not None:
            self.user_call_limits = user_call_limits
        self.time_interval = time_interval
        if ip_call_limits is not None:
            self.ip_call_limits = ip_call_limits

    @property
    def app_call_limits(self):
        """Gets the app_call_limits of this ThrottleBaseInfo.

        APP流量限制是指一个API在时长之内被每个APP访问的次数上限，该数值不超过用户流量限制值。输入的值不超过2147483647。正整数。 

        :return: The app_call_limits of this ThrottleBaseInfo.
        :rtype: int
        """
        return self._app_call_limits

    @app_call_limits.setter
    def app_call_limits(self, app_call_limits):
        """Sets the app_call_limits of this ThrottleBaseInfo.

        APP流量限制是指一个API在时长之内被每个APP访问的次数上限，该数值不超过用户流量限制值。输入的值不超过2147483647。正整数。 

        :param app_call_limits: The app_call_limits of this ThrottleBaseInfo.
        :type: int
        """
        self._app_call_limits = app_call_limits

    @property
    def name(self):
        """Gets the name of this ThrottleBaseInfo.

        流控策略名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3 ~ 64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The name of this ThrottleBaseInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ThrottleBaseInfo.

        流控策略名称。支持汉字，英文，数字，下划线，且只能以英文和汉字开头，3 ~ 64字符。 > 中文字符必须为UTF-8或者unicode编码。

        :param name: The name of this ThrottleBaseInfo.
        :type: str
        """
        self._name = name

    @property
    def time_unit(self):
        """Gets the time_unit of this ThrottleBaseInfo.

        流控的时间单位

        :return: The time_unit of this ThrottleBaseInfo.
        :rtype: str
        """
        return self._time_unit

    @time_unit.setter
    def time_unit(self, time_unit):
        """Sets the time_unit of this ThrottleBaseInfo.

        流控的时间单位

        :param time_unit: The time_unit of this ThrottleBaseInfo.
        :type: str
        """
        self._time_unit = time_unit

    @property
    def remark(self):
        """Gets the remark of this ThrottleBaseInfo.

        流控策略描述字符长度不超过255。 > 中文字符必须为UTF-8或者unicode编码。

        :return: The remark of this ThrottleBaseInfo.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ThrottleBaseInfo.

        流控策略描述字符长度不超过255。 > 中文字符必须为UTF-8或者unicode编码。

        :param remark: The remark of this ThrottleBaseInfo.
        :type: str
        """
        self._remark = remark

    @property
    def api_call_limits(self):
        """Gets the api_call_limits of this ThrottleBaseInfo.

        API流量限制是指时长内一个API能够被访问的次数上限。该值不超过系统默认配额限制，系统默认配额为200tps，用户可根据实际情况修改该系统默认配额。输入的值不超过2147483647。正整数。 

        :return: The api_call_limits of this ThrottleBaseInfo.
        :rtype: int
        """
        return self._api_call_limits

    @api_call_limits.setter
    def api_call_limits(self, api_call_limits):
        """Sets the api_call_limits of this ThrottleBaseInfo.

        API流量限制是指时长内一个API能够被访问的次数上限。该值不超过系统默认配额限制，系统默认配额为200tps，用户可根据实际情况修改该系统默认配额。输入的值不超过2147483647。正整数。 

        :param api_call_limits: The api_call_limits of this ThrottleBaseInfo.
        :type: int
        """
        self._api_call_limits = api_call_limits

    @property
    def type(self):
        """Gets the type of this ThrottleBaseInfo.

        流控策略的类型 - 1：基础，表示绑定到流控策略的单个API流控时间内能够被调用多少次。 - 2：共享，表示绑定到流控策略的所有API流控时间内能够被调用多少次。

        :return: The type of this ThrottleBaseInfo.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ThrottleBaseInfo.

        流控策略的类型 - 1：基础，表示绑定到流控策略的单个API流控时间内能够被调用多少次。 - 2：共享，表示绑定到流控策略的所有API流控时间内能够被调用多少次。

        :param type: The type of this ThrottleBaseInfo.
        :type: int
        """
        self._type = type

    @property
    def enable_adaptive_control(self):
        """Gets the enable_adaptive_control of this ThrottleBaseInfo.

        是否开启动态流控： - TRUE - FALSE  暂不支持

        :return: The enable_adaptive_control of this ThrottleBaseInfo.
        :rtype: str
        """
        return self._enable_adaptive_control

    @enable_adaptive_control.setter
    def enable_adaptive_control(self, enable_adaptive_control):
        """Sets the enable_adaptive_control of this ThrottleBaseInfo.

        是否开启动态流控： - TRUE - FALSE  暂不支持

        :param enable_adaptive_control: The enable_adaptive_control of this ThrottleBaseInfo.
        :type: str
        """
        self._enable_adaptive_control = enable_adaptive_control

    @property
    def user_call_limits(self):
        """Gets the user_call_limits of this ThrottleBaseInfo.

        [用户流量限制是指一个API在时长之内每一个用户能访问的次数上限，该数值不超过API流量限制值。输入的值不超过2147483647。正整数。](tag:hws;hws_hk;hcs;fcs;g42;)[site不支持用户流量限制,输入值为0](tag:Site)

        :return: The user_call_limits of this ThrottleBaseInfo.
        :rtype: int
        """
        return self._user_call_limits

    @user_call_limits.setter
    def user_call_limits(self, user_call_limits):
        """Sets the user_call_limits of this ThrottleBaseInfo.

        [用户流量限制是指一个API在时长之内每一个用户能访问的次数上限，该数值不超过API流量限制值。输入的值不超过2147483647。正整数。](tag:hws;hws_hk;hcs;fcs;g42;)[site不支持用户流量限制,输入值为0](tag:Site)

        :param user_call_limits: The user_call_limits of this ThrottleBaseInfo.
        :type: int
        """
        self._user_call_limits = user_call_limits

    @property
    def time_interval(self):
        """Gets the time_interval of this ThrottleBaseInfo.

        流量控制的时长单位。与“流量限制次数”配合使用，表示单位时间内的API请求次数上限。输入的值不超过2147483647。正整数。

        :return: The time_interval of this ThrottleBaseInfo.
        :rtype: int
        """
        return self._time_interval

    @time_interval.setter
    def time_interval(self, time_interval):
        """Sets the time_interval of this ThrottleBaseInfo.

        流量控制的时长单位。与“流量限制次数”配合使用，表示单位时间内的API请求次数上限。输入的值不超过2147483647。正整数。

        :param time_interval: The time_interval of this ThrottleBaseInfo.
        :type: int
        """
        self._time_interval = time_interval

    @property
    def ip_call_limits(self):
        """Gets the ip_call_limits of this ThrottleBaseInfo.

        源IP流量限制是指一个API在时长之内被每个IP访问的次数上限，该数值不超过API流量限制值。输入的值不超过2147483647。正整数。

        :return: The ip_call_limits of this ThrottleBaseInfo.
        :rtype: int
        """
        return self._ip_call_limits

    @ip_call_limits.setter
    def ip_call_limits(self, ip_call_limits):
        """Sets the ip_call_limits of this ThrottleBaseInfo.

        源IP流量限制是指一个API在时长之内被每个IP访问的次数上限，该数值不超过API流量限制值。输入的值不超过2147483647。正整数。

        :param ip_call_limits: The ip_call_limits of this ThrottleBaseInfo.
        :type: int
        """
        self._ip_call_limits = ip_call_limits

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
        if not isinstance(other, ThrottleBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
