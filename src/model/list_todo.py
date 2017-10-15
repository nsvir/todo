class ListTodo:

    """
    List Todo contains name

    Initialize an empty list
    lst = ListTodo()

    To get list
    >>> lst.list()
    []

    To add element in list
    lst.add_list(TaskList())

    To check if element is contained in list
    lst.contains_list(TaskList())
    True
    """

    def __init__(self):
        self.__lst = []

    def list(self) :
        return self.__lst

    def contains_list(self, tasklist):
        for listt in self.__lst:
            if listt.name() == tasklist.name():
                return True
        return False

    def contains_list_by_name(self, listname):
        for listt in self.__lst:
            if listt.name() == listname:
                return True
        return False

    def add_list(self, taskList):
        self.__lst.append(taskList)

    def get_list(self, namelist):
        for listt in self.__lst:
            if listt.name() == namelist:
                return listt
        return None

    def remove_list(self, namelist):
        newlst = []
        for lst in self.__lst:
            if lst.name() != namelist:
                newlst.append(lst)
        self.__lst = newlst