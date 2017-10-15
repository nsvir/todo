from model.Task import Task

class TodoDatabase:

    def __init__(self, connection):
        self.connection = connection

    def add(self, taskObject):
        self.connection.execute("INSERT into tasks values (?, ?)", (taskObject.name(), taskObject.done()))
        self.connection.commit()

    def update(self, taskObject):
        self.connection.execute("UPDATE tasks SET name = ?, isDone = ? WHERE name = ?", \
                                                    (taskObject.name(), taskObject.done(), taskObject.name()))
        self.connection.commit()


    def delete(self, taskObject):
        self.connection.execute("DELETE FROM tasks WHERE name = ?", (taskObject.name(),))
        self.connection.commit()

    def retrieve(self):
        result = []
        for taskArray in self.connection.execute("SELECT name, isDone FROM tasks"):
            result.append(Task(taskArray[0], taskArray[1]))
        return result
