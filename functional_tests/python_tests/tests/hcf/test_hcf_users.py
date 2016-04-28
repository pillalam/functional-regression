import os
import sys
import re
import base
import random
from utils import hcf_auth
from utils import hcf_users


class TestHcfUsers(base.BaseTest):

    """
    SetupClass prepares the following preconditions for
    Hcf User tests
    * Connect to the cluster URI target
    """

    @classmethod
    def setUpClass(cls):
        super(TestHcfUsers, cls).setUpClass()

        # Connect to the cluster URI target
        hcf_auth.connect_target(cls.cluster_url,
                                optional_args={'--skip-ssl-validation': ' '})
        # Loginto Cluster using creds
        hcf_auth.login(optional_args={'-u': cls.username, '-p': cls.password})

    @classmethod
    def tearDownClass(cls):
        super(TestHcfUsers, cls).tearDownClass()
        hcf_auth.logout(cls.cluster_url)

    def test_hcf_create_delete_user(self):
        # Create User
        user_name = 'hcf_test_user' + str(random.randint(1024, 4096))
        password = 'hcf-test-pwd' + str(random.randint(1024, 4096))
        out, err = hcf_users.create_user(user_name, password)
        self.verify(user_name, out)
        self.verify("OK", out)

        # Delete User
        out, err = hcf_users.delete_user(
            user_name, input_data=b'yes\n')
        self.verify("OK", out)

if __name__ == '__main__':
    base.unittest.main()
