import unittest
import os
import re
import ConfigParser


class BaseTest(unittest.TestCase):

    BASE_PATH = os.getcwd().split()[0]
    CONF_FILE = os.environ.get('READ CONFIG FILE', os.path.expanduser(
        BASE_PATH + '/config/catalog.conf'))
    Config = ConfigParser.ConfigParser()
    Config.read(CONF_FILE)
    CONF_SECTION_CONN = 'catalog-details'

    @classmethod
    def setUpClass(cls):
        cls.catalog_host = cls.Config.get(
            cls.CONF_SECTION_CONN, 'CATALOG_HOST')

    def verify(self, expression, output):
        if re.search(expression, output):
            return
        else:
            self.fail(output)
