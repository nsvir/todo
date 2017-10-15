from model.Task import Task
"""

"""
class TodoService():

    def __init__(self):
        self.todoDatabase = None
        self.tasks = []

    def addTask(self, taskName):
        self.tasks.append(Task(taskName))

    def getTask(self, taskName):
        elementsMatching = list(filter(lambda task: task.name() == taskName, self.tasks))
        if len(elementsMatching) > 0:
            return elementsMatching[0]
        return None

    def removeTask(self, taskName):
        self.tasks = list(filter(lambda taskInList: taskName != taskInList.name(), self.tasks))

    def checkTask(self, taskName):
        task = self.getTask(taskName)
        if not task is None:
            self.getTask(taskName).setIsDone()

    def getTasks(self):
        return self.tasks;
