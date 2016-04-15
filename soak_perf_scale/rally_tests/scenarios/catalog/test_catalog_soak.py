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
