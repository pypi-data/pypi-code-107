# coding: utf-8

from __future__ import absolute_import

# import models into model package
from huaweicloudsdkmrs.v1.model.add_jobs import AddJobs
from huaweicloudsdkmrs.v1.model.auto_scaling_policy import AutoScalingPolicy
from huaweicloudsdkmrs.v1.model.auto_scaling_policy_req_v11 import AutoScalingPolicyReqV11
from huaweicloudsdkmrs.v1.model.batch_create_cluster_tags_req import BatchCreateClusterTagsReq
from huaweicloudsdkmrs.v1.model.batch_create_cluster_tags_request import BatchCreateClusterTagsRequest
from huaweicloudsdkmrs.v1.model.batch_create_cluster_tags_response import BatchCreateClusterTagsResponse
from huaweicloudsdkmrs.v1.model.batch_delete_cluster_tags_req import BatchDeleteClusterTagsReq
from huaweicloudsdkmrs.v1.model.batch_delete_cluster_tags_request import BatchDeleteClusterTagsRequest
from huaweicloudsdkmrs.v1.model.batch_delete_cluster_tags_response import BatchDeleteClusterTagsResponse
from huaweicloudsdkmrs.v1.model.bootstrap_script import BootstrapScript
from huaweicloudsdkmrs.v1.model.bootstrap_script_resp import BootstrapScriptResp
from huaweicloudsdkmrs.v1.model.cluster import Cluster
from huaweicloudsdkmrs.v1.model.cluster_scaling_params import ClusterScalingParams
from huaweicloudsdkmrs.v1.model.cluster_scaling_req import ClusterScalingReq
from huaweicloudsdkmrs.v1.model.component_amb import ComponentAmb
from huaweicloudsdkmrs.v1.model.component_list import ComponentList
from huaweicloudsdkmrs.v1.model.create_and_execute_job_request import CreateAndExecuteJobRequest
from huaweicloudsdkmrs.v1.model.create_and_execute_job_response import CreateAndExecuteJobResponse
from huaweicloudsdkmrs.v1.model.create_cluster_req import CreateClusterReq
from huaweicloudsdkmrs.v1.model.create_cluster_request import CreateClusterRequest
from huaweicloudsdkmrs.v1.model.create_cluster_response import CreateClusterResponse
from huaweicloudsdkmrs.v1.model.create_cluster_tag_request import CreateClusterTagRequest
from huaweicloudsdkmrs.v1.model.create_cluster_tag_response import CreateClusterTagResponse
from huaweicloudsdkmrs.v1.model.create_scaling_policy_request import CreateScalingPolicyRequest
from huaweicloudsdkmrs.v1.model.create_scaling_policy_response import CreateScalingPolicyResponse
from huaweicloudsdkmrs.v1.model.create_tag_req import CreateTagReq
from huaweicloudsdkmrs.v1.model.delete_cluster_request import DeleteClusterRequest
from huaweicloudsdkmrs.v1.model.delete_cluster_response import DeleteClusterResponse
from huaweicloudsdkmrs.v1.model.delete_cluster_tag_request import DeleteClusterTagRequest
from huaweicloudsdkmrs.v1.model.delete_cluster_tag_response import DeleteClusterTagResponse
from huaweicloudsdkmrs.v1.model.delete_job_execution_request import DeleteJobExecutionRequest
from huaweicloudsdkmrs.v1.model.delete_job_execution_response import DeleteJobExecutionResponse
from huaweicloudsdkmrs.v1.model.host_model import HostModel
from huaweicloudsdkmrs.v1.model.job_exe_result import JobExeResult
from huaweicloudsdkmrs.v1.model.list_all_tags_request import ListAllTagsRequest
from huaweicloudsdkmrs.v1.model.list_all_tags_response import ListAllTagsResponse
from huaweicloudsdkmrs.v1.model.list_cluster_tags_request import ListClusterTagsRequest
from huaweicloudsdkmrs.v1.model.list_cluster_tags_response import ListClusterTagsResponse
from huaweicloudsdkmrs.v1.model.list_clusters_by_tags_request import ListClustersByTagsRequest
from huaweicloudsdkmrs.v1.model.list_clusters_by_tags_response import ListClustersByTagsResponse
from huaweicloudsdkmrs.v1.model.list_clusters_request import ListClustersRequest
from huaweicloudsdkmrs.v1.model.list_clusters_response import ListClustersResponse
from huaweicloudsdkmrs.v1.model.list_execute_job_request import ListExecuteJobRequest
from huaweicloudsdkmrs.v1.model.list_execute_job_response import ListExecuteJobResponse
from huaweicloudsdkmrs.v1.model.list_hosts_request import ListHostsRequest
from huaweicloudsdkmrs.v1.model.list_hosts_response import ListHostsResponse
from huaweicloudsdkmrs.v1.model.list_resource_req import ListResourceReq
from huaweicloudsdkmrs.v1.model.mrs_resource import MRSResource
from huaweicloudsdkmrs.v1.model.match import Match
from huaweicloudsdkmrs.v1.model.node_group_v10 import NodeGroupV10
from huaweicloudsdkmrs.v1.model.node_group_v11 import NodeGroupV11
from huaweicloudsdkmrs.v1.model.resources_plan import ResourcesPlan
from huaweicloudsdkmrs.v1.model.rules import Rules
from huaweicloudsdkmrs.v1.model.scale_script import ScaleScript
from huaweicloudsdkmrs.v1.model.show_cluster_details_request import ShowClusterDetailsRequest
from huaweicloudsdkmrs.v1.model.show_cluster_details_response import ShowClusterDetailsResponse
from huaweicloudsdkmrs.v1.model.show_job_exes_request import ShowJobExesRequest
from huaweicloudsdkmrs.v1.model.show_job_exes_response import ShowJobExesResponse
from huaweicloudsdkmrs.v1.model.submit_job_req_v11 import SubmitJobReqV11
from huaweicloudsdkmrs.v1.model.tag import Tag
from huaweicloudsdkmrs.v1.model.tag_plain import TagPlain
from huaweicloudsdkmrs.v1.model.tag_with_multi_value import TagWithMultiValue
from huaweicloudsdkmrs.v1.model.task_node_groups import TaskNodeGroups
from huaweicloudsdkmrs.v1.model.task_node_info import TaskNodeInfo
from huaweicloudsdkmrs.v1.model.trigger import Trigger
from huaweicloudsdkmrs.v1.model.update_cluster_scaling_request import UpdateClusterScalingRequest
from huaweicloudsdkmrs.v1.model.update_cluster_scaling_response import UpdateClusterScalingResponse
