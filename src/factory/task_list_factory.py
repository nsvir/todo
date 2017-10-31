from model.task_list import *

class TaskListFactory:
    
    def createTaskList(self, name, session):
        return TaskList(name, 0, '', 0, 0, '', [session.login()])

    def createTaskListWithElements(self, name, desapear, hour, hebdo, desapearHebdo, hourHebdo, listUsers):
        return TaskList(name, desapear, hour, hebdo, desapearHebdo, hourHebdo, listUsers)