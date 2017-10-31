class SessionUser:

    def __init__(self):
        self.__authentication = False
        self.__login = None

    def auth(self, login):
        self.__login = login
        self.__authentication = True

    def login(self):
        return self.__login

    def isAuthenticated(self):
        return self.__authentication