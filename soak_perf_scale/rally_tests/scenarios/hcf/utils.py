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

import time
import random
import commands
import requests
import testtools
from rally.task import atomic
from rally.plugins.openstack import scenario
from rally.common import log as logging
from rally.task import utils as bench_utils
import logging


class HcfScenario(scenario.OpenStackScenario, testtools.TestCase):
    @atomic.action_timer("cf.app_url_access_time")
    def _use_app(self, app_url):
        """
        :param app_url: App to use
        :returns: url request access time
        """
        status_code = requests.get(app_url).status_code
        self.assertEqual(200, status_code)
        return status_code

    @atomic.action_timer("hcf.create_org")
    def _create_org(self):
        """
        :returns: created org
        """
        logging.info("Create new organisation")
        org_name = 'og_test_org' + str(random.randint(1024, 4096))
        orgCreateCommand = "cf" + " create-org " + org_name
        status, output = self.executeShellCommand(orgCreateCommand)
        logging.info("Org created successfully")
        self.assertIn(org_name, output)
        return org_name

    def _list_org(self):
        """
        :returns: list of orgs
        """
        logging.info("List organisations")
        orgListCommand = "cf" + " orgs"
        status, output = self.executeShellCommand(orgListCommand)
        return output

    @atomic.action_timer("hcf.delete_org")
    def _delete_org(self, org_name):
        """
        :param org_name: org name
        """
        logging.info("Delete organisation")
        orgDeleteCommand = "cf" + " delete-org " + org_name + " -f"
        status, output = self.executeShellCommand(orgDeleteCommand)
        logging.info("Org deleted successfully")
        output = self._wait_for_org_delete(org_name, timeout=300,
                                           check_interval=4)
        self.assertNotIn(org_name, output)

    def _wait_for_org_delete(self, org_name, timeout=300,
                             check_interval=1):
        """Waits for specified Org to be deleted.
        :param org_name: org name
        """
        start_time = time.time()
        while True:
            orgs_list = self._list_org()
            if org_name not in orgs_list:
                print "Org deleted successfully"
                return orgs_list
            elif time.time() - start_time > timeout:
                print "Delete org timed out"
            time.sleep(check_interval)
            start_time += int(1)

    @atomic.action_timer("hcf.create_space")
    def _create_space(self, org_name):
        """
        :param: org_name: org name
        :returns: created space
        """
        targetOrgCommand = "cf" + " target -o " + org_name
        self.executeShellCommand(targetOrgCommand)
        logging.info("Create new space")
        space_name = 'sp_test_space' + str(random.randint(1024, 4096))
        spaceCreateCommand = "cf" + " create-space " + space_name + \
            " -o " + org_name
        status, output = self.executeShellCommand(spaceCreateCommand)
        logging.info("Space created successfully")
        self.assertIn(space_name, output)
        return space_name

    def _list_space(self):
        """
        :returns: list of spaces
        """
        logging.info("List spaces")
        spaceListCommand = "cf" + " spaces "
        status, output = self.executeShellCommand(spaceListCommand)
        return output

    @atomic.action_timer("hcf.delete_space")
    def _delete_space(self, space_name):
        """
        :param space_name: space name
        """
        logging.info("Delete space")
        spaceDeleteCommand = "cf" + " delete-space " + space_name + " -f"
        status, output = self.executeShellCommand(spaceDeleteCommand)
        logging.info("Space deleted successfully")
        space_list = self._list_space()
        self.assertNotIn(space_name, space_list)
        return status, output

    @atomic.action_timer("hcf.create_quota")
    def _create_quota(self):
        """
        :returns: created quota plan
        """
        logging.info("Create new quota plan")
        quota_name = 'q_test_quota_plan' + str(random.randint(1024, 4096))
        max_mem = "1G"
        total_mem = "1G"
        total_routes = "500"
        total_service_inst = "110"
        quotaCreateCommand = "cf" + " create-quota " + quota_name + \
            " -i " + max_mem + " -m " + total_mem + " -r " + total_routes + \
            " -s " + total_service_inst + " --allow-paid-service-plans"
        status, output = self.executeShellCommand(quotaCreateCommand)
        logging.info("Quota Plan created successfully")
        self.assertIn(quota_name, output)
        return quota_name

    def _list_quota(self):
        """
        :returns: list of quota plans
        """
        logging.info("List quota plans")
        quotaListCommand = "cf" + " quotas "
        status, output = self.executeShellCommand(quotaListCommand)
        return output

    @atomic.action_timer("hcf.delete_quota")
    def _delete_quota(self, quota_name):
        """
        :param quota_name: quota plan name
        """
        logging.info("Delete quota")
        quotaDeleteCommand = "cf" + " delete-quota " + quota_name + " -f"
        status, output = self.executeShellCommand(quotaDeleteCommand)
        logging.info("Quota deleted successfully")
        quota_list = self._list_quota()
        self.assertNotIn(quota_name, quota_list)
        return status, output

    @atomic.action_timer("hcf.create_domain")
    def _create_domain(self, org_name):
        """
        :param org_name: org name
        :returns: created domain
        """
        targetOrgCommand = "cf" + " target -o " + org_name
        self.executeShellCommand(targetOrgCommand)
        logging.info("Create new domain")
        domain_name = 'www' + '.' + 'dtestdomain' + \
            str(random.randint(1024, 4096)) + '.' + 'com'
        domainCreateCommand = "cf" + " create-domain " + org_name + \
            str(" ") + domain_name
        status, output = self.executeShellCommand(domainCreateCommand)
        logging.info("Domain created successfully")
        self.assertIn(domain_name, output)
        return domain_name

    def _list_domain(self):
        """
        :returns: list of domains
        """
        logging.info("Lists domains")
        domainListCommand = "cf" + " domains "
        status, output = self.executeShellCommand(domainListCommand)
        return output

    @atomic.action_timer("hcf.delete_domain")
    def _delete_domain(self, domain_name):
        """
        :param domain_name: domain name
        """
        logging.info("Delete domain")
        domainDeleteCommand = "cf" + " delete-domain " + \
            domain_name + " -f"
        status, output = self.executeShellCommand(domainDeleteCommand)
        logging.info("Domain deleted successfully")
        domain_list = self._list_domain()
        self.assertNotIn(domain_name, domain_list)
        return status, output

    def executeShellCommand(self, strCommand):
        print "str Command for execute shell"
        print strCommand
        status, output = commands.getstatusoutput(strCommand)
        return status, output

    def _connectApi_and_loginToTarget(
            self, cluster_url, strUsr, strPasswd, strOrg=None,
            strSpc=None):
        self._connectApi(cluster_url)
        self._loginToTarget(strUsr, strPasswd)

    def _connectApi(self, cluster_url):
        logging.info("Connecting ...")
        print "Connecting to api"
        strConnectApiCommand = "cf" + " api --skip-ssl-validation " \
            + cluster_url
        status, output = self.executeShellCommand(strConnectApiCommand)
        logging.info("Connected to target")
        return status, output

    def _loginToTarget(
            self, strUsr, strPasswd, strOrg=None,
            strSpc=None):
        logging.info("Logging in ...")
        if strOrg is None:
            strLoginCommand = "cf" + " login -u " + strUsr + " -p " \
                + strPasswd
        else:
            strLoginCommand = cfCLICommand + " login -u " \
                + strUsr + " -p " + strPasswd + " -o " \
                + strOrg + " -s " + strSpc
        strLogin = "no" + " | " + strLoginCommand
        status, output = self.executeShellCommand(strLogin)
        time.sleep(60)
        logging.info("Logged into target")
        return status, output

    def _logoutFromTarget(self):
        logging.info("Logging out from target")
        strLogoutCommand = "cf" + " logout"
        status, output = self.executeShellCommand(strLogoutCommand)
        logging.info("Logged out from target")
        return status, output
