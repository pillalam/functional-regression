import base
from utils import hsm_service


class TestHSMService(base.BaseTest):

    """
    SetupClass prepares the following preconditions for
    HSM Service tests
    """

    @classmethod
    def setUpClass(cls):
        super(TestHSMService, cls).setUpClass()
        pass

    @classmethod
    def tearDownClass(cls):
        super(TestHSMService, cls).tearDownClass()
        pass

    def test_get_list_catalog(self):
        # Verify Get Catalog
        response, catalog = hsm_service.show_catalog(self.catalog_host,
                                                     self.catalog_id)
        self.assertEqual("hpe-catalog", catalog['id'])
        self.assertEqual("hpe-catalog", catalog['name'])
        self.assertEqual("200", response['status'])

        # Verify list Catalog
        response, catalogs = hsm_service.list_catalogs(self.catalog_host)
        self.assertEqual("200", response['status'])
        self.assertIn(catalog, catalogs)

    def test_hsm_service_list(self):
        # Show details of a hsm service
        response, content = hsm_service.show_service(
            self.catalog_host, self.service_id)
        self.assertEqual(self.service_id, content['id'])
        self.assertEqual(self.service_name, content['name'])
        self.assertEqual("200", response['status'])

        # Lists all hsm services
        response, services = hsm_service.list_services(self.catalog_host)
        self.assertEqual("200", response['status'])
        services_list = []
        for service in services:
            services_list.append(service['name'])
        expected_services = ['MySQL', 'Mongo', 'Haven On Demand',
                             'Redis', 'hce', 'hsm', 'GuestBook',
                             'RabbitMQ', 'Postgres']
        missing_services = set(expected_services) - set(services_list)
        self.assertFalse(missing_services,
                         "Failed to find service in the fetched list %s:"
                         % ', '.join(s for s in missing_services))

        # List all versions for a hsm service
        response, versions = hsm_service.list_service_versions(
            self.catalog_host, self.service_id)
        self.assertEqual("200", response['status'])
        versions_list = []
        for ver in versions:
            versions_list.append(ver['version'])
        expected_versions = []
        expected_versions.append(self.version)
        missing_versions = set(expected_versions) - set(versions_list)
        self.assertFalse(missing_versions,
                         "Failed to find version in the fetched list %s:"
                         % ', '.join(s for s in missing_versions))

        # Show details of a hsm service with version
        response, content = hsm_service.show_service_version(
            self.catalog_host, self.service_id, self.version)
        self.assertEqual(self.service_id, content['serviceId'])
        self.assertEqual("200", response['status'])


if __name__ == '__main__':
    base.unittest.main()
