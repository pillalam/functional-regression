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

    @atomic.action_timer("catalog.list_services")
    def _list_services(self, service_name):
        """
        :returns: list of services
        """
        logging.info("List services")
        ServiceListCommand = "catalog" + " services "
        status, output = self.executeShellCommand(ServiceListCommand)
        self.assertEqual(status, 0)
        self.assertIn(service_name, output)

    @atomic.action_timer("catalog.details_service")
    def _details_service(self, service_name):
        """
        :returns: service details
        """
        logging.info("detail service")
        ServiceDetailsCommand = "catalog" + " service " + service_name
        status, output = self.executeShellCommand(ServiceDetailsCommand)
        self.assertEqual(status, 0)
        self.assertIn(service_name, output)

    @atomic.action_timer("catalog.list_instances")
    def _list_instances(self):
        """
        :returns: list of instances
        """
        logging.info("List instances")
        InstanceListCommand = "catalog" + " instances "
        status, output = self.executeShellCommand(InstanceListCommand)
        self.assertEqual(status, 0)

    @atomic.action_timer("catalog.create_mysql_service_instance")
    def _create_mysql_instance(self, service_Id, instancefile):
        """
        :returns: Mysql Service instance
        """
        logging.info("Create mysql instance")
        InstanceCreateCommand = "catalog" + " create-instance  " + \
            service_Id + "-i" + instancefile
        status, output = self.executeShellCommand(InstanceCreateCommand)
        self.assertEqual(status, 0)
        instance_Id = output
        return instance_Id

    @atomic.action_timer("catalog.delete_mysql_service_instance")
    def _delete_mysql_instance(self, instance_Id):
        logging.info("Delete mysql instance")
        InstanceDeleteCommand = "catalog" + "delete-instance " + \
            "-f " + instance_Id
        status, output = self.executeShellCommand(InstanceDeleteCommand)
        self.assertEqual(status, 0)

    def executeShellCommand(self, strCommand):
        status, output = commands.getstatusoutput(strCommand)
        return status, output
