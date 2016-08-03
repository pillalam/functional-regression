import ast
import base
import random
import time

from utils import hsm_auth
from utils import hsm_instance


class TestHSMInstance(base.BaseTest):

    """
    SetupClass prepares the following preconditions for
    HSM instance tests
    """

    @classmethod
    def setUpClass(cls):
        super(TestHSMInstance, cls).setUpClass()
        # Login to hsm api
        hsm_auth.connect_target(cls.cluster_url)

        # Target to the HSM service endpoint
        hsm_auth.login(optional_args={'-u': cls.username, '-p': cls.password})

        cls.instance_all_details = cls.get_instance_details()

    @classmethod
    def tearDownClass(cls):
        super(TestHSMInstance, cls).tearDownClass()
        pass

    def _delete_instance(self, instance_id):
        headers = self.get_token()
        # Delete a catalog instance
        response, _ = hsm_instance.delete_instance(
            self.catalog_host, instance_id, headers=headers)
        self.assertEqual(response['status'], '202')
        self.wait_for_delete_status(instance_id)

    def test_create_all_service_instances(self):
        # Get Headers
        headers = self.get_token()

        instance_all_details = self.get_instance_details()
        # Get  HSM Service Details
        for inst in self.instance_all_details:
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
                instance_details['version'], instance_details['description'],
                headers=headers, **kwargs)
            self.addCleanup(self._delete_instance,
                            instance_details['instance_id'])
            self.assertEqual(response['status'], '201')
            self.wait_for_active_state(instance_details['instance_id'])
            # List instances
            response, list_instances = hsm_instance.list_instances(
                self.catalog_host, headers=headers)
            self.assertEqual(response['status'], '200')

            # Verify details of a hsm instance
            response, get_instance = hsm_instance.show_instance(
                self.catalog_host, instance_details['instance_id'],
                headers=headers)
            self.assertEqual(response['status'], '200')
            self.assertEqual(get_instance['instance']['instance_id'],
                             str(instance_details['instance_id']))

    def test_configure_instance(self):
        headers = self.get_token()
        # Create a dev-mysql instance
        instance_details = self.instance_all_details['dev-mysql']
        kwargs = {}
        if 'kwargs' in instance_details:
            params = ast.literal_eval(instance_details['kwargs'])
            if type(params) == list:
                kwargs['parameters'] = params[0]
            else:
                kwargs['parameters'] = params
        instance_id = instance_details['instance_id'] + 'update'
        # Create HSM Instance
        response, instance = hsm_instance.create_instance(
            self.catalog_host, instance_id,
            instance_details['service_id'],
            ast.literal_eval(instance_details['labels']),
            instance_details['version'], instance_details['description'],
            headers=headers, **kwargs)
        self.addCleanup(self._delete_instance, instance_id)
        self.assertEqual(response['status'], '201')
        self.wait_for_active_state(instance_id)

        # get_instance details before updation
        _, get_inst = hsm_instance.show_instance(
            self.catalog_host, instance_id,
            headers=headers)

        # Update Dev-mysql Instance
        kwargs = {}
        parameters = [{"name": "MYSQL_ROOT_PASSWORD", "value": "pass1"}]
        kwargs['parameters'] = parameters[0]

        response, _ = hsm_instance.configure_instance(
            self.catalog_host, get_inst['instance']['instance_id'],
            get_inst['instance']['service_id'],
            get_inst['instance']['version'],
            get_inst['instance']['vendor'],
            headers=headers, **kwargs)
        self.assertEqual(response['status'], '202')
        self.wait_for_active_state(instance_id)

        # Verify Get instance after updation
        _, get_instance = hsm_instance.show_instance(
            self.catalog_host, instance_id,
            headers=headers)
        self.assertTrue(
            set(parameters[0].items()).issubset(
                set(get_instance['instance']['parameters'][0].items())))

if __name__ == '__main__':
    base.unittest.main()
