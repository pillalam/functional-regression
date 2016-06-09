import os
import sys
import re
import base
import random

from utils import hcf_auth
from utils import hcf_organisations
from utils import hcf_space
from utils import hcf_domain
from utils import hcf_apps
from utils import hcf_routes


class TestHcfRoutes(base.BaseTest):

    """
    SetupClass prepares the following preconditions for
    Organisation, Space and Domain tests
    * Connect to the cluster URI target
    """

    @classmethod
    def setUpClass(cls):
        super(TestHcfRoutes, cls).setUpClass()

        # Connect to the cluster URI target
        hcf_auth.connect_target(cls.cluster_url,
                                optional_args={'--skip-ssl-validation': ' '})
        # Loginto Cluster using creds
        hcf_auth.login(optional_args={'-u': cls.username, '-p': cls.password})

    @classmethod
    def tearDownClass(cls):
        super(TestHcfRoutes, cls).tearDownClass()
        hcf_auth.logout(cls.cluster_url)

    def test_hcf_create_delete_route(self):
        # Create Organisation
        org_name = 'og_test_org' + str(random.randint(1024, 4096))
        out, err = hcf_organisations.create_org(org_name)
        self.verify(org_name, out)
        self.verify("OK", out)

        # Create Space
        out, err = hcf_auth.target(optional_args={'-o': org_name})
        space_name = 'sp_test_space' + str(random.randint(1024, 4096))
        out, err = hcf_space.create_space(space_name)
        self.verify(space_name, out)
        self.verify("OK", out)

        # Create Domain
        domain_name = 'domain' + str(random.randint(1024, 4096)) + '.com'
        out, err = hcf_domain.create_domain(org_name, domain_name)
        self.verify(domain_name, out)
        self.verify("OK", out)

        # Create Route
        out, err = hcf_routes.create_route(space_name, domain_name)
        self.verify("Creating route", out)
        self.verify("OK", out)

        # Target space
        out, err = hcf_auth.target(optional_args={'-s': space_name})

        # List Routes
        out, err = hcf_routes.list_routes()
        self.verify("Getting routes", out)

        # push app
        app_name = 'test_app' + str(random.randint(1024, 4096))
        out, err = hcf_apps.push_app(app_name,
                                     optional_args={'-f': self.app_path})

        self.verify("Creating app " + app_name, out)
        self.verify("App started", out)

        # map route to app
        out, err = hcf_routes.map_route(app_name, domain_name)
        self.verify("Adding route " + domain_name + " to app", out)
        self.verify("OK", out)

        # unmap route from app
        out, err = hcf_routes.unmap_route(app_name, domain_name)
        self.verify("Removing route " + domain_name + " from app", out)
        self.verify("OK", out)

        # Delete routes
        out, err = hcf_routes.delete_orphaned_routes(input_data=b'yes\n')
        self.verify("Deleting route", out)
        self.verify("OK", out)

        # Delete org
        out, err = hcf_organisations.delete_org(
            org_name, input_data=b'yes\n')
        self.verify("Deleting org " + org_name, out)
        self.verify("OK", out)


if __name__ == '__main__':
    base.unittest.main()
