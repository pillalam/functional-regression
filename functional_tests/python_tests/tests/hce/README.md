# Helion Code Engine -  Functional Tests 

This Readme file contains the steps to run HCE functional tests.

## Steps to Run Test Projects:

1. Update hce.conf file in python_tests/config folder with following details:

    * url   -   HCE service endpoint details
    * username           -   HCE UAA username
    * password           -   HCE UAA password
    * repo_url           -   The URL of the repo, e.g. https://github.com/myuser/myrepo
    * branch             -   Repo branch to use e.g. master
    * ref_string         -   Repo branch to use e.g. master
    * container_id       -   ID of the build container for project
    * repo_username      -   Your repo username (e.g. GitHub username)
    * repo_password      -   Your repo password (e.g. GitHub password)

2. cd to cnap-qa/functional_tests/python_tests 

3. Export PYTHONPATH ``` export PYTHONPATH="." ```

4. Run tests using the command:
    ``` python tests/hce/test_hce_projects.py ```
 
## Steps to Run Test HCE E2EOperations:

1. Update hce.conf file in python_tests/config folder with following details:

    * url   -   HCE service endpoint details
    * username          -   HCE UAA username
    * password          -   HCE UAA password
    * repo_url          -   The URL of the repo, e.g. https://github.com/myuser/myrepo
    * branch            -   Repo branch to use e.g. master
    * ref_string        -   Repo branch to use e.g. master
    * container_id      -   ID of the build container for project
    * repo_username     -   Your repo username (e.g. GitHub username)
    * repo_password     -   Your repo password (e.g. GitHub password)
    * cf_url            -   CloudFoundry cluster URL
    * cf_username       -   CloudFoundry username
    * cf_password       -   CloudFoundry password
    * cf_org            -   CloudFoundry organization to target
    * cf_space          -   CloudFoundry space to target

2. cd to cnap-qa/functional_tests/python_tests

3. Export PYTHONPATH ``` export PYTHONPATH="." ```

4. Run tests using the command:
    ``` python tests/hce/test_hce_e2eoperations.py ```
