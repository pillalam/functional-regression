from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.hcf import utils


class HcfSoakTests(utils.HcfScenario):
    """Basic benchmark scenarios for Cloud Foundry."""

    @scenario.configure()
    def create_delete_org(self, cluster_url, username, password):
        """
           This method tests the new org create, list and delete.
           param : cluster_url, username and password
        """
        # Target to api and login to cluster url
        self._connectApi_and_loginToTarget(cluster_url, username, password)
        # Create org
        org_name = self._create_org()
        # Delete org
        self._delete_org(org_name)
        # Logout from cluster
        self._logoutFromTarget()
