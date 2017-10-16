from controller.manage_list import *
import unittest
from mockito import when, mock, any, verify, never
from bottle import template

class TestAddListTodoController(unittest.TestCase):

    def test_add_list_controller(self):
        listTodoService = mock()
        checkParam = mock()
        redirect = mock()
        taskListFactory = mock()
        manageList = ManageList(listTodoService, checkParam, taskListFactory, redirect, mock())
        when(checkParam).valid_name_list('name').thenReturn(True)
        manageList.addList('name')
        
        verify(listTodoService).add_list(any())

    def test_add_bad_list_controller(self):
        listTodoService = mock()
        checkParam = mock()
        redirect = mock()
        taskListFactory = mock()
        manageList = ManageList(listTodoService, checkParam, taskListFactory, redirect, mock())
        when(checkParam).valid_name_list('name').thenReturn(False)
        manageList.addList('name')
        
        verify(listTodoService, never).add_list(any())


class TestDeleteListTodoController(unittest.TestCase):

    def test_delete_list_controller(self):
        listTodoService = mock()
        checkParam = mock()
        redirect = mock()
        taskListFactory = mock()
        todoService = mock()
        manageList = ManageList(listTodoService, checkParam, taskListFactory,  todoService, redirect)
        when(checkParam).valid_name_list('name').thenReturn(True)
        when(todoService).getTasksByListname('name').thenReturn([])
        manageList.deleteList('name')
        
        verify(listTodoService).remove_list(any())

    def test_delete_list_with_taskcontroller(self):
        listTodoService = mock()
        checkParam = mock()
        redirect = mock()
        taskListFactory = mock()
        todoService = mock()
        task = mock()
        manageList = ManageList(listTodoService, checkParam, taskListFactory,  todoService, redirect)
        when(checkParam).valid_name_list('name').thenReturn(True)
        when(task).name().thenReturn('name')
        when(todoService).getTasksByListname('name').thenReturn([task])
        manageList.deleteList('name')
        
        verify(todoService).removeTask('name')
        verify(listTodoService).remove_list(any())

    def test_add_bad_list_controller(self):
        listTodoService = mock()
        checkParam = mock()
        redirect = mock()
        taskListFactory = mock()
        manageList = ManageList(listTodoService, checkParam, taskListFactory, redirect, mock())
        when(checkParam).valid_name_list('name').thenReturn(False)
        manageList.deleteList('name')
        
        verify(listTodoService, never).remove_list(any())

class TestListSettingsTodoController(unittest.TestCase):

    def test_condition_list_settings(self):
        listTodoService = mock()
        checkParam = mock()
        redirect = mock()
        taskListFactory = mock()
        manageList = ManageList(listTodoService, checkParam, taskListFactory, redirect, mock())
        when(listTodoService).list_exists_by_name('name').thenReturn(False)
        manageList.listSettings('name')
        
        redirect.assert_called_once_with("/")

    def test_condition_submit_list_settings(self):
        listTodoService = mock()
        checkParam = mock()
        redirect = mock()
        lst= mock()
        taskListFactory = mock()
        manageList = ManageList(listTodoService, checkParam, taskListFactory, redirect, mock())
        when(listTodoService).list_exists_by_name('name').thenReturn(True)
        when(listTodoService).get_list_name().thenReturn(['name'])
        when(listTodoService).get_lst('name').thenReturn(lst)
        when(lst).desapear().thenReturn(1)
        when(lst).hour().thenReturn('12:00')
        when(lst).hebdo().thenReturn(1)
        when(lst).desapearHebdo().thenReturn(1)
        when(lst).hourHebdo().thenReturn('')
        output = manageList.listSettings('name')
        self.assertEquals(template('src/web/template/settingsList.tpl', lists=['name'], list='name', desapear='checked', hour='12:00', hebdo='checked', desapearHebdo='checked', hourHebdo='',status='', css='../css/index.css'), output)

    def test_settings_list_controller_default(self):
        listTodoService = mock()
        checkParam = mock()
        taskListFactory = mock()
        lst = mock()
        manageList = ManageList(listTodoService, checkParam, taskListFactory, mock())
        when(listTodoService).get_list_name().thenReturn(['name'])
        when(listTodoService).get_lst('name').thenReturn(lst)
        when(lst).desapear().thenReturn(0)
        when(lst).hour().thenReturn('')
        when(lst).hebdo().thenReturn(0)
        when(lst).desapearHebdo().thenReturn(0)
        when(lst).hourHebdo().thenReturn('')
        output = manageList.getSettingsPage('', 'name', '')
        
        self.assertEquals(template('src/web/template/settingsList.tpl', lists=['name'], list='name', desapear='', hour='', hebdo='', desapearHebdo='', hourHebdo='', status='', css=''), output)

    def test_settings_list_controller_default_desapear(self):
        listTodoService = mock()
        checkParam = mock()
        taskListFactory = mock()
        lst = mock()
        manageList = ManageList(listTodoService, checkParam, taskListFactory, mock())
        when(listTodoService).get_list_name().thenReturn(['name'])
        when(listTodoService).get_lst('name').thenReturn(lst)
        when(lst).desapear().thenReturn(1)
        when(lst).hour().thenReturn('12:00')
        when(lst).hebdo().thenReturn(0)
        when(lst).desapearHebdo().thenReturn(0)
        when(lst).hourHebdo().thenReturn('')
        output = manageList.getSettingsPage('', 'name', '')
        
        self.assertEquals(template('src/web/template/settingsList.tpl', lists=['name'], list='name', desapear='checked', hour='12:00', hebdo='', desapearHebdo='', hourHebdo='',status='', css=''), output)

    def test_settings_list_controller_default_desapear(self):
        listTodoService = mock()
        checkParam = mock()
        taskListFactory = mock()
        lst = mock()
        manageList = ManageList(listTodoService, checkParam, taskListFactory, mock())
        when(listTodoService).get_list_name().thenReturn(['name'])
        when(listTodoService).get_lst('name').thenReturn(lst)
        when(lst).desapear().thenReturn(1)
        when(lst).hour().thenReturn('12:00')
        when(lst).hebdo().thenReturn(1)
        when(lst).desapearHebdo().thenReturn(1)
        when(lst).hourHebdo().thenReturn('')
        output = manageList.getSettingsPage('', 'name', '')
        
        self.assertEquals(template('src/web/template/settingsList.tpl', lists=['name'], list='name', desapear='checked', hour='12:00', hebdo='checked', desapearHebdo='checked', hourHebdo='',status='', css=''), output)

class TestSubmitListSettingsController(unittest.TestCase):

    def test_submit_with_bad_name(self):
        listTodoService = mock()
        checkParam = mock()
        taskListFactory = mock()
        lst = mock()
        redirect = mock()
        manageList = ManageList(listTodoService, checkParam, taskListFactory, redirect, mock())

        when(listTodoService).list_exists_by_name('name').thenReturn(False)
        manageList.submitListSettings('name')
        redirect.assert_called_once_with("/")

class TestTransformHourToStringController(unittest.TestCase):

    def test_transform_hour_to_string_ko(self):
        listTodoService = mock()
        checkParam = mock()
        taskListFactory = mock()
        lst = mock()
        manageList = ManageList(listTodoService, checkParam, taskListFactory, mock())

        self.assertEquals("" , manageList.transformHourToString(None))

    def test_transform_hour_to_string_ok(self):
        listTodoService = mock()
        checkParam = mock()
        taskListFactory = mock()
        lst = mock()
        manageList = ManageList(listTodoService, checkParam, taskListFactory, mock())

        self.assertEquals("23:33" , manageList.transformHourToString('23:33'))

class TestTransformCheckBoxToIntController(unittest.TestCase):

    def test_transform_checkbox_to_int_return0(self):
        listTodoService = mock()
        checkParam = mock()
        taskListFactory = mock()
        lst = mock()
        manageList = ManageList(listTodoService, checkParam, taskListFactory, mock())

        self.assertEquals(0 , manageList.transformCheckboxToInt(None))

    def test_transform_checkbox_to_int_return0_bis(self):
        listTodoService = mock()
        checkParam = mock()
        taskListFactory = mock()
        lst = mock()
        manageList = ManageList(listTodoService, checkParam, taskListFactory, mock())

        self.assertEquals(0 , manageList.transformCheckboxToInt(0))

    def test_transform_checkbox_to_int_return1(self):
        listTodoService = mock()
        checkParam = mock()
        taskListFactory = mock()
        lst = mock()
        manageList = ManageList(listTodoService, checkParam, taskListFactory, mock())

        self.assertEquals(1 , manageList.transformCheckboxToInt(1))