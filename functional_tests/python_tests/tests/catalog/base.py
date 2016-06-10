import unittest
import os
import re
import ConfigParser

from utils import catalog_service


class BaseTest(unittest.TestCase):

    @classmethod
    def get_instance_details(cls):
        '''This method fetches available services and
        forms json body for catalog instance creation'''
        expected_services = ['redis', 'vertica', 'spark', 'havenondemand',
                             'mysql', 'mysql-cluster', 'mongo', 'casandra',
                             'elasticsearch', 'dev-mysql']
        service_details = \
            list(set(cls.actual_services).intersection(set(expected_services)))
        instance_all_details = {}
        for service in service_details:
            instance_params = cls.read_from_config(service)
            instance_all_details[service] = instance_params
        return instance_all_details

    @classmethod
    def read_from_config(cls, CONF_SECTION):
        BASE_PATH = os.getcwd().split()[0]
        CONF_FILE = os.environ.get('READ CONFIG FILE', os.path.expanduser(
                                   BASE_PATH + '/config/catalog.conf'))
        cls.Config = ConfigParser.ConfigParser()
        cls.Config.read(CONF_FILE)
        cls.CONF_SECTION_CONN = CONF_SECTION
        options = cls.Config.options(CONF_SECTION)
        service_details = {}
        for option in options:
            service_details[option] = cls.Config.get(
                cls.CONF_SECTION_CONN, option)
        return service_details

    @classmethod
    def setUpClass(cls):
        cls.read_from_config(CONF_SECTION='catalog-details')
        cls.catalog_host = cls.Config.get(
            cls.CONF_SECTION_CONN, 'CATALOG_HOST')
        _, services = catalog_service.list_services(cls.catalog_host)
        cls.actual_services = []
        for s in services:
            cls.actual_services.append(s['id'].split(':')[1])
        cls.get_instance_details()

    def verify(self, expression, output):
        if re.search(expression, output):
            return
        else:
            self.fail(output)
