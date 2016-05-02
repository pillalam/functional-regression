from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.hcf import utils


class HcfSoakTests(utils.HcfScenario):
    """Basic benchmark scenarios for Cloud Foundry."""

    @scenario.configure()
    def create_delete_org_and_space(self, cluster_url, username, password):
        """
           This method tests the new space creation,list and delete.
           param : cluster_url, username and password
        """
        # Target to api and login to cluster url
        self._connectApi_and_loginToTarget(cluster_url, username, password)
        # Create org and space
        org_name = self._create_org()
        space_name = self._create_space(org_name)
        # Delete org and space
        self._delete_space(space_name)
        self._delete_org(org_name)
        # Logout from cluster
        self._logoutFromTarget()
