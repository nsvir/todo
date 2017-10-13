import mockito
import unittest

from repository.list_repository import *

class TestGetListTodo(unittest.TestCase):

    def test_get_list_repository(self):
        connection = mockito.mock()
        cursor = mockito.mock()
        mockito.when(connection).cursor().thenReturn(cursor)
        mockito.when(cursor).fetchall().thenReturn([('test', )])

        listRepository = ListRepository(connection)
        rows = listRepository.get_list_repository()
        mockito.verify(cursor).execute('SELECT * from lists')
        self.assertEquals(['test'], rows)


class TestAddListTodo(unittest.TestCase):

    def test_get_list_repository(self):
        connection = mockito.mock()
        cursor = mockito.mock()
        mockito.when(connection).cursor().thenReturn(cursor)
        mockito.when(cursor).fetchall().thenReturn([('test', )])

        listRepository = ListRepository(connection)
        rows = listRepository.add_list_into_repository('name')
        mockito.verify(cursor).execute("INSERT into lists values ('name')")


