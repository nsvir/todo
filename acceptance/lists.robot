*** Settings ***
Documentation     A test suite with a list add style test.
...
...               This test has a workflow that is created
Resource          resource.robot

*** Test Cases ***
Add a list
    Given browser is opened to tasks page
    When user write a new list "mode"
    Then List Should Contain "mode"
    [Teardown]    Close Browser

Want configure a list
    Given browser is opened to tasks page 
    And list "liste" already created
    When user click on settings button of list "liste"
    Then browser is opened to settings page of list "liste"

Configure a list
    Given browser is opened to tasks page 
    And list "liste" already created
    And user click on settings button of list "liste"
    When user submit setting form without change
    Then browser is opened to settings page of list "liste" without change

*** Keywords ***
Browser is opened to tasks page
    Open Browser To Tasks Page

User write a new list "${name}"
    Input List    ${name}
    Click Button AddList

List Should Contain "${name}"
    Page Should Contain    ${name}

List "${liste}" Already Created
    Open Browser To Tasks Page
    Input List    ${liste}
    Click Button AddList

User Click On Settings Button Of List "liste"
    Click Button SetListListe

Browser is opened to settings page of list "liste"
    Go to SettingsListe Page

User Submit Setting Form Without Change
    Click Button SubmitSettingsListe

Browser Is Opened To Settings Page Of List "liste" Without Change
    Wait Until Page Contains      Enregistré       5s