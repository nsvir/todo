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

    def test_condition_list_settings(self):
        listTodoService = mock()
        checkParam = mock()
        taskListFactory = mock()
        lst = mock()
        manageList = ManageList(listTodoService, checkParam, taskListFactory)
        when(listTodoService).list_exists_by_name('name').thenRaise(ValueError())
        
        self.assertRaises(ValueError, manageList.listSettings, 'name')

    def test_condition_submit_list_settings(self):
        listTodoService = mock()
        checkParam = mock()
        taskListFactory = mock()
        lst = mock()
        manageList = ManageList(listTodoService, checkParam, taskListFactory)
        when(listTodoService).list_exists_by_name('name').thenRaise(ValueError())
        
        self.assertRaises(ValueError, manageList.submitListSettings, 'name')

    def test_settings_list_controller_default(self):
        listTodoService = mock()
        checkParam = mock()
        taskListFactory = mock()
        lst = mock()
        manageList = ManageList(listTodoService, checkParam, taskListFactory)
        when(listTodoService).get_list_name().thenReturn(['name'])
        when(listTodoService).get_lst('name').thenReturn(lst)
        when(lst).desapear().thenReturn(0)
        when(lst).hour().thenReturn('')
        output = manageList.getSettingsPage('', 'name', '')
        
        self.assertEquals(template('src/web/template/settingsList.tpl', lists=['name'], list='name', desapear='', hour='', status='', css=''), output)

    def test_settings_list_controller_default_desapear(self):
        listTodoService = mock()
        checkParam = mock()
        taskListFactory = mock()
        lst = mock()
        manageList = ManageList(listTodoService, checkParam, taskListFactory)
        when(listTodoService).get_list_name().thenReturn(['name'])
        when(listTodoService).get_lst('name').thenReturn(lst)
        when(lst).desapear().thenReturn(1)
        when(lst).hour().thenReturn('12:00')
        output = manageList.getSettingsPage('', 'name', '')
        
        self.assertEquals(template('src/web/template/settingsList.tpl', lists=['name'], list='name', desapear='checked', hour='12:00', status='', css=''), output)

