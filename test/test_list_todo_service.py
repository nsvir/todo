import unittest
import mockito
from service.list_todo_service import *

class TestAddListTodoService(unittest.TestCase):

    def test_add_list(self):
        repository = mockito.mock()
        userrepository = mockito.mock()
        lst = mockito.mock()
        service = ListTodoService(repository, userrepository, lst)
        listtask = mockito.mock()
        mockito.when(listtask).name().thenReturn('name')
        mockito.when(listtask).desapear().thenReturn(True)
        mockito.when(listtask).hour().thenReturn('12:00')
        mockito.when(listtask).hebdo().thenReturn(False)
        mockito.when(listtask).desapearHebdo().thenReturn(False)
        mockito.when(listtask).hourHebdo().thenReturn('12:00')
        mockito.when(listtask).listUsers().thenReturn([])

        service.add_list(listtask)
        mockito.verify(lst).add_list(listtask)
        mockito.verify(repository).add_list_into_repository("name", True, '12:00' ,False, False, '12:00', [])


class TestGetListTodoService(unittest.TestCase):

    def test_get_list_name(self):
        repository = mockito.mock()
        userrepository = mockito.mock()
        lst = mockito.mock()
        session = mockito.mock()
        service = ListTodoService(repository, userrepository, lst)

        service.get_list_name(session)
        mockito.verify(repository).get_list_name_repository_by_user_name(session)

    def test_get_list_info(self):
        repository = mockito.mock()
        userrepository = mockito.mock()
        lst = mockito.mock()
        service = ListTodoService(repository, userrepository, lst)

        service.get_lst('name')
        mockito.verify(lst).get_list('name')


class TestCheckListTodoService(unittest.TestCase):

    def test_check_list(self):
        repository = mockito.mock()
        userrepository = mockito.mock()
        lst = mockito.mock()
        service = ListTodoService(repository, userrepository, lst)
        lstTask = mockito.mock()
        mockito.when(lst).contains_list(lstTask).thenReturn(True)

        service.list_exists(lstTask)
        mockito.verify(lst).contains_list(lstTask)

    def test_check_list_by_name(self):
        repository = mockito.mock()
        userrepository = mockito.mock()
        lst = mockito.mock()
        service = ListTodoService(repository, userrepository, lst)
        lstTask = mockito.mock()
        mockito.when(lst).contains_list_by_name(lstTask).thenReturn(True)

        service.list_exists_by_name(lstTask)
        mockito.verify(lst).contains_list_by_name(lstTask)

class TestSaveSettingsTodoService(unittest.TestCase):

    def test_save_settings_list(self):
        repository = mockito.mock()
        lst = mockito.mock()
        userrepository = mockito.mock()
        service = ListTodoService(repository, userrepository, lst)
        lstTask = mockito.mock()
        mockito.when(lst).contains_list(lstTask).thenReturn(False)

        service.save_settings(lstTask)
        mockito.verify(repository, mockito.never).update_settings(mockito.any(), mockito.any(), mockito.any(), mockito.any(), mockito.any(), mockito.any(), mockito.any())

    def test_save_settings_list_when_name_not_exists(self):
        repository = mockito.mock()
        lst = mockito.mock()
        userrepository = mockito.mock()
        service = ListTodoService(repository, userrepository, lst)
        lstTask = mockito.mock()
        mockito.when(lst).contains_list(lstTask).thenReturn(True)

        service.save_settings(lstTask)
        mockito.verify(repository).update_settings(mockito.any(), mockito.any(), mockito.any(), mockito.any(), mockito.any(), mockito.any() ,mockito.any())

class TestRemoveListTodoService(unittest.TestCase):

    def test_remove_list(self):
        repository = mockito.mock()
        lst = mockito.mock()
        userrepository = mockito.mock()
        service = ListTodoService(repository, userrepository, lst)

        service.remove_list('name')
        mockito.verify(lst).remove_list('name')
        mockito.verify(repository).remove_list_into_repository("name")

class TestRemoveDesableListTodoService(unittest.TestCase):

    def test_remove_desable_list(self):
        repository = mockito.mock()
        lst = mockito.mock()
        userrepository = mockito.mock()
        service = ListTodoService(repository, userrepository, lst)
        tasklist = mockito.mock()
        mockito.when(lst).list().thenReturn([tasklist])
        mockito.when(tasklist).name().thenReturn('name')
        mockito.when(tasklist).hour().thenReturn('00:00')
        mockito.when(tasklist).desapear().thenReturn(1)

        service.remove_desable_lists()
        mockito.verify(lst).remove_list('name')
        mockito.verify(repository).remove_list_into_repository("name")

    def test_not_remove_unable_list_not_desapear(self):
        repository = mockito.mock()
        lst = mockito.mock()
        userrepository = mockito.mock()
        service = ListTodoService(repository, userrepository, lst)
        tasklist = mockito.mock()
        mockito.when(lst).list().thenReturn([tasklist])
        mockito.when(tasklist).name().thenReturn('name')
        mockito.when(tasklist).hour().thenReturn('00:00')
        mockito.when(tasklist).desapear().thenReturn(0)

        service.remove_desable_lists()
        mockito.verify(lst, mockito.never).remove_list('name')
        mockito.verify(repository, mockito.never).remove_list_into_repository("name")

    def test_not_remove_desable_list_desapear(self):
        repository = mockito.mock()
        lst = mockito.mock()
        userrepository = mockito.mock()
        service = ListTodoService(repository, userrepository, lst)
        tasklist = mockito.mock()
        mockito.when(lst).list().thenReturn([tasklist])
        mockito.when(tasklist).name().thenReturn('name')
        mockito.when(tasklist).hour().thenReturn('23:59')
        mockito.when(tasklist).desapear().thenReturn(1)

        service.remove_desable_lists()
        mockito.verify(lst, mockito.never).remove_list('name')
        mockito.verify(repository, mockito.never).remove_list_into_repository("name")

class TestInitListTodoService(unittest.TestCase):

    def test_add_list(self):
        repository = mockito.mock()
        lst = mockito.mock()
        lstTask = mockito.mock()
        userrepository = mockito.mock()
        service = ListTodoService(repository, userrepository, lst)
        listtask = mockito.mock()
        factory = mockito.mock()
        mockito.when(repository).get_all_list().thenReturn([('name', 0, '12:00', 0, 0, '')])
        mockito.when(factory).createTaskListWithElements(mockito.any(), mockito.any(), mockito.any(), mockito.any(), mockito.any(), mockito.any(), mockito.any()).thenReturn(lstTask)

        service.initTodoList(lst, factory)
        mockito.verify(lst).add_list(mockito.any())

class TestGetAllLstTodoService(unittest.TestCase):

    def test_all_lst(self):
        repository = mockito.mock()
        lst = mockito.mock()
        lstTask = mockito.mock()
        userrepository = mockito.mock()
        service = ListTodoService(repository, userrepository, lst)
        
        service.get_all_lst()
        mockito.verify(lst).list()

    def test_user_lst(self):
        repository = mockito.mock()
        lst = mockito.mock()
        lstTask = mockito.mock()
        userrepository = mockito.mock()
        service = ListTodoService(repository, userrepository, lst)
        mockito.when(userrepository).get_all_list().thenReturn([['list']])
        
        self.assertIn('list', service.get_list_user())

    def test_user_by_listname(self):
        repository = mockito.mock()
        lst = mockito.mock()
        lstTask = mockito.mock()
        userrepository = mockito.mock()
        service = ListTodoService(repository, userrepository, lst)
        service.users_by_list_name('listname')

        mockito.verify(repository).getAllUsersByListName('listname')