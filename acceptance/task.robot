*** Settings ***
Documentation     A test suite with task add style
...
...               This test has a workflow that is created
Resource          resource.robot

*** Variables ***
${TASK}           Make the dishes
${REMOVETASK}           Make the dishes to remove
${CHECKTASK}      Not do the dishes
*** Test Cases ***
Add a task
    Given browser is opened to tasks page
    When user write a new "${TASK}"
    And click the button to add a task
    Then Task List Should Contain "${TASK}"
    [Teardown]    Close Browser

Check a task
  Given browser is opened to tasks page
  And task list contain "${CHECKTASK}"
  When I click the checkbox of task "${CHECKTASK}"
  Then the "${CHECKTASK}" should be done
  [Teardown]    Close Browser

Remove a task
    Given browser is opened to tasks page
    And task list contain "${REMOVETASK}"
    When I click on delete of "${REMOVETASK}"
    Then Page Should Not Contain   ${REMOVETASK}
    [Teardown]    Close Browser

*** Keywords ***
the "${CHECKTASK}" should be done
  Checkbox Should Be Selected   done${CHECKTASK}

I click the checkbox of task "${CHECKTASK}"
  Wait Until Element Is Visible    done${CHECKTASK}
  Select Checkbox    done${CHECKTASK}

I click on delete of "${name}"
  Click Element    remove${name}

task list contain "${name}"
  User write a new "${name}"
  Click the button to add a task

Browser is opened to tasks page
  Open Browser To Tasks Page

User write a new "${name}"
  Input Task    ${name}

Click the button to add a task
  Click Button AddTask

Task List Should Contain "${name}"
  Page Should Contain    ${name}
