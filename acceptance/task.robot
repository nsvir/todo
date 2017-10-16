*** Settings ***
Documentation     A test suite with task add style
...
...               This test has a workflow that is created
Resource          resource.robot

*** Variables ***
${TASK}           Make the dishes
${REMOVETASK}           Make the dishes to remove
${CHECKTASK}      Not do the dishes
${NEWTASKNAME}    Changer le nom de la tâche
${UPDATETASK}     Do homework
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

Update a task
    Given browser is opened to tasks page
    And task list contain "${UPDATETASK}"
    When I click on update of "${UPDATETASK}"
    Then Page Should Contain   ${NEWTASKNAME}
    [Teardown]    Close Browser

Update a task change name
    Given browser is opened to tasks page
    And task list contain "${UPDATETASK}"
    And I click on update of "${UPDATETASK}"
    And Page Should Contain   ${NEWTASKNAME}
    When I write a new name "new_nameyouhou"
    And I submit NameForm
    Then Page Should Contain   "new_nameyouhou"
    [Teardown]    Close Browser

*** Keywords ***
the "${CHECKTASK}" should be done
  Checkbox Should Be Selected   done${CHECKTASK}

I click the checkbox of task "${CHECKTASK}"
  Wait Until Element Is Visible    done${CHECKTASK}
  Select Checkbox    done${CHECKTASK}

I click on delete of "${name}"
  Click Element    remove${name}

I click on update of "${name}"
  Click Element    update${name}

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

I Write A New Name "new_nameyouhou"
  Input NameTask    "new_nameyouhou"

I Submit NameForm
  Click Element    submitUpdateTask