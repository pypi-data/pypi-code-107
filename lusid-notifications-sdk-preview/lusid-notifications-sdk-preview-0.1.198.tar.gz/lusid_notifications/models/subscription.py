# coding: utf-8

"""
    FINBOURNE Notifications API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.198
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid_notifications.configuration import Configuration


class Subscription(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'id': 'ResourceId',
        'display_name': 'str',
        'description': 'str',
        'status': 'str',
        'matching_pattern': 'MatchingPattern',
        'created_at': 'datetime',
        'created_by': 'str',
        'last_modified_at': 'datetime',
        'last_modified_by': 'str'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'displayName',
        'description': 'description',
        'status': 'status',
        'matching_pattern': 'matchingPattern',
        'created_at': 'createdAt',
        'created_by': 'createdBy',
        'last_modified_at': 'lastModifiedAt',
        'last_modified_by': 'lastModifiedBy'
    }

    required_map = {
        'id': 'required',
        'display_name': 'required',
        'description': 'optional',
        'status': 'required',
        'matching_pattern': 'required',
        'created_at': 'required',
        'created_by': 'required',
        'last_modified_at': 'required',
        'last_modified_by': 'required'
    }

    def __init__(self, id=None, display_name=None, description=None, status=None, matching_pattern=None, created_at=None, created_by=None, last_modified_at=None, last_modified_by=None, local_vars_configuration=None):  # noqa: E501
        """Subscription - a model defined in OpenAPI"
        
        :param id:  (required)
        :type id: lusid_notifications.ResourceId
        :param display_name:  The name of the subscription (required)
        :type display_name: str
        :param description:  The summary of the services provided by the subscription
        :type description: str
        :param status:  The current status of the subscription (required)
        :type status: str
        :param matching_pattern:  (required)
        :type matching_pattern: lusid_notifications.MatchingPattern
        :param created_at:  The time at which the subscription was made (required)
        :type created_at: datetime
        :param created_by:  The user who made the subscription (required)
        :type created_by: str
        :param last_modified_at:  The time at which the subscription was last modified (required)
        :type last_modified_at: datetime
        :param last_modified_by:  The user who last modified the subscription (required)
        :type last_modified_by: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._display_name = None
        self._description = None
        self._status = None
        self._matching_pattern = None
        self._created_at = None
        self._created_by = None
        self._last_modified_at = None
        self._last_modified_by = None
        self.discriminator = None

        self.id = id
        self.display_name = display_name
        self.description = description
        self.status = status
        self.matching_pattern = matching_pattern
        self.created_at = created_at
        self.created_by = created_by
        self.last_modified_at = last_modified_at
        self.last_modified_by = last_modified_by

    @property
    def id(self):
        """Gets the id of this Subscription.  # noqa: E501


        :return: The id of this Subscription.  # noqa: E501
        :rtype: lusid_notifications.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Subscription.


        :param id: The id of this Subscription.  # noqa: E501
        :type id: lusid_notifications.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this Subscription.  # noqa: E501

        The name of the subscription  # noqa: E501

        :return: The display_name of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Subscription.

        The name of the subscription  # noqa: E501

        :param display_name: The display_name of this Subscription.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this Subscription.  # noqa: E501

        The summary of the services provided by the subscription  # noqa: E501

        :return: The description of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Subscription.

        The summary of the services provided by the subscription  # noqa: E501

        :param description: The description of this Subscription.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this Subscription.  # noqa: E501

        The current status of the subscription  # noqa: E501

        :return: The status of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Subscription.

        The current status of the subscription  # noqa: E501

        :param status: The status of this Subscription.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def matching_pattern(self):
        """Gets the matching_pattern of this Subscription.  # noqa: E501


        :return: The matching_pattern of this Subscription.  # noqa: E501
        :rtype: lusid_notifications.MatchingPattern
        """
        return self._matching_pattern

    @matching_pattern.setter
    def matching_pattern(self, matching_pattern):
        """Sets the matching_pattern of this Subscription.


        :param matching_pattern: The matching_pattern of this Subscription.  # noqa: E501
        :type matching_pattern: lusid_notifications.MatchingPattern
        """
        if self.local_vars_configuration.client_side_validation and matching_pattern is None:  # noqa: E501
            raise ValueError("Invalid value for `matching_pattern`, must not be `None`")  # noqa: E501

        self._matching_pattern = matching_pattern

    @property
    def created_at(self):
        """Gets the created_at of this Subscription.  # noqa: E501

        The time at which the subscription was made  # noqa: E501

        :return: The created_at of this Subscription.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Subscription.

        The time at which the subscription was made  # noqa: E501

        :param created_at: The created_at of this Subscription.  # noqa: E501
        :type created_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this Subscription.  # noqa: E501

        The user who made the subscription  # noqa: E501

        :return: The created_by of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Subscription.

        The user who made the subscription  # noqa: E501

        :param created_by: The created_by of this Subscription.  # noqa: E501
        :type created_by: str
        """
        if self.local_vars_configuration.client_side_validation and created_by is None:  # noqa: E501
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def last_modified_at(self):
        """Gets the last_modified_at of this Subscription.  # noqa: E501

        The time at which the subscription was last modified  # noqa: E501

        :return: The last_modified_at of this Subscription.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_at

    @last_modified_at.setter
    def last_modified_at(self, last_modified_at):
        """Sets the last_modified_at of this Subscription.

        The time at which the subscription was last modified  # noqa: E501

        :param last_modified_at: The last_modified_at of this Subscription.  # noqa: E501
        :type last_modified_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and last_modified_at is None:  # noqa: E501
            raise ValueError("Invalid value for `last_modified_at`, must not be `None`")  # noqa: E501

        self._last_modified_at = last_modified_at

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this Subscription.  # noqa: E501

        The user who last modified the subscription  # noqa: E501

        :return: The last_modified_by of this Subscription.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this Subscription.

        The user who last modified the subscription  # noqa: E501

        :param last_modified_by: The last_modified_by of this Subscription.  # noqa: E501
        :type last_modified_by: str
        """
        if self.local_vars_configuration.client_side_validation and last_modified_by is None:  # noqa: E501
            raise ValueError("Invalid value for `last_modified_by`, must not be `None`")  # noqa: E501

        self._last_modified_by = last_modified_by

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Subscription):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Subscription):
            return True

        return self.to_dict() != other.to_dict()
