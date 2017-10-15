import unittest
import mockito
from model.list_todo import *

class TestInitListTodo(unittest.TestCase):

    def test_todo_list_vide_creation(self):
        listTodo = ListTodo()
        self.assertEqual([], listTodo.list())

class TestAddInList(unittest.TestCase):

    def test_add_in_todo_list(self):
        listTodo = ListTodo()
        taskList = mockito.mock()
        listTodo.add_list(taskList)
        self.assertIn(taskList, listTodo.list())

    def test_add3_names_in_todo_list(self):
        listTodo = ListTodo()
        taskList = mockito.mock()
        taskList2 = mockito.mock()
        taskList3 = mockito.mock()
        listTodo.add_list(taskList)
        listTodo.add_list(taskList2)
        listTodo.add_list(taskList3)
        self.assertEquals([taskList, taskList2, taskList3], listTodo.list())

class TestContainsInList(unittest.TestCase):

    def test_contains_in_todo_list_return_true(self):
        listTodo = ListTodo()
        lst=[]
        taskListfound = mockito.mock()
        taskList = mockito.mock()
        taskList2 = mockito.mock()

        listTodo.add_list(taskList)
        listTodo.add_list(taskList2)
        mockito.when(taskList).name().thenReturn('name')
        mockito.when(taskList2).name().thenReturn('liste')
        mockito.when(taskListfound).name().thenReturn('name')
        self.assertTrue(listTodo.contains_list(taskListfound))

    def test_contains_in_todo_list_return_false(self):
        listTodo = ListTodo()
        lst=[]
        taskListfound = mockito.mock()
        taskList = mockito.mock()
        taskList2 = mockito.mock()

        listTodo.add_list(taskList)
        listTodo.add_list(taskList2)
        mockito.when(taskList).name().thenReturn('name')
        mockito.when(taskList2).name().thenReturn('liste')
        mockito.when(taskListfound).name().thenReturn('liste')
        self.assertTrue(listTodo.contains_list(taskListfound))

    def test_contains_in_todo_list_in_empty(self):
        listTodo = ListTodo()
        taskList = mockito.mock()
        self.assertFalse(listTodo.contains_list(taskList))

    def test_contains_in_todo_list_multiple_return_false(self):
        listTodo = ListTodo()
        lst=[]
        taskListfound = mockito.mock()
        taskList = mockito.mock()
        taskList2 = mockito.mock()

        listTodo.add_list(taskList)
        listTodo.add_list(taskList2)
        mockito.when(taskList).name().thenReturn('name')
        mockito.when(taskList2).name().thenReturn('liste')
        mockito.when(taskListfound).name().thenReturn('liste3')
        self.assertFalse(listTodo.contains_list(taskListfound))

