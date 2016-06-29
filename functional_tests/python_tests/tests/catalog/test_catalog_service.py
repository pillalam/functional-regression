import base
from utils import catalog_service


class TestCatalogService(base.BaseTest):

    """
    SetupClass prepares the following preconditions for
    Catalog Service tests
    """

    @classmethod
    def setUpClass(cls):
        super(TestCatalogService, cls).setUpClass()
        pass

    @classmethod
    def tearDownClass(cls):
        super(TestCatalogService, cls).tearDownClass()
        pass

    def test_get_list_catalog(self):
        # Verify Get Catalog
        catalog_id = "hpe-catalog"
        response, catalog = catalog_service.show_catalog(self.catalog_host,
                                                         catalog_id)
        self.assertEqual("hpe-catalog", catalog['id'])
        self.assertEqual("hpe-catalog", catalog['name'])
        self.assertEqual("200", response['status'])

        # Verify list Catalog
        response, catalogs = catalog_service.list_catalogs(self.catalog_host)
        self.assertEqual("200", response['status'])
        self.assertIn(catalog, catalogs)

    def test_cat_service_list(self):
        service_id = "hpe-catalog:helionce"
        service_name = "Helion CodeEngine"
        version = "1.0.0"

        # Show details of a catalog service
        response, content = catalog_service.show_service(
            self.catalog_host, service_id)
        self.assertEqual(service_id, content['id'])
        self.assertEqual(service_name, content['name'])
        self.assertEqual("200", response['status'])

        # Lists all catalog services
        response, services = catalog_service.list_services(self.catalog_host)
        self.assertEqual("200", response['status'])
        services_list = []
        for service in services:
            services_list.append(service['name'])
        expected_services = ['MySQL', 'Mongo', 'Haven On Demand',
                             'Redis', 'Helion Cloud Foundry',
                             'Helion CodeEngine', 'RabbitMQ']
        missing_services = set(expected_services) - set(services_list)
        self.assertFalse(missing_services,
                         "Failed to find service in the fetched list %s:"
                         % ', '.join(s for s in missing_services))

        # List all versions for a catalog service
        response, versions = catalog_service.list_service_versions(
            self.catalog_host, service_id)
        self.assertEqual("200", response['status'])
        versions_list = []
        for ver in versions:
            versions_list.append(ver['version'])
        expected_versions = ['1.0.0']
        missing_versions = set(expected_versions) - set(versions_list)
        self.assertFalse(missing_versions,
                         "Failed to find version in the fetched list %s:"
                         % ', '.join(s for s in missing_versions))

        # Show details of a catalog service with version
        response, content = catalog_service.show_service_version(
            self.catalog_host, service_id, version)
        self.assertEqual(service_id, content['serviceId'])
        self.assertEqual("200", response['status'])


if __name__ == '__main__':
    base.unittest.main()
