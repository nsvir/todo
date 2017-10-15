import unittest
from model.task_list import *

class TestInitTaskListTodo(unittest.TestCase):

    def test_task_list_creation(self):
        taskList = TaskList('name', 0, '12:00', 0, 0, '')
        self.assertEqual('name', taskList.name())
        self.assertEqual(0, taskList.desapear())
        self.assertEqual('12:00', taskList.hour())
        self.assertEqual(0, taskList.hebdo())
        self.assertEqual(0, taskList.desapearHebdo())
        self.assertEqual('', taskList.hourHebdo())

    def test_set_parameters_to_task_list(self):
        taskList = TaskList('name', 0, '12:00', 0, 0, '')
        taskList.set_parameters(0, '13:00', 1, 1, '13:00')
        self.assertEqual('name', taskList.name())
        self.assertEqual(0, taskList.desapear())
        self.assertEqual('13:00', taskList.hour())
        self.assertEqual(1, taskList.hebdo())
        self.assertEqual(1, taskList.desapearHebdo())
        self.assertEqual('13:00', taskList.hourHebdo())
