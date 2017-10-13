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

    def add_list(self, name):
        self.list_todo.add_list(name)
        self.repository.add_list_into_repository(name)

    def get_list(self):
        return self.repository.get_list_repository()