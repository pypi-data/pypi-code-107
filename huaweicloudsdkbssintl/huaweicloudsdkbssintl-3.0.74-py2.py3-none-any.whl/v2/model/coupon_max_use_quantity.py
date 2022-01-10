# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CouponMaxUseQuantity:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'coupon_type': 'int',
        'coupon_group': 'int',
        'use_quantity_value': 'int'
    }

    attribute_map = {
        'coupon_type': 'coupon_type',
        'coupon_group': 'coupon_group',
        'use_quantity_value': 'use_quantity_value'
    }

    def __init__(self, coupon_type=None, coupon_group=None, use_quantity_value=None):
        """CouponMaxUseQuantity - a model defined in huaweicloud sdk"""
        
        

        self._coupon_type = None
        self._coupon_group = None
        self._use_quantity_value = None
        self.discriminator = None

        if coupon_type is not None:
            self.coupon_type = coupon_type
        if coupon_group is not None:
            self.coupon_group = coupon_group
        if use_quantity_value is not None:
            self.use_quantity_value = use_quantity_value

    @property
    def coupon_type(self):
        """Gets the coupon_type of this CouponMaxUseQuantity.

        |参数名称：优惠券类型| |参数的约束及描述：1：代金券，2：折扣券，3：产品券,4: 现金券|

        :return: The coupon_type of this CouponMaxUseQuantity.
        :rtype: int
        """
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, coupon_type):
        """Sets the coupon_type of this CouponMaxUseQuantity.

        |参数名称：优惠券类型| |参数的约束及描述：1：代金券，2：折扣券，3：产品券,4: 现金券|

        :param coupon_type: The coupon_type of this CouponMaxUseQuantity.
        :type: int
        """
        self._coupon_type = coupon_type

    @property
    def coupon_group(self):
        """Gets the coupon_group of this CouponMaxUseQuantity.

        |参数名称：优惠券分组| |参数的约束及描述：1: 云市场发放的券 3: 华为云券-使用限制-抵扣硬件的券 0: 华为云服务券（排除上述取值之外的券）|

        :return: The coupon_group of this CouponMaxUseQuantity.
        :rtype: int
        """
        return self._coupon_group

    @coupon_group.setter
    def coupon_group(self, coupon_group):
        """Sets the coupon_group of this CouponMaxUseQuantity.

        |参数名称：优惠券分组| |参数的约束及描述：1: 云市场发放的券 3: 华为云券-使用限制-抵扣硬件的券 0: 华为云服务券（排除上述取值之外的券）|

        :param coupon_group: The coupon_group of this CouponMaxUseQuantity.
        :type: int
        """
        self._coupon_group = coupon_group

    @property
    def use_quantity_value(self):
        """Gets the use_quantity_value of this CouponMaxUseQuantity.

        |参数名称：优惠券使用数量value| |参数的约束及描述：优惠券使用数量value。注：专用券使用数量仅指单个订单内，对于合并支付，每个订单都可以使用一张专用券|

        :return: The use_quantity_value of this CouponMaxUseQuantity.
        :rtype: int
        """
        return self._use_quantity_value

    @use_quantity_value.setter
    def use_quantity_value(self, use_quantity_value):
        """Sets the use_quantity_value of this CouponMaxUseQuantity.

        |参数名称：优惠券使用数量value| |参数的约束及描述：优惠券使用数量value。注：专用券使用数量仅指单个订单内，对于合并支付，每个订单都可以使用一张专用券|

        :param use_quantity_value: The use_quantity_value of this CouponMaxUseQuantity.
        :type: int
        """
        self._use_quantity_value = use_quantity_value

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
        if not isinstance(other, CouponMaxUseQuantity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
