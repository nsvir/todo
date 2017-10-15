from bottle import Bottle, request, template, debug, static_file, redirect
import os, sys

debug(True)

"""
Controller to manage list todo
"""
class ManageList:
    def __init__(self, listService, checkParam, taskListFactory):
        self.listService = listService
        self.checkParam = checkParam
        self.taskListFactory = taskListFactory

    def addList(self, listname):
        if (self.checkParam.valid_name_list(listname)) :
            self.listService.add_list(self.taskListFactory.createTaskList(listname))
        redirect("/")

    def listSettings(self, listname):
        lists = self.listService.get_list_name()
        output = template('src/web/template/settingsList.tpl', lists=lists, list=listname, status='')
        return output

    def submitListSettings(self, name):
        status = 'Error'
        hour = request.forms.get('timeDisapear')
        desapear = request.forms.get('desapearTask')
        if (not desapear or self.checkParam.valid_hour(hour)) :
            self.listService.save_settings(self.taskListFactory.createTaskListWithElements(name, desapear, hour))
            status = 'Enregistré'
        lists = self.listService.get_list_name()
        return template('src/web/template/settingsList.tpl', lists=lists, list=name, status=status)