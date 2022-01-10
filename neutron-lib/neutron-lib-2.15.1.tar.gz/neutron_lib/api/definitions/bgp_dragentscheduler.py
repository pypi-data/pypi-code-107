# Copyright 2016 Huawei Technologies India Pvt. Ltd.
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


ALIAS = 'bgp_dragent_scheduler'
IS_SHIM_EXTENSION = True
IS_STANDARD_ATTR_EXTENSION = False
NAME = "BGP Dynamic Routing Agent Scheduler"
DESCRIPTION = "Schedules BgpSpeakers on BgpDrAgent"
UPDATED_TIMESTAMP = '2015-07-30T10:00:00-00:00'
BGP_DRINSTANCE = 'bgp-drinstance'
BGP_DRINSTANCES = BGP_DRINSTANCE + 's'
BGP_DRAGENT = 'bgp-dragent'
BGP_DRAGENTS = BGP_DRAGENT + 's'
RESOURCE_ATTRIBUTE_MAP = {}
SUB_RESOURCE_ATTRIBUTE_MAP = None
ACTION_MAP = {}
ACTION_STATUS = {}
REQUIRED_EXTENSIONS = []
OPTIONAL_EXTENSIONS = []
