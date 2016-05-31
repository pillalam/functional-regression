# Helion Cloud Foundry Functional Tests - Steps to Run the Tests 

## Test HCF
1. Update hcf.conf file in python_tests/config folder with following details:
     * url=<target-cluster-url> eg. hcf.com
     * username=<username>
     * password=<password>
2.  cd to python_tests/ folder.  Execute:  python -v tests/hcf/test_hcf_*.py

## Test Catalog
