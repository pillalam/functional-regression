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
        super(TestHcfOrgSpaceDomain, cls).tearDownClass()
        hcf_organisations.delete_org(cls.setup_org, input_data=b'yes\n')
        hcf_auth.logout(cls.cluster_url)

    def test_hcf_org_space_domain(self):
        # Create Organisation
        org_name = 'og_test_org' + str(random.randint(1024, 4096))
        out, err = hcf_organisations.create_org(org_name)
        self.verify(org_name, out)
        self.verify("OK", out)

        # Get org info
        out, err = hcf_organisations.org_info(org_name)
        self.verify(org_name, out)

        # List Organisations
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

        # Get Space Info
        out, err = hcf_space.space(space_name)
        self.verify("Getting info for space", out)
        self.verify("OK", out)

        # Create Domain
        domain_name = 'testdomain' + str(random.randint(1024, 4096)) + '.com'
        hcf_domain.create_domain(org_name, domain_name)
        self.verify("OK", out)

        # List Domains
        out, err = hcf_domain.list_domain()
        self.verify("Getting domains in org", out)

        # List Router Groups
        out, err = hcf_domain.list_router_groups()
        self.verify("Getting router groups", out)

        # Delete domain
        hcf_auth.target(optional_args={'-o': org_name})
        out, err = hcf_domain.delete_domain(domain_name, input_data=b'yes\n')
        self.verify("OK", out)

        # Rename org
        new_org_name = 'new_og_test_org' + str(random.randint(1024, 4096))
        out, err = hcf_organisations.rename_org(org_name, new_org_name)
        self.verify(new_org_name, out)
        self.verify("OK", out)

        # Rename space
        new_space_name = 'new_sp_test_space' + str(random.randint(1024, 4096))
        out, err = hcf_space.rename_space(space_name, new_space_name)
        self.verify(new_space_name, out)
        self.verify("OK", out)

        # Delete space and org
        out, err = hcf_space.delete_space(new_space_name, input_data=b'yes\n')
        self.verify("OK", out)
        out, err = hcf_organisations.delete_org(
            new_org_name, input_data=b'yes\n')
        self.verify("OK", out)

    def test_hcf_create_duplicate_org(self):
        # Create Organization with duplicate name
        out, err = hcf_organisations.create_org(self.setup_org)
        self.verify("OK", out)
        self.verify("already exists", out)

    def test_hcf_get_nonexist_org(self):
        # Get org info for non-existing org
        orgname = 'noorg' + str(random.randint(1024, 4096))
        out, err = hcf_organisations.org_info(orgname)
        self.verify("FAILED", out)
        self.verify("not found", out)

    def test_hcf_create_org_without_quota(self):
        # Create Organization with non-existing quota
        quota_name = "no_quota" + str(random.randint(1024, 4096))
        out, err = hcf_organisations.create_org(
            self.setup_org, optional_args={'-q': quota_name})
        self.verify("FAILED", out)

    def test_hcf_rename_org_duplicate(self):
        # Create another Org for checking Rename org
        org_name1 = 'og_test_org' + str(random.randint(1024, 4096))
        out, err = hcf_organisations.create_org(org_name1)
        self.verify("OK", out)

        # Rename org with existing org (duplicate)
        out, err = hcf_organisations.rename_org(org_name1, self.setup_org)
        self.verify("FAILED", out)

        # Delete additional org created for renaming
        out, err = hcf_organisations.delete_org(org_name1, input_data=b'yes\n')
        self.verify("OK", out)

    def test_hcf_rename_space_duplicate(self):
        # Create another space for checking Rename space
        space_name1 = 'sp_test_space' + str(random.randint(1024, 4096))
        out, err = hcf_space.create_space(
            space_name1, optional_args={'-o': self.setup_org})
        self.verify("OK", out)

        # Rename space with existing space (duplicate)
        out, err = hcf_space.rename_space(space_name1, self.setup_space)
        self.verify("FAILED", out)

    def test_hcf_create_duplicate_space(self):
        # Create space with duplicate name
        out, err = hcf_space.create_space(
            self.setup_space, optional_args={'-o': self.setup_org})
        self.verify("OK", out)
        self.verify("already exists", out)

    def test_hcf_crete_space_without_org(self):
        # Create space with non-existing org
        space_name = "sp_name" + str(random.randint(1024, 4096))
        orgname = "noorg" + str(random.randint(1024, 4096))
        out, err = hcf_space.create_space(
            space_name, optional_args={'-o': orgname})
        self.verify("FAILED", out)

    def test_hcf_create_space_without_quota(self):
        # Create space with non-existing space-quota
        space_name = "sp_name" + str(random.randint(1024, 4096))
        quota_name = "quota" + str(random.randint(1024, 4096))
        out, err = hcf_space.create_space(
            space_name, optional_args={'-q': quota_name})
        self.verify("FAILED", out)

    def test_hcf_get_nonexist_space(self):
        # Get space info for non-existing space
        hcf_auth.target(optional_args={'-o': self.setup_org})
        space_name = 'nospace' + str(random.randint(1024, 4096))
        out, err = hcf_space.space(space_name)
        self.verify("FAILED", out)

    def test_hcf_delete_nonexist_space(self):
        # Delete non-existing space
        non_existing_space = "no_space_name" + str(random.randint(1024, 4096))
        hcf_auth.target(optional_args={'-o': self.setup_org})
        out, err = hcf_space.delete_space(non_existing_space,
                                          input_data=b'yes\n')
        self.verify("FAILED", out)

    def test_hcf_delete_nonexist_domain(self):
        # Delete non-existing domain
        hcf_auth.target(optional_args={'-o': self.setup_org})
        non_existing_domain = "no_domain" + str(random.randint(1024, 4096))
        out, err = hcf_domain.delete_domain(non_existing_domain,
                                            input_data=b'yes\n')
        self.verify("OK", out)
        self.verify("not found", out)

    def test_hcf_delete_nonexist_org(self):
        # Delete non-existing org
        non_existing_org = "no_org_name" + str(random.randint(1024, 4096))
        out, err = hcf_organisations.delete_org(non_existing_org,
                                                input_data=b'yes\n')
        self.verify("OK", out)
        self.verify("does not exist", out)

if __name__ == '__main__':
    base.unittest.main()
