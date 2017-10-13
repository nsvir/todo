*** Settings ***
Documentation     A test suite with task add style
...
...               This test has a workflow that is created
Resource          resource.robot

*** Variables ***
${TASK}           Make the dishes

*** Test Cases ***
Add a task
    Given browser is opened to tasks page
    When user write a new "${TASK}"
    And click the button to add a task
    Then Task List Should Contain "${TASK}"
    [Teardown]    Close Browser

*** Keywords ***
Browser is opened to tasks page
    Open Browser To Tasks Page

User write a new "${name}"
    Input Task    ${name}

Click the button to add a task
    Click Button AddTask

Task List Should Contain "${name}"
    Page Should Contain    ${name}



