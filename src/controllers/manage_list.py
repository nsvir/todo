from bottle import Bottle, request, template, debug, static_file
import os, sys
loginApp = Bottle()

debug(True)

@loginApp.route('/addList/:listname')
def addList(listname):

