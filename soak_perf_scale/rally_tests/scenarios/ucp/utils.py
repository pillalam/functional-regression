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

import random
import json
import os
import time
import commands
import requests
import testtools
from rally.task import atomic
from rally.plugins.openstack import scenario
from rally.common import log as logging
from rally.task import utils as bench_utils
import logging


class UcpScenario(scenario.OpenStackScenario, testtools.TestCase):
    def _connectTarget(self, target_url):
        logging.info("Connecting ...")
        targetCommand = "hdpctl" + " target -u" + target_url
        status, output = self.executeShellCommand(targetCommand)
        self.assertEqual(status, 0)
        logging.info("Connected to target")
        return status, output

    @atomic.action_timer("ucp.create_instance")
    def _create_instance(self):
        """
        :returns: created instance
        """
        logging.info("Creating new instance")
        instance_id = "ucpcluster" + str(random.randint(1024, 4096))
        jsonFileName = self._create_instance_json(instance_id)
        instCreateCommand = "hdpctl" + " create-instance -d " + jsonFileName
        status, output = self.executeShellCommand(instCreateCommand)
        self.assertEqual(status, 0)
        self.assertIn(instance_id, output)
        logging.info("instance created successfully")
        os.remove(jsonFileName)
        return instance_id

    @atomic.action_timer("ucp.view_instance")
    def _view_instance(self, instance_id):
        """
        :returns: instance details
        """
        logging.info("viewing instance")
        instViewCommand = "hdpctl" + " view-instance " + instance_id
        status, output = self.executeShellCommand(instViewCommand)
        self.assertEqual(status, 0)
        self.assertIn(instance_id, output)
        logging.info("instance Viewed successfully")

    @atomic.action_timer("ucp.delete_instance")
    def _delete_instance(self, instance_id):
        """
        :returns: deleted instance
        """
        logging.info("Deleting instance")
        instDeleteCommand = "hdpctl" + " delete-instance " + instance_id
        status, output = self.executeShellCommand(instDeleteCommand)
        logging.info("instance deleted successfully")
        status = self._wait_for_instance_delete(instance_id, timeout=50,
                                                check_interval=4)
        self.assertEqual(status, 0)

    def executeShellCommand(self, strCommand):
        status, output = commands.getstatusoutput(strCommand)
        return status, output

    def _create_instance_json(self, instance_id1):
        """
        :param jsonFileLocation: Location of json_create base file
        :returns: json file location
        """
        param_dict = {}
        instance_id = "ucpcluster" + str(random.randint(1024, 4096))
        jsonFileName = "jsonFile" + str(random.randint(1024, 4096))
        param_dict["name"] = "k8-guestbook"
        param_dict["version"] = "1.0.0"
        param_dict["vendor"] = "Kubernetes"
        param_dict["labels"] = "guestbook-cluster-1"
        param_dict["instance_id"] = instance_id
        param_dict["description"] = "A guestbook example cluster"
        with open(jsonFileName, 'w') as json_file:
            json.dump(param_dict, json_file)
        json_file.close()
        return jsonFileName

    def _wait_for_instance_delete(self, instance_id, timeout=50,
                                  check_interval=1):
        """Waits for specified instance to be deleted.
        :param instance_id: instance id
        """
        status = 1
        start_time = time.time()
        while True:
            instViewCommand = "hdpctl" + " view-instance " + instance_id
            status, output = self.executeShellCommand(instViewCommand)
            if status != 0:
                break
            elif time.time() - start_time > timeout:
                break
            time.sleep(check_interval)
        return status
