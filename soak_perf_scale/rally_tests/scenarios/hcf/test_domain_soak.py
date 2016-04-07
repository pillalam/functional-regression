from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.hcf import utils
from rally.task import validation


class HcfSoakTests(utils.HcfScenario):
    """Basic benchmark scenarios for Cloud Foundry."""

    @validation.required_contexts("orgs")
    @scenario.configure(context={"cleanup": ["orgs"]})
    def create_delete_domain(self, cluster_url, username, password):
        """
           This method tests the new domain creation,list and delete.
           param : cluster_url, username and password
        """
        org_name = self.context["tenant"]["org_name"]
        # Create domain
        domain_name = self._create_domain(org_name)
        # Delete domain
        self._delete_domain(domain_name)
        # Logout from cluster
        self._logoutFromTarget()
