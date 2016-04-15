# HCF Rally Tests - Steps to Run the Tests

This Readme file contains the steps to execute HCF Rally Tests

## Test Application Access

1. Create a HCF cluster and deploy the following applications.
    * sample helion-hello-world-java
2. Update following variables in HCF_Soak_Access_Application Jenkins Job
    * HLM_BASENODE_IP (Base node IP, which has rc file)
    * APP_URLS  (If more than one URL, use \n as separator. Eg http://url1/nhttp://url2)
3. Run the Jenkins job and check the result.

## Test Quota

1. Update following variables in HCF_Soak_Quota Jenkins Job
    * HLM_BASENODE_IP (Base node IP, which has rc file)
    * CLUSTER_URL 
    * USER_NAME 
    * PASSWORD
2. Run the Jenkins job and check the result.

## Test Organisation and Space

1. Update following variables in HCF_Soak_Space Jenkins Job
    * HLM_BASENODE_IP (Base node IP, which has rc file)
    * CLUSTER_URL 
    * USER_NAME 
    * PASSWORD
2. Run the Jenkins job and check the result.

