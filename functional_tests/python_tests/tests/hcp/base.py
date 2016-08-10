import unittest
import os
import re
import ConfigParser


class BaseTest(unittest.TestCase):

    BASE_PATH = os.getcwd().split()[0]
    CONF_FILE = os.environ.get('READ CONFIG FILE', os.path.expanduser(
        BASE_PATH + '/config/hcp.conf'))
    Config = ConfigParser.ConfigParser()
    Config.read(CONF_FILE)
    CONF_SECTION_CONN = 'api-details'

    @classmethod
    def setUpClass(cls):
        cls.api_url = cls.Config.get(
            cls.CONF_SECTION_CONN, 'url')
        cls.username = cls.Config.get(
            cls.CONF_SECTION_CONN, 'username')
        cls.password = cls.Config.get(
            cls.CONF_SECTION_CONN, 'password')

    def verify(self, expression, output):
        if re.search(expression, output):
            return
        else:
            self.fail(output)
