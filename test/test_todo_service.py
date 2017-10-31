import unittest
import mockito
from unittest.mock import Mock
from controller.todo import TodoApp
from service.todo_service import TodoService

class TestTodoService(unittest.TestCase):


    def test_add_task_service(self):
        taskToAdd = "my task"
        lst = "lst"
        database = Mock()
        fabrique = mockito.mock()
        task = mockito.mock()
        mockito.when(task).name().thenReturn("my task")
        mockito.when(fabrique).create(mockito.any(), mockito.any()).thenReturn(task)
        mockito.when(database).retrieve().thenReturn([])
        todoService = TodoService(database, fabrique)
        todoService.addTask(taskToAdd, lst)
        taskToAddObject = todoService.getTask(taskToAdd)
        matchedElementWithTaskToAdd = len(list(filter(lambda task: taskToAdd == task.name(), todoService.getTasks())))
        database.add.assert_called_once_with(taskToAddObject)
        self.assertEqual(1, matchedElementWithTaskToAdd)

    def test_remove_task_service(self):
        taskToRemove = "my task"
        lst = "lst"
        database = Mock()
        fabrique = mockito.mock()
        task = mockito.mock()
        mockito.when(fabrique).create(mockito.any(), mockito.any()).thenReturn(task)
        mockito.when(task).name().thenReturn("my task")
        mockito.when(database).retrieve().thenReturn([])
        todoService = TodoService(database, fabrique)
        todoService.addTask(taskToRemove, lst)
        taskToRemoveObject = todoService.getTask(taskToRemove)
        todoService.removeTask(taskToRemove)
        matchedElementWithTaskToRemove = len(list(filter(lambda task: taskToAdd == task.name(), todoService.getTasks())))
        database.delete.assert_called_once_with(taskToRemoveObject)
        self.assertEqual(0, matchedElementWithTaskToRemove)

    def test_get_existant_task_service(self):
        taskToGet = "my task"
        lst = "lst"
        database = Mock()
        fabrique = mockito.mock()
        task = mockito.mock()
        mockito.when(fabrique).create(mockito.any(), mockito.any()).thenReturn(task)
        mockito.when(database).retrieve().thenReturn([])
        todoService = TodoService(database, fabrique)
        todoService.addTask(taskToGet, lst)
        taskResult = todoService.getTask(taskToGet)
        database.assert_not_called()

    def test_get_unexistant_task_service(self):
        taskToGet = "my task"
        database = Mock()
        fabrique = mockito.mock()
        mockito.when(database).retrieve().thenReturn([])
        todoService = TodoService(database, fabrique)
        taskResult = todoService.getTask(taskToGet)
        database.assert_not_called()
        self.assertEqual(None, taskResult)

    def test_check_task_service(self):
        taskToCheck = "my task"
        lst = "lst"
        database = Mock()
        fabrique = mockito.mock()
        task = mockito.mock()
        mockito.when(task).name().thenReturn("my task")
        mockito.when(fabrique).create(mockito.any(), mockito.any()).thenReturn(task)
        mockito.when(database).retrieve().thenReturn([])
        todoService = TodoService(database, fabrique)
        todoService.addTask(taskToCheck, lst)
        todoService.checkTask(taskToCheck)
        taskToCheckObject = todoService.getTask(taskToCheck)
        taskResult = todoService.getTask(taskToCheck)
        database.update.assert_called_once_with(taskToCheckObject)

    def test_get_all_service(self):
        taskName = "me"
        lst = "lst"
        database = Mock()
        fabrique = mockito.mock()
        task = mockito.mock()
        mockito.when(fabrique).create(mockito.any(), mockito.any()).thenReturn(task)
        mockito.when(database).retrieve().thenReturn([])
        todoService = TodoService(database, fabrique)
        todoService.addTask(taskName, lst)
        listResult = todoService.getTasks()
        self.assertIn(task, listResult)
        mockito.verify(database).retrieve()

    def test_get_all_visible_service(self):
        taskName = "me"
        lst = "lst"
        database = Mock()
        fabrique = mockito.mock()
        task = mockito.mock()
        mockito.when(database).retrieve().thenReturn([])
        todoService = TodoService(database, fabrique)
        mockito.when(fabrique).create(mockito.any(), mockito.any()).thenReturn(task)
        todoService.addTask(taskName, lst)
        mockito.when(task).is_visible().thenReturn(False)
        listResult = todoService.getVisibleTasks()
        
        self.assertEquals([], listResult)
        mockito.verify(database).retrieve()

    def test_get_all_visible_service_bis(self):
        taskName = "me"
        lst = "lst"
        database = Mock()
        fabrique = mockito.mock()
        task = mockito.mock()
        mockito.when(database).retrieve().thenReturn([])
        todoService = TodoService(database, fabrique)
        mockito.when(fabrique).create(mockito.any(), mockito.any()).thenReturn(task)
        todoService.addTask(taskName, lst)
        mockito.when(task).is_visible().thenReturn(True)
        listResult = todoService.getVisibleTasks()
        
        self.assertIn(task, listResult)
        mockito.verify(database).retrieve()

    def test_get_all_tasks_by_listname_service_empty_result(self):
        taskName = "me"
        lst = "lst"
        database = Mock()
        fabrique = mockito.mock()
        task = mockito.mock()
        mockito.when(database).retrieve().thenReturn([])
        todoService = TodoService(database, fabrique)
        mockito.when(fabrique).create(mockito.any(), mockito.any()).thenReturn(task)
        todoService.addTask(taskName, lst)
        mockito.when(task).listname().thenReturn('')
        listResult = todoService.getTasksByListname('name')
        
        self.assertEquals([], listResult)
        mockito.verify(database).retrieve()

    def test_get_all_tasks_by_listname_service(self):
        taskName = "me"
        lst = "lst"
        database = Mock()
        fabrique = mockito.mock()
        task = mockito.mock()
        mockito.when(database).retrieve().thenReturn([])
        todoService = TodoService(database, fabrique)
        mockito.when(fabrique).create(mockito.any(), mockito.any()).thenReturn(task)
        todoService.addTask(taskName, lst)
        mockito.when(task).listname().thenReturn('name')
        listResult = todoService.getTasksByListname('name')
        
        self.assertIn(task, listResult)
        mockito.verify(database).retrieve()

    def test_check_task_service_task_none(self):
        taskToCheck = "my task"
        lst = "lst"
        database = Mock()
        fabrique = mockito.mock()
        mockito.when(database).retrieve().thenReturn([])
        todoService = TodoService(database, fabrique)
        todoService.checkTask(taskToCheck)

        mockito.verify(database, mockito.never).update(mockito.any())

class TestRemoveDesableTask(unittest.TestCase):

    def test_remove_task_with_empty_lst(self):
        taskToCheck = "my task"
        lst = "lst"
        database = Mock()
        fabrique = mockito.mock()
        todoService = TodoService(database, fabrique)
        todoService.remove_desable_tasks([])

        mockito.verify(database, mockito.never).remove_tasks_by_listname(mockito.any())

    def test_not_remove_task_with_lst(self):
        taskToCheck = "my task"
        lst = "lst"
        database = mockito.mock()
        lstTask = mockito.mock()
        fabrique = mockito.mock()
        mockito.when(database).retrieve().thenReturn([])
        mockito.when(lstTask).hebdo().thenReturn(1)
        mockito.when(lstTask).desapearHebdo().thenReturn(1)
        mockito.when(lstTask).hourHebdo().thenReturn('23:59')

        todoService = TodoService(database, fabrique)
        todoService.remove_desable_tasks([lstTask])

        mockito.verify(database, mockito.never).remove_tasks_by_listname(mockito.any())

    def test_remove_task_with_lst(self):
        taskName = "my task"
        lst = "lst"
        database = mockito.mock()
        lstTask = mockito.mock()
        fabrique = mockito.mock()
        task = mockito.mock()
        mockito.when(fabrique).create(mockito.any(), mockito.any()).thenReturn(task)
        mockito.when(database).retrieve().thenReturn([])
        mockito.when(lstTask).name().thenReturn("lst")
        mockito.when(lstTask).hebdo().thenReturn(1)
        mockito.when(lstTask).desapearHebdo().thenReturn(1)
        mockito.when(lstTask).hourHebdo().thenReturn('00:00')
        mockito.when(task).listname().thenReturn("lst")

        todoService = TodoService( database, fabrique)
        todoService.addTask(taskName, lst)
        todoService.remove_desable_tasks([lstTask])

        mockito.verify(database).desable_tasks_by_listname(mockito.any())
        mockito.verify(database, mockito.never).enable_tasks_by_listname(mockito.any())

    def test_remove_task_with_lst_bis_listname_not_equals(self):
        taskName = "my task"
        lst = "lstname"
        database = mockito.mock()
        lstTask = mockito.mock()
        fabrique = mockito.mock()
        task = mockito.mock()

        mockito.when(database).retrieve().thenReturn([])
        mockito.when(fabrique).create(mockito.any() ,mockito.any()).thenReturn(task)
        mockito.when(task).listname().thenReturn("test")

        todoService = TodoService(database, fabrique)
        todoService.addTask(taskName, lst)
        todoService.desable_lst_by_listname("lstname")

        mockito.verify(database).desable_tasks_by_listname(mockito.any())
        mockito.verify(task, mockito.never).invisible()

    def test_remove_task_with_lst_bis_listname_equals(self):
        database = mockito.mock()
        lstTask = mockito.mock()
        fabrique = mockito.mock()
        task = mockito.mock()

        mockito.when(database).retrieve().thenReturn([])
        mockito.when(fabrique).create(mockito.any() ,mockito.any()).thenReturn(task)
        mockito.when(task).listname().thenReturn("lstname")

        todoService = TodoService(database, fabrique)
        todoService.addTask("", "")
        todoService.desable_lst_by_listname("lstname")

        mockito.verify(database).desable_tasks_by_listname(mockito.any())
        mockito.verify(task).invisible()

    def test_enable_task_with_lst_bis_listname_not_equals(self):
        taskName = "my task"
        lst = "lstname"
        database = mockito.mock()
        lstTask = mockito.mock()
        fabrique = mockito.mock()
        task = mockito.mock()

        mockito.when(database).retrieve().thenReturn([])
        mockito.when(fabrique).create(mockito.any() ,mockito.any()).thenReturn(task)
        mockito.when(task).listname().thenReturn("test")

        todoService = TodoService(database, fabrique)
        todoService.addTask(taskName, lst)
        todoService.enable_lst_by_listname("lstname")

        mockito.verify(database).enable_tasks_by_listname(mockito.any())
        mockito.verify(task, mockito.never).visible()

    def test_enable_task_with_lst_bis_listname_equals(self):
        database = mockito.mock()
        lstTask = mockito.mock()
        fabrique = mockito.mock()
        task = mockito.mock()

        mockito.when(database).retrieve().thenReturn([])
        mockito.when(fabrique).create(mockito.any() ,mockito.any()).thenReturn(task)
        mockito.when(task).listname().thenReturn("lstname")

        todoService = TodoService(database, fabrique)
        todoService.addTask("", "")
        todoService.enable_lst_by_listname("lstname")

        mockito.verify(database).enable_tasks_by_listname(mockito.any())
        mockito.verify(task).visible()

    def test_remove_task_with_lst_bis(self):
        taskName = "my task"
        lst = "lstname"
        database = mockito.mock()
        lstTask = mockito.mock()
        fabrique = mockito.mock()
        task = mockito.mock()

        mockito.when(database).retrieve().thenReturn([])
        mockito.when(fabrique).create(mockito.any() ,mockito.any()).thenReturn(task)
        mockito.when(lstTask).listname().thenReturn("lstname")
        mockito.when(lstTask).hebdo().thenReturn(0)
        mockito.when(lstTask).desapearHebdo().thenReturn(1)
        mockito.when(lstTask).hourHebdo().thenReturn('23:59')
        mockito.when(task).listname().thenReturn(lst)

        todoService = TodoService(database, fabrique)
        todoService.addTask(taskName, lst)
        todoService.remove_desable_tasks([lstTask])

        mockito.verify(database, mockito.never).desable_tasks_by_listname(mockito.any())
        mockito.verify(database, mockito.never).enable_tasks_by_listname(mockito.any())


    def test_visible_task_with_lst_no_deseaper_hebdo(self):
        taskName = "my task"
        lst = "lst"
        database = mockito.mock()
        lstTask = mockito.mock()
        fabrique = mockito.mock()
        task = mockito.mock()
        mockito.when(fabrique).create(mockito.any(), mockito.any()).thenReturn(task)
        mockito.when(database).retrieve().thenReturn([])
        mockito.when(lstTask).name().thenReturn("lst")
        mockito.when(lstTask).hebdo().thenReturn(1)
        mockito.when(lstTask).desapearHebdo().thenReturn(0)
        mockito.when(lstTask).hourHebdo().thenReturn('00:00')
        mockito.when(task).listname().thenReturn("lst")

        todoService = TodoService( database, fabrique)
        todoService.addTask(taskName, lst)
        todoService.remove_desable_tasks([lstTask])

        mockito.verify(database, mockito.never).desable_tasks_by_listname(mockito.any())
        mockito.verify(database, mockito.never).enable_tasks_by_listname(mockito.any())



class TestUpdateTask(unittest.TestCase):

    def test_update_task(self):
        taskName = "name"
        lst = "lstname"
        database = mockito.mock()
        fabrique = mockito.mock()
        task = mockito.mock()

        mockito.when(database).retrieve().thenReturn([])
        mockito.when(fabrique).create(mockito.any(), mockito.any()).thenReturn(task)
        todoService = TodoService(database, fabrique)
        todoService.addTask(taskName, lst)
        mockito.when(task).name().thenReturn('name')
        todoService.updateTask('name', 'new')

        mockito.verify(database).update_with_old_name(mockito.any(), mockito.any())

    def test_update_none_task(self):
        taskName = "name"
        lst = "lstname"
        database = mockito.mock()
        fabrique = mockito.mock()
        mockito.when(database).retrieve().thenReturn([])

        todoService = TodoService(database, fabrique)
        todoService.updateTask('name', 'new')

        mockito.verify(database, mockito.never).update_with_old_name(mockito.any(), mockito.any())

class TestTakeTask(unittest.TestCase):

    def test_take_task(self):
        taskName = "name"
        lst = "lstname"
        database = mockito.mock()
        fabrique = mockito.mock()
        task = mockito.mock()

        mockito.when(database).retrieve().thenReturn([])
        mockito.when(fabrique).create(mockito.any(), mockito.any()).thenReturn(task)
        todoService = TodoService(database, fabrique)
        todoService.addTask(taskName, lst)
        mockito.when(task).name().thenReturn('name')
        todoService.takeTask('name', 'login')

        mockito.verify(database).takeTask(mockito.any())

    def test_update_none_task(self):
        taskName = "name"
        lst = "lstname"
        database = mockito.mock()
        fabrique = mockito.mock()
        mockito.when(database).retrieve().thenReturn([])

        todoService = TodoService(database, fabrique)
        todoService.takeTask('name', 'login')

        mockito.verify(database, mockito.never).takeTask(mockito.any())
