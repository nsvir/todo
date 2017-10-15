from model.task_list import *

class TaskListFactory:
    
    def createTaskList(self, name):
        return TaskList(name, 0, '')

    def createTaskListWithElements(self, name, desapear, hour):
        if desapear == None or desapear == 0:
            desapear = 0
        else:
            desapear = 1
        if hour == None:
            hour = ''
        return TaskList(name, desapear, hour)