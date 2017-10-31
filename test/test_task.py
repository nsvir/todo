import unittest
import mockito
from model.Task import *

class TestUser(unittest.TestCase):

    def test_user(self):
        task = Task('name', 'listname')
        self.assertEquals('name', task.name())
        self.assertEquals('listname', task.listname())
        self.assertFalse(task.done())
        self.assertTrue(task.is_visible())
        self.assertEquals('', task.login())

    def test_user_set_done(self):
        task = Task('name', 'listname')
        task.setIsDone()
        self.assertTrue(task.done())

    def test_user_set_name(self):
        task = Task('name', 'listname')
        task.set_name('ok')
        self.assertEquals('ok', task.name())

    def test_user_invisible(self):
        task = Task('name', 'listname')
        task.invisible()
        self.assertFalse(task.is_visible())

    def test_user_visible(self):
        task = Task('name', 'listname')
        task.visible()
        self.assertTrue(task.is_visible())

    def test_user_set_login(self):
        task = Task('name', 'listname')
        task.setLogin('login')
        self.assertEquals('login', task.login())