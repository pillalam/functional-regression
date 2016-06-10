import ast
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

    def test_create_all_service_instances(self):
        instance_all_details = self.get_instance_details()
        # Create Service Catalog Instances
        for inst in instance_all_details:
            instance_details = instance_all_details[inst]
            kwargs = {}
            if 'kwargs' in instance_details:
                params = ast.literal_eval(instance_details['kwargs'])
                if type(params) == list:
                    kwargs['parameters'] = params[0]
                else:
                    kwargs['parameters'] = params
            # Create Catalog Instance
            response, instance = catalog_instance.create_instance(
                self.catalog_host, instance_details['instance_id'],
                instance_details['service_id'],
                ast.literal_eval(instance_details['labels']),
                instance_details['version'],
                instance_details['description'], **kwargs)
            self.assertEqual(response['status'], '201')

            # List instances
            response, list_instances = catalog_instance.list_instances(
                self.catalog_host)
            self.assertEqual(response['status'], '200')

            # Verify details of a catalog instance
            response, get_instance = catalog_instance.show_instance(
                self.catalog_host, instance_details['instance_id'])
            self.assertEqual(response['status'], '200')
            self.assertEqual(get_instance['id'],
                             str(instance_details['instance_id']))

            # Delete a catalog instance
            response, content = catalog_instance.delete_instance(
                self.catalog_host, instance_details['instance_id'])
            self.assertEqual(response['status'], '202')

if __name__ == '__main__':
    base.unittest.main()
