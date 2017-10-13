*** Settings ***
Documentation     A test suite with a list add style test.
...
...               This test has a workflow that is created
Resource          resource.robot

*** Test Cases ***
Valid Login
    Given browser is opened to tasks page
    When user write a new list "mode"
    Then List Should Contain "mode"
    [Teardown]    Close Browser

*** Keywords ***
Browser is opened to tasks page
    Open Browser To Tasks Page

User write a new list "${name}"
    Input List    ${name}
    Click Button AddList

List Should Contain "${name}"
    Page Should Contain    ${name}

