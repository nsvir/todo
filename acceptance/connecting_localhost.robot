*** Settings ***
Documentation     A test suite with a single test for bottle connection
...
...               This test has a workflow that is created using keywords in
...               the imported resource file.
Resource          resource.robot

*** Test Cases ***
Connect to Todo App
    Open Browser To Todo Page
    Todo Page Should Be Open
