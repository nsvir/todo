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

    def add_list(self, taskList):
        self.__lst.append(taskList)
