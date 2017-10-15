from bottle import Bottle, template, redirect, request
import os, sys
from service.todo_service import TodoService


"""
Controller to redirect todo requests
"""
class TodoApp():
    def __init__(self, listTodoServer, \
                todoService = TodoService(), template = template, \
                request = request, redirect = redirect):
        self.service = todoService
        self.template = template
        self.listTodoServer = listTodoServer
        self.request = request
        self.redirect = redirect

    def home(self):
        tasks = self.service.getTasks()
        lists = self.listTodoServer.get_list_name()
        output = self.template('src/web/template/make.tpl', tasks=tasks, lists=lists, list=None)
        return output

    def addTask(self, task):
        self.service.addTask(task)
        self.redirect("/")

    def removeTask(self, task):
        self.service.removeTask(task)
        self.redirect("/")
