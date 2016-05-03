import os
import sys
import re
import base
import random
from utils import hcf_auth
from utils import hcf_users
from utils import hcf_space
from utils import hcf_organisations


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

        # Create an organisation to bind with user
        cls.org_name = 'og_test_org' + str(random.randint(1024, 4096))
        hcf_organisations.create_org(cls.org_name)

        # Create a space to bind with user
        out, err = hcf_auth.target(optional_args={'-o': cls.org_name})
        cls.space_name = 'sp_test_space' + str(random.randint(1024, 4096))
        out, err = hcf_space.create_space(cls.space_name)
        out, err = hcf_auth.target(optional_args={'-s': cls.space_name})

    @classmethod
    def tearDownClass(cls):
        super(TestHcfUsers, cls).tearDownClass()
        hcf_space.delete_space(cls.space_name, input_data=b'yes\n')
        hcf_organisations.delete_org(cls.org_name, input_data=b'yes\n')
        hcf_auth.logout(cls.cluster_url)

    def test_hcf_user_operations(self):
        # Create user
        user_name = 'hcf_test_user' + str(random.randint(1024, 4096))
        password = 'hcf-test-pwd' + str(random.randint(1024, 4096))
        out, err = hcf_users.create_user(user_name, password)
        self.verify(user_name, out)
        self.verify("OK", out)

        # Set role for user in an organisation
        org_role = "OrgManager"
        out, err = hcf_users.set_org_role(user_name, self.org_name, org_role)
        self.verify("OK", out)
        self.verify(self.org_name, out)
        self.verify(org_role, out)

        # Unset role for user in an organisation
        out, err = hcf_users.unset_org_role(user_name, self.org_name, org_role)
        self.verify("OK", out)
        self.verify(self.org_name, out)

        # Set role for user in a space
        space_role = "SpaceDeveloper"
        out, err = hcf_users.set_space_role(
            user_name, self.org_name, self.space_name, space_role)
        self.verify("OK", out)
        self.verify(self.space_name, out)
        self.verify(space_role, out)

        # Unset role for user in a space
        out, err = hcf_users.unset_space_role(
            user_name, self.org_name, self.space_name, space_role)
        self.verify("OK", out)
        self.verify(self.space_name, out)

        # Delete User
        out, err = hcf_users.delete_user(
            user_name, input_data=b'yes\n')
        self.verify("OK", out)

if __name__ == '__main__':
    base.unittest.main()
