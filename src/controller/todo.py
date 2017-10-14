from bottle import Bottle, template
import os, sys

"""
Controller to redirect todo requests
"""
class TodoApp(Bottle):
    def __init__(self, todoService = None, template = template):
        self.service = todoService
        self.template = template

    def home(self):
        #output = self.template('src/web/template/make.tpl', rows=[], lists=[], list=None)
        return None

