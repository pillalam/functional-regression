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


## Test HCF User Acceptance (Upstream) Tests on AWS
* Set the following variables:
```
     $ HCF_DOMAIN=mydomain.com
     $ HCF_USER=admin
     $ HCF_PASSWORD=mypass
     $ HCF_SDL_VERSION=hcf-0.16.11_0.g60bd33d.master
```

* Run the docker:
```
     $ docker run -it  \
       -- name hcf-cats \
       -- rm \
       -- env DOMAIN=${HCF_DOMAIN} \
       -- env CLUSTER_ADMIN_PASSWORD=${HCF_PASSWORD} \
       -- env CLUSTER_ADMIN_USERNAME=${HCF_USER} \
       docker-registry.helion.space/helioncf/hcf-acceptance-tests:${HCF_SDL_VERSION}
```
