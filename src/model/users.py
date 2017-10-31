class Users:
    
    def __init__(self):
        self.__list_users = []

    def user_exists(self, login, password):
        for user in self.__list_users:
            if user.login() == login and user.password() == password:
                return True 
        return False

    def set_users(self, users):
        self.__list_users = users