import unittest
import mockito
from unittest.mock import Mock
from controller.todo import TodoApp
from service.todo_service import TodoService

class TestTodoService(unittest.TestCase):


    def test_add_task_service(self):
        taskToAdd = "my task"
        database = Mock()
        mockito.when(database).retrieve().thenReturn([])
        todoService = TodoService(todoDatabase = database)
        todoService.addTask(taskToAdd)
        taskToAddObject = todoService.getTask(taskToAdd)
        matchedElementWithTaskToAdd = len(list(filter(lambda task: taskToAdd == task.name(), todoService.getTasks())))
        database.add.assert_called_once_with(taskToAddObject)
        self.assertEqual(1, matchedElementWithTaskToAdd)

    def test_remove_task_service(self):
        taskToRemove = "my task"
        database = Mock()
        mockito.when(database).retrieve().thenReturn([])
        todoService = TodoService(todoDatabase = database)
        todoService.addTask(taskToRemove)
        taskToRemoveObject = todoService.getTask(taskToRemove)
        todoService.removeTask(taskToRemove)
        matchedElementWithTaskToRemove = len(list(filter(lambda task: taskToAdd == task.name(), todoService.getTasks())))
        database.delete.assert_called_once_with(taskToRemoveObject)
        self.assertEqual(0, matchedElementWithTaskToRemove)

    def test_get_existant_task_service(self):
        taskToGet = "my task"
        database = Mock()
        mockito.when(database).retrieve().thenReturn([])
        todoService = TodoService(todoDatabase = database)
        todoService.addTask(taskToGet)
        taskResult = todoService.getTask(taskToGet)
        database.assert_not_called()
        self.assertEqual(taskToGet, taskResult.name())

    def test_get_unexistant_task_service(self):
        taskToGet = "my task"
        database = Mock()
        mockito.when(database).retrieve().thenReturn([])
        todoService = TodoService(todoDatabase = database)
        taskResult = todoService.getTask(taskToGet)
        database.assert_not_called()
        self.assertEqual(None, taskResult)

    def test_check_task_service(self):
        taskToCheck = "my task"
        database = Mock()
        mockito.when(database).retrieve().thenReturn([])
        todoService = TodoService(todoDatabase = database)
        todoService.addTask(taskToCheck)
        todoService.checkTask(taskToCheck)
        taskToCheckObject = todoService.getTask(taskToCheck)
        taskResult = todoService.getTask(taskToCheck)
        database.update.assert_called_once_with(taskToCheckObject)
        self.assertTrue(taskResult.done())

    def test_get_all_service(self):
        taskName = "me"
        database = Mock()
        mockito.when(database).retrieve().thenReturn([])
        todoService = TodoService(database)
        todoService.addTask(taskName)
        listResult = todoService.getTasks()
        self.assertIn(todoService.getTask(taskName), listResult)
        mockito.verify(database).retrieve()
