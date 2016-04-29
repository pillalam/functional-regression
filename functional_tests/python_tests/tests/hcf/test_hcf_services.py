import os
import sys
import re
import base
import random
from utils import hcf_auth
from utils import hcf_organisations
from utils import hcf_services
from utils import hcf_space


class TestHcfServices(base.BaseTest):

    """
    SetupClass prepares the following preconditions for
    Services tests
    * Connect to the cluster URI target
    * Create Organisation and space
    """

    @classmethod
    def setUpClass(cls):
        super(TestHcfServices, cls).setUpClass()

        # Connect to the cluster URI target
        hcf_auth.connect_target(cls.cluster_url,
                                optional_args={'--skip-ssl-validation': ' '})
        # Loginto Cluster using creds
        hcf_auth.login(optional_args={'-u': cls.username, '-p': cls.password})
        # Create and target Organisation
        cls.setup_org = 'og_test_org' + str(random.randint(1024, 4096))
        out, err = hcf_organisations.create_org(cls.setup_org)
        out, err = hcf_auth.target(optional_args={'-o': cls.setup_org})
        # Create and target Space
        cls.setup_space = 'sp_test_space' + str(random.randint(1024, 4096))
        out, err = hcf_space.create_space(cls.setup_space)
        out, err = hcf_auth.target(optional_args={'-o': cls.setup_org,
                                   '-s': cls.setup_space})

    @classmethod
    def tearDownClass(cls):
        super(TestHcfServices, cls).tearDownClass()
        hcf_space.delete_space(cls.setup_space, input_data=b'yes\n')
        hcf_organisations.delete_org(cls.setup_org, input_data=b'yes\n')
        hcf_auth.logout(cls.cluster_url)

    def test_hcf_list_services(self):
        # List all services
        out, err = hcf_services.list_services()
        self.verify(
            "Getting services in org " + self.setup_org + ""
            " / space " + self.setup_space + " as hdpqa@hp.com...",
            out)
        self.verify("OK", out)

if __name__ == '__main__':
    base.unittest.main()
