import os
import sys
import re
import base
import random
from utils import hce_auth
from utils import hce_projects


class TestHceProjects(base.BaseTest):

    """
    SetupClass prepares the following preconditions
    """

    @classmethod
    def setUpClass(cls):
        super(TestHceProjects, cls).setUpClass()

        # Login to Cluster using credentials
        hce_auth.login(cls.username, cls.password)

    @classmethod
    def tearDownClass(cls):
        super(TestHceProjects, cls).tearDownClass()
        hce_auth.logout()

    def test_hce_projects(self):
        # Create Project
        project_name = 'test_proj' + str(random.randint(1024, 4096))
        runtime_type = "java"
        repo_url = "https://github.com/myuser/myrepo"
        container = "build container"
        target = "target url"
        out, err = hce_projects.create_project(optional_orgs={'--name=':
                                               project_name, '--runtime=':
                                               runtime_type, '--repo=':
                                               repo_url, '--container-id=':
                                               container, '--target-id=':
                                               target})

        # List Projects
        out, err = hce_projects.list_projects()

        # Delete Projects
        out, err = hce_projects.delete_project(optional_orgs={'--project-id=':
                                               project_name})

if __name__ == '__main__':
    base.unittest.main()
