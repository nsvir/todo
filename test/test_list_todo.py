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

    def test_contains_in_todo_list_by_name_return_true(self):
        listTodo = ListTodo()
        lst=[]
        taskList = mockito.mock()
        taskList2 = mockito.mock()

        listTodo.add_list(taskList)
        listTodo.add_list(taskList2)
        mockito.when(taskList).name().thenReturn('name')
        mockito.when(taskList2).name().thenReturn('liste')
        self.assertTrue(listTodo.contains_list_by_name('name'))

    def test_contains_in_todo_list_by_name_return_false(self):
        listTodo = ListTodo()
        lst=[]
        taskList = mockito.mock()
        taskList2 = mockito.mock()

        listTodo.add_list(taskList)
        listTodo.add_list(taskList2)
        mockito.when(taskList).name().thenReturn('name')
        mockito.when(taskList2).name().thenReturn('liste')
        self.assertTrue(listTodo.contains_list_by_name('liste'))

    def test_contains_in_todo_list_by_name_in_empty(self):
        listTodo = ListTodo()
        taskList = mockito.mock()
        self.assertFalse(listTodo.contains_list_by_name('taskList'))

    def test_contains_in_todo_list_by_name_multiple_return_false(self):
        listTodo = ListTodo()
        lst=[]
        taskList = mockito.mock()
        taskList2 = mockito.mock()

        listTodo.add_list(taskList)
        listTodo.add_list(taskList2)
        mockito.when(taskList).name().thenReturn('name')
        mockito.when(taskList2).name().thenReturn('liste')
        self.assertFalse(listTodo.contains_list_by_name('taskListfound'))

class TestGetList(unittest.TestCase):

    def test_get_lst_exists(self):
        listTodo = ListTodo()
        lst=[]
        taskListfound = mockito.mock()
        taskList = mockito.mock()
        taskList2 = mockito.mock()

        listTodo.add_list(taskList)
        listTodo.add_list(taskList2)
        mockito.when(taskList).name().thenReturn('name')
        mockito.when(taskList2).name().thenReturn('liste')
        self.assertEquals(taskList, listTodo.get_list('name'))

    def test_get_list_return_ok(self):
        listTodo = ListTodo()
        lst=[]
        taskListfound = mockito.mock()
        taskList = mockito.mock()
        taskList2 = mockito.mock()

        listTodo.add_list(taskList)
        listTodo.add_list(taskList2)
        mockito.when(taskList).name().thenReturn('name')
        mockito.when(taskList2).name().thenReturn('liste')
        self.assertEquals(taskList2, listTodo.get_list('liste'))

    def test_get_list_todo_in_empty(self):
        listTodo = ListTodo()
        taskList = mockito.mock()
        self.assertIsNone(listTodo.get_list('taskList'))

    def test_list_multiple_return_none(self):
        listTodo = ListTodo()
        lst=[]
        taskListfound = mockito.mock()
        taskList = mockito.mock()
        taskList2 = mockito.mock()

        listTodo.add_list(taskList)
        listTodo.add_list(taskList2)
        mockito.when(taskList).name().thenReturn('name')
        mockito.when(taskList2).name().thenReturn('liste')
        self.assertIsNone(listTodo.get_list('liste3'))

class TestRemoveInList(unittest.TestCase):

    def test_remove_in_todo_list_empty(self):
        listTodo = ListTodo()
        taskList = mockito.mock()
        listTodo.remove_list('name')
        self.assertEquals([], listTodo.list())

    def test_remove_names_in_todo_list(self):
        listTodo = ListTodo()
        taskList = mockito.mock()
        taskList2 = mockito.mock()
        taskList3 = mockito.mock()
        listTodo.add_list(taskList)
        listTodo.add_list(taskList2)
        listTodo.add_list(taskList3)
        mockito.when(taskList).name().thenReturn('name')
        mockito.when(taskList2).name().thenReturn('name2')
        mockito.when(taskList3).name().thenReturn('name3')
        listTodo.remove_list('name2')
        self.assertEquals([taskList, taskList3], listTodo.list())