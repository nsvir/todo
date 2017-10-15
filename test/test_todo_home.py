import unittest
from unittest.mock import Mock
from controller.todo import TodoApp

class TestTodoHome(unittest.TestCase):

    def test_home_returns_template(self):
        template_mock = Mock(return_value="mocked stuff")
        html_page = TodoApp(template = template_mock).home()
        template_mock.assert_called_once()
