from model.Task import Task
from repository.TodoDatabase import TodoDatabase
import time
"""

"""
class TodoService():

    def __init__(self, todoDatabase, fabrique_task):
        self.todoDatabase = todoDatabase
        self.tasks = todoDatabase.retrieve()
        self.fabrique_task = fabrique_task

    def addTask(self, taskName, listname):
        taskObject = self.fabrique_task.create(taskName, listname)
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
        print('here')
        self.tasks.remove(taskObject)

    def checkTask(self, taskName):
        task = self.getTask(taskName)
        if not task is None:
            self.getTask(taskName).setIsDone()
            self.todoDatabase.update(task)

    def updateTask(self, taskName, newTaskName):
        task = self.getTask(taskName)
        if not task is None:
            self.getTask(taskName).set_name(newTaskName)
            self.todoDatabase.update_with_old_name(taskName, task)

    def getTasks(self):
        return self.tasks;

    def getVisibleTasks(self):
        res = []
        for t in self.tasks:
            if t.is_visible():
                res.append(t)
        return res

    def getTasksByListname(self, listname):
        res = []
        for t in self.tasks:
            if t.listname() == listname:
                res.append(t)
        return res

    def remove_desable_tasks(self, lstsTask):
        for lst in lstsTask:
            if lst.hebdo() == 1 and lst.desapearHebdo() ==1 and lst.hourHebdo() != '':
                minutes = lst.hourHebdo()[3:]
                heur = lst.hourHebdo()[:2]
                now_min = time.strftime("%M")
                now_hour = time.strftime("%H")
                if (now_hour > heur or (now_hour == heur and now_min > minutes)) :
                    self.desable_lst_by_listname(lst.name())
                else :
                    self.enable_lst_by_listname(lst.name())

    def desable_lst_by_listname(self, listname):
        self.todoDatabase.desable_tasks_by_listname(listname)
        for task in self.tasks:
            if task.listname() == listname:
                task.invisible()

    def enable_lst_by_listname(self, listname):
        self.todoDatabase.enable_tasks_by_listname(listname)
        for task in self.tasks:
            if task.listname() == listname:
                task.visible()

    def takeTask(self, taskname, login):
        task = self.getTask(taskname)
        if not task is None: 
            task.setLogin(login)
            self.todoDatabase.takeTask(task)