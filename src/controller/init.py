from bottle import Bottle, request, template, debug, static_file, redirect
import os, sys

debug(True)

"""
Controller to manage list todo
"""
class Init:
    def __init__(self, listService, listRepository, taskListFactory):
        self.listService = listService
        self.listRepository = listRepository
        self.taskListFactory = taskListFactory

    def initTodoList(self, listTodo):
        self.listService.initTodoList(listTodo, self.taskListFactory)