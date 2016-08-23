import unittest
import os
import re
import ConfigParser


class BaseTest(unittest.TestCase):

    BASE_PATH = os.getcwd().split()[0]
    CONF_FILE = os.environ.get('READ CONFIG FILE', os.path.expanduser(
        BASE_PATH + '/config/hce.conf'))
    Config = ConfigParser.ConfigParser()
    Config.read(CONF_FILE)
    CONF_SECTION_CONN = 'api-details'

    @classmethod
    def setUpClass(cls):
        cls.cluster_url = cls.Config.get(
            cls.CONF_SECTION_CONN, 'url')
        cls.username = cls.Config.get(
            cls.CONF_SECTION_CONN, 'username')
        cls.password = cls.Config.get(
            cls.CONF_SECTION_CONN, 'password')
        cls.cf_url = cls.Config.get(
            'cf-cluster-details', 'cf_url')
        cls.cf_username = cls.Config.get(
            'cf-cluster-details', 'cf_username')
        cls.cf_password = cls.Config.get(
            'cf-cluster-details', 'cf_password')
        cls.cf_org = cls.Config.get(
            'cf-cluster-details', 'cf_org')
        cls.cf_space = cls.Config.get(
            'cf-cluster-details', 'cf_space')
        cls.branch = cls.Config.get(
            'project-details', 'branch')
        cls.ref_string = cls.Config.get(
            'project-details', 'ref_string')
        cls.repo_url = cls.Config.get(
            'project-details', 'repo_url')
        cls.container_id = cls.Config.get(
            'project-details', 'container_id')
        cls.repo_username = cls.Config.get(
            'project-details', 'repo_username')
        cls.repo_password = cls.Config.get(
            'project-details', 'repo_password')

    def verify(self, expression, output):
        if re.search(expression, output):
            return
        else:
            self.fail(output)
