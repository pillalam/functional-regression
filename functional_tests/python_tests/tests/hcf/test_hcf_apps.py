import os
import sys
import re
import base
import random
import time

from utils import hcf_auth
from utils import hcf_organisations
from utils import hcf_space
from utils import hcf_apps


class TestHcfApps(base.BaseTest):

    """
    SetupClass prepares the following preconditions for
    Application tests
    * Connect to the cluster URI target
    * Login to the cluster
    * Create Organisation
    * Create Space
    """

    @classmethod
    def setUpClass(cls):
        super(TestHcfApps, cls).setUpClass()

        # Connect to the cluster URI target
        hcf_auth.connect_target(cls.cluster_url,
                                optional_args={'--skip-ssl-validation': ' '})
        # Loginto Cluster using creds
        hcf_auth.login(optional_args={'-u': cls.username, '-p': cls.password})

        # Create Organisation
        cls.org_name = 'og_test_org' + str(random.randint(1024, 4096))
        out, err = hcf_organisations.create_org(cls.org_name)

        # Create Space
        out, err = hcf_auth.target(optional_args={'-o': cls.org_name})
        cls.space_name = 'sp_test_space' + str(random.randint(1024, 4096))
        out, err = hcf_space.create_space(cls.space_name)

    @classmethod
    def tearDownClass(cls):
        super(TestHcfApps, cls).tearDownClass()

        # Delete org
        out, err = hcf_organisations.delete_org(
            cls.org_name, input_data=b'yes\n')

        # Logout from Cluster
        hcf_auth.logout(cls.cluster_url)

    def test_hcf_apps(self):

        # Target space
        out, err = hcf_auth.target(optional_args={'-s': self.space_name})

        # Push application
        out, err = hcf_apps.push_app(self.app_dir, self.app_path)

        # verify if application deployed successfully
        time.sleep(60)
        self.verify("deployed", out)
        regex2 = 'http:\/\/(.+?)\/ deployed'
        app_url = re.findall(regex2, out)
        r = requests.get("http://" + app_url[0])
        self.assertEqual(200, r.status_code)

        # List application
        out, err = hcf_apps.list_apps()
        self.verify(self.app_dir, out)

        # Scale application
        mem_limit = "1G"
        disk_limit = "1G"
        no_of_instances = "2"
        out, err = hcf_apps.scale_app(
            self.app_dir, optional_args={
                '-i': no_of_instances,
                '-k': disk_limit,
                '-m': mem_limit, '-f': ' '})
        self.verify("OK", out)

        # Delete application
        out, err = hcf_apps.delete_app(self.app_dir, input_data=b'yes\n')
        self.verify("OK", out)

if __name__ == '__main__':
    base.unittest.main()
