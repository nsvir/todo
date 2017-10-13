from controller.manage_list import *
import unittest
from mockito import when, mock
from bottle import template

class TestAddListTodoController(unittest.TestCase):

    def test_add_list_controller(self):
        listTodoService = mock()
        manageList = ManageList(listTodoService)
        when(listTodoService).add_list('name').thenRaise(ValueError())
        
        self.assertRaises(ValueError, manageList.addList, 'name')

class TestListSettingsTodoController(unittest.TestCase):

    def test_settings_list_controller(self):
        listTodoService = mock()
        manageList = ManageList(listTodoService)
        when(listTodoService).get_list().thenReturn(['name'])
        output = manageList.listSettings('name')
        
        self.assertEquals(template('src/web/template/settingsList.tpl', lists=['name'], list='name'), output)