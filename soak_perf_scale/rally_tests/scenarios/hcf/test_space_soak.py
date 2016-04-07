from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.hcf import utils
from rally.task import validation


class HcfSoakTests(utils.HcfScenario):
    """Basic benchmark scenarios for Cloud Foundry."""

    @validation.required_contexts("orgs")
    @scenario.configure(context={"cleanup": ["orgs"]})
    def create_delete_space(self, cluster_url, username, password):
        """
           This method tests the new space creation,list and delete.
           param : cluster_url, username and password
        """
        org_name = self.context["tenant"]["org_name"]
        # Create space
        space_name = self._create_space(org_name)
        # Delete space
        self._delete_space(space_name)
        # Logout from cluster
        self._logoutFromTarget()
