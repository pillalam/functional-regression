# Helion Code Engine Soak  Tests - Steps to Run the Tests

## Test HCE Projects

1. Update hce.properties file under soak_perf_scale/jmeter_tests/scenarios/hce with the following details:
    * hce_endpoint_url   -   HCE service endpoint details
    * username           -   HCE UAA username
    * password           -   HCE UAA password
    * branch             -   Repo branch to use e.g. master
    * repo_url           -   The URL of the repo, e.g. https://github.com/myuser/myrepo
    * container_id       -   ID of the build container for project
    * repo_user_name     -   Your repo username (e.g. GitHub username)
    * repo_password      -   Your repo password (e.g. GitHub password).
    * hcf_url            -   CloudFoundry cluster URL
    * hcf_username       -   CloudFoundry username
    * hcf_password       -   CloudFoundry password
    * hcf_org            -   CloudFoundry organization to target
    * hcf_space          -   CloudFoundry space to target


2. Update soak properties (threads,ramp_up, duration) and run the tests from jmeter UI or CLI.
