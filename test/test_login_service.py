import unittest
import mockito
from service.login_service import *

class TestLoginService(unittest.TestCase):

    def test_init_users(self):
        repository = mockito.mock()
        listUsesrs = mockito.mock()
        factory = mockito.mock()
        cryptage = mockito.mock()
        user = mockito.mock()

        service = LoginService(repository, listUsesrs, factory, cryptage)
        mockito.when(repository).get_all_list().thenReturn([['user', 'pass']])
        mockito.when(factory).create(mockito.any(), mockito.any()).thenReturn(user)
        service.init_users()

        mockito.verify(listUsesrs).set_users([user])

    def test_exists_users(self):
        repository = mockito.mock()
        listUsesrs = mockito.mock()
        factory = mockito.mock()
        cryptage = mockito.mock()

        service = LoginService(repository, listUsesrs, factory, cryptage)
        
        mockito.when(cryptage).crypt('password').thenReturn('password')
        mockito.when(listUsesrs).user_exists('login', 'password').thenReturn(True)
        self.assertTrue(service.user_exists('login', 'password'))

    def test_inexists_users(self):
        repository = mockito.mock()
        listUsesrs = mockito.mock()
        factory = mockito.mock()
        cryptage = mockito.mock()

        service = LoginService(repository, listUsesrs, factory, cryptage)
        
        mockito.when(cryptage).crypt('password').thenReturn('passezrezword')
        mockito.when(listUsesrs).user_exists('login', 'passezrezword').thenReturn(False)
        self.assertFalse(service.user_exists('login', 'password'))