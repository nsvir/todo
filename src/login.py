from bottle import Bottle, request

loginApp = Bottle()

count = 1
tasks = []

@loginApp.route('/hello')
def hello():
        global count
        count = count + 1
        return 'You have %d things.' % count

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
