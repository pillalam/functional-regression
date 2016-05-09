from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.catalog import utils


class CatalogServiceSoakTests(utils.CatalogScenario):
    """Basic benchmark scenarios for Catalog service"""

    @scenario.configure()
    def list_detail_service(self, service_name):
        """
           This tests the list and details service functionality.
        """
        # list services
        self._list_services(service_name)
        # detail service
        self._details_service(service_name)
