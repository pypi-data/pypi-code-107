# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlSlowLogList:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'count': 'str',
        'time': 'str',
        'lock_time': 'str',
        'rows_sent': 'str',
        'rows_examined': 'str',
        'database': 'str',
        'users': 'str',
        'query_sample': 'str',
        'type': 'str',
        'start_time': 'str',
        'client_ip': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'count': 'count',
        'time': 'time',
        'lock_time': 'lock_time',
        'rows_sent': 'rows_sent',
        'rows_examined': 'rows_examined',
        'database': 'database',
        'users': 'users',
        'query_sample': 'query_sample',
        'type': 'type',
        'start_time': 'start_time',
        'client_ip': 'client_ip'
    }

    def __init__(self, node_id=None, count=None, time=None, lock_time=None, rows_sent=None, rows_examined=None, database=None, users=None, query_sample=None, type=None, start_time=None, client_ip=None):
        """MysqlSlowLogList - a model defined in huaweicloud sdk"""
        
        

        self._node_id = None
        self._count = None
        self._time = None
        self._lock_time = None
        self._rows_sent = None
        self._rows_examined = None
        self._database = None
        self._users = None
        self._query_sample = None
        self._type = None
        self._start_time = None
        self._client_ip = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if count is not None:
            self.count = count
        if time is not None:
            self.time = time
        if lock_time is not None:
            self.lock_time = lock_time
        if rows_sent is not None:
            self.rows_sent = rows_sent
        if rows_examined is not None:
            self.rows_examined = rows_examined
        if database is not None:
            self.database = database
        if users is not None:
            self.users = users
        if query_sample is not None:
            self.query_sample = query_sample
        if type is not None:
            self.type = type
        if start_time is not None:
            self.start_time = start_time
        if client_ip is not None:
            self.client_ip = client_ip

    @property
    def node_id(self):
        """Gets the node_id of this MysqlSlowLogList.

        节点ID。

        :return: The node_id of this MysqlSlowLogList.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this MysqlSlowLogList.

        节点ID。

        :param node_id: The node_id of this MysqlSlowLogList.
        :type: str
        """
        self._node_id = node_id

    @property
    def count(self):
        """Gets the count of this MysqlSlowLogList.

        执行次数。

        :return: The count of this MysqlSlowLogList.
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this MysqlSlowLogList.

        执行次数。

        :param count: The count of this MysqlSlowLogList.
        :type: str
        """
        self._count = count

    @property
    def time(self):
        """Gets the time of this MysqlSlowLogList.

        执行时间。

        :return: The time of this MysqlSlowLogList.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this MysqlSlowLogList.

        执行时间。

        :param time: The time of this MysqlSlowLogList.
        :type: str
        """
        self._time = time

    @property
    def lock_time(self):
        """Gets the lock_time of this MysqlSlowLogList.

        等待锁时间。

        :return: The lock_time of this MysqlSlowLogList.
        :rtype: str
        """
        return self._lock_time

    @lock_time.setter
    def lock_time(self, lock_time):
        """Sets the lock_time of this MysqlSlowLogList.

        等待锁时间。

        :param lock_time: The lock_time of this MysqlSlowLogList.
        :type: str
        """
        self._lock_time = lock_time

    @property
    def rows_sent(self):
        """Gets the rows_sent of this MysqlSlowLogList.

        结果行数量。

        :return: The rows_sent of this MysqlSlowLogList.
        :rtype: str
        """
        return self._rows_sent

    @rows_sent.setter
    def rows_sent(self, rows_sent):
        """Sets the rows_sent of this MysqlSlowLogList.

        结果行数量。

        :param rows_sent: The rows_sent of this MysqlSlowLogList.
        :type: str
        """
        self._rows_sent = rows_sent

    @property
    def rows_examined(self):
        """Gets the rows_examined of this MysqlSlowLogList.

        扫描的行数量。

        :return: The rows_examined of this MysqlSlowLogList.
        :rtype: str
        """
        return self._rows_examined

    @rows_examined.setter
    def rows_examined(self, rows_examined):
        """Sets the rows_examined of this MysqlSlowLogList.

        扫描的行数量。

        :param rows_examined: The rows_examined of this MysqlSlowLogList.
        :type: str
        """
        self._rows_examined = rows_examined

    @property
    def database(self):
        """Gets the database of this MysqlSlowLogList.

        所属数据库。

        :return: The database of this MysqlSlowLogList.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this MysqlSlowLogList.

        所属数据库。

        :param database: The database of this MysqlSlowLogList.
        :type: str
        """
        self._database = database

    @property
    def users(self):
        """Gets the users of this MysqlSlowLogList.

        账号。

        :return: The users of this MysqlSlowLogList.
        :rtype: str
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this MysqlSlowLogList.

        账号。

        :param users: The users of this MysqlSlowLogList.
        :type: str
        """
        self._users = users

    @property
    def query_sample(self):
        """Gets the query_sample of this MysqlSlowLogList.

        执行语法。

        :return: The query_sample of this MysqlSlowLogList.
        :rtype: str
        """
        return self._query_sample

    @query_sample.setter
    def query_sample(self, query_sample):
        """Sets the query_sample of this MysqlSlowLogList.

        执行语法。

        :param query_sample: The query_sample of this MysqlSlowLogList.
        :type: str
        """
        self._query_sample = query_sample

    @property
    def type(self):
        """Gets the type of this MysqlSlowLogList.

        语句类型。

        :return: The type of this MysqlSlowLogList.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MysqlSlowLogList.

        语句类型。

        :param type: The type of this MysqlSlowLogList.
        :type: str
        """
        self._type = type

    @property
    def start_time(self):
        """Gets the start_time of this MysqlSlowLogList.

        发生时间,UTC时间

        :return: The start_time of this MysqlSlowLogList.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this MysqlSlowLogList.

        发生时间,UTC时间

        :param start_time: The start_time of this MysqlSlowLogList.
        :type: str
        """
        self._start_time = start_time

    @property
    def client_ip(self):
        """Gets the client_ip of this MysqlSlowLogList.

        IP地址。

        :return: The client_ip of this MysqlSlowLogList.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this MysqlSlowLogList.

        IP地址。

        :param client_ip: The client_ip of this MysqlSlowLogList.
        :type: str
        """
        self._client_ip = client_ip

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
        if not isinstance(other, MysqlSlowLogList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
