import unittest
import mockito
from model.users import *

class TestUsers(unittest.TestCase):

    def test_init_users(self):
        users = Users()
        self.assertFalse(users.user_exists('login', 'password'))

    def test_set_users(self):
        users = Users()
        user = mockito.mock()
        mockito.when(user).login().thenReturn('login')
        mockito.when(user).password().thenReturn('password')
        users.set_users([user])
        self.assertTrue(users.user_exists('login', 'password'))

    def test_set_users_false(self):
        users = Users()
        user = mockito.mock()
        mockito.when(user).login().thenReturn('log')
        mockito.when(user).password().thenReturn('password')
        users.set_users([user])
        self.assertFalse(users.user_exists('login', 'password'))