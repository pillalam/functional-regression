# Helion Cloud Foundry Functional Tests - Steps to Run the Tests 

## Test HCF
1. Update hcf.conf file in python_tests/config folder with following details:
     * url=<target-cluster-url> eg. api.hcf.com
     * username=<username>
     * password=<password>
2.  cd to python_tests/ folder.  Execute:  python -v tests/hcf/test_hcf_<*>.py
    or "for hcf_tests in tests/hcf/test_hcf_*.py; do python "$hcf_tests"; done"

## Test Catalog
