import os
import sys
import re
import base
import random

from utils import hcf_auth
from utils import hcf_organisations
from utils import hcf_marketplace
from utils import hcf_space


class TestHcfMarketplace(base.BaseTest):

    """
    SetupClass prepares the following preconditions for
    Marketplace tests
    * Connect to the cluster URI target
    """

    @classmethod
    def setUpClass(cls):
        super(TestHcfMarketplace, cls).setUpClass()

        # Connect to the cluster URI target
        hcf_auth.connect_target(cls.cluster_url,
                                optional_args={'--skip-ssl-validation': ' '})
        # Log into Cluster using creds
        hcf_auth.login(optional_args={'-u': cls.username, '-p': cls.password})
        # Create organisation
        cls.setup_org = 'og_test_org' + str(random.randint(1024, 4096))
        out, err = hcf_organisations.create_org(cls.setup_org)
        out, err = hcf_auth.target(optional_args={'-o': cls.setup_org})
        # Create Space
        cls.setup_space = 'sp_test_space' + str(random.randint(1024, 4096))
        out, err = hcf_space.create_space(cls.setup_space)
        out, err = hcf_auth.target(optional_args={'-o': cls.setup_org,
                                                  '-s': cls.setup_space})

    @classmethod
    def tearDownClass(cls):
        super(TestHcfMarketplace, cls).tearDownClass()
        hcf_organisations.delete_org(cls.setup_org, input_data=b'yes\n')
        hcf_auth.logout(cls.cluster_url)

    def test_hcf_marketplace(self):
        # List all offerings
        out, err = hcf_marketplace.marketplace()
        self.verify("OK", out)
        self.verify(
            "Getting services from marketplace in org " + self.setup_org + ""
            " / space " + self.setup_space, out)

if __name__ == '__main__':
    base.unittest.main()
