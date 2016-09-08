# Helion Stackato 4.0 Functional Tests - Steps to Run the Tests 

## Preparation
1. sudo apt-get install git python-pip
2. sudo pip install httplib2
3. Install CLIs - HCP, HSM, CF , and HCE
4. Add location of CLI to PATH
5. export PYTHONPATH=~/cnap-qa/functional_tests/python_tests/ 


## Test HCF
1. Update hcf.conf file in python_tests/config folder with following details:
     * url
     * username
     * password
2.  cd to functional_tests/python_tests
    * To run just one test: python -v tests/hcf/test_hcf_<>.py
    * To run all the tests: ./test_hcf_functional.sh

## Test HSM
1. Update hsm.conf in python_tests/config folder with following details:
     * url 
     * username
     * password 
     

## Test HCP
1. Update hcp.conf in python_tests/config folder with following details:
     * url 
     * username
     * password 


## Test HCE - Smoke Tests
1. Install jq(1.5+) using sudo apt-get install jq
2. Install smoke test using HCE-CLI with the command - sudo ./hce install-smoke-test
3. Execute the smoke test by running the command:
   /usr/local/bin/smoke-hce  <HCE_PUBLIC_API_URL> <HCE_USERNAME> <HCE_PASSWORD> <GITHUB_USERNAME> <GITHUB_PASSWORD> <LOGDIR>
   * HCE_PUBLIC_API_URL - hce endpoint url
   * HCE_USERNAME       - hce username
   * HCE_PASSWORD       - hce password
   * GITHUB_USERNAME    - github repo username
   * GITHUB_PASSWORD    - github repo password
   * LOGDIR             - path for the log directory
