from bottle import Bottle, request, template, debug, static_file, redirect
import os, sys
from init import *

listApp = Bottle()

debug(True)

"""
Controller to manage list todo
"""
class ManageList:
    def __init__(self, listTodoService):
        self.listTodoService = listTodoService

    def addList(self, listname):
        print("ok")
        listTodoService.add_list(listname)
        print('here')

myapp = ManageList(listTodoService=listTodoService)
listApp.route("/addList/:listname")(myapp.addList)