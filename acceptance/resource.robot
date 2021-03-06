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
${LOGIN URL}      http://${SERVER}/login
${SETTINGS LISTE URL}      http://${SERVER}/listSettings/liste
${SETTINGS LISTE654 URL}      http://${SERVER}/listSettings/liste

*** Keywords ***
Open Browser To Tasks Page
    Open Browser    ${TASKS URL}    ${BROWSER}
    Set Selenium Speed    ${DELAY}

Open Browser To Login Page
    Open Browser    ${LOGIN URL}    ${BROWSER}
    Set Selenium Speed    ${DELAY}

Open Browser to SettingsListe Page
    Open Browser    ${SETTINGS LISTE URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}

Go to SettingsListe Page
    Go To    ${SETTINGS LISTE URL}  
    Set Selenium Speed    ${DELAY}

Go to SettingsListe654 Page
    Go To    ${SETTINGS LISTE654 URL}  
    Set Selenium Speed    ${DELAY}

Input List
    [Arguments]    ${name}
    Input Text    inputListe        ${name}

Input Login
    Input Text    login    test

Input Password
    Input Text    password    test

Input Bad Login
    Input Text    login    tesert

Input Bad Password
    Input Text    password    tesert

Input Task
    [Arguments]    ${name}
    Input Text    inputTask        ${name}

Input TimeDeseaper
    [Arguments]    ${time}
    Input Text    timeDisapear        ${time}

Input TimeDeseaperHebdo
    [Arguments]    ${time}
    Input Text    timeDisapearHebdo        ${time}

Input NameTask
    [Arguments]    ${name}
    Input Text    newTaskName        ${name}

Click Button AddList
    Click Element    addList

Click Button AddTask
    Click Element    addTask

Click Button SetListListe
    Click Element    list_liste

Click Button SetListListe654
    Click Element    list_liste654

Click Button SetListListeTestByTime
    Click Element    list_deletelistebytimetest

Click Button DeleteListListe
    Click Element    delete_list_deletelistetest

Click Button DeleteListListeByTime
    Click Element    delete_list_deletelistebytimetest

Click Button SubmitSettingsListe
    Click Element    settings_submit

Click Checkbox Disapear
    Click Element   desapearTask

Click Checkbox DisapearHebdo
    Click Element   desapearTaskHebdo

Click Checkbox Hebdo
    Click Element   hebdo

Click Button Home
    Click Element   desapearTask

Click Button Connect
    Click Element   login_submit