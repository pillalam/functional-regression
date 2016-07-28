import os
import json
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
        cls.project_name = 'test_proj' + str(random.randint(1024, 4096))

    @classmethod
    def tearDownClass(cls):
        super(TestHceProjects, cls).tearDownClass()
        hce_auth.logout()

    def test_hce_projects(self):
        # Create Project
        out, err = hce_projects.create_project(
            optional_args={'--name=': self.project_name,
                           '--branch=': self.branch,
                           '--repo=': self.repo_url,
                           '--container-id=': self.container_id,
                           '--target-id=': self.deployment_target_id,
                           '--username=': self.repo_username,
                           '--password=': self.repo_password, '--json': ''})
        out = json.loads(out)
        self.verify(str(out['name']), self.project_name)
        project_id = str(out['id'])

        # List Projects
        out, err = hce_projects.list_projects()
        self.verify(project_id, out)
        self.verify(self.project_name, out)

        # Update Project details
        updated_project_name = self.project_name + '_updated'
        out, err = hce_projects.update_project(
            optional_args={'--project-id=': project_id,
                           '--name=': updated_project_name, '--json': ''})
        out = json.loads(out)
        self.verify(str(out['name']), updated_project_name)
        self.verify(project_id, str(out['id']))

        # Delete Projects
        out, err = hce_projects.delete_project(optional_args={'--project-id=':
                                               project_id})
        self.verify('deleted', out)

if __name__ == '__main__':
    base.unittest.main()
