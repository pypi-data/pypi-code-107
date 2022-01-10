# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteRecordSetResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'zone_id': 'str',
        'zone_name': 'str',
        'type': 'str',
        'ttl': 'int',
        'records': 'list[str]',
        'create_at': 'str',
        'update_at': 'str',
        'status': 'str',
        'default': 'bool',
        'project_id': 'str',
        'links': 'PageLink'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'zone_id': 'zone_id',
        'zone_name': 'zone_name',
        'type': 'type',
        'ttl': 'ttl',
        'records': 'records',
        'create_at': 'create_at',
        'update_at': 'update_at',
        'status': 'status',
        'default': 'default',
        'project_id': 'project_id',
        'links': 'links'
    }

    def __init__(self, id=None, name=None, description=None, zone_id=None, zone_name=None, type=None, ttl=None, records=None, create_at=None, update_at=None, status=None, default=None, project_id=None, links=None):
        """DeleteRecordSetResponse - a model defined in huaweicloud sdk"""
        
        super(DeleteRecordSetResponse, self).__init__()

        self._id = None
        self._name = None
        self._description = None
        self._zone_id = None
        self._zone_name = None
        self._type = None
        self._ttl = None
        self._records = None
        self._create_at = None
        self._update_at = None
        self._status = None
        self._default = None
        self._project_id = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if zone_id is not None:
            self.zone_id = zone_id
        if zone_name is not None:
            self.zone_name = zone_name
        if type is not None:
            self.type = type
        if ttl is not None:
            self.ttl = ttl
        if records is not None:
            self.records = records
        if create_at is not None:
            self.create_at = create_at
        if update_at is not None:
            self.update_at = update_at
        if status is not None:
            self.status = status
        if default is not None:
            self.default = default
        if project_id is not None:
            self.project_id = project_id
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this DeleteRecordSetResponse.

        Record Set的ID。

        :return: The id of this DeleteRecordSetResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeleteRecordSetResponse.

        Record Set的ID。

        :param id: The id of this DeleteRecordSetResponse.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this DeleteRecordSetResponse.

        Record Set的名称。

        :return: The name of this DeleteRecordSetResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeleteRecordSetResponse.

        Record Set的名称。

        :param name: The name of this DeleteRecordSetResponse.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this DeleteRecordSetResponse.

        Record Set的描述信息。

        :return: The description of this DeleteRecordSetResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeleteRecordSetResponse.

        Record Set的描述信息。

        :param description: The description of this DeleteRecordSetResponse.
        :type: str
        """
        self._description = description

    @property
    def zone_id(self):
        """Gets the zone_id of this DeleteRecordSetResponse.

        托管该记录的zone_id。

        :return: The zone_id of this DeleteRecordSetResponse.
        :rtype: str
        """
        return self._zone_id

    @zone_id.setter
    def zone_id(self, zone_id):
        """Sets the zone_id of this DeleteRecordSetResponse.

        托管该记录的zone_id。

        :param zone_id: The zone_id of this DeleteRecordSetResponse.
        :type: str
        """
        self._zone_id = zone_id

    @property
    def zone_name(self):
        """Gets the zone_name of this DeleteRecordSetResponse.

        托管该记录的zone_name。

        :return: The zone_name of this DeleteRecordSetResponse.
        :rtype: str
        """
        return self._zone_name

    @zone_name.setter
    def zone_name(self, zone_name):
        """Sets the zone_name of this DeleteRecordSetResponse.

        托管该记录的zone_name。

        :param zone_name: The zone_name of this DeleteRecordSetResponse.
        :type: str
        """
        self._zone_name = zone_name

    @property
    def type(self):
        """Gets the type of this DeleteRecordSetResponse.

        记录类型。

        :return: The type of this DeleteRecordSetResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeleteRecordSetResponse.

        记录类型。

        :param type: The type of this DeleteRecordSetResponse.
        :type: str
        """
        self._type = type

    @property
    def ttl(self):
        """Gets the ttl of this DeleteRecordSetResponse.

        解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。

        :return: The ttl of this DeleteRecordSetResponse.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """Sets the ttl of this DeleteRecordSetResponse.

        解析记录在本地DNS服务器的缓存时间，缓存时间越长更新生效越慢，以秒为单位。

        :param ttl: The ttl of this DeleteRecordSetResponse.
        :type: int
        """
        self._ttl = ttl

    @property
    def records(self):
        """Gets the records of this DeleteRecordSetResponse.

        域名解析后的值。

        :return: The records of this DeleteRecordSetResponse.
        :rtype: list[str]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this DeleteRecordSetResponse.

        域名解析后的值。

        :param records: The records of this DeleteRecordSetResponse.
        :type: list[str]
        """
        self._records = records

    @property
    def create_at(self):
        """Gets the create_at of this DeleteRecordSetResponse.

        创建时间。

        :return: The create_at of this DeleteRecordSetResponse.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this DeleteRecordSetResponse.

        创建时间。

        :param create_at: The create_at of this DeleteRecordSetResponse.
        :type: str
        """
        self._create_at = create_at

    @property
    def update_at(self):
        """Gets the update_at of this DeleteRecordSetResponse.

        更新时间。

        :return: The update_at of this DeleteRecordSetResponse.
        :rtype: str
        """
        return self._update_at

    @update_at.setter
    def update_at(self, update_at):
        """Sets the update_at of this DeleteRecordSetResponse.

        更新时间。

        :param update_at: The update_at of this DeleteRecordSetResponse.
        :type: str
        """
        self._update_at = update_at

    @property
    def status(self):
        """Gets the status of this DeleteRecordSetResponse.

        资源状态。

        :return: The status of this DeleteRecordSetResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DeleteRecordSetResponse.

        资源状态。

        :param status: The status of this DeleteRecordSetResponse.
        :type: str
        """
        self._status = status

    @property
    def default(self):
        """Gets the default of this DeleteRecordSetResponse.

        标识是否由系统默认生成，系统默认生成的Record Set不能删除。

        :return: The default of this DeleteRecordSetResponse.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this DeleteRecordSetResponse.

        标识是否由系统默认生成，系统默认生成的Record Set不能删除。

        :param default: The default of this DeleteRecordSetResponse.
        :type: bool
        """
        self._default = default

    @property
    def project_id(self):
        """Gets the project_id of this DeleteRecordSetResponse.

        该Record Set所属的项目ID。

        :return: The project_id of this DeleteRecordSetResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this DeleteRecordSetResponse.

        该Record Set所属的项目ID。

        :param project_id: The project_id of this DeleteRecordSetResponse.
        :type: str
        """
        self._project_id = project_id

    @property
    def links(self):
        """Gets the links of this DeleteRecordSetResponse.


        :return: The links of this DeleteRecordSetResponse.
        :rtype: PageLink
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this DeleteRecordSetResponse.


        :param links: The links of this DeleteRecordSetResponse.
        :type: PageLink
        """
        self._links = links

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
        if not isinstance(other, DeleteRecordSetResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
