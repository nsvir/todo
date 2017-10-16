import os.path
from init import *
from db.connect import *
from model.list_todo import *
from controller.init import *
from controller.manage_list import *

from repository.list_repository import *
from repository.TodoDatabase import TodoDatabase

from service.list_todo_service import *
from service.check_parameter import *
from service.todo_service import TodoService

from factory.task_list_factory import *
from factory.task_factory import *
from controller.todo import TodoApp
#Initialization

# static_css
def static_css(path):
    return static_file(path, root="src/web/css/")


#Connection database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db/todo.db")
connection = Connection()
conn = connection.create_connection(db_path)
taskListFactory = TaskListFactory()
taskFactory = TaskFactory()

#initialize list todo
checkParameter = CheckParameter()
listRepository = ListRepository(conn)
listTodo = ListTodo()
listTodoService = ListTodoService(listRepository, listTodo)
todoService = TodoService(TodoDatabase(conn), taskFactory)
init = Init(listTodoService, listRepository, taskListFactory, todoService)
init.initTodoList(listTodo)

todoApp = Bottle()
myTodoApp = TodoApp(listTodoService, todoService)



listApp = Bottle()
css = Bottle()

myapp = ManageList(listService=listTodoService, checkParam=checkParameter, taskListFactory=taskListFactory, todoService=todoService)
listApp.route("/addList/:listname")(myapp.addList)
listApp.route("/listSettings/:listname")(myapp.listSettings)
listApp.route("/listSettings/settingsForm/:name", 'POST')(myapp.submitListSettings)
listApp.route("/deleteList/:name")(myapp.deleteList)

todoApp.route("/")(myTodoApp.home)
todoApp.route("/addTask/:task/:listname")(myTodoApp.addTask)
todoApp.route("/removeTask/:task")(myTodoApp.removeTask)
todoApp.route("/updateTask/:task")(myTodoApp.updateTask)
todoApp.route("/taskDone/:task")(myTodoApp.checkTask)
todoApp.route("/updateTask/submitUpdateTask/:oldname/:newname")(myTodoApp.submitUpdateTask)
css.route('/css/:path')(static_css)
