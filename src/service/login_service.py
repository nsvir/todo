import sqlite3
from sqlite3 import Error
from model.users import *


class LoginService:

    """
    Service for todo list

    When add a list, the model have this list and it save on database
    When get a list, request to database
    """

    def __init__(self, repository, list_users, user_factory, cryptage):
        self.repository = repository
        self.list_users = list_users
        self.user_factory = user_factory
        self.cryptage = cryptage

    def init_users(self):
        users = self.repository.get_all_list()
        lst = []
        for row in users:
            lst.append(self.user_factory.create(row[0], row[1]))
        self.list_users.set_users(lst)

    def user_exists(self, login, password):
        pass_crypt = self.cryptage.crypt(password)
        return self.list_users.user_exists(login, pass_crypt)