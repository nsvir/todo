from tools.todo import Todo
import random, string

from locust import HttpLocust, TaskSet, task

###
# Helpers
###

# Create a random string with a specific length
def randomString(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

# TaskSet for the Todo server
class TodoTaskSet(TaskSet):

    def on_start(self):
        self.todo = Todo(self.client)

###
# Behaviors
###

# Simple reading behavior which only monitor
class ReadingBehavior(TodoTaskSet):

    @task(1)
    def addRemoveTask(self):
        self.todo.showTasks()

# More complexe and stressful behavior
# 1 human task
# 2 automatic tasks
class CreatingBehavior(TodoTaskSet):

    list = [ str(i) + "" + randomString(50) for i in range(20) ]

    @task(1)
    def create_list_plus_task_and_remove_them(self):
        self.todo.addList("maison")
        self.todo.addTask("vaisselle", "maison")
        self.todo.removeTask("vaisselle")
        self.todo.removeList("maison")

    @task(1)
    def create_random_lists_and_remove_them(self):
        list_names = []
        uniq = "1_"
        for i in range(random.randint(0,9)):
            list_name = uniq + random.choice(self.list)
            list_names.append(list_name)
            self.todo.addList(list_name)
        for list_name in list_names:
            self.todo.removeList(list_name)

    @task(1)
    def create_random_tasks_and_remove_them(self):
        task_names = []
        uniq = "2_"
        list_name = uniq + random.choice(self.list)
        self.todo.addList(list_name)
        for i in range(random.randint(0,9)):
            task_name = uniq + random.choice(self.list)
            task_names.append(task_name)
            self.todo.addTask(task_names, list_name)
        for task in task_names:
            self.todo.removeTask(task)
        self.todo.removeList(list_name)

# Users

class ReadingUser(HttpLocust):
    task_set = ReadingBehavior
    min_wait = 1000
    max_wait = 5000

class CreatingUser(HttpLocust):
    task_set = CreatingBehavior
    min_wait = 1000 #5000
    max_wait = 5000 #15000
