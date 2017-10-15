from controller.init import *
import unittest
from mockito import when, mock, any
from bottle import template

class TestAddListTodoController(unittest.TestCase):

    def test_add_list_controller(self):
        listTodoService = mock()
        listRepository = mock()
        taskListFactory = mock()
        init = Init(listTodoService, listRepository, taskListFactory)
        when(listTodoService).initTodoList(listTodoService).thenReturn(True)
        when(listTodoService).remove_desable_lists().thenRaise(ValueError())
        
        self.assertRaises(ValueError, init.initTodoList, any())