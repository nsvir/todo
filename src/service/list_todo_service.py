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
        self.repository.add_list_into_repository(taskList.name(), taskList.desapear(), taskList.hour(), taskList.hebdo(), taskList.desapearHebdo(), taskList.hourHebdo())

    def remove_list(self, listname):
        self.list_todo.remove_list(listname)
        self.repository.remove_list_into_repository(listname)

    def get_list_name(self):
        return self.repository.get_list_name_repository()

    def list_exists_by_name(self, listname):
        return self.list_todo.contains_list_by_name(listname)

    def list_exists(self, taskList):
        return self.list_todo.contains_list(taskList)

    def save_settings(self, taskList):
        if self.list_todo.contains_list(taskList):
            self.repository.update_settings(taskList.name(), taskList.desapear(), taskList.hour(), taskList.hebdo(), taskList.desapearHebdo(), taskList.hourHebdo())

    def initTodoList(self, listTodo, factory):
        results = self.repository.get_all_list()
        for res in results: 
            lst = factory.createTaskListWithElements(res[0], res[1], res[2], res[3], res[4], res[5])
            listTodo.add_list(lst)

    def get_lst(self, name):
        return self.list_todo.get_list(name)