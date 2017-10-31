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
        objectTaskToAdd = mockito.mock()
        
        mockito.when(objectTaskToAdd).name().thenReturn("me")
        mockito.when(objectTaskToAdd).done().thenReturn(False)
        mockito.when(objectTaskToAdd).listname().thenReturn("lst")
        mockito.when(objectTaskToAdd).is_visible().thenReturn(True)
        mockito.when(objectTaskToAdd).login().thenReturn('login')

        TodoDatabase(connection).add(objectTaskToAdd)
        connection.execute.assert_called_once_with("INSERT into tasks values (?, ?, ?, ?, ?)", ("me", False, "lst", True, 'login'))
        connection.commit.assert_called_once()

    def test_update_task_database(self):
        connection = Mock()
        objectTaskToUpdate = Task("me", "lst")
        TodoDatabase(connection).update(objectTaskToUpdate)
        connection.execute.assert_called_once_with("UPDATE tasks SET name = ?, isDone = ? WHERE name = ?", \
                                                    ("me", False, "me"))
        connection.commit.assert_called_once()

    def test_update_name_task_database(self):
        connection = Mock()
        objectTaskToUpdate = mockito.mock()
        mockito.when(objectTaskToUpdate).name().thenReturn("me")
        TodoDatabase(connection).update_with_old_name("avant", objectTaskToUpdate)
        connection.execute.assert_called_once_with("UPDATE tasks SET name = ? WHERE name = ?", \
                                                    ("me", "avant"))
        connection.commit.assert_called_once()

    def test_retrieve_task_database(self):
        connection = Mock()
        mockito.when(connection).execute('SELECT name, isDone, listname, visible, login FROM tasks').thenReturn([["me", True, "list", True, 'login']])
        listResult = TodoDatabase(connection).retrieve()
        task = listResult[0]
        self.assertEquals(task.name(), "me")
        self.assertTrue(task.done())
        self.assertEquals(task.listname(), "list")
        self.assertTrue(task.is_visible())
        self.assertEquals('login', task.login())

    def test_delete_task_databse(self):
        connection = Mock()
        objectTaskToRemove = Task("me", "lst")
        TodoDatabase(connection).delete(objectTaskToRemove)
        connection.execute.assert_called_once_with("DELETE FROM tasks WHERE name = 'me'")
        connection.commit.assert_called_once()

    def test_desable_task_databse(self):
        connection = Mock()
        TodoDatabase(connection).desable_tasks_by_listname('name')
        connection.execute.assert_called_once_with("UPDATE tasks SET visible = 'FALSE' WHERE listname = 'name'")
        connection.commit.assert_called_once()

    def test_enable_task_databse(self):
        connection = Mock()
        TodoDatabase(connection).enable_tasks_by_listname('name')
        connection.execute.assert_called_once_with("UPDATE tasks SET visible = 'TRUE' WHERE listname = 'name'")
        connection.commit.assert_called_once()

    def test_update_login_task_database(self):
        connection = Mock()
        objectTaskToUpdate = mockito.mock()
        mockito.when(objectTaskToUpdate).name().thenReturn("me")
        mockito.when(objectTaskToUpdate).login().thenReturn("login")
        TodoDatabase(connection).takeTask(objectTaskToUpdate)
        connection.execute.assert_called_once_with("UPDATE tasks SET login = ? WHERE name = ?", \
                                                    ("login", "me"))
        connection.commit.assert_called_once()