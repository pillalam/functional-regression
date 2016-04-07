from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.hcf import utils


class HcfSoakTests(utils.HcfScenario):
    """Basic benchmark scenarios for Cloud Foundry."""

    @scenario.configure()
    def create_delete_quota(self, cluster_url, username, password):
        """
           This method tests the Quota Plan create, list and delete.
           param : cluster_url, username and password
        """
        # Target to api and login to cluster url
        self._connectApi_and_loginToTarget(cluster_url, username, password)
        # Create quota plan
        quota_plan_name = self._create_quota()
        # Delete quota plan
        self._delete_quota(quota_plan_name)
        # Logout from cluster
        self._logoutFromTarget()
