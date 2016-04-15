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

import commands
import requests
import testtools
from rally.task import atomic
from rally.plugins.openstack import scenario
from rally.common import log as logging
from rally.task import utils as bench_utils
import logging


class CatalogScenario(scenario.OpenStackScenario, testtools.TestCase):

    @atomic.action_timer("catalog.list_catalog")
    def _list_catalog(self, catalog_name):
        """
        :returns: list of catalogs
        """
        logging.info("List catalogs")
        catalogListCommand = "catalog" + " list"
        status, output = self.executeShellCommand(catalogListCommand)
        self.assertEqual(status, 0)
        self.assertIn(catalog_name, output)

    @atomic.action_timer("catalog.details_catalog")
    def _details_catalog(self, catalog_name):
        """
        :returns: catalog details
        """
        logging.info("detail catalog")
        catalogDetailsCommand = "catalog" + " details " + catalog_name
        status, output = self.executeShellCommand(catalogDetailsCommand)
        self.assertEqual(status, 0)
        self.assertIn(catalog_name, output)

    def executeShellCommand(self, strCommand):
        status, output = commands.getstatusoutput(strCommand)
        return status, output
