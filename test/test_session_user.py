import unittest
import mockito
from model.session_user import *

class TestSessionUser(unittest.TestCase):

    def test_init_session_user(self):
        session = SessionUser()
        self.assertFalse(session.isAuthenticated())
        self.assertIsNone(session.login())

    def test_auth_session_user(self):
        session = SessionUser()
        session.auth('login')
        self.assertTrue(session.isAuthenticated())
        self.assertEquals('login', session.login())