# HCP Functional Tests 

This Readme file contains the steps to run HCP functional tests.

## Steps to Run:

1. Update hcp.conf file in python_tests/config folder with following details:

    ``` a. url = <hcp-endpoint> ```
    
    ``` b. username = <hcp-username> ```
    
    ``` c. password = <hcp-password> ```
    

2. cd to cnap-qa/functional_tests/python_tests

3. Export PYTHONPATH ``` export PYTHONPATH="." ```

4. Run tests/hcp/<test_script_name>
    * Example
    ``` python tests/hcp/test_hcp_users.py ```
