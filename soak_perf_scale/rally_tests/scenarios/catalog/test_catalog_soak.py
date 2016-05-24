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

    @scenario.configure()
    def create_delete_mysql_instance(self, service_Id, instanceFile):
        """
           This method tests create and delete functionality for
           mysql service instance
        """
        #  Create Mysql instance
        instance_Id = self.create_mysql_instance(service_Id, instanceFile)

        #  Delete Mysql instance
        self._delete_mysql_instance(instance_Id)

    @scenario.configure()
    def create_delete_spark_instance(self, service_Id, instanceFile):
        """
           This method tests create and delete functionality for
           spark service instance
        """
        #  Create Spark service instance
        instance_Id = self.create_spark_instance(service_Id, instanceFile)

        #  Delete Spark service instance
        self._delete_spark_instance(instance_Id)

    @scenario.configure()
    def create_delete_cassandra_instance(self, service_Id, instanceFile):
        """
           This method tests create and delete functionality for
           cassandra service instance
        """
        #  Create Cassandra service instance
        instance_Id = self.create_cassandra_instance(service_Id, instanceFile)

        #  Delete Cassandra service  instance
        self._delete_cassandra_instance(instance_Id)

