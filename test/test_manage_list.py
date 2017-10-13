from controller.manage_list import *
import unittest
import mockito


class TestAddListTodoController(unittest.TestCase):

    def test_add_list_controller(self):
        listTodoService = mockito.mock()
        manageList = ManageList(listTodoService)
        mockito.when(listTodoService).add_list('name').thenRaise(ValueError())
        
        #self.assertRaises(ValueError, manageList.addList, 'name')