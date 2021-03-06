import unittest
import os
import re
import ConfigParser


class BaseTest(unittest.TestCase):

    BASE_PATH = os.getcwd().split()[0]
    CONF_FILE = os.environ.get('READ CONFIG FILE', os.path.expanduser(
        BASE_PATH + '/config/hcf.conf'))
    Config = ConfigParser.ConfigParser()
    Config.read(CONF_FILE)
    CONF_SECTION_CONN = 'cluster-details'

    @classmethod
    def setUpClass(cls):
        cls.cluster_url = cls.Config.get(
            cls.CONF_SECTION_CONN, 'url')
        cls.username = cls.Config.get(
            cls.CONF_SECTION_CONN, 'username')
        cls.password = cls.Config.get(
            cls.CONF_SECTION_CONN, 'password')
        cls.app_path = cls.Config.get(
            cls.CONF_SECTION_CONN, 'app_path')
        cls.docker_image = cls.Config.get(
            'application-details', 'docker_image')
        cls.app_url = cls.Config.get(
            'application-details', 'git_url')
        cls.hsm_api = cls.Config.get(
            'hsm-service-details', 'api')
        cls.hsm_username = cls.Config.get(
            'hsm-service-details', 'username')
        cls.hsm_password = cls.Config.get(
            'hsm-service-details', 'password')
        cls.instance_name = cls.Config.get(
            'hsm-service-details', 'instance_name')
        cls.cf_instance_name = cls.Config.get(
            'hsm-service-details', 'cf_instance_name')

    def verify(self, expression, output):
        if re.search(expression, output):
            return
        else:
            self.fail(output)
