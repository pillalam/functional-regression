#Copyright 2016: HPE Inc.
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

from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.ucp import utils


class UcpInstanceTests(utils.UcpScenario):
    """Basic benchmark scenarios for UCP."""
    @scenario.configure()
    def create_delete_instance(self, target_url):
        """
        This method tests the new instance create, view and delete.
        param : target_url
        """
        # connecting to target
        self._connectTarget(target_url)
        # Create instance
        inst_name = self._create_instance()
        # View instance
        self._view_instance(inst_name)
        # Delete instance
        self._delete_instance(inst_name)
