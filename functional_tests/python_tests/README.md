# Helion Stackato 4.0 Functional Tests - Steps to Run the Tests 

## Preparation
1. sudo apt-get install git python-pip
2. sudo pip install httplib2
3. Install CLIs - HCP, HSM, CF , and HCE
4. Add location of CLI to PATH - export PATH=$PATH:{CLI_LOCATION}
5. Clone repo: git clone git@github.com:hpcloud/cnap-qa.git 
6. export PYTHONPATH=~/cnap-qa/functional_tests/python_tests/ 


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
2. If needed unset http_proxy,https_proxy,HTTP_PROXY,HTTPS_PROXY     
3. cd to functional_tests/python_tests
    * To run just one test: python -v tests/hsm/test_hsm_<>.py
    * To run all the tests: ./test_hsm_functional.sh

## Test HCP
1. Update hcp.conf in python_tests/config folder with following details:
     * url 
     * username
     * password 
      
