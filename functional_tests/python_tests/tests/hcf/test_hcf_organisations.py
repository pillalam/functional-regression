import os
import sys
import re
import base
import random
from utils import hcf_auth
from utils import hcf_organisations

class TestHcfOrganisations(base.BaseTest):

    """
    SetupClass prepares the following preconditions for
    Organisation tests
    * Connect to the cluster URI target
    """

    @classmethod
    def setUpClass(cls):
        super(TestHcfOrganisations, cls).setUpClass()

        # Connect to the cluster URI target
        hcf_auth.connect_target(cls.cluster_url,
                                optional_args={'--skip-ssl-validation': ' '})
        # Loginto Cluster using creds
        hcf_auth.login(optional_args={'-u': cls.username, '-p': cls.password})

    @classmethod
    def tearDownClass(cls):
        super(TestHcfOrganisations, cls).tearDownClass()
        hcf_auth.logout(cls.cluster_url)

    def test_hcf_create_list_delete_org(self):
        # Create Organisation
        org_name = 'og_test_org' + str(random.randint(1024, 4096))
        out, err = hcf_organisations.create_org(org_name)
        self.verify(org_name, out)
        self.verify("OK", out)

        # List Organisation
        out, err = hcf_organisations.list_orgs()
        self.verify(org_name, out)

        # Delete Organisation
        out, err = hcf_organisations.delete_org(
            org_name, input_data=b'yes\n')
        self.verify("OK", out)

if __name__ == '__main__':
    base.unittest.main()
