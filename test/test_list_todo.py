import unittest
from list_todo import *

class TestInitListTodo(unittest.TestCase):

    def test_todo_list_vide_creation(self):
        listTodo = ListTodo()
        self.assertEqual([], listTodo.list())

class TestAddInList(unittest.TestCase):

    def test_add_in_todo_list(self):
        listTodo = ListTodo()
        listTodo.add_list("liste1")
        self.assertEquals(["liste1"], listTodo.list())

    def test_add3_names_in_todo_list(self):
        listTodo = ListTodo()
        listTodo.add_list("liste1")
        listTodo.add_list("liste2")
        listTodo.add_list("liste3")
        self.assertEquals(["liste1", "liste2", "liste3"], listTodo.list())

class TestContainsInList(unittest.TestCase):

    def test_contains_in_todo_list_return_true(self):
        listTodo = ListTodo()
        listTodo.add_list("liste1")
        self.assertTrue(listTodo.contains_list("liste1"))

    def test_contains_in_todo_list_return_false(self):
        listTodo = ListTodo()
        listTodo.add_list("liste1")
        self.assertFalse(listTodo.contains_list("liste2"))

    def test_contains_in_todo_list_in_empty(self):
        listTodo = ListTodo()
        self.assertFalse(listTodo.contains_list("liste"))

