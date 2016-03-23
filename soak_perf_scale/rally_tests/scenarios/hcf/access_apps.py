import csv
import random
import time
from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.als import utils
import logging


class AlsApps(utils.AlsScenario):
    """Basic benchmark scenarios for Als."""

    @scenario.configure(context={"cleanup": ["als"]})
    def access_apps(self, urls_path):
        """
           This method tests the usage of deployed apps from app_urls.csv,
           which are populated by deploy app method.
           param urls_path: path for csv file with app's to be used
        """

        reader = csv.reader(open(urls_path, 'rb'))
        for row in reader:
            if "fibonacci" not in row[0]:
                time.sleep(4)
                try:
                    self._use_app(row[0])
                except Exception:
                    logging.error('Url %s didnt return 200', row[0])

    @scenario.configure(context={"cleanup": ["als"]})
    def access_fibonacci_app(self, urls_path, fib_id_strt, fib_id_end):
        reader = csv.reader(open(urls_path, 'rb'))
        fib_id = random.randint(fib_id_strt, fib_id_end)
        for row in reader:
            if "fibonacci" in row[0]:
                try:
                    self._access_fib_app(row[0], fib_id)
                except Exception:
                    logging.error('Url %s didnt return 200', row[0])

    @scenario.configure(context={"cleanup": ["als"]})
    def access_deployment_test_app(self, urls_path, ver_start, ver_end,
                                   helionCLICommand, appLocation, cluster_url,
                                   username, password):
        reader = csv.reader(open(urls_path, 'rb'))
        for row in reader:
            if "deployment" in row[0]:
                ver = random.randint(ver_start, ver_end)
                try:
                    self.access_test_deploy_app(row[0], ver, helionCLICommand,
                                                appLocation, cluster_url,
                                                username, password)
                except Exception:
                    logging.error('Deployment Verification Failed')

    @scenario.configure(context={"cleanup": ["als"]})
    def access_mysql_db_app(self, urls_path):
        """ Checks the POST/GET API calls using Java, mysql """
        reader = csv.reader(open(urls_path, 'rb'))
        for row in reader:
            if "mysql" in row[0]:
                try:
                    data = self.post_data_mysqldb_app(row[0])
                    self.get_data_mysqldb_app(row[0], data)
                except Exception:
                    logging.error('Data POST/GET failed')
