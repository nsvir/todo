from bottle import Bottle, template, redirect, request
import os, sys
from service.todo_service import TodoService


"""
Controller to redirect todo requests
"""
class TodoApp():

    def __init__(self, listTodoService, \
                todoService = TodoService(), template = template, \
                request = request, redirect = redirect):
        self.service = todoService
        self.template = template
        self.listTodoService = listTodoService
        self.request = request
        self.redirect = redirect

    def home(self):
        self.listTodoService.remove_desable_lists()
        tasks = self.service.getTasks()
        lists = self.listTodoService.get_list_name()
        output = self.template('src/web/template/make.tpl', tasks=tasks, lists=lists, list=None)
        return output

    def addTask(self, task):
        self.service.addTask(task)
        self.redirect("/")

    def removeTask(self, task):
        self.service.removeTask(task)
        self.redirect("/")

    def checkTask(self, task):
        self.service.checkTask(task)
        self.redirect("/")
