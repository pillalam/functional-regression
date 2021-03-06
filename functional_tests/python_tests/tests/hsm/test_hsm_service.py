import base
from utils import hsm_auth
from utils import hsm_service


class TestHSMService(base.BaseTest):

    """
    SetupClass prepares the following preconditions for
    HSM Service tests
    """

    @classmethod
    def setUpClass(cls):
        super(TestHSMService, cls).setUpClass()
        # Login to hsm api
        hsm_auth.connect_target(cls.cluster_url)
        cls.update_hsm_config()
        # Target to the HSM service endpoint
        hsm_auth.login(optional_args={'-u': cls.username, '-p': cls.password})

    @classmethod
    def tearDownClass(cls):
        super(TestHSMService, cls).tearDownClass()
        pass

    def test_get_list_catalog(self):
        headers = self.get_token()
        # Verify Get Catalog
        response, catalog = hsm_service.show_catalog(
            self.catalog_host, self.catalog_id, headers=headers)
        self.assertEqual("hpe-catalog", catalog['id'])
        self.assertEqual("hpe-catalog", catalog['name'])
        self.assertEqual("200", response['status'])

        # Verify list Catalog
        response, catalogs = hsm_service.list_catalogs(self.catalog_host,
                                                       headers=headers)
        self.assertEqual("200", response['status'])
        self.assertIn(catalog, catalogs)

    def test_hsm_service_list(self):
        headers = self.get_token()
        # Show details of a hsm service
        response, content = hsm_service.show_service(
            self.catalog_host, self.service_id, headers=headers)
        self.assertEqual(self.service_id, content['id'])
        self.assertEqual(self.service_name, content['name'])
        self.assertEqual("200", response['status'])

        # Lists all hsm services
        response, services = hsm_service.list_services(self.catalog_host,
                                                       headers=headers)
        self.assertEqual("200", response['status'])
        services_list = []
        for service in services:
            services_list.append(service['name'])
        expected_services = ['dev-mysql', 'dev-mongo', 'dev-redis',
                             'dev-rabbitmq', 'dev-postgres', 'havenondemand',
                             'k8-guestbook', 'hce', 'hcf', 'hsc', 'hsm',
                             'rds-mysql', 'rds-postgres']
        missing_services = set(expected_services) - set(services_list)
        self.assertFalse(missing_services,
                         "Failed to find service in the fetched list %s:"
                         % ', '.join(s for s in missing_services))

        # List all versions for a hsm service
        response, versions = hsm_service.list_service_versions(
            self.catalog_host, self.service_id, headers=headers)
        self.assertEqual("200", response['status'])
        sdl_versions = versions[0]['sdl_versions'].keys()
        product_version = versions[0]['product_version']
        missing_versions = []
        missing_versions = set(self.sdl_versions) - set(sdl_versions)
        self.assertFalse(missing_versions,
                         "Failed to find version in the fetched list %s:"
                         % ', '.join(s for s in missing_versions))

        # Show details of a hsm service with version
        response, content = hsm_service.show_service_version(
            self.catalog_host, self.service_id, self.product_version,
            self.sdl_versions[0], headers=headers)
        self.assertEqual(self.service_id, content['service_id'])
        self.assertEqual("200", response['status'])


if __name__ == '__main__':
    base.unittest.main(verbosity=2)
