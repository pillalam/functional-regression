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

        # Create Domain
        cls.domain_name = 'domain' + str(random.randint(1024, 4096)) + '.com'
        out, err = hcf_domain.create_domain(cls.org_name, cls.domain_name)

    @classmethod
    def tearDownClass(cls):
        super(TestHcfRoutes, cls).tearDownClass()
        # Delete Domain
        hcf_auth.target(optional_args={'-o': cls.org_name})
        out, err = hcf_domain.delete_domain(cls.domain_name,
                                            input_data=b'yes\n')

        # Delete org
        out, err = hcf_organisations.delete_org(
            cls.org_name, input_data=b'yes\n')

        # Logout from Cluster
        hcf_auth.logout(cls.cluster_url)
        if os.path.isdir(cls.app_dir):
            common.executeShellCommand(
                'rm -rf ' + str(cls.app_dir))

    def test_hcf_routes(self):
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

        # map route to non-existing domain
        domainname = "nodoamin"
        out, err = hcf_routes.map_route(self.app_dir, domainname)
        self.verify("FAILED", out)

        # unmap route to non-existing domain
        domainname = "nodoamin"
        out, err = hcf_routes.unmap_route(self.app_dir, domainname)
        self.verify("FAILED", out)

        # Delete routes
        out, err = hcf_routes.delete_orphaned_routes(input_data=b'yes\n')
        self.verify("Deleting route", out)
        self.verify("OK", out)

    def test_hcf_create_duplicate_route(self):
        # Target space and create Route
        out, err = hcf_auth.target(optional_args={'-o': self.org_name,
                                                  '-s': self.space_name})
        out, err = hcf_routes.create_route(self.space_name, self.domain_name)

        # Create Duplicate Route
        out, err = hcf_auth.target(optional_args={'-o': self.org_name,
                                                  '-s': self.space_name})
        out, err = hcf_routes.create_route(self.space_name, self.domain_name)
        self.verify("already exists", out)

        # Delete Route
        hcf_auth.target(optional_args={'-o': self.org_name})
        out, err = hcf_routes.delete_route(self.domain_name,
                                           input_data=b'yes\n')
        self.verify("OK", out)

    def test_hcf_create_route_without_space(self):
        # Create Route with non-existing space
        spacename = "nospace"
        out, err = hcf_routes.create_route(spacename, self.domain_name)
        self.verify("FAILED", out)

    def test_hcf_create_route_without_domain(self):
        # Create Route with non-existing domain
        domainname = "nodomain"
        out, err = hcf_routes.create_route(self.space_name, domainname)
        self.verify("FAILED", out)

    def test_hcf_create_route_invalid_host(self):
        # Create Route with invalid host
        hostname = "invali_host@@@"
        out, err = hcf_routes.create_route(self.space_name, self.domain_name,
                                           optional_args={'-n': hostname})
        self.verify("FAILED", out)

    def test_hcf_create_route_invalid_path(self):
        # Create Route with invalid path
        path = "nopath"
        out, err = hcf_routes.create_route(self.space_name, self.domain_name,
                                           optional_args={'-p': path})
        self.verify("FAILED", out)

    def test_hcf_check_route_without_path(self):
        # Check Route with non-existing host
        hostname = "nohost"
        out, err = hcf_routes.check_route(hostname, self.domain_name)
        self.verify("does not exist", out)

    def test_hcf_map_route_without_app(self):
        # Map Route with non-existing app
        appname = "noapp"
        out, err = hcf_routes.map_route(appname, self.domain_name)
        self.verify("FAILED", out)

    def test_hcf_unmap_route_without_app(self):
        appname = "noapp"
        # Unmap Route with non-existing domain
        out, err = hcf_routes.unmap_route(appname, self.domain_name)
        self.verify("FAILED", out)

    def test_hcf_delete_route_without_domain(self):
        # Delete Route with non-existing domain
        domainname = "nodomain"
        out, err = hcf_routes.delete_route(domainname, input_data=b'yes\n')
        self.verify("FAILED", out)

if __name__ == '__main__':
    base.unittest.main()
