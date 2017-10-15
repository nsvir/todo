from bottle import Bottle, template
import os, sys


"""
Controller to redirect todo requests
"""
class TodoApp():
    def __init__(self, listTodoService, todoService = None, template = template):
        self.service = todoService
        self.template = template
        self.listTodoService = listTodoService

    def home(self):
        self.listTodoService.remove_desable_lists()
        lists = self.listTodoService.get_list_name()
        output = self.template('src/web/template/make.tpl', rows=[], lists=lists, list=None)
        return output
