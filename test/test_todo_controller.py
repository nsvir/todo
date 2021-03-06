import unittest
from unittest.mock import Mock
from controller.todo import TodoApp
from service.todo_service import TodoService
from mockito import verify, any, mock
import mockito

class TestTodoController(unittest.TestCase):

    def test_add_a_task_controller(self):
        request = Mock()
        taskTest = "test"
        form = Mock()
        session = Mock()
        todoService = Mock()
        redirect = Mock()
        todoApp = TodoApp(session, listTodoService = Mock(), todoService = todoService, request = request, redirect = redirect)
        todoApp.addTask(taskTest, "lst")
        todoService.addTask.assert_called_once_with(taskTest, "lst")
        redirect.assert_called_once_with("/")


    def test_remove_a_task_controller(self):
        request = Mock()
        taskTest = "test"
        form = Mock()
        todoService = Mock()
        redirect = Mock()
        session = Mock()
        todoApp = TodoApp(session, listTodoService = Mock(), todoService = todoService, request = request, redirect = redirect)
        todoApp.addTask(taskTest, "lst")
        todoApp.removeTask(taskTest)
        todoService.removeTask.assert_called_once_with(taskTest)
        redirect.assert_called()
        self.assertEqual(2, redirect.call_count)

    def test_check_a_task_controller(self):
        request = Mock()
        taskTest = "test"
        form = Mock()
        todoService = Mock()
        session = Mock()
        redirect = Mock()
        todoApp = TodoApp(session, listTodoService = Mock(), todoService = todoService, request = request, redirect = redirect)
        todoApp.checkTask(taskTest)
        todoService.checkTask.assert_called_once_with(taskTest)
        redirect.assert_called_once_with("/")

    def test_home_returns_template_with_all_task(self):
        template_mock = Mock(return_value="mocked stuff")
        listTodoService = mockito.mock()
        todoService = mockito.mock()
        session = mockito.mock()
        mockito.when(listTodoService).remove_desable_lists().thenReturn(['name'])
        mockito.when(todoService).getTasksByListname('name').thenReturn([])
        mockito.when(session).isAuthenticated().thenReturn(True)
        html_page = TodoApp(session, template = template_mock, listTodoService = listTodoService, todoService = todoService).home()
        template_mock.assert_called_once()
        mockito.verify(todoService, mockito.never).removeTask(mockito.any())

    def test_home_returns_template_without_task(self):
        template_mock = Mock(return_value="mocked stuff")
        listTodoService = mockito.mock()
        todoService = mockito.mock()
        task = mockito.mock()
        session = mockito.mock()
        mockito.when(task).name().thenReturn('name')
        mockito.when(listTodoService).remove_desable_lists().thenReturn(['name'])
        mockito.when(todoService).getTasksByListname('name').thenReturn([task])
        mockito.when(session).isAuthenticated().thenReturn(True)
        html_page = TodoApp(session, template = template_mock, listTodoService = listTodoService, todoService = todoService).home()
        template_mock.assert_called_once()
        mockito.verify(todoService).removeTask('name')

    def test_home_returns_template(self):
        template_mock = Mock(return_value="mocked stuff")
        listTodoService = mockito.mock()
        session = mockito.mock()
        mockito.when(listTodoService).remove_desable_lists().thenReturn([])
        mockito.when(session).isAuthenticated().thenReturn(True)
        mockito.when(listTodoService).getTasksByListname(mockito.any()).thenReturn([])
        html_page = TodoApp(session, template = template_mock, listTodoService = listTodoService, todoService = Mock()).home()
        template_mock.assert_called_once()

    def test_home_returns_login_template(self):
        redirect = mockito.mock()
        listTodoService = mockito.mock()
        session = mockito.mock()
        mockito.when(session).isAuthenticated().thenReturn(False)
        html_page = TodoApp(session, listTodoService = listTodoService, todoService = Mock(), redirect = redirect).home()
        redirect.assert_called_once()

    def test_update_settings_returns_template(self):
        template_mock = Mock(return_value="mocked stuff")
        session = mockito.mock()
        html_page = TodoApp(session, template = template_mock, listTodoService = Mock(), todoService = Mock()).updateTask('')
        template_mock.assert_called_once()

    def test_submit_update_settings_redirect_home(self):
        redirect = Mock()
        todoService = mock()
        session = mockito.mock()
        TodoApp(session, listTodoService = Mock(), todoService = todoService, redirect= redirect).submitUpdateTask('old', 'new')
        verify(todoService).updateTask(any(), any())
        redirect.assert_called_once_with("/")

    def test_take_task(self):
        redirect = Mock()
        todoService = mock()
        session = mockito.mock()
        TodoApp(session, listTodoService = Mock(), todoService = todoService, redirect= redirect).takeTask('name')
        verify(todoService).takeTask(any(), any())
        redirect.assert_called_once_with("/")
