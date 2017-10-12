class ListTodo:

    def __init__(self):
        self.__lst = []

    def list(self) :
        return self.__lst

    def contains_list(self, listname):
        return listname in self.__lst

    def add_list(self, listname):
        self.__lst.append(listname)
