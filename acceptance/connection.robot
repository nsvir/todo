*** Settings ***
Documentation     A test suite with a list add style test.
...
...               This test has a workflow that is created
Resource          resource.robot

*** Test Cases ***
Connect an user
    Given browser is opened to login page
    When user enter his identification
    And submit connection
    Then Page should be home
    [Teardown]    Close Browser

Connect a bad user with bad login and bad password
    Given browser is opened to login page
    When user enter his false identification
    And submit connection
    Then Page should be submitLogin
    [Teardown]    Close Browser

Connect a bad user with bad password
    Given browser is opened to login page
    When user enter his good name and bad pass
    And submit connection
    Then Page should be submitLogin
    [Teardown]    Close Browser

*** Keywords ***

browser is opened to login page
    Open Browser To Login Page

User Enter His Identification
    Input Login 
    Input Password

User Enter His False Identification
    Input Bad Login 
    Input Bad Password

User Enter His Good Name And Bad Pass
    Input Login 
    Input Bad Password

Submit Connection
    Click Button Connect

Page Should Be Home
    Location Should Be    http://localhost:8080/

Page Should Be SubmitLogin
    Location Should Be    http://localhost:8080/submitLogin