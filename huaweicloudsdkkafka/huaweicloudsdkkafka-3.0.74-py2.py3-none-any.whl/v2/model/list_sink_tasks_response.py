# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSinkTasksResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'tasks': 'list[ListSinkTasksRespTasks]',
        'total_number': 'int',
        'max_tasks': 'int',
        'quota_tasks': 'int'
    }

    attribute_map = {
        'tasks': 'tasks',
        'total_number': 'total_number',
        'max_tasks': 'max_tasks',
        'quota_tasks': 'quota_tasks'
    }

    def __init__(self, tasks=None, total_number=None, max_tasks=None, quota_tasks=None):
        """ListSinkTasksResponse - a model defined in huaweicloud sdk"""
        
        super(ListSinkTasksResponse, self).__init__()

        self._tasks = None
        self._total_number = None
        self._max_tasks = None
        self._quota_tasks = None
        self.discriminator = None

        if tasks is not None:
            self.tasks = tasks
        if total_number is not None:
            self.total_number = total_number
        if max_tasks is not None:
            self.max_tasks = max_tasks
        if quota_tasks is not None:
            self.quota_tasks = quota_tasks

    @property
    def tasks(self):
        """Gets the tasks of this ListSinkTasksResponse.

        转储任务列表。

        :return: The tasks of this ListSinkTasksResponse.
        :rtype: list[ListSinkTasksRespTasks]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this ListSinkTasksResponse.

        转储任务列表。

        :param tasks: The tasks of this ListSinkTasksResponse.
        :type: list[ListSinkTasksRespTasks]
        """
        self._tasks = tasks

    @property
    def total_number(self):
        """Gets the total_number of this ListSinkTasksResponse.

        转储任务总数。

        :return: The total_number of this ListSinkTasksResponse.
        :rtype: int
        """
        return self._total_number

    @total_number.setter
    def total_number(self, total_number):
        """Sets the total_number of this ListSinkTasksResponse.

        转储任务总数。

        :param total_number: The total_number of this ListSinkTasksResponse.
        :type: int
        """
        self._total_number = total_number

    @property
    def max_tasks(self):
        """Gets the max_tasks of this ListSinkTasksResponse.

        总的支持任务个数。

        :return: The max_tasks of this ListSinkTasksResponse.
        :rtype: int
        """
        return self._max_tasks

    @max_tasks.setter
    def max_tasks(self, max_tasks):
        """Sets the max_tasks of this ListSinkTasksResponse.

        总的支持任务个数。

        :param max_tasks: The max_tasks of this ListSinkTasksResponse.
        :type: int
        """
        self._max_tasks = max_tasks

    @property
    def quota_tasks(self):
        """Gets the quota_tasks of this ListSinkTasksResponse.

        任务总数的配额。

        :return: The quota_tasks of this ListSinkTasksResponse.
        :rtype: int
        """
        return self._quota_tasks

    @quota_tasks.setter
    def quota_tasks(self, quota_tasks):
        """Sets the quota_tasks of this ListSinkTasksResponse.

        任务总数的配额。

        :param quota_tasks: The quota_tasks of this ListSinkTasksResponse.
        :type: int
        """
        self._quota_tasks = quota_tasks

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
        if not isinstance(other, ListSinkTasksResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
