import unittest
import os
import re
import ConfigParser
import time

from utils import hsm_service
from utils import hsm_auth
from utils import hsm_instance


class BaseTest(unittest.TestCase):
    BASE_PATH = os.getcwd().split()[0]
    CONF_FILE = os.environ.get('READ CONFIG FILE', os.path.expanduser(
        BASE_PATH + '/config/hsm.conf'))
    Config = ConfigParser.ConfigParser()
    Config.read(CONF_FILE)
    config_sections = Config.sections()
    CONF_SECTION_CONN1 = 'command'
    CONF_SECTION_CONN2 = 'catalog-details'
    token_file = os.environ.get('READ CONFIG FILE', os.path.expanduser(
        os.getenv("HOME") + '/.hsm/config.json'))

    @classmethod
    def get_instance_details(cls):
        '''This method fetches available services and
        forms json body for hsm instance creation'''
        expected_services = []
        for s in cls.config_sections:
            if s != 'catalog-details' and s != 'command':
                expected_services.append(s)
        service_details = \
            list(set(cls.actual_services).intersection(set(expected_services)))
        instance_all_details = {}
        for service in service_details:
            instance_params = cls.read_from_config(service)
            instance_all_details[service] = instance_params
        return instance_all_details

    @classmethod
    def read_from_config(cls, CONF_SECTION):
        cls.CONF_SECTION_CONN = CONF_SECTION
        options = cls.Config.options(CONF_SECTION)
        service_details = {}
        for option in options:
            service_details[option] = cls.Config.get(
                cls.CONF_SECTION_CONN, option)
        return service_details

    @classmethod
    def setUpClass(cls):

        cls.cluster_url = cls.Config.get(
            cls.CONF_SECTION_CONN1, 'url')
        cls.username = cls.Config.get(
            cls.CONF_SECTION_CONN1, 'username')
        cls.password = cls.Config.get(
            cls.CONF_SECTION_CONN1, 'password')
        cls.read_from_config(CONF_SECTION='catalog-details')
        cls.catalog_host = cls.cluster_url.split('//', 1)[1]
        cls.catalog_id = cls.Config.get(
            cls.CONF_SECTION_CONN2, 'catalog_id')
        cls.service_id = cls.Config.get(
            cls.CONF_SECTION_CONN2, 'service_id')
        cls.service_name = cls.Config.get(
            cls.CONF_SECTION_CONN2, 'service_name')
        cls.version = cls.Config.get(
            cls.CONF_SECTION_CONN2, 'version')

        # Login to hsm api
        hsm_auth.connect_target(cls.cluster_url)

        # Target to the HSM service endpoint
        hsm_auth.login(optional_args={'-u': cls.username, '-p': cls.password})
        # Get services
        _, services = hsm_service.list_services(cls.catalog_host,
                                                headers=cls.get_token())
        cls.actual_services = []
        for s in services:
            cls.actual_services.append(s['name'])
        cls.get_instance_details()

    def verify(self, expression, output):
        if re.search(expression, output):
            return
        else:
            self.fail(output)

    @classmethod
    def get_token(cls):
        token_string = [line.rstrip('\n') for line in open(cls.token_file)]
        token = "bearer " + \
            token_string[2].split(':')[1].split(',')[0].strip(' ')[1:-1]
        return token

    def wait_for_active_state(cls, instance_id):
        # Getting instance status
        instance_status = cls.get_instance_status(instance_id)
        timeout = 300
        start_time = int(time.time())
        # Waiting for ACTIVE status
        while(instance_status != 'running'):
            time.sleep(10)
            instance_status = cls.get_instance_status(instance_id)
            timeElapsed = int(time.time()) - start_time
            if(instance_status == 'failed'):
                raise Exception(
                    "instance %s entered failed status." %
                    instance_id)
            if (timeElapsed >= 600):
                raise Exception(
                    "instance %s Failed to reach Active State in 600 sec" %
                    instance_id)
        return instance_id

    def get_instance_status(cls, instance_id):
        headers = cls.get_token()
        try:
            instance_status = None
            response, content = hsm_instance.show_instance(
                cls.catalog_host, instance_id, headers=headers)
            if not str(response.status).startswith('20'):
                raise Exception(
                    "response status is not matched, "
                    "response is %s : %s" %
                    (str(response), str(content)))
            instance_status = content['instance']['state']
            return instance_status
        except (Exception) as e:
            raise Exception(
                " Failed to get instance status : %s" % e)

    def wait_for_delete_status(cls, instance_id):
        headers = cls.get_token()
        timeout = 300
        response, _ = hsm_instance.show_instance(
            cls.catalog_host, instance_id, headers=headers)
        status_code = response['status']
        start_time = int(time.time())
        while(status_code != '404'):
            time.sleep(20)
            timeElapsed = int(time.time()) - start_time
            response, _ = hsm_instance.show_instance(
                cls.catalog_host, instance_id, headers=headers)
            status_code = response['status']
            if (timeElapsed >= int(timeout)):
                raise Exception(
                    'Failed to get deleted %s in required time %s '
                    'seconds' % (instance_id, timeout))
        return instance_id
