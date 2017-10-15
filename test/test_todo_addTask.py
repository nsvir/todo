import unittest
import mockito
from unittest.mock import Mock
from controller.todo import TodoApp
from service.todo_service import TodoService

class TestTodoManageTask(unittest.TestCase):

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

    def test_add_task_service(self):
        taskToAdd = "my task"
        todoService = TodoService()
        todoService.addTask(taskToAdd)
        self.assertIn(taskToAdd, todoService.getTasks())
