from bottle import Bottle
from init import listApp, todoApp, css

rootApp = Bottle()

if __name__ == '__main__':
    rootApp.merge(todoApp)
    rootApp.merge(listApp)
    rootApp.merge(css)
    rootApp.run(debug=True)

run(host='localhost', port=8080)
