from bottle import Bottle, request, template, debug, static_file, redirect
import os, sys
from init import *

listApp = Bottle()

debug(True)

"""
Controller to manage list todo
"""

@listApp.route('/addList/:listname')
def addList(listname):
    listTodoService.add_list(listname)
    redirect("/")
