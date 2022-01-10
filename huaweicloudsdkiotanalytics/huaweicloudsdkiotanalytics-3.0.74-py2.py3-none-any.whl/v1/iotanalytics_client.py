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


class IoTAnalyticsClient(Client):
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
        super(IoTAnalyticsClient, self).__init__()
        self.model_package = importlib.import_module("huaweicloudsdkiotanalytics.v1.model")
        self.preset_headers = {'User-Agent': 'HuaweiCloud-SDK-Python'}

    @classmethod
    def new_builder(cls, clazz=None):
        if clazz is None:
            return ClientBuilder(cls)

        if clazz.__name__ != "IoTAnalyticsClient":
            raise TypeError("client type error, support client type is IoTAnalyticsClient")

        return ClientBuilder(clazz)

    def create_asset_model(self, request):
        """创建资产模型

        创建资产模型

        :param CreateAssetModelRequest request
        :return: CreateAssetModelResponse
        """
        return self.create_asset_model_with_http_info(request)

    def create_asset_model_with_http_info(self, request):
        """创建资产模型

        创建资产模型

        :param CreateAssetModelRequest request
        :return: CreateAssetModelResponse
        """

        all_params = ['asset_model']
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
            resource_path='/v1/{project_id}/asset-models',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAssetModelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_asset_model(self, request):
        """删除资产模型

        删除资产模型

        :param DeleteAssetModelRequest request
        :return: DeleteAssetModelResponse
        """
        return self.delete_asset_model_with_http_info(request)

    def delete_asset_model_with_http_info(self, request):
        """删除资产模型

        删除资产模型

        :param DeleteAssetModelRequest request
        :return: DeleteAssetModelResponse
        """

        all_params = ['model_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'model_id' in local_var_params:
            path_params['model_id'] = local_var_params['model_id']

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
            resource_path='/v1/{project_id}/asset-models/{model_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAssetModelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_asset_models(self, request):
        """获取资产模型列表

        获取资产模型列表

        :param ListAssetModelsRequest request
        :return: ListAssetModelsResponse
        """
        return self.list_asset_models_with_http_info(request)

    def list_asset_models_with_http_info(self, request):
        """获取资产模型列表

        获取资产模型列表

        :param ListAssetModelsRequest request
        :return: ListAssetModelsResponse
        """

        all_params = ['filter', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
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
            resource_path='/v1/{project_id}/asset-models',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAssetModelsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_asset_model(self, request):
        """获取资产模型详情

        获取资产模型详情

        :param ShowAssetModelRequest request
        :return: ShowAssetModelResponse
        """
        return self.show_asset_model_with_http_info(request)

    def show_asset_model_with_http_info(self, request):
        """获取资产模型详情

        获取资产模型详情

        :param ShowAssetModelRequest request
        :return: ShowAssetModelResponse
        """

        all_params = ['model_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'model_id' in local_var_params:
            path_params['model_id'] = local_var_params['model_id']

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
            resource_path='/v1/{project_id}/asset-models/{model_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAssetModelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_asset_model(self, request):
        """修改资产模型

        修改资产模型

        :param UpdateAssetModelRequest request
        :return: UpdateAssetModelResponse
        """
        return self.update_asset_model_with_http_info(request)

    def update_asset_model_with_http_info(self, request):
        """修改资产模型

        修改资产模型

        :param UpdateAssetModelRequest request
        :return: UpdateAssetModelResponse
        """

        all_params = ['model_id', 'asset_model']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'model_id' in local_var_params:
            path_params['model_id'] = local_var_params['model_id']

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
            resource_path='/v1/{project_id}/asset-models/{model_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateAssetModelResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_asset_new(self, request):
        """创建资产

        创建资产

        :param CreateAssetNewRequest request
        :return: CreateAssetNewResponse
        """
        return self.create_asset_new_with_http_info(request)

    def create_asset_new_with_http_info(self, request):
        """创建资产

        创建资产

        :param CreateAssetNewRequest request
        :return: CreateAssetNewResponse
        """

        all_params = ['asset']
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
            resource_path='/v1/{project_id}/assets',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateAssetNewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_asset_new(self, request):
        """删除资产

        删除资产

        :param DeleteAssetNewRequest request
        :return: DeleteAssetNewResponse
        """
        return self.delete_asset_new_with_http_info(request)

    def delete_asset_new_with_http_info(self, request):
        """删除资产

        删除资产

        :param DeleteAssetNewRequest request
        :return: DeleteAssetNewResponse
        """

        all_params = ['asset_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

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
            resource_path='/v1/{project_id}/assets/{asset_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteAssetNewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_assets_new(self, request):
        """获取资产列表

        获取资产列表

        :param ListAssetsNewRequest request
        :return: ListAssetsNewResponse
        """
        return self.list_assets_new_with_http_info(request)

    def list_assets_new_with_http_info(self, request):
        """获取资产列表

        获取资产列表

        :param ListAssetsNewRequest request
        :return: ListAssetsNewResponse
        """

        all_params = ['type', 'limit', 'offset', 'filter']
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
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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
            resource_path='/v1/{project_id}/assets',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListAssetsNewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def publish_root_asset(self, request):
        """发布资产

        发布资产

        :param PublishRootAssetRequest request
        :return: PublishRootAssetResponse
        """
        return self.publish_root_asset_with_http_info(request)

    def publish_root_asset_with_http_info(self, request):
        """发布资产

        发布资产

        :param PublishRootAssetRequest request
        :return: PublishRootAssetResponse
        """

        all_params = ['root_asset_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'root_asset_id' in local_var_params:
            path_params['root_asset_id'] = local_var_params['root_asset_id']

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
            resource_path='/v1/{project_id}/assets/{root_asset_id}/publish',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='PublishRootAssetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_asset_new(self, request):
        """获取资产详情

        获取资产详情

        :param ShowAssetNewRequest request
        :return: ShowAssetNewResponse
        """
        return self.show_asset_new_with_http_info(request)

    def show_asset_new_with_http_info(self, request):
        """获取资产详情

        获取资产详情

        :param ShowAssetNewRequest request
        :return: ShowAssetNewResponse
        """

        all_params = ['asset_id', 'type']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

        query_params = []
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))

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
            resource_path='/v1/{project_id}/assets/{asset_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAssetNewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_asset_new(self, request):
        """修改资产

        修改资产

        :param UpdateAssetNewRequest request
        :return: UpdateAssetNewResponse
        """
        return self.update_asset_new_with_http_info(request)

    def update_asset_new_with_http_info(self, request):
        """修改资产

        修改资产

        :param UpdateAssetNewRequest request
        :return: UpdateAssetNewResponse
        """

        all_params = ['asset_id', 'asset_info']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

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
            resource_path='/v1/{project_id}/assets/{asset_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateAssetNewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_last_property_value(self, request):
        """获取资产属性最新值

        获取资产属性最新值

        :param ShowLastPropertyValueRequest request
        :return: ShowLastPropertyValueResponse
        """
        return self.show_last_property_value_with_http_info(request)

    def show_last_property_value_with_http_info(self, request):
        """获取资产属性最新值

        获取资产属性最新值

        :param ShowLastPropertyValueRequest request
        :return: ShowLastPropertyValueResponse
        """

        all_params = ['asset_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

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
            resource_path='/v1/{project_id}/assets/{asset_id}/property-values/query-last',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowLastPropertyValueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_metric_value(self, request):
        """获取资产属性聚合值

        获取资产属性聚合值

        :param ShowMetricValueRequest request
        :return: ShowMetricValueResponse
        """
        return self.show_metric_value_with_http_info(request)

    def show_metric_value_with_http_info(self, request):
        """获取资产属性聚合值

        获取资产属性聚合值

        :param ShowMetricValueRequest request
        :return: ShowMetricValueResponse
        """

        all_params = ['asset_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

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
            resource_path='/v1/{project_id}/assets/{asset_id}/metrics/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowMetricValueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_property_raw_value(self, request):
        """获取资产属性历史值

        获取资产属性历史值

        :param ShowPropertyRawValueRequest request
        :return: ShowPropertyRawValueResponse
        """
        return self.show_property_raw_value_with_http_info(request)

    def show_property_raw_value_with_http_info(self, request):
        """获取资产属性历史值

        获取资产属性历史值

        :param ShowPropertyRawValueRequest request
        :return: ShowPropertyRawValueResponse
        """

        all_params = ['asset_id', 'request']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'asset_id' in local_var_params:
            path_params['asset_id'] = local_var_params['asset_id']

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
            resource_path='/v1/{project_id}/assets/{asset_id}/property-values/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPropertyRawValueResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_datasource(self, request):
        """创建数据源

        创建数据源

        :param CreateDatasourceRequest request
        :return: CreateDatasourceResponse
        """
        return self.create_datasource_with_http_info(request)

    def create_datasource_with_http_info(self, request):
        """创建数据源

        创建数据源

        :param CreateDatasourceRequest request
        :return: CreateDatasourceResponse
        """

        all_params = ['create_datasource_request_body']
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
            resource_path='/v1/{project_id}/datasources',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateDatasourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_datasource(self, request):
        """删除数据源

        删除数据源

        :param DeleteDatasourceRequest request
        :return: DeleteDatasourceResponse
        """
        return self.delete_datasource_with_http_info(request)

    def delete_datasource_with_http_info(self, request):
        """删除数据源

        删除数据源

        :param DeleteDatasourceRequest request
        :return: DeleteDatasourceResponse
        """

        all_params = ['datasource_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'datasource_id' in local_var_params:
            path_params['datasource_id'] = local_var_params['datasource_id']

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
            resource_path='/v1/{project_id}/datasources/{datasource_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteDatasourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_all_data_source(self, request):
        """查询数据源列表

        查询数据源列表

        :param ShowAllDataSourceRequest request
        :return: ShowAllDataSourceResponse
        """
        return self.show_all_data_source_with_http_info(request)

    def show_all_data_source_with_http_info(self, request):
        """查询数据源列表

        查询数据源列表

        :param ShowAllDataSourceRequest request
        :return: ShowAllDataSourceResponse
        """

        all_params = ['name', 'type', 'limit', 'offset']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
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
            resource_path='/v1/{project_id}/datasources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowAllDataSourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_data_source(self, request):
        """查询数据源详情

        查询数据源详情

        :param ShowDataSourceRequest request
        :return: ShowDataSourceResponse
        """
        return self.show_data_source_with_http_info(request)

    def show_data_source_with_http_info(self, request):
        """查询数据源详情

        查询数据源详情

        :param ShowDataSourceRequest request
        :return: ShowDataSourceResponse
        """

        all_params = ['datasource_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'datasource_id' in local_var_params:
            path_params['datasource_id'] = local_var_params['datasource_id']

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
            resource_path='/v1/{project_id}/datasources/{datasource_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDataSourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_data_source(self, request):
        """修改数据源

        修改数据源

        :param UpdateDataSourceRequest request
        :return: UpdateDataSourceResponse
        """
        return self.update_data_source_with_http_info(request)

    def update_data_source_with_http_info(self, request):
        """修改数据源

        修改数据源

        :param UpdateDataSourceRequest request
        :return: UpdateDataSourceResponse
        """

        all_params = ['datasource_id', 'update_data_source_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'datasource_id' in local_var_params:
            path_params['datasource_id'] = local_var_params['datasource_id']

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
            resource_path='/v1/{project_id}/datasources/{datasource_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDataSourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_group(self, request):
        """创建存储组

        创建存储组

        :param CreateGroupRequest request
        :return: CreateGroupResponse
        """
        return self.create_group_with_http_info(request)

    def create_group_with_http_info(self, request):
        """创建存储组

        创建存储组

        :param CreateGroupRequest request
        :return: CreateGroupResponse
        """

        all_params = ['create_group_request_body']
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
            resource_path='/v1/{project_id}/data-store-groups',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_group(self, request):
        """删除存储组

        删除存储组

        :param DeleteGroupRequest request
        :return: DeleteGroupResponse
        """
        return self.delete_group_with_http_info(request)

    def delete_group_with_http_info(self, request):
        """删除存储组

        删除存储组

        :param DeleteGroupRequest request
        :return: DeleteGroupResponse
        """

        all_params = ['group_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v1/{project_id}/data-store-groups/{group_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_groups(self, request):
        """查询存储组列表

        查询存储组列表

        :param ListGroupsRequest request
        :return: ListGroupsResponse
        """
        return self.list_groups_with_http_info(request)

    def list_groups_with_http_info(self, request):
        """查询存储组列表

        查询存储组列表

        :param ListGroupsRequest request
        :return: ListGroupsResponse
        """

        all_params = ['unit', 'type', 'group_id', 'name', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'unit' in local_var_params:
            query_params.append(('unit', local_var_params['unit']))
        if 'type' in local_var_params:
            query_params.append(('type', local_var_params['type']))
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v1/{project_id}/data-store-groups',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListGroupsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_group(self, request):
        """更新存储组

        更新存储组

        :param UpdateGroupRequest request
        :return: UpdateGroupResponse
        """
        return self.update_group_with_http_info(request)

    def update_group_with_http_info(self, request):
        """更新存储组

        更新存储组

        :param UpdateGroupRequest request
        :return: UpdateGroupResponse
        """

        all_params = ['group_id', 'update_group_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'group_id' in local_var_params:
            path_params['group_id'] = local_var_params['group_id']

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
            resource_path='/v1/{project_id}/data-store-groups/{group_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateGroupResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_data_store(self, request):
        """删除存储

        删除存储

        :param DeleteDataStoreRequest request
        :return: DeleteDataStoreResponse
        """
        return self.delete_data_store_with_http_info(request)

    def delete_data_store_with_http_info(self, request):
        """删除存储

        删除存储

        :param DeleteDataStoreRequest request
        :return: DeleteDataStoreResponse
        """

        all_params = ['data_store_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'data_store_id' in local_var_params:
            path_params['data_store_id'] = local_var_params['data_store_id']

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
            resource_path='/v1/{project_id}/data-stores/{data_store_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteDataStoreResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_data_stores(self, request):
        """查询存储列表

        查询存储列表

        :param ListDataStoresRequest request
        :return: ListDataStoresResponse
        """
        return self.list_data_stores_with_http_info(request)

    def list_data_stores_with_http_info(self, request):
        """查询存储列表

        查询存储列表

        :param ListDataStoresRequest request
        :return: ListDataStoresResponse
        """

        all_params = ['group_id', 'data_store_id', 'name', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'group_id' in local_var_params:
            query_params.append(('group_id', local_var_params['group_id']))
        if 'data_store_id' in local_var_params:
            query_params.append(('data_store_id', local_var_params['data_store_id']))
        if 'name' in local_var_params:
            query_params.append(('name', local_var_params['name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v1/{project_id}/data-stores',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListDataStoresResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_data_store(self, request):
        """更新存储

        更新存储

        :param UpdateDataStoreRequest request
        :return: UpdateDataStoreResponse
        """
        return self.update_data_store_with_http_info(request)

    def update_data_store_with_http_info(self, request):
        """更新存储

        更新存储

        :param UpdateDataStoreRequest request
        :return: UpdateDataStoreResponse
        """

        all_params = ['data_store_id', 'update_data_store_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'data_store_id' in local_var_params:
            path_params['data_store_id'] = local_var_params['data_store_id']

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
            resource_path='/v1/{project_id}/data-stores/{data_store_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateDataStoreResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_history(self, request):
        """根据标签查询设备历史值

        根据标签查询设备历史值

        :param ListHistoryRequest request
        :return: ListHistoryResponse
        """
        return self.list_history_with_http_info(request)

    def list_history_with_http_info(self, request):
        """根据标签查询设备历史值

        根据标签查询设备历史值

        :param ListHistoryRequest request
        :return: ListHistoryResponse
        """

        all_params = ['data_store_id', 'list_history_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'data_store_id' in local_var_params:
            path_params['data_store_id'] = local_var_params['data_store_id']

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
            resource_path='/v1/{project_id}/data-stores/{data_store_id}/property-values/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListHistoryResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_metrics(self, request):
        """根据标签聚合、查询指标数据

        根据标签聚合、查询数据

        :param ListMetricsRequest request
        :return: ListMetricsResponse
        """
        return self.list_metrics_with_http_info(request)

    def list_metrics_with_http_info(self, request):
        """根据标签聚合、查询指标数据

        根据标签聚合、查询数据

        :param ListMetricsRequest request
        :return: ListMetricsResponse
        """

        all_params = ['data_store_id', 'list_metrics_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'data_store_id' in local_var_params:
            path_params['data_store_id'] = local_var_params['data_store_id']

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
            resource_path='/v1/{project_id}/data-stores/{data_store_id}/metrics/query',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListMetricsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_property_values(self, request):
        """查询设备属性最新状态值

        查询设备属性最新状态值

        :param ShowPropertyValuesRequest request
        :return: ShowPropertyValuesResponse
        """
        return self.show_property_values_with_http_info(request)

    def show_property_values_with_http_info(self, request):
        """查询设备属性最新状态值

        查询设备属性最新状态值

        :param ShowPropertyValuesRequest request
        :return: ShowPropertyValuesResponse
        """

        all_params = ['data_store_id', 'show_property_values_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'data_store_id' in local_var_params:
            path_params['data_store_id'] = local_var_params['data_store_id']

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
            resource_path='/v1/{project_id}/data-stores/{data_store_id}/property-values/query-last',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPropertyValuesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_tag_values(self, request):
        """查询标签的值列表

        查询标签的值列表

        :param ListTagValuesRequest request
        :return: ListTagValuesResponse
        """
        return self.list_tag_values_with_http_info(request)

    def list_tag_values_with_http_info(self, request):
        """查询标签的值列表

        查询标签的值列表

        :param ListTagValuesRequest request
        :return: ListTagValuesResponse
        """

        all_params = ['data_store_id', 'tag_name', 'filters', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'data_store_id' in local_var_params:
            path_params['data_store_id'] = local_var_params['data_store_id']
        if 'tag_name' in local_var_params:
            path_params['tag_name'] = local_var_params['tag_name']

        query_params = []
        if 'filters' in local_var_params:
            query_params.append(('filters', local_var_params['filters']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v1/{project_id}/data-stores/{data_store_id}/tags/{tag_name}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTagValuesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_dev_data(self, request):
        """通过API数据源上报设备数据

        通过API数据源上报设备数据

        :param AddDevDataRequest request
        :return: AddDevDataResponse
        """
        return self.add_dev_data_with_http_info(request)

    def add_dev_data_with_http_info(self, request):
        """通过API数据源上报设备数据

        通过API数据源上报设备数据

        :param AddDevDataRequest request
        :return: AddDevDataResponse
        """

        all_params = ['datasource_id', 'add_dev_data_request_body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'datasource_id' in local_var_params:
            path_params['datasource_id'] = local_var_params['datasource_id']

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
            resource_path='/v1/{project_id}/datasources/{datasource_id}/dev-data',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddDevDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def add_pipeline_job(self, request):
        """新建管道作业

        新建管道作业时，需要在URL中指定是更新哪一个作业，将在body中附带完整的作业信息。（作业中各算子的详细配置请参考算子配置章节。） check参数表示是否需要对作业配置进行检查，若为false，则不检查，将作业保存为草稿；若为true，则对作业配置进行检查。当检查不通过时，将作业状态修改为草稿；检查通过时，将作业状态修改为就绪，并返回成功。

        :param AddPipelineJobRequest request
        :return: AddPipelineJobResponse
        """
        return self.add_pipeline_job_with_http_info(request)

    def add_pipeline_job_with_http_info(self, request):
        """新建管道作业

        新建管道作业时，需要在URL中指定是更新哪一个作业，将在body中附带完整的作业信息。（作业中各算子的详细配置请参考算子配置章节。） check参数表示是否需要对作业配置进行检查，若为false，则不检查，将作业保存为草稿；若为true，则对作业配置进行检查。当检查不通过时，将作业状态修改为草稿；检查通过时，将作业状态修改为就绪，并返回成功。

        :param AddPipelineJobRequest request
        :return: AddPipelineJobResponse
        """

        all_params = ['add_pipeline_job_request_body', 'check']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'check' in local_var_params:
            query_params.append(('check', local_var_params['check']))

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
            resource_path='/v1/{project_id}/pipelines',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='AddPipelineJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_pipeline_job(self, request):
        """删除管道作业

        删除用户指定的管道作业

        :param DeletePipelineJobRequest request
        :return: DeletePipelineJobResponse
        """
        return self.delete_pipeline_job_with_http_info(request)

    def delete_pipeline_job_with_http_info(self, request):
        """删除管道作业

        删除用户指定的管道作业

        :param DeletePipelineJobRequest request
        :return: DeletePipelineJobResponse
        """

        all_params = ['pipeline_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

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
            resource_path='/v1/{project_id}/pipelines/{pipeline_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeletePipelineJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_pipeline_jobs(self, request):
        """获取管道作业列表

        获取用户下的所有管道作业，支持分页。

        :param ListPipelineJobsRequest request
        :return: ListPipelineJobsResponse
        """
        return self.list_pipeline_jobs_with_http_info(request)

    def list_pipeline_jobs_with_http_info(self, request):
        """获取管道作业列表

        获取用户下的所有管道作业，支持分页。

        :param ListPipelineJobsRequest request
        :return: ListPipelineJobsResponse
        """

        all_params = ['data_store_id', 'data_store_group_id', 'data_source_id', 'pipeline_name', 'operator_class_name', 'offset', 'limit', 'sync_status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'data_store_id' in local_var_params:
            query_params.append(('data_store_id', local_var_params['data_store_id']))
        if 'data_store_group_id' in local_var_params:
            query_params.append(('data_store_group_id', local_var_params['data_store_group_id']))
        if 'data_source_id' in local_var_params:
            query_params.append(('data_source_id', local_var_params['data_source_id']))
        if 'pipeline_name' in local_var_params:
            query_params.append(('pipeline_name', local_var_params['pipeline_name']))
        if 'operator_class_name' in local_var_params:
            query_params.append(('operator_class_name', local_var_params['operator_class_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sync_status' in local_var_params:
            query_params.append(('sync_status', local_var_params['sync_status']))

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
            resource_path='/v1/{project_id}/pipelines',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListPipelineJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_pipeline_job(self, request):
        """获取管道作业详情

        获取指定管道作业的详情

        :param ShowPipelineJobRequest request
        :return: ShowPipelineJobResponse
        """
        return self.show_pipeline_job_with_http_info(request)

    def show_pipeline_job_with_http_info(self, request):
        """获取管道作业详情

        获取指定管道作业的详情

        :param ShowPipelineJobRequest request
        :return: ShowPipelineJobResponse
        """

        all_params = ['pipeline_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

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
            resource_path='/v1/{project_id}/pipelines/{pipeline_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowPipelineJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def start_pipeline_job(self, request):
        """启动管道作业

        提交管道作业到运行环境，实时接收数据源的数据并按用户定义的数据清洗逻辑对数据进行处理。

        :param StartPipelineJobRequest request
        :return: StartPipelineJobResponse
        """
        return self.start_pipeline_job_with_http_info(request)

    def start_pipeline_job_with_http_info(self, request):
        """启动管道作业

        提交管道作业到运行环境，实时接收数据源的数据并按用户定义的数据清洗逻辑对数据进行处理。

        :param StartPipelineJobRequest request
        :return: StartPipelineJobResponse
        """

        all_params = ['pipeline_id', 'parallel', 'rtu', 'resume_savepoint']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

        query_params = []
        if 'parallel' in local_var_params:
            query_params.append(('parallel', local_var_params['parallel']))
        if 'rtu' in local_var_params:
            query_params.append(('rtu', local_var_params['rtu']))
        if 'resume_savepoint' in local_var_params:
            query_params.append(('resume_savepoint', local_var_params['resume_savepoint']))

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
            resource_path='/v1/{project_id}/pipelines/{pipeline_id}/start',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StartPipelineJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def stop_pipeline_job(self, request):
        """停止管道作业

        停止一个正在运行中的管道作业

        :param StopPipelineJobRequest request
        :return: StopPipelineJobResponse
        """
        return self.stop_pipeline_job_with_http_info(request)

    def stop_pipeline_job_with_http_info(self, request):
        """停止管道作业

        停止一个正在运行中的管道作业

        :param StopPipelineJobRequest request
        :return: StopPipelineJobResponse
        """

        all_params = ['pipeline_id', 'trigger_savepoint']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

        query_params = []
        if 'trigger_savepoint' in local_var_params:
            query_params.append(('trigger_savepoint', local_var_params['trigger_savepoint']))

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
            resource_path='/v1/{project_id}/pipelines/{pipeline_id}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StopPipelineJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_pipeline_job(self, request):
        """更新管道作业

        更新管道作业时，需要在URL中指定是更新哪一个作业，将在body中附带完整的作业信息。（管道作业详细配置，每个作业可选择不同的算子进行组合，各算子的使用方法详见：数据管道算子配置指南。） check参数表示是否需要对作业配置进行检查，若为false，则不检查，将作业保存为草稿；若为true，则对作业配置进行检查。当检查不通过时，将作业状态修改为草稿；检查通过时，将作业状态修改为就绪，并返回成功。

        :param UpdatePipelineJobRequest request
        :return: UpdatePipelineJobResponse
        """
        return self.update_pipeline_job_with_http_info(request)

    def update_pipeline_job_with_http_info(self, request):
        """更新管道作业

        更新管道作业时，需要在URL中指定是更新哪一个作业，将在body中附带完整的作业信息。（管道作业详细配置，每个作业可选择不同的算子进行组合，各算子的使用方法详见：数据管道算子配置指南。） check参数表示是否需要对作业配置进行检查，若为false，则不检查，将作业保存为草稿；若为true，则对作业配置进行检查。当检查不通过时，将作业状态修改为草稿；检查通过时，将作业状态修改为就绪，并返回成功。

        :param UpdatePipelineJobRequest request
        :return: UpdatePipelineJobResponse
        """

        all_params = ['pipeline_id', 'update_pipeline_job_request_body', 'check']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'pipeline_id' in local_var_params:
            path_params['pipeline_id'] = local_var_params['pipeline_id']

        query_params = []
        if 'check' in local_var_params:
            query_params.append(('check', local_var_params['check']))

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
            resource_path='/v1/{project_id}/pipelines/{pipeline_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdatePipelineJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_streaming_job(self, request):
        """新建实时作业

        除名称和描述外，可先不提供作业的详细配置信息。 check参数表示是否需要对作业配置进行检查，若为false，则不检查，将作业保存为草稿；若为true，则对作业配置进行检查，无论检查是否通过，都将作业及配置信息保存为草稿，当检查不通过时，返回失败及错误信息，检查通过时，将作业状态修改为就绪，并返回成功。

        :param CreateStreamingJobRequest request
        :return: CreateStreamingJobResponse
        """
        return self.create_streaming_job_with_http_info(request)

    def create_streaming_job_with_http_info(self, request):
        """新建实时作业

        除名称和描述外，可先不提供作业的详细配置信息。 check参数表示是否需要对作业配置进行检查，若为false，则不检查，将作业保存为草稿；若为true，则对作业配置进行检查，无论检查是否通过，都将作业及配置信息保存为草稿，当检查不通过时，返回失败及错误信息，检查通过时，将作业状态修改为就绪，并返回成功。

        :param CreateStreamingJobRequest request
        :return: CreateStreamingJobResponse
        """

        all_params = ['create_streaming_job_request_body', 'check']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'check' in local_var_params:
            query_params.append(('check', local_var_params['check']))

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
            resource_path='/v1/{project_id}/streaming/jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateStreamingJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_streaming_job_by_id(self, request):
        """删除实时作业

        删除用户指定的作业

        :param DeleteStreamingJobByIdRequest request
        :return: DeleteStreamingJobByIdResponse
        """
        return self.delete_streaming_job_by_id_with_http_info(request)

    def delete_streaming_job_by_id_with_http_info(self, request):
        """删除实时作业

        删除用户指定的作业

        :param DeleteStreamingJobByIdRequest request
        :return: DeleteStreamingJobByIdResponse
        """

        all_params = ['job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/streaming/jobs/{job_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteStreamingJobByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_job_by_id(self, request):
        """获取实时作业详情

        获取指定作业的详情

        :param ShowJobByIdRequest request
        :return: ShowJobByIdResponse
        """
        return self.show_job_by_id_with_http_info(request)

    def show_job_by_id_with_http_info(self, request):
        """获取实时作业详情

        获取指定作业的详情

        :param ShowJobByIdRequest request
        :return: ShowJobByIdResponse
        """

        all_params = ['job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/streaming/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowJobByIdResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_jobs(self, request):
        """获取实时作业列表

        获取用户下的所有实时分析作业，支持分页。

        :param ShowJobsRequest request
        :return: ShowJobsResponse
        """
        return self.show_jobs_with_http_info(request)

    def show_jobs_with_http_info(self, request):
        """获取实时作业列表

        获取用户下的所有实时分析作业，支持分页。

        :param ShowJobsRequest request
        :return: ShowJobsResponse
        """

        all_params = ['job_input_type', 'offset', 'limit', 'sync_status']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_input_type' in local_var_params:
            query_params.append(('job_input_type', local_var_params['job_input_type']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'sync_status' in local_var_params:
            query_params.append(('sync_status', local_var_params['sync_status']))

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
            resource_path='/v1/{project_id}/streaming/jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_streaming_job(self, request):
        """更新实时作业

        更新作业时，需要在URL中指定是更新哪一个作业，将在body中附带完整的作业信息。 check参数表示是否需要对作业配置进行检查，若为false，则不检查，将作业保存为草稿；若为true，则对作业配置进行检查，无论检查是否通过，都将作业及配置信息保存为草稿，当检查不通过时，返回失败及错误信息，检查通过时，将作业状态修改为就绪，并返回成功。

        :param UpdateStreamingJobRequest request
        :return: UpdateStreamingJobResponse
        """
        return self.update_streaming_job_with_http_info(request)

    def update_streaming_job_with_http_info(self, request):
        """更新实时作业

        更新作业时，需要在URL中指定是更新哪一个作业，将在body中附带完整的作业信息。 check参数表示是否需要对作业配置进行检查，若为false，则不检查，将作业保存为草稿；若为true，则对作业配置进行检查，无论检查是否通过，都将作业及配置信息保存为草稿，当检查不通过时，返回失败及错误信息，检查通过时，将作业状态修改为就绪，并返回成功。

        :param UpdateStreamingJobRequest request
        :return: UpdateStreamingJobResponse
        """

        all_params = ['job_id', 'update_streaming_job_request_body', 'check']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'check' in local_var_params:
            query_params.append(('check', local_var_params['check']))

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
            resource_path='/v1/{project_id}/streaming/jobs/{job_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateStreamingJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def start_job(self, request):
        """启动实时作业

        提交作业到运行环境，实时接收数据并按用户定义的业务逻辑对数据进行处理。

        :param StartJobRequest request
        :return: StartJobResponse
        """
        return self.start_job_with_http_info(request)

    def start_job_with_http_info(self, request):
        """启动实时作业

        提交作业到运行环境，实时接收数据并按用户定义的业务逻辑对数据进行处理。

        :param StartJobRequest request
        :return: StartJobResponse
        """

        all_params = ['job_id', 'parallel', 'rtu', 'resume_savepoint']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'parallel' in local_var_params:
            query_params.append(('parallel', local_var_params['parallel']))
        if 'rtu' in local_var_params:
            query_params.append(('rtu', local_var_params['rtu']))
        if 'resume_savepoint' in local_var_params:
            query_params.append(('resume_savepoint', local_var_params['resume_savepoint']))

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
            resource_path='/v1/{project_id}/streaming/jobs/{job_id}/start',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StartJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def stop_job(self, request):
        """停止实时作业

        停止一个正在运行中的作业

        :param StopJobRequest request
        :return: StopJobResponse
        """
        return self.stop_job_with_http_info(request)

    def stop_job_with_http_info(self, request):
        """停止实时作业

        停止一个正在运行中的作业

        :param StopJobRequest request
        :return: StopJobResponse
        """

        all_params = ['job_id', 'trigger_savepoint']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

        query_params = []
        if 'trigger_savepoint' in local_var_params:
            query_params.append(('trigger_savepoint', local_var_params['trigger_savepoint']))

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
            resource_path='/v1/{project_id}/streaming/jobs/{job_id}/stop',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='StopJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_computing_resource(self, request):
        """创建批计算资源

        创建批计算资源。

        :param CreateComputingResourceRequest request
        :return: CreateComputingResourceResponse
        """
        return self.create_computing_resource_with_http_info(request)

    def create_computing_resource_with_http_info(self, request):
        """创建批计算资源

        创建批计算资源。

        :param CreateComputingResourceRequest request
        :return: CreateComputingResourceResponse
        """

        all_params = ['body']
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
            resource_path='/v1/{project_id}/batch-computing-resources',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateComputingResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_computing_resource(self, request):
        """删除批计算资源

        删除批计算资源。

        :param DeleteComputingResourceRequest request
        :return: DeleteComputingResourceResponse
        """
        return self.delete_computing_resource_with_http_info(request)

    def delete_computing_resource_with_http_info(self, request):
        """删除批计算资源

        删除批计算资源。

        :param DeleteComputingResourceRequest request
        :return: DeleteComputingResourceResponse
        """

        all_params = ['computing_resource_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'computing_resource_id' in local_var_params:
            path_params['computing_resource_id'] = local_var_params['computing_resource_id']

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
            resource_path='/v1/{project_id}/batch-computing-resources/{computing_resource_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteComputingResourceResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_computing_resources(self, request):
        """查询批计算资源列表

        查询批计算资源列表。

        :param ListComputingResourcesRequest request
        :return: ListComputingResourcesResponse
        """
        return self.list_computing_resources_with_http_info(request)

    def list_computing_resources_with_http_info(self, request):
        """查询批计算资源列表

        查询批计算资源列表。

        :param ListComputingResourcesRequest request
        :return: ListComputingResourcesResponse
        """

        all_params = ['computing_resource_name', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'computing_resource_name' in local_var_params:
            query_params.append(('computing_resource_name', local_var_params['computing_resource_name']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v1/{project_id}/batch-computing-resources',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListComputingResourcesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def export_dataset(self, request):
        """下载离线作业结果

        将SQL语句的查询结果下载到本地，只支持下载“QUERY”类型作业的查询结果。

        :param ExportDatasetRequest request
        :return: ExportDatasetResponse
        """
        return self.export_dataset_with_http_info(request)

    def export_dataset_with_http_info(self, request):
        """下载离线作业结果

        将SQL语句的查询结果下载到本地，只支持下载“QUERY”类型作业的查询结果。

        :param ExportDatasetRequest request
        :return: ExportDatasetResponse
        """

        all_params = ['job_id', 'run_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'run_id' in local_var_params:
            path_params['run_id'] = local_var_params['run_id']

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
            resource_path='/v1/{project_id}/batch/jobs/{job_id}/runs/{run_id}/export-dataset',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ExportDatasetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def import_data(self, request):
        """执行导入数据离线作业

        将数据从文件导入OBS表。

        :param ImportDataRequest request
        :return: ImportDataResponse
        """
        return self.import_data_with_http_info(request)

    def import_data_with_http_info(self, request):
        """执行导入数据离线作业

        将数据从文件导入OBS表。

        :param ImportDataRequest request
        :return: ImportDataResponse
        """

        all_params = ['body']
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
            resource_path='/v1/{project_id}/batch/jobs/import/runs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ImportDataResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_dataset(self, request):
        """查询离线作业结果

        在执行SQL查询语句的作业完成后，查看该作业执行的结果。目前仅支持查看“QUERY”类型作业的执行结果。该API只能查看前1000条的结果记录，若要查看全部的结果记录，需要先导出查询结果再进行查看。

        :param ShowDatasetRequest request
        :return: ShowDatasetResponse
        """
        return self.show_dataset_with_http_info(request)

    def show_dataset_with_http_info(self, request):
        """查询离线作业结果

        在执行SQL查询语句的作业完成后，查看该作业执行的结果。目前仅支持查看“QUERY”类型作业的执行结果。该API只能查看前1000条的结果记录，若要查看全部的结果记录，需要先导出查询结果再进行查看。

        :param ShowDatasetRequest request
        :return: ShowDatasetResponse
        """

        all_params = ['job_id', 'run_id', 'offset', 'limit']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'run_id' in local_var_params:
            path_params['run_id'] = local_var_params['run_id']

        query_params = []
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))

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
            resource_path='/v1/{project_id}/batch/jobs/{job_id}/runs/{run_id}/query-dataset',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowDatasetResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def validate_sql(self, request):
        """检查离线作业SQL语法

        检查离线作业SQL语法。

        :param ValidateSqlRequest request
        :return: ValidateSqlResponse
        """
        return self.validate_sql_with_http_info(request)

    def validate_sql_with_http_info(self, request):
        """检查离线作业SQL语法

        检查离线作业SQL语法。

        :param ValidateSqlRequest request
        :return: ValidateSqlResponse
        """

        all_params = ['body']
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
            resource_path='/v1/{project_id}/batch/validate-sql',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ValidateSqlResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_batch_job(self, request):
        """创建离线作业

        创建离线作业。

        :param CreateBatchJobRequest request
        :return: CreateBatchJobResponse
        """
        return self.create_batch_job_with_http_info(request)

    def create_batch_job_with_http_info(self, request):
        """创建离线作业

        创建离线作业。

        :param CreateBatchJobRequest request
        :return: CreateBatchJobResponse
        """

        all_params = ['body']
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
            resource_path='/v1/{project_id}/batch/jobs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateBatchJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_batch_job(self, request):
        """删除离线作业

        删除离线作业。

        :param DeleteBatchJobRequest request
        :return: DeleteBatchJobResponse
        """
        return self.delete_batch_job_with_http_info(request)

    def delete_batch_job_with_http_info(self, request):
        """删除离线作业

        删除离线作业。

        :param DeleteBatchJobRequest request
        :return: DeleteBatchJobResponse
        """

        all_params = ['job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/batch/jobs/{job_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteBatchJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_batch_jobs(self, request):
        """查询离线作业列表

        查询离线作业列表。

        :param ListBatchJobsRequest request
        :return: ListBatchJobsResponse
        """
        return self.list_batch_jobs_with_http_info(request)

    def list_batch_jobs_with_http_info(self, request):
        """查询离线作业列表

        查询离线作业列表。

        :param ListBatchJobsRequest request
        :return: ListBatchJobsResponse
        """

        all_params = ['offset', 'limit', 'has_schedule', 'job_name', 'schedule_status', 'order_by', 'order']
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
        if 'has_schedule' in local_var_params:
            query_params.append(('has_schedule', local_var_params['has_schedule']))
        if 'job_name' in local_var_params:
            query_params.append(('job_name', local_var_params['job_name']))
        if 'schedule_status' in local_var_params:
            query_params.append(('schedule_status', local_var_params['schedule_status']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

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
            resource_path='/v1/{project_id}/batch/jobs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListBatchJobsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_batch_job(self, request):
        """查询离线作业详情

        查询离线作业详情。

        :param ShowBatchJobRequest request
        :return: ShowBatchJobResponse
        """
        return self.show_batch_job_with_http_info(request)

    def show_batch_job_with_http_info(self, request):
        """查询离线作业详情

        查询离线作业详情。

        :param ShowBatchJobRequest request
        :return: ShowBatchJobResponse
        """

        all_params = ['job_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/batch/jobs/{job_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowBatchJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def update_batch_job(self, request):
        """修改离线作业

        修改离线作业。

        :param UpdateBatchJobRequest request
        :return: UpdateBatchJobResponse
        """
        return self.update_batch_job_with_http_info(request)

    def update_batch_job_with_http_info(self, request):
        """修改离线作业

        修改离线作业。

        :param UpdateBatchJobRequest request
        :return: UpdateBatchJobResponse
        """

        all_params = ['job_id', 'body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/batch/jobs/{job_id}',
            method='PUT',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='UpdateBatchJobResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_run(self, request):
        """执行离线作业

        执行离线作业。

        :param CreateRunRequest request
        :return: CreateRunResponse
        """
        return self.create_run_with_http_info(request)

    def create_run_with_http_info(self, request):
        """执行离线作业

        执行离线作业。

        :param CreateRunRequest request
        :return: CreateRunResponse
        """

        all_params = ['job_id', 'body']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']

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
            resource_path='/v1/{project_id}/batch/jobs/{job_id}/runs',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateRunResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_run(self, request):
        """停止离线作业

        停止提交中或运行中的离线作业，若作业已经执行结束或失败则无法停止。

        :param DeleteRunRequest request
        :return: DeleteRunResponse
        """
        return self.delete_run_with_http_info(request)

    def delete_run_with_http_info(self, request):
        """停止离线作业

        停止提交中或运行中的离线作业，若作业已经执行结束或失败则无法停止。

        :param DeleteRunRequest request
        :return: DeleteRunResponse
        """

        all_params = ['job_id', 'run_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'run_id' in local_var_params:
            path_params['run_id'] = local_var_params['run_id']

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
            resource_path='/v1/{project_id}/batch/jobs/{job_id}/runs/{run_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteRunResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_runs(self, request):
        """查询离线作业运行列表

        查询离线作业运行列表。

        :param ListRunsRequest request
        :return: ListRunsResponse
        """
        return self.list_runs_with_http_info(request)

    def list_runs_with_http_info(self, request):
        """查询离线作业运行列表

        查询离线作业运行列表。

        :param ListRunsRequest request
        :return: ListRunsResponse
        """

        all_params = ['offset', 'limit', 'start_time', 'end_time', 'sql_pattern', 'sql_type', 'job_type', 'status', 'order_by', 'order', 'job_name']
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
        if 'start_time' in local_var_params:
            query_params.append(('start_time', local_var_params['start_time']))
        if 'end_time' in local_var_params:
            query_params.append(('end_time', local_var_params['end_time']))
        if 'sql_pattern' in local_var_params:
            query_params.append(('sql_pattern', local_var_params['sql_pattern']))
        if 'sql_type' in local_var_params:
            query_params.append(('sql_type', local_var_params['sql_type']))
        if 'job_type' in local_var_params:
            query_params.append(('job_type', local_var_params['job_type']))
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))
        if 'job_name' in local_var_params:
            query_params.append(('job_name', local_var_params['job_name']))

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
            resource_path='/v1/{project_id}/batch/jobs/runs',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListRunsResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_run(self, request):
        """查询离线作业运行详情

        查询离线作业运行详情。

        :param ShowRunRequest request
        :return: ShowRunResponse
        """
        return self.show_run_with_http_info(request)

    def show_run_with_http_info(self, request):
        """查询离线作业运行详情

        查询离线作业运行详情。

        :param ShowRunRequest request
        :return: ShowRunResponse
        """

        all_params = ['job_id', 'run_id', 'with_details']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'job_id' in local_var_params:
            path_params['job_id'] = local_var_params['job_id']
        if 'run_id' in local_var_params:
            path_params['run_id'] = local_var_params['run_id']

        query_params = []
        if 'with_details' in local_var_params:
            query_params.append(('with_details', local_var_params['with_details']))

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
            resource_path='/v1/{project_id}/batch/jobs/{job_id}/runs/{run_id}',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowRunResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def create_table(self, request):
        """创建离线数据表

        创建离线数据表。

        :param CreateTableRequest request
        :return: CreateTableResponse
        """
        return self.create_table_with_http_info(request)

    def create_table_with_http_info(self, request):
        """创建离线数据表

        创建离线数据表。

        :param CreateTableRequest request
        :return: CreateTableResponse
        """

        all_params = ['body']
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
            resource_path='/v1/{project_id}/tables',
            method='POST',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='CreateTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def delete_table(self, request):
        """删除离线数据表

        删除离线数据表。

        :param DeleteTableRequest request
        :return: DeleteTableResponse
        """
        return self.delete_table_with_http_info(request)

    def delete_table_with_http_info(self, request):
        """删除离线数据表

        删除离线数据表。

        :param DeleteTableRequest request
        :return: DeleteTableResponse
        """

        all_params = ['table_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'table_id' in local_var_params:
            path_params['table_id'] = local_var_params['table_id']

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
            resource_path='/v1/{project_id}/tables/{table_id}',
            method='DELETE',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='DeleteTableResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def list_tables(self, request):
        """查询离线数据表列表

        查询离线数据表列表。

        :param ListTablesRequest request
        :return: ListTablesResponse
        """
        return self.list_tables_with_http_info(request)

    def list_tables_with_http_info(self, request):
        """查询离线数据表列表

        查询离线数据表列表。

        :param ListTablesRequest request
        :return: ListTablesResponse
        """

        all_params = ['keyword', 'tag', 'offset', 'limit', 'order_by', 'order']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'keyword' in local_var_params:
            query_params.append(('keyword', local_var_params['keyword']))
        if 'tag' in local_var_params:
            query_params.append(('tag', local_var_params['tag']))
        if 'offset' in local_var_params:
            query_params.append(('offset', local_var_params['offset']))
        if 'limit' in local_var_params:
            query_params.append(('limit', local_var_params['limit']))
        if 'order_by' in local_var_params:
            query_params.append(('order_by', local_var_params['order_by']))
        if 'order' in local_var_params:
            query_params.append(('order', local_var_params['order']))

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
            resource_path='/v1/{project_id}/tables',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ListTablesResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_table_preview(self, request):
        """预览离线数据表内容

        预览离线数据表内容。

        :param ShowTablePreviewRequest request
        :return: ShowTablePreviewResponse
        """
        return self.show_table_preview_with_http_info(request)

    def show_table_preview_with_http_info(self, request):
        """预览离线数据表内容

        预览离线数据表内容。

        :param ShowTablePreviewRequest request
        :return: ShowTablePreviewResponse
        """

        all_params = ['table_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'table_id' in local_var_params:
            path_params['table_id'] = local_var_params['table_id']

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
            resource_path='/v1/{project_id}/tables/{table_id}/preview',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTablePreviewResponse',
            response_headers=response_headers,
            auth_settings=auth_settings,
            collection_formats=collection_formats,
            request_type=request.__class__.__name__)


    def show_table_schema(self, request):
        """查询离线数据表结构

        查询离线数据表结构。

        :param ShowTableSchemaRequest request
        :return: ShowTableSchemaResponse
        """
        return self.show_table_schema_with_http_info(request)

    def show_table_schema_with_http_info(self, request):
        """查询离线数据表结构

        查询离线数据表结构。

        :param ShowTableSchemaRequest request
        :return: ShowTableSchemaResponse
        """

        all_params = ['table_id']
        local_var_params = {}
        for attr in request.attribute_map:
            if hasattr(request, attr):
                local_var_params[attr] = getattr(request, attr)

        collection_formats = {}

        path_params = {}
        if 'table_id' in local_var_params:
            path_params['table_id'] = local_var_params['table_id']

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
            resource_path='/v1/{project_id}/tables/{table_id}/schema',
            method='GET',
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
            body=body_params,
            post_params=form_params,
            response_type='ShowTableSchemaResponse',
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
        :param header_params: Header parameters to be placed in the request header.
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
            request_type=request_type)
