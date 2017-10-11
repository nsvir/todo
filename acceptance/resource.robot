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
${VALID USER}     demo
${VALID PASSWORD}    mode
${TODO URL}      http://${SERVER}/todo
${WELCOME URL}    http://${SERVER}/welcome.html
${ERROR URL}      http://${SERVER}/error.html
${TASKS URL}      http://${SERVER}/tasks

*** Keywords ***
Open Browser To Todo Page
    Open Browser    ${TODO URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    Todo Page Should Be Open

Open Browser To Tasks Page
    Open Browser    ${TASKS URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}

Todo Page Should Be Open
    Title Should Be    Todo Page

Go To Login Page
    Go To    ${LOGIN URL}
    Login Page Should Be Open

Input Username
    [Arguments]    ${username}
    Input Text    username_field    ${username}

Input Password
    [Arguments]    ${password}
    Input Text    password_field    ${password}

Input Text
    [Arguments]    ${name}
    Input Text    inputList    ${name}

Submit Credentials
    Click Button    login_button

Welcome Page Should Be Open
    Location Should Be    ${WELCOME URL}
    Title Should Be    Welcome Page
