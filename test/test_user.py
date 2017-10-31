import unittest
import mockito
from model.user import *

class TestUser(unittest.TestCase):

    def test_user(self):
        user = User('login', 'password')
        self.assertEquals('login', user.login())
        self.assertEquals('password', user.password())