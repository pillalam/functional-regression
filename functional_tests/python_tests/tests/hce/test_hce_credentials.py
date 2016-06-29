import os
import sys
import re
import base
import random
from utils import hce_auth
from utils import hce_credentials


class TestHceCredentials(base.BaseTest):

    """
    SetupClass prepares the following preconditions
    """

    @classmethod
    def setUpClass(cls):
        super(TestHceCredentials, cls).setUpClass()

        # Login to Cluster using credentials
        hce_auth.login(cls.username, cls.password)

    @classmethod
    def tearDownClass(cls):
        super(TestHceCredentials, cls).tearDownClass()
        hce_auth.logout()

    def test_hce_credentials(self):
        # List Credentials
        out, err = hce_credentials.list_credentials()


if __name__ == '__main__':
    base.unittest.main()
