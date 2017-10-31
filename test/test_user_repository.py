import unittest
import mockito
from repository.user_repository import *
from model.user import *

class TestUserDatabase(unittest.TestCase):

    def test_get_all_list(self):
        connection = mockito.mock()
        cursor = mockito.mock()
        mockito.when(connection).cursor().thenReturn(cursor)
        mockito.when(cursor).fetchall().thenReturn([('user', 'pass')])

        repository = UserRepository(connection)
        rows = repository.get_all_list()
        mockito.verify(cursor).execute('SELECT * from users')
        self.assertEquals([('user', 'pass')], rows)