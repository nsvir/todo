import unittest
from model.task_list import *

class TestInitTaskListTodo(unittest.TestCase):

    def test_task_list_creation(self):
        taskList = TaskList('name', True, '12:00')
        self.assertEqual('name', taskList.name())
        self.assertEqual(True, taskList.desapear())
        self.assertEqual('12:00', taskList.hour())

    def test_set_parameters_to_task_list(self):
        taskList = TaskList('name', True, '12:00')
        taskList.set_parameters(False, '13:00')
        self.assertEqual('name', taskList.name())
        self.assertEqual(False, taskList.desapear())
        self.assertEqual('13:00', taskList.hour())
