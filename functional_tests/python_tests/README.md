# Helion Stackato 4.0 Functional Tests - Steps to Run the Tests 

## Preparation
1. sudo apt-get install python-pip
2. sudo pip install httplib2
3. Install CLIs - HCP, HSM, CF , and HCE
4. Add location of CLI to PATH
5. export PYTHONPATH=~/cnap-qa/functional_tests/python_tests/ 


## Test HCF
1. Update hcf.conf file in python_tests/config folder with following details:
     * url
     * username
     * password
2.  cd to python_tests/ folder.  Execute:  python -v tests/hcf/test_hcf_<*>.py
    or "for hcf_tests in tests/hcf/test_hcf_*.py; do python "$hcf_tests"; done"

## Test HSM
1. Update hsm.conf in python_tests/config folder with following details:
     * url 
     * username
     * password 
     * 

## Test HCP
