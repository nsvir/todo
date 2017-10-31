from controller.login import *
import unittest
import mockito
from bottle import template

class TestLoginController(unittest.TestCase):

    def test_get_login_page(self):
        userService = mockito.mock()
        session = mockito.mock()
        checkParam = mockito.mock()
        template = mockito.mock()
        login = Login(session, userService, checkParam, template)
        
        self.assertEquals(template('src/web/template/login.tpl', status=''), login.login())


