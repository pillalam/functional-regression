#!/bin/bash

if [ ! -n "${TEST_SCRIPT}" ] && [ ! -n "${TEST_PROPERTIES}" ] 
then
     echo " Please set TEST_SCRIPT, TEST_PROPERTIES parameters and run again..."
     echo " --------------------------------------------------------------------------"
     echo " Example: export TEST_SCRIPT=scenarios/console/test_console.jmx"
     echo "          export TEST_PROPERTIES=common/properties/stratos.properties"
     echo " --------------------------------------------------------------------------"
    exit 1
fi

# Setting Variable
JMETER_PATH=$HOME/apache-jmeter-3.0/bin
CMDRUNNER=$JMETER_PATH/../lib/ext/CMDRunner.jar
TEST_RESULTS=jmeter_results_$(date +%m%d%y%H%M%S)
COMMON_PROPERTIES=common/properties/common.properties

# Create Test Results Directory
mkdir ${TEST_RESULTS}
echo " Created ${PWD}/${TEST_RESULTS} test results directory."
echo " --------------------------------------------------------------------------"

JTL_RESULTS_PATH=${TEST_RESULTS}/test_aggregate_results.jtl
CSV_RESULTS_PATH=${TEST_RESULTS}/test_csv_results.csv

echo " JMeter test started..."
echo " --------------------------------------------------------------------------"

${JMETER_PATH}/jmeter -n -t ${TEST_SCRIPT} -p ${TEST_PROPERTIES} -q ${COMMON_PROPERTIES} -l ${JTL_RESULTS_PATH}
echo " JMeter test completed."
echo " Test Aggregare Report is at ${JTL_RESULTS_PATH} "
echo " --------------------------------------------------------------------------"

echo " Genearting CSV Format Results..."
echo " --------------------------------------------------------------------------"
java -jar  ${CMDRUNNER} --tool Reporter --generate-csv ${CSV_RESULTS_PATH} --input-jtl ${JTL_RESULTS_PATH} --plugin-type AggregateReport
echo " Generated CSV Format Results. "
echo " --------------------------------------------------------------------------"

echo " CSV Format Test Results"
echo " --------------------------------------------------------------------------"
cat ${CSV_RESULTS_PATH}
echo " Test CSV Logs Report is at ${CSV_RESULTS_PATH}"
echo " --------------------------------------------------------------------------"
