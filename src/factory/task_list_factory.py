from model.task_list import *

class TaskListFactory:
    
    def createTaskList(self, name):
        return TaskList(name, 0, '', 0, 0, '')

    def createTaskListWithElements(self, name, desapear, hour, hebdo, desapearHebdo, hourHebdo):
        return TaskList(name, desapear, hour, hebdo, desapearHebdo, hourHebdo)