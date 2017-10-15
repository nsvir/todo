from model.Task import Task
from repository.TodoDatabase import TodoDatabase
"""

"""
class TodoService():

    def __init__(self, todoDatabase):
        self.todoDatabase = todoDatabase
        self.tasks = todoDatabase.retrieve()

    def addTask(self, taskName):
        taskObject = Task(taskName)
        self.tasks.append(taskObject)
        self.todoDatabase.add(taskObject)

    def getTask(self, taskName):
        elementsMatching = list(filter(lambda task: task.name() == taskName, self.tasks))
        if len(elementsMatching) > 0:
            return elementsMatching[0]
        return None

    def removeTask(self, taskName):
        taskObject = self.getTask(taskName)
        self.todoDatabase.delete(taskObject)
        self.tasks.remove(taskObject)

    def checkTask(self, taskName):
        task = self.getTask(taskName)
        if not task is None:
            self.getTask(taskName).setIsDone()
            self.todoDatabase.update(task)

    def getTasks(self):
        return self.tasks;
