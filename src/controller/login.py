from bottle import Bottle, request, template, debug, static_file, redirect
import os, sys

debug(True)

class Login:

    def __init__(self, session, loginservice, checkParam, template = template, redirect = redirect):
        self.session = session
        self.redirect = redirect
        self.template = template
        self.loginService = loginservice
        self.checkParam = checkParam

    def login(self):
        output = self.template('src/web/template/login.tpl', status = '')
        return output

    def postLogin(self):
        login = request.forms.get('login')
        password = request.forms.get('password')
        status = 'Error'
        if self.checkParam.valid_name_list(login) and self.checkParam.valid_name_list(password) and self.loginService.user_exists(login, password):
            self.session.auth(login)
            redirect("/")
        output = self.template('src/web/template/login.tpl', status = status)
        return output