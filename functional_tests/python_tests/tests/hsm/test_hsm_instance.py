import ast
import base
import random

from utils import hsm_instance


class TestHSMInstance(base.BaseTest):

    """
    SetupClass prepares the following preconditions for
    HSM instance tests
    """

    @classmethod
    def setUpClass(cls):
        super(TestHSMInstance, cls).setUpClass()
        pass

    @classmethod
    def tearDownClass(cls):
        super(TestHSMInstance, cls).tearDownClass()
        pass

    def test_create_all_service_instances(self):
        instance_all_details = self.get_instance_details()
        # Get  HSM Service Details
        for inst in instance_all_details:
            instance_details = instance_all_details[inst]
            kwargs = {}
            if 'kwargs' in instance_details:
                params = ast.literal_eval(instance_details['kwargs'])
                if type(params) == list:
                    kwargs['parameters'] = params[0]
                else:
                    kwargs['parameters'] = params
            # Create HSM Instance
            response, instance = hsm_instance.create_instance(
                self.catalog_host, instance_details['instance_id'],
                instance_details['service_id'],
                ast.literal_eval(instance_details['labels']),
                instance_details['version'],
                instance_details['description'], **kwargs)
            self.assertEqual(response['status'], '201')

            # List instances
            response, list_instances = hsm_instance.list_instances(
                self.catalog_host)
            self.assertEqual(response['status'], '200')

            # Verify details of a hsm instance
            response, get_instance = hsm_instance.show_instance(
                self.catalog_host, instance_details['instance_id'])
            self.assertEqual(response['status'], '200')
            self.assertEqual(get_instance['instance']['instance_id'],
                             str(instance_details['instance_id']))

            # Delete a catalog instance
            response, content = hsm_instance.delete_instance(
                self.catalog_host, instance_details['instance_id'])
            self.assertEqual(response['status'], '202')

if __name__ == '__main__':
    base.unittest.main()
