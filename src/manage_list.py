from bottle import Bottle, request, template, debug, static_file, redirect
import os, sys
from list_todo import *
from list_todo_service import *

listApp = Bottle()
listTodo = ListTodo()
listTodoService = ListTodoService(listTodo)

debug(True)

@listApp.route('/addList/:listname')
def addList(listname):
    listTodoService.add_list(listname)
    redirect("/")
