import os.path
from init import *
from db.connect import *
from model.list_todo import *
from service.list_todo_service import *

from repository.list_repository import *
from controller.manage_list import *


#Initialization

#Connection database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db/todo.db")
connection = Connection()
conn = connection.create_connection(db_path)

#initialize list todo
listRepository = ListRepository(conn)
listTodo = ListTodo()
listTodoService = ListTodoService(listRepository, listTodo)

listApp = Bottle()

myapp = ManageList(listService=listTodoService)
listApp.route("/addList/:listname")(myapp.addList)
listApp.route("/listSettings/:listname")(myapp.listSettings)