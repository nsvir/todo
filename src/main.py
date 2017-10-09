from bottle import Bottle
from login import loginApp

rootApp = Bottle()

if __name__ == '__main__':
    rootApp.merge(loginApp)
    rootApp.run(debug=True)

run(host='localhost', port=8080)
