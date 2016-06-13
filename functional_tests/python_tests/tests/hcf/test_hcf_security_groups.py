import os
import sys
import re
import base
import random

from utils import hcf_auth
from utils import hcf_organisations
from utils import hcf_space
from utils import hcf_security_groups


class TestHcfSecurityGroups(base.BaseTest):

    """
    SetupClass prepares the following preconditions for
    Organisation, Space and Domain tests
    * Connect to the cluster URI target
    """

    @classmethod
    def setUpClass(cls):
        super(TestHcfSecurityGroups, cls).setUpClass()

        # Connect to the cluster URI target
        hcf_auth.connect_target(cls.cluster_url,
                                optional_args={'--skip-ssl-validation': ' '})
        # Loginto Cluster using creds
        hcf_auth.login(optional_args={'-u': cls.username, '-p': cls.password})

        # Create Organisation
        cls.org_name = 'org_test' + str(random.randint(1024, 4096))
        out, err = hcf_organisations.create_org(cls.org_name)

        # Create Space
        out, err = hcf_auth.target(optional_args={'-o': cls.org_name})
        cls.space_name = 'space_test' + str(random.randint(1024, 4096))
        out, err = hcf_space.create_space(cls.space_name)

    @classmethod
    def tearDownClass(cls):
        # Delete org
        out, err = hcf_organisations.delete_org(
            cls.org_name, input_data=b'yes\n')

        super(TestHcfSecurityGroups, cls).tearDownClass()
        hcf_auth.logout(cls.cluster_url)

    def test_hcf_create_delete_security_group(self):
        # Create Security Group Rules File
        jsonFileName = hcf_security_groups.create_secgroup_rule_json()

        # Create Security Group
        secgroup_name = 'sg_test' + str(random.randint(1024, 4096))
        out, err = hcf_security_groups.create_security_group(secgroup_name,
                                                             jsonFileName)
        self.verify(secgroup_name, out)
        self.verify("OK", out)

        # List Security Groups
        out, err = hcf_security_groups.list_security_groups()
        self.verify(secgroup_name, out)
        self.verify("OK", out)

        # Target space
        out, err = hcf_auth.target(optional_args={'-o': self.org_name,
                                                  '-s': self.space_name})

        # Bind Security Group
        out, err = hcf_security_groups.bind_security_group(
            secgroup_name, self.org_name, self.space_name)
        self.verify("Assigning security group ", out)
        self.verify("OK", out)

        # Unbind Security Group
        out, err = hcf_security_groups.unbind_security_group(
            secgroup_name, self.org_name, self.space_name)
        self.verify("Unbinding security group ", out)
        self.verify("OK", out)

        # Bind Staging Security Group
        out, err = hcf_security_groups.bind_staging_security_group(
            secgroup_name)
        self.verify("Binding security group " + secgroup_name +
                    " to staging", out)
        self.verify("OK", out)

        # List Staging Security Groups
        out, err = hcf_security_groups.list_staging_security_groups()
        self.verify(secgroup_name, out)

        # Unbind Staging Security Group
        out, err = hcf_security_groups.unbind_staging_security_group(
            secgroup_name)
        self.verify("Unbinding security group " + secgroup_name +
                    " from defaults for staging", out)
        self.verify("OK", out)

        # Bind Running Security Group
        out, err = hcf_security_groups.bind_running_security_group(
            secgroup_name)
        self.verify("Binding security group " + secgroup_name +
                    " to defaults for running", out)
        self.verify("OK", out)

        # List Running Security Groups
        out, err = hcf_security_groups.list_running_security_groups()
        self.verify(secgroup_name, out)

        # Unbind Running Security Group
        out, err = hcf_security_groups.unbind_running_security_group(
            secgroup_name)
        self.verify("Unbinding security group " + secgroup_name +
                    " from defaults for running", out)
        self.verify("OK", out)

        # Delete Security Group and Rules file
        out, err = hcf_security_groups.delete_security_group(
            secgroup_name, input_data=b'yes\n')
        self.verify("Deleting security group", out)
        self.verify("OK", out)
        os.remove(jsonFileName)

if __name__ == '__main__':
    base.unittest.main()
