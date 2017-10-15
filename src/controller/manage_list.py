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
        if self.listService.list_exists_by_name(listname):
            return self.getSettingsPage("", listname, "../css/index.css")
        redirect("/")

    def submitListSettings(self, name):
        if self.listService.list_exists_by_name(name):
            status = 'Error'
            hour = request.forms.get('timeDisapear')
            desapear = request.forms.get('desapearTask')
            lst = self.listService.get_lst(name)
            if (not desapear or self.checkParam.valid_hour(hour)) :
                desa_pear = 1
                ho_ur = ''
                if desapear == None or desapear == 0:
                    desa_pear = 0
                if hour != None:
                    ho_ur = hour
                lst.set_parameters(desa_pear, ho_ur)
                self.listService.save_settings(lst)
                status = 'Enregistré'
            text_desapear = 'Les tâches de la liste disparaissent à ' + lst.hour()
            if lst.desapear() == 0 :
                text_desapear = 'Les tâches de la liste ne disparaissent pas à ' + lst.hour()
            return template('src/web/template/settingsListResult.tpl', list=name, desapear=text_desapear, status = status, css="../../css/index.css")
        redirect("/")

    def getSettingsPage(self, status, listname, css):
        lst = self.listService.get_lst(listname)
        desapear = ''
        if lst.desapear() == 1:
            desapear = 'checked'
        hour = lst.hour()
        output = template('src/web/template/settingsList.tpl', list=listname, desapear=desapear, hour=hour, css=css)
        return output