import unittest
import mockito
from unittest.mock import Mock
from controller.todo import TodoApp
from service.todo_service import TodoService
from repository.TodoDatabase import TodoDatabase
from model.Task import Task

class TestTodoDatabase(unittest.TestCase):

    def test_add_task_database(self):
        connection = Mock()
        objectTaskToAdd = Task("me")
        TodoDatabase(connection).add(objectTaskToAdd)
        connection.execute.assert_called_once_with("INSERT into tasks values (?, ?)", ("me", False))
        connection.commit.assert_called_once()

    def test_update_task_database(self):
        connection = Mock()
        objectTaskToUpdate = Task("me")
        TodoDatabase(connection).update(objectTaskToUpdate)
        connection.execute.assert_called_once_with("UPDATE tasks SET name = ?, isDone = ? WHERE name = ?", \
                                                    ("me", False, "me"))
        connection.commit.assert_called_once()

    def test_retrieve_task_database(self):
        connection = Mock()
        task = Task("me", True)
        mockito.when(connection).execute('SELECT name, isDone FROM tasks').thenReturn([[task.name(), task.done()]])
        listResult = TodoDatabase(connection).retrieve()
        self.assertEquals(task.name(), listResult[0].name())
        self.assertEquals(task.done(), listResult[0].done())

    def test_delete_task_databse(self):
        connection = Mock()
        objectTaskToRemove = Task("me")
        TodoDatabase(connection).delete(objectTaskToRemove)
        connection.execute.assert_called_once_with("DELETE FROM tasks WHERE name = ?", "me")
        connection.commit.assert_called_once()
