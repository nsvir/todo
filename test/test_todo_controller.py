import unittest
from unittest.mock import Mock
from controller.todo import TodoApp
from service.todo_service import TodoService

class TestTodoController(unittest.TestCase):

    def test_add_a_task_controller(self):
        request = Mock()
        taskTest = "test"
        form = Mock()
        todoService = Mock()
        redirect = Mock()
        todoApp = TodoApp(listTodoServer = Mock(), todoService = todoService, request = request, redirect = redirect)
        todoApp.addTask(taskTest)
        todoService.addTask.assert_called_once_with(taskTest)
        redirect.assert_called_once_with("/")


    def test_remove_a_task_controller(self):
        request = Mock()
        taskTest = "test"
        form = Mock()
        todoService = Mock()
        redirect = Mock()
        todoApp = TodoApp(listTodoServer = Mock(), todoService = todoService, request = request, redirect = redirect)
        todoApp.addTask(taskTest)
        todoApp.removeTask(taskTest)
        todoService.removeTask.assert_called_once_with(taskTest)
        redirect.assert_called()
        self.assertEqual(2, redirect.call_count)
