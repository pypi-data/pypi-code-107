# coding: utf-8

from __future__ import absolute_import

import datetime
import re
import importlib

import six

from huaweicloudsdkcore.client import Client, ClientBuilder
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkcore.utils import http_utils
from huaweicloudsdkcore.sdk_stream_request import SdkStreamRequest


class IecAsyncClient(Client):
    """
    :param configuration: .Configuration object for this client
    :param pool_threads: The number of threads to use for async requests
        to the API. More threads means more concurrent API requests.
    """

    PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
    NATIVE_TYPES_MAPPING = {
        'int': int,
        'long': int if six.PY3 else long,
        'float': float,
        'str': str,
        'bool': bool,
        'date': datetime.date,
        'datetime': datetime.datetime,
        'object': object,
    }

    def __init__(self):
        super(IecAsyncClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkiec.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls, "GlobalCredentials")

        if clazz.__name__ != "IecClient":
            raise TypeError("client type error, support client type is IecClient")

        return ClientBuilder(clazz, "GlobalCredentials")

    def add_nics_async(self, request):
        """添加网卡

        添加网卡。

        :param AddNicsRequest request
        :return: AddNicsResponse
        """
        return self.add_nics_with_http_info(request)

    def add_nics_with_http_info(self, request):
        """添加网卡

        添加网卡。

        :param AddNicsRequest request
        :return: AddNicsResponse
        """

        all_params = ['instance_id', 'add_nics_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/cloudservers/{instance_id}/nics',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddNicsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_reboot_instance_async(self, request):
        """批量重启边缘实例

        批量重启边缘实例。

        :param BatchRebootInstanceRequest request
        :return: BatchRebootInstanceResponse
        """
        return self.batch_reboot_instance_with_http_info(request)

    def batch_reboot_instance_with_http_info(self, request):
        """批量重启边缘实例

        批量重启边缘实例。

        :param BatchRebootInstanceRequest request
        :return: BatchRebootInstanceResponse
        """

        all_params = ['batch_reboot_instance_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/cloudservers/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchRebootInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_start_instance_async(self, request):
        """批量启动边缘实例

        批量操作启动边缘实例。

        :param BatchStartInstanceRequest request
        :return: BatchStartInstanceResponse
        """
        return self.batch_start_instance_with_http_info(request)

    def batch_start_instance_with_http_info(self, request):
        """批量启动边缘实例

        批量操作启动边缘实例。

        :param BatchStartInstanceRequest request
        :return: BatchStartInstanceResponse
        """

        all_params = ['batch_start_instance_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/cloudservers/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchStartInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def batch_stop_instance_async(self, request):
        """批量关机边缘实例

        批量关闭边缘实例。

        :param BatchStopInstanceRequest request
        :return: BatchStopInstanceResponse
        """
        return self.batch_stop_instance_with_http_info(request)

    def batch_stop_instance_with_http_info(self, request):
        """批量关机边缘实例

        批量关闭边缘实例。

        :param BatchStopInstanceRequest request
        :return: BatchStopInstanceResponse
        """

        all_params = ['batch_stop_instance_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/cloudservers/action',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='BatchStopInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def change_os_async(self, request):
        """切换操作系统

        切换边缘实例操作系统，支持边缘实例创建成功后，保持ip、数据盘不变的情况下重装操作系统。  调用该接口后，系统将卸载系统盘，然后使用新镜像重新创建系统盘，并挂载至实例，实现切换操作系统功能。

        :param ChangeOsRequest request
        :return: ChangeOsResponse
        """
        return self.change_os_with_http_info(request)

    def change_os_with_http_info(self, request):
        """切换操作系统

        切换边缘实例操作系统，支持边缘实例创建成功后，保持ip、数据盘不变的情况下重装操作系统。  调用该接口后，系统将卸载系统盘，然后使用新镜像重新创建系统盘，并挂载至实例，实现切换操作系统功能。

        :param ChangeOsRequest request
        :return: ChangeOsResponse
        """

        all_params = ['instance_id', 'change_os_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/cloudservers/{instance_id}/change-os',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ChangeOsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_deployment_async(self, request):
        """创建部署计划

        为方便您的统一管理，以及跨边缘站点管理资源，IEC基于业务场景角度，定义了边缘业务。 边缘业务即为逻辑层面的一套资源管理集合。这里的资源主要是指计算实例，包含实例规格、镜像、硬盘、网络等方面。通过指定计算实例的数量、调度策略以及区域分布等形成一套管理集合。[了解更多](https://support.huaweicloud.com/usermanual-iec/iec_02_0301.html)  创建一个部署计划并执行，即可创建一个边缘业务。  - 边缘业务下实例分布取决于部署计划的实例分布与调度策略。 - 边缘业务下实例名称、规格、镜像等参数取决于部署计划配置计算实例字段。

        :param CreateDeploymentRequest request
        :return: CreateDeploymentResponse
        """
        return self.create_deployment_with_http_info(request)

    def create_deployment_with_http_info(self, request):
        """创建部署计划

        为方便您的统一管理，以及跨边缘站点管理资源，IEC基于业务场景角度，定义了边缘业务。 边缘业务即为逻辑层面的一套资源管理集合。这里的资源主要是指计算实例，包含实例规格、镜像、硬盘、网络等方面。通过指定计算实例的数量、调度策略以及区域分布等形成一套管理集合。[了解更多](https://support.huaweicloud.com/usermanual-iec/iec_02_0301.html)  创建一个部署计划并执行，即可创建一个边缘业务。  - 边缘业务下实例分布取决于部署计划的实例分布与调度策略。 - 边缘业务下实例名称、规格、镜像等参数取决于部署计划配置计算实例字段。

        :param CreateDeploymentRequest request
        :return: CreateDeploymentResponse
        """

        all_params = ['create_deployment_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/deployments',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateDeploymentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_keypair_async(self, request):
        """创建和导入密钥

        创建SSH密钥，或把公钥导入系统，生成密钥对。  创建SSH密钥成功后，请把响应数据中的私钥内容保存到本地文件，用户使用该私钥登录边缘实例。为保证边缘实例安全，私钥数据只能读取一次，请妥善保管。

        :param CreateKeypairRequest request
        :return: CreateKeypairResponse
        """
        return self.create_keypair_with_http_info(request)

    def create_keypair_with_http_info(self, request):
        """创建和导入密钥

        创建SSH密钥，或把公钥导入系统，生成密钥对。  创建SSH密钥成功后，请把响应数据中的私钥内容保存到本地文件，用户使用该私钥登录边缘实例。为保证边缘实例安全，私钥数据只能读取一次，请妥善保管。

        :param CreateKeypairRequest request
        :return: CreateKeypairResponse
        """

        all_params = ['create_keypair_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/os-keypairs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateKeypairResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_port_async(self, request):
        """创建端口

        创建端口。

        :param CreatePortRequest request
        :return: CreatePortResponse
        """
        return self.create_port_with_http_info(request)

    def create_port_with_http_info(self, request):
        """创建端口

        创建端口。

        :param CreatePortRequest request
        :return: CreatePortResponse
        """

        all_params = ['create_port_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/ports',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePortResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_security_group_async(self, request):
        """创建边缘安全组

        根据用户的请求内容，创建对应的安全组。

        :param CreateSecurityGroupRequest request
        :return: CreateSecurityGroupResponse
        """
        return self.create_security_group_with_http_info(request)

    def create_security_group_with_http_info(self, request):
        """创建边缘安全组

        根据用户的请求内容，创建对应的安全组。

        :param CreateSecurityGroupRequest request
        :return: CreateSecurityGroupResponse
        """

        all_params = ['create_security_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/security-groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_security_group_rule_async(self, request):
        """创建安全组规则

        根据用户的请求内容，创建安全组规则。

        :param CreateSecurityGroupRuleRequest request
        :return: CreateSecurityGroupRuleResponse
        """
        return self.create_security_group_rule_with_http_info(request)

    def create_security_group_rule_with_http_info(self, request):
        """创建安全组规则

        根据用户的请求内容，创建安全组规则。

        :param CreateSecurityGroupRuleRequest request
        :return: CreateSecurityGroupRuleResponse
        """

        all_params = ['create_security_group_rule_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/security-group-rules',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateSecurityGroupRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_vpc_async(self, request):
        """创建虚拟私有云

        根据用户的请求内容，创建虚拟私有云。

        :param CreateVpcRequest request
        :return: CreateVpcResponse
        """
        return self.create_vpc_with_http_info(request)

    def create_vpc_with_http_info(self, request):
        """创建虚拟私有云

        根据用户的请求内容，创建虚拟私有云。

        :param CreateVpcRequest request
        :return: CreateVpcResponse
        """

        all_params = ['create_vpc_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/vpcs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateVpcResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_deployment_async(self, request):
        """删除部署计划

        删除部署计划。

        :param DeleteDeploymentRequest request
        :return: DeleteDeploymentResponse
        """
        return self.delete_deployment_with_http_info(request)

    def delete_deployment_with_http_info(self, request):
        """删除部署计划

        删除部署计划。

        :param DeleteDeploymentRequest request
        :return: DeleteDeploymentResponse
        """

        all_params = ['deployment_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/deployments/{deployment_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteDeploymentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_edge_cloud_async(self, request):
        """删除边缘业务

        删除边缘业务以及其下边缘实例。

        :param DeleteEdgeCloudRequest request
        :return: DeleteEdgeCloudResponse
        """
        return self.delete_edge_cloud_with_http_info(request)

    def delete_edge_cloud_with_http_info(self, request):
        """删除边缘业务

        删除边缘业务以及其下边缘实例。

        :param DeleteEdgeCloudRequest request
        :return: DeleteEdgeCloudResponse
        """

        all_params = ['edgecloud_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edgecloud_id' in local_var_params:
            path_params['edgecloud_id'] = local_var_params['edgecloud_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/edgeclouds/{edgecloud_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteEdgeCloudResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_instances_async(self, request):
        """批量删除边缘实例

        批量删除边缘实例。

        :param DeleteInstancesRequest request
        :return: DeleteInstancesResponse
        """
        return self.delete_instances_with_http_info(request)

    def delete_instances_with_http_info(self, request):
        """批量删除边缘实例

        批量删除边缘实例。

        :param DeleteInstancesRequest request
        :return: DeleteInstancesResponse
        """

        all_params = ['delete_instances_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/cloudservers/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_keypair_async(self, request):
        """删除密钥

        删除密钥。

        :param DeleteKeypairRequest request
        :return: DeleteKeypairResponse
        """
        return self.delete_keypair_with_http_info(request)

    def delete_keypair_with_http_info(self, request):
        """删除密钥

        删除密钥。

        :param DeleteKeypairRequest request
        :return: DeleteKeypairResponse
        """

        all_params = ['keypair_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'keypair_name' in local_var_params:
            path_params['keypair_name'] = local_var_params['keypair_name']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/os-keypairs/{keypair_name}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteKeypairResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_nics_async(self, request):
        """删除网卡

        删除网卡。

        :param DeleteNicsRequest request
        :return: DeleteNicsResponse
        """
        return self.delete_nics_with_http_info(request)

    def delete_nics_with_http_info(self, request):
        """删除网卡

        删除网卡。

        :param DeleteNicsRequest request
        :return: DeleteNicsResponse
        """

        all_params = ['instance_id', 'delete_nics_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'instance_id' in local_var_params:
            path_params['instance_id'] = local_var_params['instance_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/cloudservers/{instance_id}/nics/delete',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteNicsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_port_async(self, request):
        """删除端口

        删除端口。

        :param DeletePortRequest request
        :return: DeletePortResponse
        """
        return self.delete_port_with_http_info(request)

    def delete_port_with_http_info(self, request):
        """删除端口

        删除端口。

        :param DeletePortRequest request
        :return: DeletePortResponse
        """

        all_params = ['port_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/ports/{port_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeletePortResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_security_group_async(self, request):
        """删除安全组

        根据安全组的ID，删除对应的安全组。

        :param DeleteSecurityGroupRequest request
        :return: DeleteSecurityGroupResponse
        """
        return self.delete_security_group_with_http_info(request)

    def delete_security_group_with_http_info(self, request):
        """删除安全组

        根据安全组的ID，删除对应的安全组。

        :param DeleteSecurityGroupRequest request
        :return: DeleteSecurityGroupResponse
        """

        all_params = ['security_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/security-groups/{security_group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_security_group_rule_async(self, request):
        """删除安全组规则

        根据安全组的ID，删除对应的安全组。

        :param DeleteSecurityGroupRuleRequest request
        :return: DeleteSecurityGroupRuleResponse
        """
        return self.delete_security_group_rule_with_http_info(request)

    def delete_security_group_rule_with_http_info(self, request):
        """删除安全组规则

        根据安全组的ID，删除对应的安全组。

        :param DeleteSecurityGroupRuleRequest request
        :return: DeleteSecurityGroupRuleResponse
        """

        all_params = ['security_group_rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'security_group_rule_id' in local_var_params:
            path_params['security_group_rule_id'] = local_var_params['security_group_rule_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/security-group-rules/{security_group_rule_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteSecurityGroupRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_subnet_async(self, request):
        """删除子网

        根据子网的ID，删除子网。

        :param DeleteSubnetRequest request
        :return: DeleteSubnetResponse
        """
        return self.delete_subnet_with_http_info(request)

    def delete_subnet_with_http_info(self, request):
        """删除子网

        根据子网的ID，删除子网。

        :param DeleteSubnetRequest request
        :return: DeleteSubnetResponse
        """

        all_params = ['subnet_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/subnets/{subnet_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteSubnetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_vpc_async(self, request):
        """删除虚拟私有云

        根据虚拟机私有云的ID，删除对应的虚拟私有云。

        :param DeleteVpcRequest request
        :return: DeleteVpcResponse
        """
        return self.delete_vpc_with_http_info(request)

    def delete_vpc_with_http_info(self, request):
        """删除虚拟私有云

        根据虚拟机私有云的ID，删除对应的虚拟私有云。

        :param DeleteVpcRequest request
        :return: DeleteVpcResponse
        """

        all_params = ['vpc_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/vpcs/{vpc_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteVpcResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def execute_deployment_async(self, request):
        """执行部署计划

        执行部署计划，创建一个边缘业务。单租户默认可创建10个边缘业务。

        :param ExecuteDeploymentRequest request
        :return: ExecuteDeploymentResponse
        """
        return self.execute_deployment_with_http_info(request)

    def execute_deployment_with_http_info(self, request):
        """执行部署计划

        执行部署计划，创建一个边缘业务。单租户默认可创建10个边缘业务。

        :param ExecuteDeploymentRequest request
        :return: ExecuteDeploymentResponse
        """

        all_params = ['deployment_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/deployments/{deployment_id}/deploy',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ExecuteDeploymentResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def expand_edgecloud_async(self, request):
        """扩容边缘业务

        执行部署计划，对边缘业务进行扩容操作。

        :param ExpandEdgecloudRequest request
        :return: ExpandEdgecloudResponse
        """
        return self.expand_edgecloud_with_http_info(request)

    def expand_edgecloud_with_http_info(self, request):
        """扩容边缘业务

        执行部署计划，对边缘业务进行扩容操作。

        :param ExpandEdgecloudRequest request
        :return: ExpandEdgecloudResponse
        """

        all_params = ['deployment_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'deployment_id' in local_var_params:
            path_params['deployment_id'] = local_var_params['deployment_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/deployments/{deployment_id}/expand',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ExpandEdgecloudResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_bandwidths_async(self, request):
        """查询带宽列表

        查询带宽列表。

        :param ListBandwidthsRequest request
        :return: ListBandwidthsResponse
        """
        return self.list_bandwidths_with_http_info(request)

    def list_bandwidths_with_http_info(self, request):
        """查询带宽列表

        查询带宽列表。

        :param ListBandwidthsRequest request
        :return: ListBandwidthsResponse
        """

        all_params = ['limit', 'offset', 'site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'site_id' in local_var_params:
            query_params.append(('site_id', local_var_params['site_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/bandwidths',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBandwidthsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_deployments_async(self, request):
        """查询部署计划列表

        查询部署计划列表。

        :param ListDeploymentsRequest request
        :return: ListDeploymentsResponse
        """
        return self.list_deployments_with_http_info(request)

    def list_deployments_with_http_info(self, request):
        """查询部署计划列表

        查询部署计划列表。

        :param ListDeploymentsRequest request
        :return: ListDeploymentsResponse
        """

        all_params = ['offset', 'limit', 'status', 'id', 'edgecloud_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'edgecloud_id' in local_var_params:
            query_params.append(('edgecloud_id', local_var_params['edgecloud_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/deployments',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDeploymentsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_edge_cloud_async(self, request):
        """查询边缘业务列表

        查询边缘业务列表。

        :param ListEdgeCloudRequest request
        :return: ListEdgeCloudResponse
        """
        return self.list_edge_cloud_with_http_info(request)

    def list_edge_cloud_with_http_info(self, request):
        """查询边缘业务列表

        查询边缘业务列表。

        :param ListEdgeCloudRequest request
        :return: ListEdgeCloudResponse
        """

        all_params = ['offset', 'limit', 'name', 'id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/edgeclouds',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListEdgeCloudResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_flavors_async(self, request):
        """查询边缘规格列表

        查询边缘规格列表。

        :param ListFlavorsRequest request
        :return: ListFlavorsResponse
        """
        return self.list_flavors_with_http_info(request)

    def list_flavors_with_http_info(self, request):
        """查询边缘规格列表

        查询边缘规格列表。

        :param ListFlavorsRequest request
        :return: ListFlavorsResponse
        """

        all_params = ['offset', 'limit', 'name', 'area', 'province', 'city', 'operator', 'id', 'site_ids']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'area' in local_var_params:
            query_params.append(('area', local_var_params['area']))
        if 'province' in local_var_params:
            query_params.append(('province', local_var_params['province']))
        if 'city' in local_var_params:
            query_params.append(('city', local_var_params['city']))
        if 'operator' in local_var_params:
            query_params.append(('operator', local_var_params['operator']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'site_ids' in local_var_params:
            query_params.append(('site_ids', local_var_params['site_ids']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/cloudservers/flavors',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListFlavorsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_images_async(self, request):
        """查询镜像列表

        根据不同条件查询镜像列表，例:  -  查询已注册的私有镜像列表: visibility=private - 公共镜像: visibility=public

        :param ListImagesRequest request
        :return: ListImagesResponse
        """
        return self.list_images_with_http_info(request)

    def list_images_with_http_info(self, request):
        """查询镜像列表

        根据不同条件查询镜像列表，例:  -  查询已注册的私有镜像列表: visibility=private - 公共镜像: visibility=public

        :param ListImagesRequest request
        :return: ListImagesResponse
        """

        all_params = ['imagetype', 'protected', 'id', 'visibility', 'status', 'name', 'os_type', 'virtual_env_type', 'isregistered', 'limit', 'offset', 'sort_key', 'sort_dir', 'support_kvm', 'support_kvm_gpu_type', 'support_kvm_ascend_310', 'support_kvm_hi1822_hiovs', 'support_arm', 'support_gpu_t4']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'imagetype' in local_var_params:
            query_params.append(('__imagetype', local_var_params['imagetype']))
        if 'protected' in local_var_params:
            query_params.append(('protected', local_var_params['protected']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'visibility' in local_var_params:
            query_params.append(('visibility', local_var_params['visibility']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'os_type' in local_var_params:
            query_params.append(('__os_type', local_var_params['os_type']))
        if 'virtual_env_type' in local_var_params:
            query_params.append(('virtual_env_type', local_var_params['virtual_env_type']))
        if 'isregistered' in local_var_params:
            query_params.append(('__isregistered', local_var_params['isregistered']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'sort_key' in local_var_params:
            query_params.append(('sort_key', local_var_params['sort_key']))
        if 'sort_dir' in local_var_params:
            query_params.append(('sort_dir', local_var_params['sort_dir']))
        if 'support_kvm' in local_var_params:
            query_params.append(('__support_kvm', local_var_params['support_kvm']))
        if 'support_kvm_gpu_type' in local_var_params:
            query_params.append(('__support_kvm_gpu_type', local_var_params['support_kvm_gpu_type']))
        if 'support_kvm_ascend_310' in local_var_params:
            query_params.append(('__support_kvm_ascend_310', local_var_params['support_kvm_ascend_310']))
        if 'support_kvm_hi1822_hiovs' in local_var_params:
            query_params.append(('__support_kvm_hi1822_hiovs', local_var_params['support_kvm_hi1822_hiovs']))
        if 'support_arm' in local_var_params:
            query_params.append(('__support_arm', local_var_params['support_arm']))
        if 'support_gpu_t4' in local_var_params:
            query_params.append(('__support_gpu_t4', local_var_params['support_gpu_t4']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/images',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListImagesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_instances_async(self, request):
        """查询边缘实例列表

        查询边缘实例列表。

        :param ListInstancesRequest request
        :return: ListInstancesResponse
        """
        return self.list_instances_with_http_info(request)

    def list_instances_with_http_info(self, request):
        """查询边缘实例列表

        查询边缘实例列表。

        :param ListInstancesRequest request
        :return: ListInstancesResponse
        """

        all_params = ['offset', 'limit', 'status', 'name', 'area', 'province', 'city', 'edgecloud_id', 'site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'area' in local_var_params:
            query_params.append(('area', local_var_params['area']))
        if 'province' in local_var_params:
            query_params.append(('province', local_var_params['province']))
        if 'city' in local_var_params:
            query_params.append(('city', local_var_params['city']))
        if 'edgecloud_id' in local_var_params:
            query_params.append(('edgecloud_id', local_var_params['edgecloud_id']))
        if 'site_id' in local_var_params:
            query_params.append(('site_id', local_var_params['site_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/cloudservers',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListInstancesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_keypairs_async(self, request):
        """查询密钥列表

        查询密钥信息列表。

        :param ListKeypairsRequest request
        :return: ListKeypairsResponse
        """
        return self.list_keypairs_with_http_info(request)

    def list_keypairs_with_http_info(self, request):
        """查询密钥列表

        查询密钥信息列表。

        :param ListKeypairsRequest request
        :return: ListKeypairsResponse
        """

        all_params = ['limit', 'offset', 'name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/os-keypairs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListKeypairsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_ports_async(self, request):
        """查询端口列表

        查询端口的列表信息

        :param ListPortsRequest request
        :return: ListPortsResponse
        """
        return self.list_ports_with_http_info(request)

    def list_ports_with_http_info(self, request):
        """查询端口列表

        查询端口的列表信息

        :param ListPortsRequest request
        :return: ListPortsResponse
        """

        all_params = ['limit', 'offset', 'network_id', 'id', 'name', 'admin_state_up', 'fixed_ips', 'mac_address', 'device_id', 'device_owner', 'status', 'security_groups']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'network_id' in local_var_params:
            query_params.append(('network_id', local_var_params['network_id']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'admin_state_up' in local_var_params:
            query_params.append(('admin_state_up', local_var_params['admin_state_up']))
        if 'fixed_ips' in local_var_params:
            query_params.append(('fixed_ips', local_var_params['fixed_ips']))
            collection_formats['fixed_ips'] = 'multi'
        if 'mac_address' in local_var_params:
            query_params.append(('mac_address', local_var_params['mac_address']))
        if 'device_id' in local_var_params:
            query_params.append(('device_id', local_var_params['device_id']))
        if 'device_owner' in local_var_params:
            query_params.append(('device_owner', local_var_params['device_owner']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'security_groups' in local_var_params:
            query_params.append(('security_groups', local_var_params['security_groups']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/ports',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPortsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_quota_async(self, request):
        """查询配额

        查询租户资源配额。

        :param ListQuotaRequest request
        :return: ListQuotaResponse
        """
        return self.list_quota_with_http_info(request)

    def list_quota_with_http_info(self, request):
        """查询配额

        查询租户资源配额。

        :param ListQuotaRequest request
        :return: ListQuotaResponse
        """

        all_params = []
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/edgeclouds/quotas',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListQuotaResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_security_group_rules_async(self, request):
        """查询安全组规则列表

        根据用户的查询条件，获取安全组规则的列表信息。

        :param ListSecurityGroupRulesRequest request
        :return: ListSecurityGroupRulesResponse
        """
        return self.list_security_group_rules_with_http_info(request)

    def list_security_group_rules_with_http_info(self, request):
        """查询安全组规则列表

        根据用户的查询条件，获取安全组规则的列表信息。

        :param ListSecurityGroupRulesRequest request
        :return: ListSecurityGroupRulesResponse
        """

        all_params = ['limit', 'offset', 'security_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'security_group_id' in local_var_params:
            query_params.append(('security_group_id', local_var_params['security_group_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/security-group-rules',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSecurityGroupRulesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_security_groups_async(self, request):
        """查询安全组列表

        根据特定查询条件，获取安全组的列表信息。

        :param ListSecurityGroupsRequest request
        :return: ListSecurityGroupsResponse
        """
        return self.list_security_groups_with_http_info(request)

    def list_security_groups_with_http_info(self, request):
        """查询安全组列表

        根据特定查询条件，获取安全组的列表信息。

        :param ListSecurityGroupsRequest request
        :return: ListSecurityGroupsResponse
        """

        all_params = ['limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/security-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSecurityGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_sites_async(self, request):
        """查询边缘站点列表

        查询边缘站点列表。  - 边缘站点：靠近终端应用的位置，基于一个或多个运营商建立的一个城市级站点。边缘站点提供物理隔离的资源池，提供多元算力、存储和网络的能力。用户可以将业务灵活就近部署在边缘站点上，以降低网络时延和成本。 - 边缘区域：为依据边缘站点的物理位置划分的区域，一个边缘区域包含多个相靠近的边缘站点的集合。IEC当前提供城市级、省级和大区级三个分布层级的边缘区域。

        :param ListSitesRequest request
        :return: ListSitesResponse
        """
        return self.list_sites_with_http_info(request)

    def list_sites_with_http_info(self, request):
        """查询边缘站点列表

        查询边缘站点列表。  - 边缘站点：靠近终端应用的位置，基于一个或多个运营商建立的一个城市级站点。边缘站点提供物理隔离的资源池，提供多元算力、存储和网络的能力。用户可以将业务灵活就近部署在边缘站点上，以降低网络时延和成本。 - 边缘区域：为依据边缘站点的物理位置划分的区域，一个边缘区域包含多个相靠近的边缘站点的集合。IEC当前提供城市级、省级和大区级三个分布层级的边缘区域。

        :param ListSitesRequest request
        :return: ListSitesResponse
        """

        all_params = ['limit', 'offset', 'id', 'area', 'province', 'city', 'flavor', 'volume_type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'area' in local_var_params:
            query_params.append(('area', local_var_params['area']))
        if 'province' in local_var_params:
            query_params.append(('province', local_var_params['province']))
        if 'city' in local_var_params:
            query_params.append(('city', local_var_params['city']))
        if 'flavor' in local_var_params:
            query_params.append(('flavor', local_var_params['flavor']))
        if 'volume_type' in local_var_params:
            query_params.append(('volume_type', local_var_params['volume_type']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/sites',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSitesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_subnets_async(self, request):
        """查询子网列表

        根据查询条件获取子网的列表信息。

        :param ListSubnetsRequest request
        :return: ListSubnetsResponse
        """
        return self.list_subnets_with_http_info(request)

    def list_subnets_with_http_info(self, request):
        """查询子网列表

        根据查询条件获取子网的列表信息。

        :param ListSubnetsRequest request
        :return: ListSubnetsResponse
        """

        all_params = ['vpc_id', 'limit', 'offset', 'site_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'vpc_id' in local_var_params:
            query_params.append(('vpc_id', local_var_params['vpc_id']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'site_id' in local_var_params:
            query_params.append(('site_id', local_var_params['site_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/subnets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListSubnetsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_vpcs_async(self, request):
        """查询虚拟私有云列表

        获取虚拟私有云的列表。

        :param ListVpcsRequest request
        :return: ListVpcsResponse
        """
        return self.list_vpcs_with_http_info(request)

    def list_vpcs_with_http_info(self, request):
        """查询虚拟私有云列表

        获取虚拟私有云的列表。

        :param ListVpcsRequest request
        :return: ListVpcsResponse
        """

        all_params = ['limit', 'offset', 'id', 'name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/vpcs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListVpcsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_bandwidth_async(self, request):
        """查询带宽详情

        查询带宽详情。

        :param ShowBandwidthRequest request
        :return: ShowBandwidthResponse
        """
        return self.show_bandwidth_with_http_info(request)

    def show_bandwidth_with_http_info(self, request):
        """查询带宽详情

        查询带宽详情。

        :param ShowBandwidthRequest request
        :return: ShowBandwidthResponse
        """

        all_params = ['bandwidth_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'bandwidth_id' in local_var_params:
            path_params['bandwidth_id'] = local_var_params['bandwidth_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/bandwidths/{bandwidth_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowBandwidthResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_edge_cloud_async(self, request):
        """查询边缘业务详情

        查询边缘业务详情。

        :param ShowEdgeCloudRequest request
        :return: ShowEdgeCloudResponse
        """
        return self.show_edge_cloud_with_http_info(request)

    def show_edge_cloud_with_http_info(self, request):
        """查询边缘业务详情

        查询边缘业务详情。

        :param ShowEdgeCloudRequest request
        :return: ShowEdgeCloudResponse
        """

        all_params = ['edgecloud_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'edgecloud_id' in local_var_params:
            path_params['edgecloud_id'] = local_var_params['edgecloud_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/edgeclouds/{edgecloud_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowEdgeCloudResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_image_async(self, request):
        """查询镜像详情

        查询镜像详情。

        :param ShowImageRequest request
        :return: ShowImageResponse
        """
        return self.show_image_with_http_info(request)

    def show_image_with_http_info(self, request):
        """查询镜像详情

        查询镜像详情。

        :param ShowImageRequest request
        :return: ShowImageResponse
        """

        all_params = ['image_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'image_id' in local_var_params:
            path_params['image_id'] = local_var_params['image_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/images/{image_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowImageResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_instance_async(self, request):
        """查询边缘实例详情

        查询边缘实例详情。

        :param ShowInstanceRequest request
        :return: ShowInstanceResponse
        """
        return self.show_instance_with_http_info(request)

    def show_instance_with_http_info(self, request):
        """查询边缘实例详情

        查询边缘实例详情。

        :param ShowInstanceRequest request
        :return: ShowInstanceResponse
        """

        all_params = ['server_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/cloudservers/{server_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_keypair_async(self, request):
        """查询密钥详情

        查询密钥信息列表。

        :param ShowKeypairRequest request
        :return: ShowKeypairResponse
        """
        return self.show_keypair_with_http_info(request)

    def show_keypair_with_http_info(self, request):
        """查询密钥详情

        查询密钥信息列表。

        :param ShowKeypairRequest request
        :return: ShowKeypairResponse
        """

        all_params = ['keypair_name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'keypair_name' in local_var_params:
            path_params['keypair_name'] = local_var_params['keypair_name']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/os-keypairs/{keypair_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowKeypairResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_port_async(self, request):
        """查询端口详情

        根据端口的ID，获取端口的详细信息。

        :param ShowPortRequest request
        :return: ShowPortResponse
        """
        return self.show_port_with_http_info(request)

    def show_port_with_http_info(self, request):
        """查询端口详情

        根据端口的ID，获取端口的详细信息。

        :param ShowPortRequest request
        :return: ShowPortResponse
        """

        all_params = ['port_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/ports/{port_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPortResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_security_group_async(self, request):
        """查询安全组详情

        根据安全组的ID，获取特定安全组的详细信息。

        :param ShowSecurityGroupRequest request
        :return: ShowSecurityGroupResponse
        """
        return self.show_security_group_with_http_info(request)

    def show_security_group_with_http_info(self, request):
        """查询安全组详情

        根据安全组的ID，获取特定安全组的详细信息。

        :param ShowSecurityGroupRequest request
        :return: ShowSecurityGroupResponse
        """

        all_params = ['security_group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'security_group_id' in local_var_params:
            path_params['security_group_id'] = local_var_params['security_group_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/security-groups/{security_group_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSecurityGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_security_group_rule_async(self, request):
        """查询安全组规则详情

        根据安全组规则的ID，获取安全组规则的详细信息。

        :param ShowSecurityGroupRuleRequest request
        :return: ShowSecurityGroupRuleResponse
        """
        return self.show_security_group_rule_with_http_info(request)

    def show_security_group_rule_with_http_info(self, request):
        """查询安全组规则详情

        根据安全组规则的ID，获取安全组规则的详细信息。

        :param ShowSecurityGroupRuleRequest request
        :return: ShowSecurityGroupRuleResponse
        """

        all_params = ['security_group_rule_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'security_group_rule_id' in local_var_params:
            path_params['security_group_rule_id'] = local_var_params['security_group_rule_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/security-group-rules/{security_group_rule_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSecurityGroupRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_subnet_async(self, request):
        """查询子网详情

        根据子网的ID，获取子网的详细信息。

        :param ShowSubnetRequest request
        :return: ShowSubnetResponse
        """
        return self.show_subnet_with_http_info(request)

    def show_subnet_with_http_info(self, request):
        """查询子网详情

        根据子网的ID，获取子网的详细信息。

        :param ShowSubnetRequest request
        :return: ShowSubnetResponse
        """

        all_params = ['subnet_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/subnets/{subnet_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowSubnetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_volume_async(self, request):
        """查询硬盘详情

        查询硬盘详情。

        :param ShowVolumeRequest request
        :return: ShowVolumeResponse
        """
        return self.show_volume_with_http_info(request)

    def show_volume_with_http_info(self, request):
        """查询硬盘详情

        查询硬盘详情。

        :param ShowVolumeRequest request
        :return: ShowVolumeResponse
        """

        all_params = ['volume_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'volume_id' in local_var_params:
            path_params['volume_id'] = local_var_params['volume_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/cloudvolumes/{volume_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowVolumeResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_vpc_async(self, request):
        """查询虚拟私有云详情

        根据虚拟私有云ID，获取虚拟私有云的详情。

        :param ShowVpcRequest request
        :return: ShowVpcResponse
        """
        return self.show_vpc_with_http_info(request)

    def show_vpc_with_http_info(self, request):
        """查询虚拟私有云详情

        根据虚拟私有云ID，获取虚拟私有云的详情。

        :param ShowVpcRequest request
        :return: ShowVpcResponse
        """

        all_params = ['vpc_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/vpcs/{vpc_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowVpcResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_instance_async(self, request):
        """修改边缘实例

        修改边缘实例。

        :param UpdateInstanceRequest request
        :return: UpdateInstanceResponse
        """
        return self.update_instance_with_http_info(request)

    def update_instance_with_http_info(self, request):
        """修改边缘实例

        修改边缘实例。

        :param UpdateInstanceRequest request
        :return: UpdateInstanceResponse
        """

        all_params = ['server_id', 'update_instance_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'server_id' in local_var_params:
            path_params['server_id'] = local_var_params['server_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/cloudservers/{server_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateInstanceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_port_async(self, request):
        """更新端口

        更新端口。

        :param UpdatePortRequest request
        :return: UpdatePortResponse
        """
        return self.update_port_with_http_info(request)

    def update_port_with_http_info(self, request):
        """更新端口

        更新端口。

        :param UpdatePortRequest request
        :return: UpdatePortResponse
        """

        all_params = ['port_id', 'update_port_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'port_id' in local_var_params:
            path_params['port_id'] = local_var_params['port_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/ports/{port_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePortResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_subnet_async(self, request):
        """更新子网

        更新子网的基本信息。

        :param UpdateSubnetRequest request
        :return: UpdateSubnetResponse
        """
        return self.update_subnet_with_http_info(request)

    def update_subnet_with_http_info(self, request):
        """更新子网

        更新子网的基本信息。

        :param UpdateSubnetRequest request
        :return: UpdateSubnetResponse
        """

        all_params = ['subnet_id', 'update_subnet_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'subnet_id' in local_var_params:
            path_params['subnet_id'] = local_var_params['subnet_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/subnets/{subnet_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateSubnetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_vpc_async(self, request):
        """更新虚拟私有云

        更新虚拟私有云的信息

        :param UpdateVpcRequest request
        :return: UpdateVpcResponse
        """
        return self.update_vpc_with_http_info(request)

    def update_vpc_with_http_info(self, request):
        """更新虚拟私有云

        更新虚拟私有云的信息

        :param UpdateVpcRequest request
        :return: UpdateVpcResponse
        """

        all_params = ['vpc_id', 'update_vpc_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'vpc_id' in local_var_params:
            path_params['vpc_id'] = local_var_params['vpc_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/vpcs/{vpc_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateVpcResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_firewall_async(self, request):
        """创建网络ACL

        创建网络ACL。

        :param CreateFirewallRequest request
        :return: CreateFirewallResponse
        """
        return self.create_firewall_with_http_info(request)

    def create_firewall_with_http_info(self, request):
        """创建网络ACL

        创建网络ACL。

        :param CreateFirewallRequest request
        :return: CreateFirewallResponse
        """

        all_params = ['create_firewall_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/firewalls',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateFirewallResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_firewall_async(self, request):
        """删除网络ACL

        删除网络ACL。

        :param DeleteFirewallRequest request
        :return: DeleteFirewallResponse
        """
        return self.delete_firewall_with_http_info(request)

    def delete_firewall_with_http_info(self, request):
        """删除网络ACL

        删除网络ACL。

        :param DeleteFirewallRequest request
        :return: DeleteFirewallResponse
        """

        all_params = ['firewall_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'firewall_id' in local_var_params:
            path_params['firewall_id'] = local_var_params['firewall_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/firewalls/{firewall_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteFirewallResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_firewalls_async(self, request):
        """查询网络ACL列表

        查询网络ACL列表。

        :param ListFirewallsRequest request
        :return: ListFirewallsResponse
        """
        return self.list_firewalls_with_http_info(request)

    def list_firewalls_with_http_info(self, request):
        """查询网络ACL列表

        查询网络ACL列表。

        :param ListFirewallsRequest request
        :return: ListFirewallsResponse
        """

        all_params = ['limit', 'offset', 'id', 'name']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'id' in local_var_params:
            query_params.append(('id', local_var_params['id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/firewalls',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListFirewallsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_firewall_async(self, request):
        """查询网络ACL详情

        查询网络ACL详情。

        :param ShowFirewallRequest request
        :return: ShowFirewallResponse
        """
        return self.show_firewall_with_http_info(request)

    def show_firewall_with_http_info(self, request):
        """查询网络ACL详情

        查询网络ACL详情。

        :param ShowFirewallRequest request
        :return: ShowFirewallResponse
        """

        all_params = ['firewall_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'firewall_id' in local_var_params:
            path_params['firewall_id'] = local_var_params['firewall_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/firewalls/{firewall_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowFirewallResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_firewall_async(self, request):
        """更新网络ACL

        更新网络ACL。

        :param UpdateFirewallRequest request
        :return: UpdateFirewallResponse
        """
        return self.update_firewall_with_http_info(request)

    def update_firewall_with_http_info(self, request):
        """更新网络ACL

        更新网络ACL。

        :param UpdateFirewallRequest request
        :return: UpdateFirewallResponse
        """

        all_params = ['firewall_id', 'update_firewall_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'firewall_id' in local_var_params:
            path_params['firewall_id'] = local_var_params['firewall_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/firewalls/{firewall_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateFirewallResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_firewall_rule_async(self, request):
        """更新网络ACL规则

        更新网络ACL规则。

        :param UpdateFirewallRuleRequest request
        :return: UpdateFirewallRuleResponse
        """
        return self.update_firewall_rule_with_http_info(request)

    def update_firewall_rule_with_http_info(self, request):
        """更新网络ACL规则

        更新网络ACL规则。

        :param UpdateFirewallRuleRequest request
        :return: UpdateFirewallRuleResponse
        """

        all_params = ['firewall_id', 'update_firewall_rule_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'firewall_id' in local_var_params:
            path_params['firewall_id'] = local_var_params['firewall_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/firewalls/{firewall_id}/firewall-rules',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateFirewallRuleResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_public_ip_async(self, request):
        """创建弹性公网IP

        根据用户的请求内容，创建弹性公网IP

        :param CreatePublicIpRequest request
        :return: CreatePublicIpResponse
        """
        return self.create_public_ip_with_http_info(request)

    def create_public_ip_with_http_info(self, request):
        """创建弹性公网IP

        根据用户的请求内容，创建弹性公网IP

        :param CreatePublicIpRequest request
        :return: CreatePublicIpResponse
        """

        all_params = ['create_public_ip_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/publicips',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreatePublicIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_public_ip_async(self, request):
        """删除弹性公网IP

        根据弹性公网IP的ID，删除对应的弹性公网IP。

        :param DeletePublicIpRequest request
        :return: DeletePublicIpResponse
        """
        return self.delete_public_ip_with_http_info(request)

    def delete_public_ip_with_http_info(self, request):
        """删除弹性公网IP

        根据弹性公网IP的ID，删除对应的弹性公网IP。

        :param DeletePublicIpRequest request
        :return: DeletePublicIpResponse
        """

        all_params = ['publicip_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/publicips/{publicip_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeletePublicIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_public_ips_async(self, request):
        """查询弹性公网IP列表

        获取弹性公网IP列表信息。

        :param ListPublicIpsRequest request
        :return: ListPublicIpsResponse
        """
        return self.list_public_ips_with_http_info(request)

    def list_public_ips_with_http_info(self, request):
        """查询弹性公网IP列表

        获取弹性公网IP列表信息。

        :param ListPublicIpsRequest request
        :return: ListPublicIpsResponse
        """

        all_params = ['limit', 'offset', 'site_id', 'port_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'site_id' in local_var_params:
            query_params.append(('site_id', local_var_params['site_id']))
        if 'port_id' in local_var_params:
            query_params.append(('port_id', local_var_params['port_id']))

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/publicips',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPublicIpsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_public_ip_async(self, request):
        """查询弹性公网IP

        获取弹性公网IP的详情信息。

        :param ShowPublicIpRequest request
        :return: ShowPublicIpResponse
        """
        return self.show_public_ip_with_http_info(request)

    def show_public_ip_with_http_info(self, request):
        """查询弹性公网IP

        获取弹性公网IP的详情信息。

        :param ShowPublicIpRequest request
        :return: ShowPublicIpResponse
        """

        all_params = ['publicip_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/publicips/{publicip_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPublicIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_public_ip_async(self, request):
        """更新弹性公网IP

        更新弹性公网IP的信息，主要用于解绑和绑定EIP和VIP之间的关系。

        :param UpdatePublicIpRequest request
        :return: UpdatePublicIpResponse
        """
        return self.update_public_ip_with_http_info(request)

    def update_public_ip_with_http_info(self, request):
        """更新弹性公网IP

        更新弹性公网IP的信息，主要用于解绑和绑定EIP和VIP之间的关系。

        :param UpdatePublicIpRequest request
        :return: UpdatePublicIpResponse
        """

        all_params = ['publicip_id', 'update_public_ip_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'publicip_id' in local_var_params:
            path_params['publicip_id'] = local_var_params['publicip_id']

        query_params = []

        header_params = {}

        form_params = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        if isinstance(request, SdkStreamRequest):
            body_params = request.get_file_stream()

        response_headers = []

        header_params['Content-Type'] = http_utils.select_header_content_type(
            ['application/json'])

        auth_settings = []

        return self.call_api(
            resource_path='/v1/publicips/{publicip_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePublicIpResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def call_api(self, resource_path, method, path_params=None, query_params=None, header_params=None, body=None,
                 post_params=None, response_type=None, response_headers=None, auth_settings=None,
                 collection_formats=None, request_type=None):
        """Makes the HTTP request and returns deserialized data.

        :param resource_path: Path to method endpoint.
        :param method: Method to call.
        :param path_params: Path parameters in the url.
        :param query_params: Query parameters in the url.
        :param header_params: Header parameters to be
            placed in the request header.
        :param body: Request body.
        :param post_params dict: Request post form parameters,
            for `application/x-www-form-urlencoded`, `multipart/form-data`.
        :param auth_settings list: Auth Settings names for the request.
        :param response_type: Response data type.
        :param response_headers: Header should be added to response data.
        :param collection_formats: dict of collection formats for path, query,
            header, and post parameters.
        :param request_type: Request data type.
        :return:
            Return the response directly.
        """
        return self.do_http_request(
            method=method,
            resource_path=resource_path,
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body,
            post_params=post_params,
            response_type=response_type,
            response_headers=response_headers,
            collection_formats=collection_formats,
            request_type=request_type,
	    async_request=True)
