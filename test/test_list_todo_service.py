import unittest
import mockito
from list_todo_service import *

class TestInitListTodoService(unittest.TestCase):

    def test_add_list(self):
        lst = mockito.mock()
        service = ListTodoService(lst)

        service.add_list("name")
        mockito.verify(lst).add_list("name")
