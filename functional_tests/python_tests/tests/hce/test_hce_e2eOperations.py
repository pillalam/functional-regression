import os
import json
import sys
import re
import base
import random
import time
from utils import hce_auth
from utils import hce_projects
from utils import hce_deployment_targets
from utils import hce_pipelines
from utils import hce_builds


class TestHceProjects(base.BaseTest):

    """
    SetupClass prepares the following preconditions
    """

    @classmethod
    def setUpClass(cls):
        super(TestHceProjects, cls).setUpClass()

        # Login to Cluster using credentials
        hce_auth.login(cls.username, cls.password)
        cls.dep_target_name = 'test_dep_target' + \
            str(random.randint(1024, 4096))
        cls.project_name = 'test_proj' + str(random.randint(1024, 4096))

    @classmethod
    def tearDownClass(cls):
        super(TestHceProjects, cls).tearDownClass()
        hce_auth.logout()

    def test_hce_e2eScenario(self):

        # Create deployment target
        out, err = hce_deployment_targets.create_deployment_target(
            optional_args={'--label=': self.dep_target_name,
                           '--url=': self.cf_url,
                           '--username=': self.cf_username,
                           '--password=': self.cf_password,
                           '--org=': self.cf_org,
                           '--space=': self.cf_space, '--json': ''})
        out = json.loads(out)
        self.verify(str(out['name']), self.dep_target_name)
        target_id = str(out['deployment_target_id'])

        # List and verify the deployment target
        out, err = hce_deployment_targets.list_deployment_targets()
        self.verify(target_id, out)
        self.verify(self.dep_target_name, out)

        # Create project
        out, err = hce_projects.create_project(
            optional_args={'--name=': self.project_name,
                           '--branch=': self.branch,
                           '--repo=': self.repo_url,
                           '--container-id=': self.container_id,
                           '--target-id=': target_id,
                           '--username=': self.repo_username,
                           '--password=': self.repo_password, '--json': ''})
        out = json.loads(out)
        self.verify(str(out['name']), self.project_name)
        project_id = str(out['id'])

        # List and verify the project details
        out, err = hce_projects.list_projects()
        self.verify(project_id, out)
        self.verify(self.project_name, out)

        # Trigger a build for this project
        out, err = hce_pipelines.trigger_pipeline(
            optional_args={'--project-id=': project_id,
                           '--ref=': self.ref_string, '--json': ''})
        out = json.loads(out)
        build_id = str(out['id'])

        # Verify build status
        out, err = hce_builds.get_build(
            optional_args={'--build-id=': build_id, '--json': ''})
        out = json.loads(out)
        timeout = 600
        t_value = 0
        c_time = time.time()
        while (t_value < timeout):
            if("events" not in out):
                time.sleep(5)
                t_value = time.time() - c_time
                out, err = hce_builds.get_build(
                    optional_args={'--build-id=': build_id, '--json': ''})
                continue
            else:
                break
        out = json.loads(out)
        events = out['events']
        if("Building" in events[0].values()):
            if("succeeded" in events[0].values()):
                print "\n\nEvent LOG : Building succeeded "
                while(events.__len__() == 1):
                    out, err = hce_builds.get_build(
                        optional_args={'--build-id=': build_id, '--json': ''})
                    out = json.loads(out)
                    events = out['events']
            elif("failed" in events[0].values()):
                print "\n\nBuilding failed: Exiting.."
                sys.exit(1)
        if("Testing" in out['events'][1].values()):
            if("succeeded" in events[1].values()):
                print "\n\nEvent LOG : Testing succeeded"
                while(events.__len__() == 2):
                    out, err = hce_builds.get_build(
                        optional_args={'--build-id=': build_id, '--json': ''})
                    out = json.loads(out)
                    events = out['events']
            elif("failed" in events[1].values()):
                print "\n\nTesting failed: Exiting.."
                sys.exit(1)
        if("Deploying" in out['events'][2].values()):
            if("succeeded" in events[2].values()):
                print "\n\nEvent LOG : Deploying  succeeded"
                while(events.__len__() == 3):
                    out, err = hce_builds.get_build(
                        optional_args={'--build-id=': build_id, '--json': ''})
                    out = json.loads(out)
                    events = out['events']
            elif("failed" in events[2].values()):
                print "\n\nDeploying failed: Exiting.."
                sys.exit(1)
        if("pipeline_completed" in out['events'][3].values()):
            if("succeeded" in events[3].values()):
                print "\n\nEvent LOG : pipeline_completion  succeeded"
            elif("failed" in events[3].values()):
                print "\n\nPipeline completion failed: Exiting.."

        # Delete Project
        out, err = hce_projects.delete_project(optional_args={'--project-id=':
                                               project_id})

        self.verify('deleted', out)

        # Delete deployment target
        out, err = hce_deployment_targets.delete_deployment_target(
            optional_args={'--target-id=': target_id})
        self.verify('deleted', out)

if __name__ == '__main__':
    base.unittest.main(verbosity=2)
