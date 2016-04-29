import os
import sys
import re
import base
import random
from utils import hcf_auth
from utils import hcf_organisations
from utils import hcf_space
from utils import hcf_domain


class TestHcfOrgSpaceDomain(base.BaseTest):

    """
    SetupClass prepares the following preconditions for
    Organisation, Space and Domain tests
    * Connect to the cluster URI target
    """

    @classmethod
    def setUpClass(cls):
        super(TestHcfOrgSpaceDomain, cls).setUpClass()

        # Connect to the cluster URI target
        hcf_auth.connect_target(cls.cluster_url,
                                optional_args={'--skip-ssl-validation': ' '})
        # Loginto Cluster using creds
        hcf_auth.login(optional_args={'-u': cls.username, '-p': cls.password})

    @classmethod
    def tearDownClass(cls):
        super(TestHcfOrgSpaceDomain, cls).tearDownClass()
        hcf_auth.logout(cls.cluster_url)

    def test_hcf_org_space_domain(self):
        # Create Organisation
        org_name = 'og_test_org' + str(random.randint(1024, 4096))
        out, err = hcf_organisations.create_org(org_name)
        self.verify(org_name, out)
        self.verify("OK", out)

        # List Organisation
        out, err = hcf_organisations.list_orgs()
        self.verify(org_name, out)

        # Create Space
        out, err = hcf_auth.target(optional_args={'-o': org_name})
        space_name = 'sp_test_space' + str(random.randint(1024, 4096))
        out, err = hcf_space.create_space(space_name)
        self.verify(space_name, out)
        self.verify("OK", out)

        # List Spaces
        out, err = hcf_space.list_space()
        self.verify(space_name, out)

        # List Domains
        out, err = hcf_domain.list_domain()
        self.verify("Getting domains in org " + org_name, out)

        # Delete space and org
        out, err = hcf_space.delete_space(space_name, input_data=b'yes\n')
        self.verify("OK", out)
        out, err = hcf_organisations.delete_org(
            org_name, input_data=b'yes\n')
        self.verify("OK", out)

if __name__ == '__main__':
    base.unittest.main()
