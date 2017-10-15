"""
Task represent a task
"""

class Task():

    def __init__(self, name, isDone = False):
        self._name = name
        self._done = isDone

    def setIsDone(self):
        self._done = True

    def done(self):
        return self._done

    def name(self):
        return self._name
