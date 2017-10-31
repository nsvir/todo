from controller.init import *
import unittest
from mockito import when, mock, any, verify
from bottle import template

class TestAddListTodoController(unittest.TestCase):

    def test_add_list_controller(self):
        listTodoService = mock()
        listRepository = mock()
        taskListFactory = mock()
        serviceTodo = mock()
        userService = mock()
        init = Init(listTodoService, listRepository, userService, taskListFactory, serviceTodo)
        
        init.initTodoList(any())
        verify(listTodoService).initTodoList(any(), any())
        verify(listTodoService).remove_desable_lists()
        verify(serviceTodo).remove_desable_tasks(any())
        verify(userService).init_users()