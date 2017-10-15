import mockito
import unittest

from repository.list_repository import *

class TestGetListTodo(unittest.TestCase):

    def test_get_list_repository(self):
        connection = mockito.mock()
        cursor = mockito.mock()
        mockito.when(connection).cursor().thenReturn(cursor)
        mockito.when(cursor).fetchall().thenReturn([('test', 0, '12:00')])

        listRepository = ListRepository(connection)
        rows = listRepository.get_list_name_repository()
        mockito.verify(cursor).execute('SELECT * from lists')
        self.assertEquals(['test'], rows)

    def test_get_all_list_repository(self):
        connection = mockito.mock()
        cursor = mockito.mock()
        mockito.when(connection).cursor().thenReturn(cursor)
        mockito.when(cursor).fetchall().thenReturn([('test', 0, '12:00')])

        listRepository = ListRepository(connection)
        rows = listRepository.get_all_list()
        mockito.verify(cursor).execute('SELECT * from lists')
        self.assertEquals([('test', 0, '12:00')], rows)


class TestAddListTodo(unittest.TestCase):

    def test_add_list_repository(self):
        connection = mockito.mock()
        cursor = mockito.mock()
        mockito.when(connection).cursor().thenReturn(cursor)

        listRepository = ListRepository(connection)
        rows = listRepository.add_list_into_repository('name', 0, '12:00', 0, 0, '')
        mockito.verify(cursor).execute("INSERT into lists values ('name', 0, '12:00', 0, 0, '')")

class TestRemoveListTodo(unittest.TestCase):

    def test_remove_list_repository(self):
        connection = mockito.mock()
        cursor = mockito.mock()
        mockito.when(connection).cursor().thenReturn(cursor)

        listRepository = ListRepository(connection)
        rows = listRepository.remove_list_into_repository('name')
        mockito.verify(cursor).execute("DELETE from lists where name='name'")

class TestUpdateSettingsListTodo(unittest.TestCase):

    def test_update_list_settings_repository(self):
        connection = mockito.mock()
        cursor = mockito.mock()
        mockito.when(connection).cursor().thenReturn(cursor)

        listRepository = ListRepository(connection)
        rows = listRepository.update_settings('name', 0, '12:00', 0, 0, '')
        mockito.verify(cursor).execute("UPDATE lists set desable = 0, hour = '12:00', hebdo = 0, desable_hebdo = 0, hour_hebdo = '' where name='name'")

