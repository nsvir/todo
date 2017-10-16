from bottle import Bottle, request, template, debug, static_file, redirect
import os, sys

debug(True)

"""
Controller to manage list todo
"""
class Init:
    def __init__(self, listService, listRepository, taskListFactory, todoService):
        self.listService = listService
        self.listRepository = listRepository
        self.taskListFactory = taskListFactory
        self.todoService = todoService

    def initTodoList(self, listTodo):
        self.listService.initTodoList(listTodo, self.taskListFactory)
        self.listService.remove_desable_lists()
        self.todoService.remove_desable_tasks(self.listService.get_all_lst())