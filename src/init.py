import os.path
from init import *
from db.connect import *
from model.list_todo import *
from service.list_todo_service import *
from controller.init import *
from repository.list_repository import *
from controller.manage_list import *
from service.check_parameter import *

from factory.task_list_factory import *

#Initialization

#Connection database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db/todo.db")
connection = Connection()
conn = connection.create_connection(db_path)
taskListFactory = TaskListFactory()

#initialize list todo
checkParameter = CheckParameter()
listRepository = ListRepository(conn)
listTodo = ListTodo()
listTodoService = ListTodoService(listRepository, listTodo)
init = Init(listTodoService, listRepository, taskListFactory)
init.initTodoList(listTodo)

listApp = Bottle()

myapp = ManageList(listService=listTodoService, checkParam=checkParameter, taskListFactory=taskListFactory)
listApp.route("/addList/:listname")(myapp.addList)
listApp.route("/listSettings/:listname")(myapp.listSettings)
listApp.route("/listSettings/settingsForm/:name", 'POST')(myapp.submitListSettings)