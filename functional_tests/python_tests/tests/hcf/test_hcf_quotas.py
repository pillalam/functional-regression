import os
import sys
import re
import base
import random
from utils import hcf_auth
from utils import hcf_quotas
from utils import hcf_organisations


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
        self.verify(quota_name, out)

        # Create Org
        org_name = 'og_test_org' + str(random.randint(1024, 4096))
        out, err = hcf_organisations.create_org(org_name)
        self.verify(org_name, out)
        self.verify("OK", out)

        # Set Quota to Org
        out, err = hcf_quotas.set_quota(org_name, quota_name)
        self.verify("OK", out)

        # Delete Org
        out, err = hcf_organisations.delete_org(
            org_name, input_data=b'yes\n')

        # Delete Quotas
        out, err = hcf_quotas.delete_quota(
            quota_name, input_data=b'yes\n')
        self.verify("OK", out)


if __name__ == '__main__':
    base.unittest.main()
