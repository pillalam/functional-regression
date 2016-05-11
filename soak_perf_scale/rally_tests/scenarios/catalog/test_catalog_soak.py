from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.catalog import utils


class CatalogSoakTests(utils.CatalogScenario):
    """Basic benchmark scenarios for Catalog."""

    @scenario.configure()
    def list_detail_catalog(self, catalog_name):
        """
           This method tests the list and details catalog.
        """
        #  list catalog
        self._list_catalog(catalog_name)
        #  detail catalog
        self._details_catalog(catalog_name)

    @scenario.configure()
    def list_detail_service(self, service_name):
        """
           This tests the list and details service functionality.
        """
        # list services
        self._list_services(service_name)
        # detail service
        self._details_service(service_name)

    @scenario.configure()
    def list_instances(self):
        """
           This method tests list instances functionality.
        """
        # list instances
        self._list_instances()
