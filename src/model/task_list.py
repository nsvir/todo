class TaskList:
    
    def __init__(self, name, desapear, hour, hebdo, desapearHebdo, hourHebdo, listUsers):
        self.__name = name
        self.__desapear = desapear
        self.__hour = hour
        self.__hebdo = hebdo
        self.__desapearHebdo = desapearHebdo
        self.__hourHebdo = hourHebdo
        self.__listUsers = listUsers

    def set_parameters(self, desapear, hour, hebdo, desapearHebdo, hourHebdo, listUsers):
        self.__desapear = desapear
        self.__hour = hour
        self.__hebdo = hebdo
        self.__desapearHebdo = desapearHebdo
        self.__hourHebdo = hourHebdo
        self.__listUsers = listUsers

    def hour(self):
        return self.__hour

    def name(self):
        return self.__name

    def desapear(self):
        return self.__desapear

    def hebdo(self):
        return self.__hebdo

    def desapearHebdo(self):
        return self.__desapearHebdo

    def hourHebdo(self):
        return self.__hourHebdo

    def listUsers(self):
        return self.__listUsers