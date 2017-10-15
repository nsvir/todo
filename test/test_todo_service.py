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
        taskToAdd = "my task"
        todoService = TodoService()
        todoService.addTask(taskToAdd)
        todoService.removeTask(taskToAdd)
        matchedElementWithTaskToAdd = len(list(filter(lambda task: taskToAdd == task.name(), todoService.getTasks())))
        self.assertEqual(0, matchedElementWithTaskToAdd)
