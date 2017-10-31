import os.path
from init import *
from db.connect import *
from model.list_todo import *
from model.users import *
from model.session_user import *

from controller.init import *
from controller.manage_list import *

from repository.list_repository import *
from repository.TodoDatabase import TodoDatabase
from repository.user_repository import *

from service.list_todo_service import *
from service.check_parameter import *
from service.todo_service import TodoService
from service.login_service import *
from service.cryptage import *

from factory.task_list_factory import *
from factory.task_factory import *
from factory.user_factory import *

from controller.todo import TodoApp
from controller.login import Login
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

#init session
session = SessionUser()
userRepository = UserRepository(conn)

#initialize list todo
checkParameter = CheckParameter()
listRepository = ListRepository(conn)
listTodo = ListTodo()
listTodoService = ListTodoService(listRepository, userRepository, listTodo)
todoService = TodoService(TodoDatabase(conn), taskFactory)
#login

list_users = Users()
user_factory = UserFactory()
cryptage = Cryptage()
loginService = LoginService(userRepository, list_users, user_factory, cryptage)

init = Init(listTodoService, listRepository, loginService, taskListFactory, todoService)
init.initTodoList(listTodo)

todoApp = Bottle()
myTodoApp = TodoApp(session, listTodoService, todoService)

#login
login = Login(session, loginService, checkParameter)

listApp = Bottle()
css = Bottle()

myapp = ManageList(session=session, listService=listTodoService, checkParam=checkParameter, taskListFactory=taskListFactory, todoService=todoService)
listApp.route("/addList/:listname")(myapp.addList)
listApp.route("/listSettings/:listname")(myapp.listSettings)
listApp.route("/listSettings/settingsForm/:name", 'POST')(myapp.submitListSettings)
listApp.route("/deleteList/:name")(myapp.deleteList)

todoApp.route("/")(myTodoApp.home)
todoApp.route("/addTask/:task/:listname")(myTodoApp.addTask)
todoApp.route("/removeTask/:task")(myTodoApp.removeTask)
todoApp.route("/updateTask/:task")(myTodoApp.updateTask)
todoApp.route("/takeTask/:task")(myTodoApp.takeTask)
todoApp.route("/taskDone/:task")(myTodoApp.checkTask)
todoApp.route("/updateTask/submitUpdateTask/:oldname/:newname")(myTodoApp.submitUpdateTask)

todoApp.route("/login")(login.login)
todoApp.route("/submitLogin", 'POST')(login.postLogin)

css.route('/css/:path')(static_css)
