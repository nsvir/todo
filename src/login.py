from bottle import Bottle, request, template, debug, static_file
import os, sys
from list_todo import *
from list_todo_service import *

listTodo = ListTodo()
listTodoService = ListTodoService(listTodo)

loginApp = Bottle()

count = 1
tasks = []
dirname = os.path.dirname(sys.argv[0])
debug(True)

@loginApp.route('/css/:path')
def static_css(path):
    return static_file(path, root="src/web/css/")

@loginApp.route('/js/:path')
def static_js(path):
    return static_file(path, root="src/web/js/")

@loginApp.route('/tasks')
def hello():
    result = ['ok']
    lists = listTodoService.get_list()
    listname = 'list1'
    output = template('src/web/template/make.tpl', rows=result, lists=lists, list=listname)
    return output

@loginApp.get('/login') # or @route('/login')
def login():
        return login_html()

@loginApp.post('/login') # or @route('/login', method='POST')
def do_login():
        global tasks
        task = request.forms.get('task')
        tasks.append(task)
        return login()

def login_html():

        body="<ul>"
        global tasks
        for v in tasks:
                body += "<li>" + v + "</li>"
        body += "</ul>"

        form= '''
        <form action="/login" method="post">
        Task: <input name="task" type="text" />
        <input value="Login" type="submit" />
        </form>'''

        return body + form
