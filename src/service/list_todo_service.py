import sqlite3
from sqlite3 import Error
from model.list_todo import *


class ListTodoService:

    """
    Service for todo list

    When add a list, the model have this list and it save on database
    When get a list, request to database
    """

    def __init__(self, repository, list_todo):
        self.repository = repository
        self.list_todo = list_todo

    def add_list(self, taskList):
        self.list_todo.add_list(taskList)
        self.repository.add_list_into_repository(taskList.name(), taskList.desapear(), taskList.hour())

    def get_list_name(self):
        return self.repository.get_list_name_repository()

    def list_exists(self, taskList):
        return self.list_todo.contains_list(taskList)

    def save_settings(self, taskList):
        if self.list_todo.contains_list(taskList):
            self.repository.update_settings(taskList.name(), taskList.desapear(), taskList.hour())

    def initTodoList(self, listTodo, factory):
        results = self.repository.get_all_list()
        for res in results: 
            lst = factory.createTaskListWithElements(res[0], res[1], res[2])
            listTodo.add_list(lst)
