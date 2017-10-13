class ListRepository:

    """
    repository list
    """

    def __init__(self, connection):
        self.connection = connection

    def add_list_into_repository(self, name):
        with self.connection:
            cur = self.connection.cursor()
            cur.execute("INSERT into lists values ('" + name +"')")
            rows = cur.fetchall()
            return rows

    def get_list_repository(self):
        with self.connection:
            cur = self.connection.cursor()
            cur.execute("SELECT * from lists")
            rows = cur.fetchall()
            return list(rows)