import os
import sys
import re
import base
import random
from utils import hcf_auth
from utils import hcf_hsm_instances


class TestHcfHsmServiceInstance(base.BaseTest):

    """
    SetupClass prepares the following preconditions for
    Hcf - Hsm Service integration tests
    * Login to Hsm service
    """

    @classmethod
    def setUpClass(cls):
        super(TestHcfHsmServiceInstance, cls).setUpClass()

        # Target to the HSM service endpoint
        hcf_auth.hsm_api(cls.hsm_api)

        # Log into Hsm Service
        hcf_auth.login(optional_args={'-u': cls.hsm_username,
                                      '-p': cls.hsm_password})

    @classmethod
    def tearDownClass(cls):
        super(TestHcfHsmServiceInstance, cls).tearDownClass()

    def test_hcf_hsm_service_instances(self):
        # enable service instance
        out, err = hcf_hsm_instances.enable_service_instance(
            self.instance_name, self.cf_instance_name)
        self.verify("OK", out)

        # list service instances
        out, err = hcf_hsm_instances.list_service_instances()
        self.verify("OK", out)

        # disable service instance
        out, err = hcf_hsm_instances.disable_service_instance(
            self.cf_instance_name)
        self.verify("OK", out)

if __name__ == '__main__':
    base.unittest.main()
