from bottle import Bottle, request, template, debug, static_file, redirect
import os, sys

debug(True)

"""
Controller to manage list todo
"""
class ManageList:
    def __init__(self, listService):
        self.listService = listService

    def addList(self, listname):
        self.listService.add_list(listname)
        redirect("/")

    def listSettings(self, listname):
        lists = self.listService.get_list()
        output = template('src/web/template/settingsList.tpl', lists=lists, list=listname)
        return output
