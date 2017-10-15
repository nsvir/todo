class TaskList:
    
    def __init__(self, name, desapear, hour):
        self.__name = name
        self.__desapear = desapear
        self.__hour = hour

    def set_parameters(self, desapear, hour):
        self.__desapear = desapear
        self.__hour = hour

    def hour(self):
        return self.__hour

    def name(self):
        return self.__name

    def desapear(self):
        return self.__desapear