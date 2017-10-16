from bottle import Bottle, template, redirect, request
import os, sys
from service.todo_service import TodoService


"""
Controller to redirect todo requests
"""
class TodoApp():

    def __init__(self, listTodoService, \
                todoService, template = template, \
                request = request, redirect = redirect):
        self.service = todoService
        self.template = template
        self.listTodoService = listTodoService
        self.request = request
        self.redirect = redirect

    def home(self):
        res = self.listTodoService.remove_desable_lists()
        for tasklist in res:
            tasks = self.service.getTasksByListname(tasklist)
            for t in tasks:
                self.service.removeTask(t.name())
        self.service.remove_desable_tasks(self.listTodoService.get_all_lst())
        tasks = self.service.getVisibleTasks()
        lists = self.listTodoService.get_list_name()
        output = self.template('src/web/template/make.tpl', tasks=tasks, lists=lists, list=None)
        return output

    def addTask(self, task, listname):
        self.service.addTask(task ,listname)
        self.redirect("/")

    def removeTask(self, task):
        self.service.removeTask(task)
        self.redirect("/")

    def updateTask(self, task):
        return self.template('src/web/template/updateTask.tpl', task=task)

    def submitUpdateTask(self, oldname, newname):
        self.service.updateTask(oldname, newname)
        self.redirect("/")

    def checkTask(self, task):
        self.service.checkTask(task)
        self.redirect("/")
