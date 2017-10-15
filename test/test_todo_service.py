import unittest
from unittest.mock import Mock
from controller.todo import TodoApp
from service.todo_service import TodoService

class TestTodoService(unittest.TestCase):


    def test_add_task_service(self):
        taskToAdd = "my task"
        todoService = TodoService()
        todoService.addTask(taskToAdd)
        matchedElementWithTaskToAdd = len(list(filter(lambda task: taskToAdd == task.name(), todoService.getTasks())))
        self.assertEqual(1, matchedElementWithTaskToAdd)

    def test_remove_task_service(self):
        taskToRemove = "my task"
        todoService = TodoService()
        todoService.addTask(taskToRemove)
        todoService.removeTask(taskToRemove)
        matchedElementWithTaskToRemove = len(list(filter(lambda task: taskToAdd == task.name(), todoService.getTasks())))
        self.assertEqual(0, matchedElementWithTaskToRemove)

    def test_get_existant_task_service(self):
        taskToGet = "my task"
        todoService = TodoService()
        todoService.addTask(taskToGet)
        taskResult = todoService.getTask(taskToGet)
        self.assertEqual(taskToGet, taskResult.name())

    def test_get_unexistant_task_service(self):
        taskToGet = "my task"
        todoService = TodoService()
        taskResult = todoService.getTask(taskToGet)
        self.assertEqual(None, taskResult)

    def test_check_task_service(self):
        taskToCheck = "my task"
        todoService = TodoService()
        todoService.addTask(taskToCheck)
        todoService.checkTask(taskToCheck)
        taskResult = todoService.getTask(taskToCheck)
        self.assertTrue(taskResult.done())
