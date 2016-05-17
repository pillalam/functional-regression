import base
import random
from utils import catalog_instance


class TestCatalogInstance(base.BaseTest):

    """
    SetupClass prepares the following preconditions for
    Catalog instance tests
    """

    @classmethod
    def setUpClass(cls):
        super(TestCatalogInstance, cls).setUpClass()
        pass

    @classmethod
    def tearDownClass(cls):
        super(TestCatalogInstance, cls).tearDownClass()
        pass

    def test_cat_instance(self):
        instance_id = "1001"
        instance_name = 'instance_' + str(random.randint(1, 1000))
        service_id = "hpe-catalog:mysql"
        version = "5.6"
        # Create a catalog instance
        response, instance = catalog_instance.create_instance(
            self.catalog_host, instance_name, service_id, version)
        self.assertEqual(response['status'], '200')
        self.assertEqual(instance['instance_name'], instance_name)

        # List instances
        response, content = catalog_instance.list_instances(self.catalog_host)
        self.assertEqual(response['status'], '200')

        # Show details of a catalog instance
        response, content = catalog_instance.show_instance(
            self.catalog_host, instance_id)
        self.assertEqual(response['status'], '200')

        # Delete a catalog instance
        response, instance = catalog_instance.delete_instance(
            self.catalog_host, instance['instance_id'])
        self.assertEqual(response['status'], '200')

if __name__ == '__main__':
    base.unittest.main()
