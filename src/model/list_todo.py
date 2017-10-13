class ListTodo:

    """
    List Todo contains name

    Initialize an empty list
    lst = ListTodo()

    To get list
    >>> lst.list()
    []

    To add element in list
    >>> lst.add_list("name")

    To check if element is contained in list
    >>> lst.contains_list("name")
    True
    """

    def __init__(self):
        self.__lst = []

    def list(self) :
        return self.__lst

    def contains_list(self, listname):
        return listname in self.__lst

    def add_list(self, listname):
        self.__lst.append(listname)
