from model.task_list import *

class TaskListFactory:
    
    def createTaskList(self, name):
        return TaskList(name, 0, '', 0, 0, '')

    def createTaskListWithElements(self, name, desapear, hour, hebdo, desapearHebdo, hourHebdo):
        if desapear == None or desapear == 0:
            desapear = 0
        else:
            desapear = 1
        if hour == None:
            hour = ''
        if hebdo == None or hebdo == 0:
            hebdo = 0
        else:
            hebdo = 1
        if desapearHebdo == None or desapearHebdo == 0:
            desapearHebdo = 0
        else:
            desapearHebdo = 1
        if hourHebdo == None:
            hourHebdo = ''
        return TaskList(name, desapear, hour, hebdo, desapearHebdo, hourHebdo)