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

    def test_cat_service_list(self):
        # Lists all catalog services
        response, content = catalog_service.list_service(self.catalog_host)
        self.assertEqual("hpe-catalog", content[0]['catalogId'])
        self.assertEqual("200", response['status'])

if __name__ == '__main__':
    base.unittest.main()
