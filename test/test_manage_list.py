from controller.manage_list import *
import unittest
from mockito import when, mock, any
from bottle import template

class TestAddListTodoController(unittest.TestCase):

    def test_add_list_controller(self):
        listTodoService = mock()
        checkParam = mock()
        taskListFactory = mock()
        manageList = ManageList(listTodoService, checkParam, taskListFactory)
        when(checkParam).valid_name_list('name').thenReturn(True)
        when(listTodoService).add_list(any()).thenRaise(ValueError())
        
        self.assertRaises(ValueError, manageList.addList, 'name')

class TestListSettingsTodoController(unittest.TestCase):

    def test_settings_list_controller(self):
        listTodoService = mock()
        checkParam = mock()
        taskListFactory = mock()
        manageList = ManageList(listTodoService, checkParam, taskListFactory)
        when(listTodoService).get_list_name().thenReturn(['name'])
        output = manageList.listSettings('name')
        
        self.assertEquals(template('src/web/template/settingsList.tpl', lists=['name'], list='name', status=''), output)

