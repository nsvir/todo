class User : 

    def __init__(self, login, password):
        self.__login = login
        self.__password = password 

    def login(self):
        return self.__login

    def password(self):
        return self.__password