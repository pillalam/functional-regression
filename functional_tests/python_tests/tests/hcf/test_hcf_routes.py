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
from utils import hcf_routes
from utils import hcf_domain
from urlparse import urlparse
from utils import common


class TestHcfRoutes(base.BaseTest):

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
        super(TestHcfRoutes, cls).setUpClass()

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
        parsed = urlparse(cls.app_url)
        link = parsed.path.split('/')
        cls.app_dir = link[len(link)-1]

    @classmethod
    def tearDownClass(cls):
        super(TestHcfRoutes, cls).tearDownClass()

        # Delete org
        out, err = hcf_organisations.delete_org(
            cls.org_name, input_data=b'yes\n')

        # Logout from Cluster
        hcf_auth.logout(cls.cluster_url)
        if os.path.isdir(cls.app_dir):
            common.executeShellCommand(
                'rm -rf ' + str(cls.app_dir))

    def test_hcf_routes_(self):
        # Target space
        out, err = hcf_auth.target(optional_args={'-s': self.space_name})

        # Create Domain
        domain_name = 'domain' + str(random.randint(1024, 4096)) + '.com'
        out, err = hcf_domain.create_domain(self.org_name, domain_name)
        self.verify(domain_name, out)
        self.verify("OK", out)

        # Create Route
        out, err = hcf_routes.create_route(self.space_name, domain_name)
        self.verify("Creating route", out)
        self.verify("OK", out)

        # Target space
        out, err = hcf_auth.target(optional_args={'-s': self.space_name})

        # List Routes
        out, err = hcf_routes.list_routes()
        self.verify("Getting routes", out)

        # download app
        out, err = hcf_apps.downloadApplication(self.app_url, self.app_dir)

        # Push application
        out, err = hcf_apps.push_app(self.app_dir, self.app_dir)

        # verify if application deployed successfully
        time.sleep(60)
        self.verify("App started", out)

        # map route to app
        out, err = hcf_routes.map_route(self.app_dir, domain_name)
        self.verify("Adding route " + domain_name + " to app", out)
        self.verify("OK", out)

        # unmap route from app
        out, err = hcf_routes.unmap_route(self.app_dir, domain_name)
        self.verify("Removing route " + domain_name + " from app", out)
        self.verify("OK", out)

        # Delete routes
        out, err = hcf_routes.delete_orphaned_routes(input_data=b'yes\n')
        self.verify("Deleting route", out)
        self.verify("OK", out)

if __name__ == '__main__':
    base.unittest.main(verbosity=2)
