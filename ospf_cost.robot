*** Settings ***
Library        ats.robot.pyATSRobot
Library        genie.libs.robot.GenieRobot
Library        unicon.robot.UniconRobot
Suite setup    Setup

*** Variables ***
${testbed}    ./tb.yaml

*** Keywords ***
Setup
    use genie testbed "${testbed}"
    connect to devices "xr1"

*** Test Cases ***
Verify Cost 10
    ${output}=    execute "show ospf interface Gi0/0/0/0 | i Cost" on device "xr1"
    Should Contain  ${output}    Cost: 10
