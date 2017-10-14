*** Settings ***
Documentation     A resource file with reusable keywords and variables.
...
...               The system specific keywords created here form our own
...               domain specific language. They utilize keywords provided
...               by the imported Selenium2Library.
Library           Selenium2Library

*** Variables ***
${SERVER}         localhost:8080
${BROWSER}        Firefox
${DELAY}          0
${TASKS URL}      http://${SERVER}/
${SETTINGS LISTE URL}      http://${SERVER}/listSettings/liste

*** Keywords ***
Open Browser To Tasks Page
    Open Browser    ${TASKS URL}    ${BROWSER}
    Set Selenium Speed    ${DELAY}

Open Browser to SettingsListe Page
    Open Browser    ${SETTINGS LISTE URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}

Go to SettingsListe Page
    Go To    ${SETTINGS LISTE URL}  
    Set Selenium Speed    ${DELAY}

Input List
    [Arguments]    ${name}
    Input Text    inputListe        ${name}

Input Task
    [Arguments]    ${name}
    Input Text    inputTask        ${name}

Click Button AddList
    Click Element    addList

Click Button AddTask
    Click Element    addTask

Click Button SetListListe
    Click Element    list_liste

Click Button SubmitSettingsListe
    Click Element    settings_submit