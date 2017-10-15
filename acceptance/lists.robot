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
    When user submit setting form
    Then changes are enregistred

Configure a list with only hour input
    Given browser is opened to tasks page 
    And list "liste" already created
    And user click on settings button of list "liste"
    And user write on timeDeseaper "12:00"
    When user submit setting form
    Then changes are enregistred

Configure a list with check and hour input
    Given browser is opened to tasks page 
    And list "liste" already created
    And user click on settings button of list "liste"
    And user click on disapear checkbox
    And user write on timeDeseaper "12:00"
    When user submit setting form
    Then changes are enregistred

Configure a list with check and bad hour input
    Given browser is opened to tasks page 
    And list "liste" already created
    And user click on settings button of list "liste"
    And user click on disapear checkbox
    And user write on timeDeseaper "32:00"
    When user submit setting form
    Then changes are not enregistred

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

User Submit Setting Form
    Click Button SubmitSettingsListe

Changes Are Enregistred
    Wait Until Page Contains      Enregistré       5s

User Write On TimeDeseaper "${time}"
    Input TimeDeseaper    ${time}

User Click On Disapear Checkbox
    Click Checkbox Disapear

Changes Are Not Enregistred
    Wait Until Page Contains      Error       5s