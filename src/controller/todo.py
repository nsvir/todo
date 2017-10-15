from bottle import Bottle, template
import os, sys


"""
Controller to redirect todo requests
"""
class TodoApp():
    def __init__(self, listTodoServer, todoService = None, template = template):
        self.service = todoService
        self.template = template
        self.listTodoServer = listTodoServer

    def home(self):
        lists = self.listTodoServer.get_list_name()
        output = self.template('src/web/template/make.tpl', rows=[], lists=lists, list=None)
        return output
