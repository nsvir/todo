from model.Task import Task
"""

"""
class TodoService():

    def __init__(self):
        self.todoDatabase = None
        self.tasks = []

    def addTask(self, task):
        self.tasks.append(Task(task))

    def removeTask(self, task):
        self.tasks = list(filter(lambda taskInList: task != taskInList.name(), self.tasks))

    def getTasks(self):
        return self.tasks;
