*** Settings ***
Documentation     A test suite with a list add style test.
...
...               This test has a workflow that is created
using keywords in the imported resource file.
Resource          resource.robot

*** Test Cases ***
Valid Login
    Given browser is opened to tasks page
    When user write a new list "mode"
    Then list is created

*** Keywords ***
Browser is opened to tasks page
    Open Browser To Tasks Page

User write a new list "${name}"
    Input Text id=inputList    ${name}
    Click element id=addList

List is created

