import unittest
import mockito
from service.list_todo_service import *

class TestAddListTodoService(unittest.TestCase):

    def test_add_list(self):
        repository = mockito.mock()
        lst = mockito.mock()
        service = ListTodoService(repository, lst)

        service.add_list("name")
        mockito.verify(lst).add_list("name")
        mockito.verify(repository).add_list_into_repository("name")


class TestGetListTodoService(unittest.TestCase):

    def test_get_list(self):
        repository = mockito.mock()
        lst = mockito.mock()
        service = ListTodoService(repository, lst)

        service.get_list()
        mockito.verify(repository).get_list_repository()
