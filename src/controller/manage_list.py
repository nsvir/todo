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
            hebdo = request.forms.get('hebdo')
            desapearHebdo = request.forms.get('desapearTaskHebdo')
            hourHebdo = request.forms.get('timeDisapearHebdo')

            lst = self.listService.get_lst(name)
            if ((not desapear or self.checkParam.valid_hour(hour)) and (not desapearHebdo or self.checkParam.valid_hour(hourHebdo))):
                desa_pear = self.transformCheckboxToInt(desapear)
                desa_pearHebdo= self.transformCheckboxToInt(desapearHebdo)
                he_bdo = self.transformCheckboxToInt(hebdo)
                ho_ur = self.transformHourToString(hour)
                ho_urHebdo = self.transformHourToString(hourHebdo)
                
                lst.set_parameters(desa_pear, ho_ur, he_bdo, desa_pearHebdo, ho_urHebdo)
                self.listService.save_settings(lst)
                status = 'Enregistré'
            text_desapear = ''
            text_hebdo = 'Les tâches ne sont pas hebdomadaires'
            if lst.desapear() == 0:
                text_desapear = 'Les tâches de la liste ne disparaissent pas'
            if lst.hebdo() == 0:
                if lst.desapear() == 1:
                    text_desapear = 'Les tâches de la liste disparaissent à ' + lst.hour()
            else :
                text_hebdo = 'Les tâches sont hebdomadaires'
                if lst.desapearHebdo() == 0:
                    text_hebdo += ' et disparaissent à ' + lst.hourHebdo()
            return template('src/web/template/settingsListResult.tpl', list=name, desapear=text_desapear, hebdo= text_hebdo, status = status, css="../../css/index.css")
        redirect("/")

    def transformCheckboxToInt(self, checkbox):
        res = 1
        if checkbox == None or checkbox == 0:
            res = 0
        return res

    def transformHourToString(self, hour):
        if hour == None:
            return ''
        return hour

    def getSettingsPage(self, status, listname, css):
        lst = self.listService.get_lst(listname)
        desapear = ''
        hebdo = ''
        desapearHebdo = ''
        if lst.desapear() == 1:
            desapear = 'checked'
        if lst.hebdo() == 1:
            hebdo = 'checked'
        if lst.desapearHebdo() == 1:
            desapearHebdo = 'checked'
        hour = lst.hour()
        hourHebdo = lst.hourHebdo()
        output = template('src/web/template/settingsList.tpl', list=listname, desapear=desapear, hour=hour, hebdo=hebdo, desapearHebdo=desapearHebdo, hourHebdo=hourHebdo, status= status, css=css)
        return output