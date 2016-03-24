#Copyright 2015: HP Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import time
import requests
import testtools
from rally.common import logging as logging
from rally.task import atomic
from rally.task import utils as bench_utils
from rally.plugins.openstack import scenario


class CfScenario(scenario.OpenStackScenario, testtools.TestCase):
    @atomic.action_timer("als.app_url")
    def _use_app(self, app_url):
        """
        :param app_url: App to use
        :returns: url request access time
        """
        status_code = requests.get(app_url).status_code
        self.assertEqual(200, status_code)
        return status_code
