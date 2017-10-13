from bottle import Bottle
from login import loginApp
from controller.manage_list import listApp

rootApp = Bottle()

if __name__ == '__main__':
    rootApp.merge(loginApp)
    rootApp.merge(listApp)
    rootApp.run(debug=True)

run(host='localhost', port=8080)
