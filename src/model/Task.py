"""
Task represent a task
"""

class Task():

    def __init__(self, name, listname, isDone = False, visible=True):
        self._name = name
        self._done = isDone
        self._listname = listname
        self._visible = visible

    def setIsDone(self):
        self._done = True

    def done(self):
        return self._done

    def name(self):
        return self._name

    def listname(self):
        return self._listname

    def set_name(self, name):
        self._name = name

    def invisible(self):
        self._visible = False

    def visible(self):
        self._visible = True

    def is_visible(self):
        return self._visible
