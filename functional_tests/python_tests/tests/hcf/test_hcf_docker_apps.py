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


class TestHcfDockerApps(base.BaseTest):

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
        super(TestHcfDockerApps, cls).setUpClass()

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
        super(TestHcfDockerApps, cls).tearDownClass()

        # Delete org
        out, err = hcf_organisations.delete_org(
            cls.org_name, input_data=b'yes\n')

        # Logout from Cluster
        hcf_auth.logout(cls.cluster_url)

    def test_hcf_docker_apps(self):

        # Target space
        out, err = hcf_auth.target(optional_args={'-s': self.space_name})

        # Enable diego_docker feature flag
        feature_name = "diego_docker"
        out, err = hcf_apps.feature_flag(feature_name)
        while True:
            if "enabled" in out:
                break
            else:
                out, err = hcf_apps.enable_feature_flag(feature_name)
                self.verify("Feature " + feature_name + " Enabled", out)
                break

        # Push Docker application
        docker_app_name = 'docker_test_app' + str(random.randint(1024, 4096))
        docker_app_out, err = hcf_apps.push_docker_app(
            docker_app_name, optional_args={'-o': self.docker_image})
        time.sleep(60)
        self.verify("App started", docker_app_out)

        # Show docker application
        out, err = hcf_apps.show_app(docker_app_name)
        self.verify(docker_app_name, out)

        # List application
        out, err = hcf_apps.list_apps()
        self.verify(docker_app_name, out)

        # Delete docker application
        out, err = hcf_apps.delete_app(docker_app_name, input_data=b'yes\n')
        self.verify("OK", out)

if __name__ == '__main__':
    base.unittest.main(verbosity=2)
