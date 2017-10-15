*** Settings ***
Documentation     A test suite with a list add style test.
...
...               This test has a workflow that is created
Resource          resource.robot

*** Test Cases ***
Add a list with a good name
    Given browser is opened to tasks page
    When user write a new list "mode"
    Then List Should Contain "mode"
    [Teardown]    Close Browser

Add a list with a bad name
    Given browser is opened to tasks page
    When user write a new list "<scr*$>"
    Then List Should Not Contain "<scr*$>"
    [Teardown]    Close Browser

Want configure a list and submit without change
    Given browser is opened to tasks page 
    And list "liste" already created
    When user click on settings button of list "liste"
    Then browser is opened to settings page of list "liste"
    [Teardown]    Close Browser

Configure a list
    Given browser is opened to tasks page 
    And list "liste" already created
    And user click on settings button of list "liste"
    When user submit setting form
    Then changes are enregistred
    [Teardown]    Close Browser

Configure a list and return to home page
    Given browser is opened to tasks page 
    And list "liste" already created
    And user click on settings button of list "liste"
    When user click on home button
    Then browser is opened to tasks page
    [Teardown]    Close Browser

Configure a list with only hour input
    Given browser is opened to tasks page 
    And list "liste" already created
    And user click on settings button of list "liste"
    And user write on timeDeseaper "12:00"
    When user submit setting form
    Then changes are enregistred
    [Teardown]    Close Browser

Configure a list with only hour hebdo input
    Given browser is opened to tasks page 
    And list "liste" already created
    And user click on settings button of list "liste"
    And user write on timeDeseaperHebdo "12:00"
    When user submit setting form
    Then changes are enregistred
    [Teardown]    Close Browser

Configure a list with check and hour input
    Given browser is opened to tasks page 
    And list "liste" already created
    And user click on settings button of list "liste"
    And user click on disapear checkbox
    And user write on timeDeseaper "12:00"
    When user submit setting form
    Then changes are enregistred
    [Teardown]    Close Browser

Configure a list with checkhebdo and hourhebdo input
    Given browser is opened to tasks page 
    And list "liste" already created
    And user click on settings button of list "liste"
    And user click on disapearHebdo checkbox
    And user write on timeDeseaperHebdo "12:00"
    When user submit setting form
    Then changes are enregistred
    [Teardown]    Close Browser

Configure a list with checkhebdo and hourhebdo input and hebdo input
    Given browser is opened to tasks page 
    And list "liste" already created
    And user click on settings button of list "liste"
    And user click on hebdo checkbox
    And user click on disapearHebdo checkbox
    And user write on timeDeseaperHebdo "12:00"
    When user submit setting form
    Then changes are enregistred
    [Teardown]    Close Browser

Configure a list with check and bad hour input
    Given browser is opened to tasks page 
    And list "liste654" already created
    And user click on settings button of list "liste654"
    And user click on disapear checkbox
    And user write on timeDeseaper "32:00"
    When user submit setting form
    Then changes are not enregistred
    [Teardown]    Close Browser

Configure a list with check and bad hour hebdo input
    Given browser is opened to tasks page 
    And list "liste654" already created
    And user click on settings button of list "liste654"
    And user click on disapearHebdo checkbox
    And user write on timeDeseaperHebdo "32:00"
    When user submit setting form
    Then changes are not enregistred
    [Teardown]    Close Browser

Remove a list
    Given browser is opened to tasks page 
    And list "deletelistetest" already created
    When user click on delete button of list "deletelistetest"
    Then List Should Not Contain "deletelistetest"
    [Teardown]    Close Browser

*** Keywords ***
Browser is opened to tasks page
    Open Browser To Tasks Page

User write a new list "${name}"
    Input List    ${name}
    Click Button AddList

List Should Contain "${name}"
    Page Should Contain    ${name}

List Should Not Contain "${name}"
    Page Should Not Contain    ${name}

List "${liste}" Already Created
    Open Browser To Tasks Page
    Input List    ${liste}
    Click Button AddList

User Click On Settings Button Of List "liste"
    Click Button SetListListe

User Click On Settings Button Of List "liste654"
    Click Button SetListListe654

User Click On Delete Button Of List "deletelistetest"
    Click Button DeleteListListe

Browser is opened to settings page of list "liste"
    Go to SettingsListe Page

Browser is opened to settings page of list "liste654"
    Go to SettingsListe654 Page

User Submit Setting Form
    Click Button SubmitSettingsListe

Changes Are Enregistred
    Wait Until Page Contains      Enregistré       5s

User Write On TimeDeseaper "${time}"
    Input TimeDeseaper    ${time}

User Write On TimeDeseaperHebdo "${time}"
    Input TimeDeseaperHebdo    ${time}

User Click On Disapear Checkbox
    Click Checkbox Disapear

User Click On DisapearHebdo Checkbox
    Click Checkbox DisapearHebdo

User Click On Hebdo Checkbox
    Click Checkbox Hebdo

Changes Are Not Enregistred
    Wait Until Page Contains      Error       5s

User Click On Home Button
    Click Button Home