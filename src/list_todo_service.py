import sqlite3
from sqlite3 import Error
from list_todo import *
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "todo.db")

class ListTodoService:

    def __init__(self, list_todo):
        self.list_todo = list_todo

    def add_list(self, name):
        self.list_todo.add_list(name)
        add_list_into_repoditory(name)

    def get_list(self):
        return get_list_repoditory()


##DATABASE
def create_connection(database):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)

    return None

def add_list_into_repoditory(name):
    database = "todo.db"
    conn = create_connection(db_path)
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT into lists values ('" + name +"')")

        rows = cur.fetchall()

        return rows

def get_list_repoditory():
    database = "todo.db"
    conn = create_connection(db_path)
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * from lists")

        rows = cur.fetchall()

        return list(rows)
