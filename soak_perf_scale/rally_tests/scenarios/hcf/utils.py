# Copyright 2015: HP Inc.
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

import csv
import time
import requests
import random
import yaml
import subprocess
import re
import os
import testtools
import sys
import getopt
import commands
import shutil
import time
import random
from rally.common import log as logging
from rally.task import atomic
import logging
from rally.task import utils as bench_utils
from rally.plugins.openstack import scenario


class AlsScenario(scenario.OpenStackScenario, testtools.TestCase):
    @atomic.action_timer("als.app_url")
    def _use_app(self, app_url):
        """
        :param app_url: App to use
        :returns: als_url request access time
        """

        status_code = requests.get(app_url).status_code
        self.assertEqual(200, status_code)
        return status_code

    @atomic.action_timer("als.als.application_post_request")
    def post_data_mysqldb_app(self, app_url):
        """ Inserts string to the mysql db using POST API call """
        db_data = self._generate_random_name(prefix="rally_db")
        # post request to add data to db
        resp = requests.post(app_url, data={"name": db_data})
        status_code = resp.status_code
        resp_status = str(resp.text).strip()
        var = str(resp.text).strip()
        self.assertEqual(200, status_code)
        self.assertEqual('0', var)
        return db_data

    @atomic.action_timer("als.application_get_request")
    def get_data_mysqldb_app(self, app_url, db_data):
        """ Retrieves the data from the mysql db using GET API call """
        response = requests.get(app_url)
        status_code = response.status_code
        data_items = str(response.text).split()
        self.assertEqual(200, status_code)
        self.assertIn(db_data, data_items)

    @atomic.action_timer("als._access_fib_app")
    def _access_fib_app(self, app_url, fib_id):
        """
        :param app_url: App to use
        """
        app_url = app_url + 'fib/%s' % fib_id
        response = requests.get(app_url)
        status_code = response.status_code
        output = response.json()
        self.assertEqual(200, status_code)
        self.assertEqual(fib_id, output["fib_id"])
        return status_code

    def access_test_deploy_app(self, app_url, version, helionCLICommand,
                               appLocation, cluster_url, username, password):
        print "Deploying with version ", version
        conStatus = 1
        conStatus, conOutput = self.connectTarget(
            helionCLICommand, cluster_url)
        time.sleep(2)
        # Login to Cluster URL
        if conStatus:
            logging.critical('Connect to %s is failed', cluster_url)
            logging.critical('Console output is %s', conOutput)
        else:
            self.loginToTarget(helionCLICommand, username, password)
        with atomic.ActionTimer(self, "als.app_deploy_time"):
            os.chdir(appLocation)
            if (os.path.isfile("stackato.yml") or
                    os.path.isfile("manifest.yml")):
                subprocess.check_output("echo %s > ./static/version.txt" % (
                    version), shell=True)
                strDeployCommand = helionCLICommand + " push -n --timeout 5m"
                status, output = self.executeShellCommand(strDeployCommand)
            else:
                logging.critical("Application configuration file is missing.")
                exit()
            if "deployed" not in output:
                logging.critical("App deployment failed")
                exit()
        app_url = app_url + 'version'
        with atomic.ActionTimer(self, "als.app_access_time"):
            requests.get(app_url)
        # Delay, before getting the correct version details
        for i in range(1, 9):
            resp = requests.get(app_url)
            resp_json = resp.json()
            time.sleep(5)
        self.assertEqual(version, resp_json[u'version'])
        self.assertEqual(200, resp.status_code)

    def _update_cluster_yml(self, ymlFileLocation, network_id, keypair):
        """
        :param ymlFileLocation: Location of yml_create base file
        :keypair:keypair to be used in cluster creation
        :returns: updated yml file location
        """

        with open(ymlFileLocation, 'r') as yaml_file:
            param_dict = yaml.load(yaml_file)
        yaml_file.close()

        self.cluster_prefix = self._generate_random_name(
            prefix="rallycluster", length=7)
        self.ymlFileLocation = ymlFileLocation
        param_dict["admin-email"] = self.cluster_prefix + "@test.com"
        param_dict["admin-org"] = self.cluster_prefix
        param_dict["admin-password"] = self.cluster_prefix
        param_dict["cluster-prefix"] = self.cluster_prefix
        param_dict["cluster-title"] = self.cluster_prefix
        param_dict["keypair-name"] = keypair
        param_dict["network-id"] = network_id
        new_yml_file = ymlFileLocation.replace('.', '_') + self.cluster_prefix + \
            '.yml'
        with open(new_yml_file, 'w') as yaml_file:
            yaml_file.write(yaml.dump(param_dict, default_flow_style=False))
        yaml_file.close()
        return new_yml_file, self.cluster_prefix

    def _merge_csv_files(self, csv_file_path_list, ymlFileLocation):
        """
        :param csv_file_path_list: list containing csv file paths
        :param ymlFileLocation: Location to create new file,
         merging all urls in csv files.
        :returns path of file containing all the urls.
        """
        new_csv = ymlFileLocation.replace('.', '_') + "merged_urls.csv"
        fout = open(new_csv, "w")
        for csv_file in csv_file_path_list:
            for line in open(csv_file):
                fout.write(line)
        fout.close()
        return new_csv

    def _update_add_dea_yml(self, ymlFileLocation, dea_flavor):
        dict_for_dea_data = {}
        with open(ymlFileLocation, 'r') as yaml_file:
            param_dict = yaml.load(yaml_file)
        yaml_file.close()
        dict_for_dea_data["cluster-prefix"] = param_dict["cluster-prefix"]
        dict_for_dea_data["constructor-flavor"] = \
            param_dict["constructor-flavor"]
        dict_for_dea_data["constructor-image-name"] = \
            param_dict["constructor-image-name"]
        dict_for_dea_data["flavor"] = dea_flavor
        dict_for_dea_data["http-proxy"] = param_dict["http-proxy"]
        dict_for_dea_data["https-proxy"] = param_dict["https-proxy"]
        dict_for_dea_data["keypair-name"] = param_dict["keypair-name"]
        dict_for_dea_data["max-cluster-wait-duration"] = \
            param_dict["max-cluster-wait-duration"]
        dict_for_dea_data["network-id"] = param_dict["network-id"]
        dict_for_dea_data["seed-node-image-name"] = \
            param_dict["seed-node-image-name"]
        dict_for_dea_data["service-flavor"] = param_dict["service-flavor"]
        dict_for_dea_data["upstream-proxy"] = param_dict["upstream-proxy"]
        dict_for_dea_data["version"] = param_dict["version"]
        new_yml_file = ymlFileLocation.replace('.', '_') + '_add_dea.yml'
        with open(new_yml_file, 'w') as yaml_file:
            yaml_file.write(
                yaml.dump(dict_for_dea_data, default_flow_style=False))
        yaml_file.close()
        return new_yml_file

    def _update_cluster_delete_yml(self, ymlFileLocation, network_id, keypair):
        """
        :param ymlFileLocation: Location of yml_create base file
        :keypair:keypair to be used in cluster creation
        :returns: updated yml file location
        """

        with open(ymlFileLocation, 'r') as yaml_file:
            param_dict = yaml.load(yaml_file)
        yaml_file.close()
        param_dict["cluster-prefix"] = self.cluster_prefix
        param_dict["keypair-name"] = keypair
        param_dict["network-id"] = network_id
        new_yml_file = ymlFileLocation.replace('.', '_') + \
            self.cluster_prefix + '.yml'
        with open(new_yml_file, 'w') as yaml_file:
            yaml_file.write(yaml.dump(param_dict, default_flow_style=False))
        yaml_file.close()
        return new_yml_file

    def _create_cluster(self, cluster_command, yml_location):
        """
        :param yml_location: yml file location for creating cluster
        :param cluster_command: command for cluster operation
        :returns: cluster url after successfull creation
        """
        output = None
        print "%s create-cluster --load %s" % (cluster_command, yml_location)
        time.sleep(5)
        try:
            output = subprocess.check_output("%s create-cluster --load %s" % (
                cluster_command, yml_location), shell=True)
        except subprocess.CalledProcessError as e:
            logging.critical("Command Failed:Return Code:"+str(e.returncode))
            logging.critical("Command Failed:Output message:"+e.output)
            exit(1)
        regex = 'Cluster URL: (.*)'

        if re.search(regex, output):
                cluster_url = re.findall(regex, output)
                return cluster_url[0]
        else:
            logging.critical('Cluster Creation Failed')
            exit(1)

    def _delete_cluster(self, cluster_command, yml_location):
        """
        :param yml_location: yml file location for deleting cluster
        :param cluster_command: command for cluster operation
        """
        output = None
        time.sleep(5)
        try:
            output = \
                subprocess.check_output("yes|%s delete-cluster --load %s" % (
                    cluster_command, yml_location), shell=True,
                    stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            logging.critical("Command Failed:Return Code:"+str(e.returncode))
            logging.critical("Command Failed:Output message:"+e.output)
            exit(1)
        logging.info("Cluster Deletion Completed")

    @atomic.action_timer("als.add_dea_to_cluster")
    def add_dea_to_cluster(self, cluster_command, yml_location):
        """
        :param yml_location: yml file location for adding dea to cluster
        :param cluster_command: command for cluster operation
        """
        output = None
        time.sleep(5)
        try:
            output = subprocess.check_output("%s add-role dea  --load %s" % (
                cluster_command, yml_location), shell=True,
                stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            logging.critical("Command Failed:Return Code:"+str(e.returncode))
            logging.critical("Command Failed:Output message:"+e.output)
            exit(1)
        logging.info("Add Dea Operation Completed")

    def _deploy_app(self, cluster_url, helion_path, app_path,
                    cluster_password, deployed_app_urls_loc,
                    deploy_docker_apps=False, docker_app_path=None, apps_dir_path):
        """Deploys all apps mentioned in app_path file.
           returns: The file with deployed apps url's.
        """
        cluster_username = self.cluster_prefix + "@test.com"
        app_reader = csv.reader(open(app_path, 'rb'))
        if deploy_docker_apps:
            docker_app_reader = csv.reader(open(docker_app_path, 'rb'))
        output = None
        conStatus = 1
        conOutput = None
        loginStatus = 1
        loginOutput = None
        deployStatus = 1
        deployOutput = None

        # Connnect to Cluster URL
        conStatus, conOutput = self.connectTarget(helion_path, cluster_url)
        time.sleep(2)

        # Login to Cluster URL
        if conStatus:
            logging.critical('Connect to %s is failed', cluster_url)
            logging.critical('Console output is %s', conOutput)
            exit(1)
        else:
            loginStatus, loginOutput = self.loginToTarget(
                helion_path, cluster_username, cluster_password)
        deploy_urls = None
        # Deploy App
        if loginStatus:
            logging.critical('Logging to Cluster is failed')
            logging.critical("Console output is %s ", loginOutput)
            exit(1)
        else:
            for app in reader:
                deployStatus, deployOutput = \
                    self.deployApp(helion_path, app[0], apps_dir_path)
        # Check Deploy
                if deployStatus:
                    logging.critical("Deploy App is failed.")
                    logging.critical("Console output is %s", deployOutput)
                else:
                    logging.info("Deploy App is succesful.")
                    logging.info("Console output is %s", deployOutput)
                    use_app = 'http:\/\/(.*)\/ deployed'
                    if re.search(use_app, deployOutput):
                        logging.info(
                            "Successfully Deployed app at path %s", app[0])
                        app = re.findall(use_app, deployOutput)
                        app = "http://" + app[0]
                        deploy_urls = \
                            deployed_app_urls_loc+self.cluster_prefix+".csv"
                        os.system("touch %s" % deploy_urls)
                        csv_writer = csv.writer(open(deploy_urls, 'a'))
                        csv_writer.writerow([app, ])
                        logging.info("urls written to csv")
            if deploy_docker_apps:
                for app in docker_app_reader:
                    deployStatus, deployOutput = \
                        self.deployDockerApp(helion_path, app[0])
                if deployStatus:
                    logging.critical("Deploy App is failed.")
                else:
                    logging.info("Deploy Docker App is succesful.")
                    logging.info("Console output is %s", deployOutput)
                    use_app = 'http:\/\/(.*)\/ deployed'
                    if re.search(use_app, deployOutput):
                        logging.info(
                            "Successfully Deployed Docker app at path %s",
                            app[0])
                        app = re.findall(use_app, deployOutput)
                        app = "http://" + app[0]
                        deploy_urls = \
                            deployed_app_urls_loc+self.cluster_prefix+".csv"
                        os.system("touch %s" % deploy_urls)
                        csv_writer = csv.writer(open(deploy_urls, 'a'))
                        csv_writer.writerow([app, ])
                        logging.info("urls written to csv")
        return deploy_urls

    def connectTarget(self, helion_path, cluster_url):
        logging.info("Connecting ...")
        targetCommand = helion_path + " target -n " + cluster_url
        status, output = self.executeShellCommand(targetCommand)
        logging.info("Connected to target")
        return status, output

    def executeShellCommand(self, strCommand):
        status, output = commands.getstatusoutput(strCommand)
        return status, output

    def loginToTarget(
            self, helionCLICommand, strUsr, strPasswd, strOrg=None,
            strSpc=None):
        logging.info("Logging in ...")
        if strOrg is None:
            strLoginCommand = helionCLICommand + " login -n " \
                + strUsr + " --password " + strPasswd
        else:
            strLoginCommand = helionCLICommand + " login -n " \
                + strUsr + " --password " + strPasswd + " --organization " \
                + strOrg + " --space " + strSpc
        status, output = self.executeShellCommand(strLoginCommand)
        logging.info("Logged into target")
        return status, output

    def deployApp(self, helionCLICommand, appLocation, appDirLocation):
        logging.info("deploying application ...")
        status = 1
        os.chdir(appDirLocation)
        git_url = "http://github.com"
        url  = git_url+"/"+appLocation
        git.Git().clone(url)
        os.chdir(appLocation)
        if (os.path.isfile("stackato.yml") or os.path.isfile("manifest.yml")):
            strDeployCommand = helionCLICommand + " push -n --timeout 5m"
            status, output = self.executeShellCommand(strDeployCommand)
        else:
            output = "Application configuration file is missing."
        return status, output

    def deployDockerApp(self, helionCLICommand, appLocation):
        logging.info("deploying docker application ...")
        status = 1
        app_folder = self.generate_random_name()
        os.chdir("..")
        os.mkdir(app_folder)
        os.chdir(app_folder)
        strDeployCommand = helionCLICommand + " push -n --docker-image " \
            + appLocation + " --timeout 5m "
        status, output = self.executeShellCommand(strDeployCommand)
        return status, output
