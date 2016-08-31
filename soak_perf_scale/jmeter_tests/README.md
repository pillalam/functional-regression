# JMeter Tests

Jmeter soak tests

## JMeter Setup

* Install JMeter 3.0 from http://jmeter.apache.org/download_jmeter.cgi

    ```
    $ cd $HOME
    $ wget http://mirror.fibergrid.in/apache//jmeter/binaries/apache-jmeter-3.0.tgz
    $ tar -xvf apache-jmeter-3.0.tgz
    $ rm apache-jmeter-3.0.tgz
    ```
    
* Install JMeter Standard Plug-In from https://jmeter-plugins.org/downloads/old
   * NOTE: Standard Plug-In (CMDRunner.jar) is used to generate csv report from JMeter aggregate report. Scripts will run without Standrad Plug-In.
    
    ```
    $ mkdir jmeter-plugins-temp
    $ cd jmeter-plugins-temp
    $ wget http://jmeter-plugins.org/downloads/file/JMeterPlugins-Standard-1.4.0.zip
    $ tar -xvf JMeterPlugins-Standard-1.4.0.zip
    $ cp lib/ext/* $HOME/apache-jmeter-3.0/lib/ext/
    $ cd ..
    $ rm -rf jmeter-plugins-temp
    ```
    
## Execute JMeter Wrapper Script

* Go to JMeter Tests location
    
    ```
    $ cd $HOME/cnap-qa/soak_perf_scale/jmeter_tests
    ```
    
* Update the test properties file
    
    ```
    $ vi common/properties/<feature>.properites
    Example:
    $ vi common/properties/stratos.properties
    ```
    
* Set the test script and its properties file location - TEST_SCRIPT and TEST_PROPERTIES
    
    ```
    $ export TEST_SCRIPT=scenarios/console/test_console.jmx
    $ export TEST_PROPERTIES=common/properties/stratos.properties
    ```
    
* Execute the JMeter Wraper Script
    * Make sure to execute the script from cnap-qa/soak_perf_scale/jmeter_tests location
    
    ```
    $ cd $HOME/cnap-qa/soak_perf_scale/jmeter_tests
    $ common/drivers/jmeter_wrapper.sh
    ```
    
* Test Results - Wrapper script will give the test results (Aggregate and CSV logs) location
