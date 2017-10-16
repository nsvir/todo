from model.Task import *

class TaskFactory:
    
    def create(self, name, lst):
        return Task(name, lst)