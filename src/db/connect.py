#!/usr/bin/python

import sqlite3
from sqlite3 import Error


class Connection:

    """
    Create connection to database

    conn = Connection()
    conn.create_connection("data.db")
    """

    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return None
