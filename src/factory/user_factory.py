from model.user import *

class UserFactory:
    
    def create(self, name, password):
        return User(name, password)