"""
Definition of Todo entrypoints
"""

class Todo():

    def __init__(self, client):
        self.client = client

    def addList(self, list_name):
        self.client.get("/addList/{}".format(list_name))

    def removeList(self, list_name):
        self.client.get("/deleteList/{}".format(list_name))

    def addTask(self, task, list_name):
        self.client.get("/addTask/{}/{}".format(task, list_name))

    def removeTask(self, task):
        self.client.get("/removeTask/{}".format(task))

    def showTasks(self):
        self.client.get("/")
