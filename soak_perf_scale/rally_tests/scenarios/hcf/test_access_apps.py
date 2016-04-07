import csv
from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.hcf import utils
import logging


class CfAppAccess(utils.CfScenario):
    """Basic benchmark scenarios """

    @scenario.configure()
    def access_apps(self, urls_path):
        """
           This method tests the usage of deployed apps from apps_url_list.csv,
           param urls_path: path for csv file with app's to be used
        """

        reader = csv.reader(open(urls_path, 'rb'))
        for row in reader:
                try:
                    self._use_app(row[0])
                except Exception:
                    logging.error('Url %s didnt return 200', row[0])
