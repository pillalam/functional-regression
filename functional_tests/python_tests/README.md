# HCF Functional Tests - Steps to Run the Tests 

This Readme file contains the steps to run hcf functional tests.
## Test Organisation
1. Update run.conf file in python_tests/config folder with following details:
     * url=<target-cluster-url>
     * username=<username>
     * password=<password>
2.  cd to python_tests/ folder.  Execute:  python -v tests/hcf/test_hcf_organisations.py
