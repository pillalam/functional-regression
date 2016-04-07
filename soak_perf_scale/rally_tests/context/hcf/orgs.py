# Copyright 2016: HPE Inc.
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

from rally.common.i18n import _
from rally.common import log as logging
from rally.common import utils as rutils
from rally import consts
from rally.task import context
from rally.task import scenario
from rally.plugins.openstack.scenarios.hcf import utils as hcf_utils


LOG = logging.getLogger(__name__)


@context.configure(name="orgs", order=500)
class OrgGenerator(context.Context):
    """Context class for adding orgs."""

    CONFIG_SCHEMA = {
        "type": "object",
        "$schema": consts.JSON_SCHEMA,
        "properties": {
            "cluster_url": {
                "type": "string"
            },
            "username": {
                "type": "string"
            },
            "password": {
                "type": "string"
            }
        },
        "additionalProperties": False
    }

    @logging.log_task_wrapper(LOG.info, _("Exit context: `orgs`"))
    def setup(self):
        self.username = self.config["username"]
        self.password = self.config["password"]
        self.cluster_url = self.config["cluster_url"]
        print "in setup"
        for user, tenant_id in rutils.iterate_per_tenants(
                self.context["users"]):
            self.hcf_util = hcf_utils.HcfScenario(
                {"user": user,
                 "task": self.context["task"],
                 "config": self.context["config"]})
            self.hcf_util._connectApi_and_loginToTarget(self.cluster_url,
                                                        self.username,
                                                        self.password)
            self.org_name = self.hcf_util._create_org()
            self.context["tenants"][tenant_id]["org_name"] = self.org_name

    def cleanup(self):
        print "in cleanup"
        self.hcf_util._connectApi_and_loginToTarget(self.cluster_url,
                                                    self.username,
                                                    self.password)
        self.hcf_util._delete_org(self.org_name)
        self.hcf_util._logoutFromTarget()
