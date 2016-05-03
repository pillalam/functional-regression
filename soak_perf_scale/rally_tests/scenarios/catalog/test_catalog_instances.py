from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.catalog import utils


class CatalogInstanceSoakTests(utils.CatalogScenario):
    """Basic benchmark scenarios for Catalog Instance."""

    @scenario.configure()
    def list_instances(self):
        """
           This method tests list instances functionality.
        """
        # list instances
        self._list_instances()
