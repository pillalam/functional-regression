import os
import sys
import re
import base
import random

from utils import hcf_auth
from utils import hcf_quotas
from utils import hcf_organisations
from utils import hcf_space


class TestHcfQuotas(base.BaseTest):

    """
    SetupClass prepares the following preconditions for
    Quota tests
    * Connect to the cluster URI target
    """

    @classmethod
    def setUpClass(cls):
        super(TestHcfQuotas, cls).setUpClass()

        # Connect to the cluster URI target
        hcf_auth.connect_target(cls.cluster_url,
                                optional_args={'--skip-ssl-validation': ' '})
        # Loginto Cluster using creds
        hcf_auth.login(optional_args={'-u': cls.username, '-p': cls.password})

    @classmethod
    def tearDownClass(cls):
        super(TestHcfQuotas, cls).tearDownClass()
        hcf_auth.logout(cls.cluster_url)

    def test_hcf_create_delete_quota(self):
        # Create Quota
        quota_name = 'quota_test' + str(random.randint(1024, 4096))
        out, err = hcf_quotas.create_quota(quota_name)
        self.verify(quota_name, out)
        self.verify("OK", out)

        # List Quotas
        out, err = hcf_quotas.list_quotas()
        self.verify("Getting quotas", out)
        self.verify("OK", out)

        # Display Quota Info
        out, err = hcf_quotas.quota_info(quota_name)
        self.verify("OK", out)

        # Update Quota
        out, err = hcf_quotas.update_quota(quota_name,
                                           optional_args={'-m': '1G'})
        self.verify("OK", out)

        # Create Org
        org_name = 'og_test_org' + str(random.randint(1024, 4096))
        out, err = hcf_organisations.create_org(org_name)
        self.verify(org_name, out)
        self.verify("OK", out)

        # Set Quota to Org
        out, err = hcf_quotas.set_quota(org_name, quota_name)
        self.verify("Setting quota " + quota_name + " to org " + org_name, out)
        self.verify("OK", out)

        # Set Target to Org
        out, err = hcf_quotas.set_target(optional_args={'-o': org_name})

        # Create Space-Quota
        space_quota_name = 'sp_quota_test' + str(random.randint(1024, 4096))
        out, err = hcf_quotas.create_space_quota(space_quota_name)
        self.verify(space_quota_name, out)
        self.verify("OK", out)

        # Create Space
        space_name = 'sp_test' + str(random.randint(1024, 4096))
        out, err = hcf_space.create_space(space_name)
        self.verify(space_name, out)
        self.verify("OK", out)

        # Update Space Quota
        out, err = hcf_quotas.update_space_quota(space_quota_name,
                                                 optional_args={'-s': '150'})
        self.verify("OK", out)

        # Display Space Quota Info
        out, err = hcf_quotas.space_quota_info(space_quota_name)
        self.verify("OK", out)

        # Set Space-Quota to Space
        out, err = hcf_quotas.set_space_quota(space_name, space_quota_name)
        self.verify("Assigning space quota " + space_quota_name, out)
        self.verify("OK", out)

        # List Space-Quotas
        out, err = hcf_quotas.list_space_quotas()
        self.verify("Getting space quotas", out)
        self.verify("OK", out)

        # Unset Space-Quota
        out, err = hcf_quotas.unset_space_quota(space_name, space_quota_name)
        self.verify("Unassigning space quota " + space_quota_name, out)
        self.verify("OK", out)

        # Delete Space-Quota
        out, err = hcf_quotas.delete_space_quota(
            space_quota_name, input_data=b'yes\n')
        self.verify("Deleting space quota " + space_quota_name, out)
        self.verify("OK", out)

        # Delete Space
        out, err = hcf_space.delete_space(
            space_name, input_data=b'yes\n')
        self.verify("OK", out)

        # Delete Org
        out, err = hcf_organisations.delete_org(
            org_name, input_data=b'yes\n')
        self.verify("OK", out)

        # Delete Quota
        out, err = hcf_quotas.delete_quota(
            quota_name, input_data=b'yes\n')
        self.verify("Deleting quota", out)
        self.verify("OK", out)

if __name__ == '__main__':
    base.unittest.main()
