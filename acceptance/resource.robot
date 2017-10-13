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

*** Keywords ***
Open Browser To Tasks Page
    Open Browser    ${TASKS URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}

Input List
    [Arguments]    ${name}
    Input Text    inputListe        ${name}

Click Addlist
    Click Element    addList