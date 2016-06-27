# HCE Functional Tests 

This Readme file contains the steps to run HCE functional tests.

## Steps to Run:

1. Update hce.conf file in python_tests/config folder with following details:
    * url=<target-api-url> eg. api.hce.com
    * username=<username>
    * password=<password>

2. cd to cnap-qa/functional_tests/python_tests 

3. Export PYTHONPATH ``` export PYTHONPATH="." ```

4. Run tests/hce/<test_script_name>
    * Example 
    ``` python tests/hce/test_hce_projects.py ```
