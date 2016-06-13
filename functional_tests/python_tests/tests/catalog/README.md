# HSM Functional Tests 

This Readme file contains the steps to run HSM functional tests.

## Steps to Run:

1. Update configuration file, catalog.json under cnap-qa/functional_tests/python_tests/config
    * Parameters to Update
    ``` CATALOG_HOST = <catalog-host-ip> ```

2. cd to cnap-qa/functional_tests/python_tests 

3. Export PYTHONPATH ``` export PYTHONPATH="." ```

4. Run tests/catalog/<test_script_name>
    * Example 
    ``` python tests/catalog/test_catalog_instance.py ```
