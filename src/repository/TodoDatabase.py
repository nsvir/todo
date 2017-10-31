from model.Task import Task

class TodoDatabase:

    def __init__(self, connection):
        self.connection = connection

    def add(self, taskObject):
        self.connection.execute("INSERT into tasks values (?, ?, ?, ?, ?)", (taskObject.name(), taskObject.done(), taskObject.listname(), taskObject.is_visible(), taskObject.login()))
        self.connection.commit()

    def update(self, taskObject):
        self.connection.execute("UPDATE tasks SET name = ?, isDone = ? WHERE name = ?", \
                                                    (taskObject.name(), taskObject.done(), taskObject.name()))
        self.connection.commit()

    def update_with_old_name(self, taskname, taskObject):
        self.connection.execute("UPDATE tasks SET name = ? WHERE name = ?", \
                                                    (taskObject.name(), taskname))
        self.connection.commit()

    def delete(self, taskObject):
        self.connection.execute("DELETE FROM tasks WHERE name = '"+ (taskObject.name())+ "'")
        self.connection.commit()

    def retrieve(self):
        result = []
        for taskArray in self.connection.execute("SELECT name, isDone, listname, visible, login FROM tasks"):
            result.append(Task(taskArray[0], taskArray[2], taskArray[1], taskArray[3], taskArray[4]))
        return result

    def desable_tasks_by_listname(self, listname):
        self.connection.execute("UPDATE tasks SET visible = 'FALSE' WHERE listname = '"+ listname+ "'")
        self.connection.commit()

    def enable_tasks_by_listname(self, listname):
        self.connection.execute("UPDATE tasks SET visible = 'TRUE' WHERE listname = '"+ listname+ "'")
        self.connection.commit()

    def takeTask(self, taskObject):
        self.connection.execute("UPDATE tasks SET login = ? WHERE name = ?", \
                                                    (taskObject.login(), taskObject.name()))
        self.connection.commit()