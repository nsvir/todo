import unittest
import mockito
from service.list_todo_service import *

class TestAddListTodoService(unittest.TestCase):

    def test_add_list(self):
        repository = mockito.mock()
        lst = mockito.mock()
        service = ListTodoService(repository, lst)
        listtask = mockito.mock()
        mockito.when(listtask).name().thenReturn('name')
        mockito.when(listtask).desapear().thenReturn(True)
        mockito.when(listtask).hour().thenReturn('12:00')

        service.add_list(listtask)
        mockito.verify(lst).add_list(listtask)
        mockito.verify(repository).add_list_into_repository("name", True, '12:00')


class TestGetListTodoService(unittest.TestCase):

    def test_get_list(self):
        repository = mockito.mock()
        lst = mockito.mock()
        service = ListTodoService(repository, lst)

        service.get_list_name()
        mockito.verify(repository).get_list_name_repository()


class TestCheckListTodoService(unittest.TestCase):

    def test_check_list(self):
        repository = mockito.mock()
        lst = mockito.mock()
        service = ListTodoService(repository, lst)
        lstTask = mockito.mock()
        mockito.when(lst).contains_list(lstTask).thenReturn(True)

        service.list_exists(lstTask)
        mockito.verify(lst).contains_list(lstTask)

class TestSaveSettingsTodoService(unittest.TestCase):

    def test_save_settings_list(self):
        repository = mockito.mock()
        lst = mockito.mock()
        service = ListTodoService(repository, lst)
        lstTask = mockito.mock()
        mockito.when(lst).contains_list(lstTask).thenReturn(False)

        service.save_settings(lstTask)
        mockito.verify(repository, mockito.never).update_settings(mockito.any(), mockito.any(), mockito.any())

    def test_save_settings_list_when_name_not_exists(self):
        repository = mockito.mock()
        lst = mockito.mock()
        service = ListTodoService(repository, lst)
        lstTask = mockito.mock()
        mockito.when(lst).contains_list(lstTask).thenReturn(True)

        service.save_settings(lstTask)
        mockito.verify(repository).update_settings(mockito.any(), mockito.any(), mockito.any())
