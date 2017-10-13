class ListRepository:

    """
    repository list
    """

    def __init__(self, connection):
        self.connection = connection

    def add_list_into_repository(self, name):
        cur = self.connection.cursor()
        cur.execute("INSERT into lists values ('" + name +"')")

    def get_list_repository(self):
        cur = self.connection.cursor()
        cur.execute("SELECT * from lists")
        rows = cur.fetchall()
        lst = []
        for row in rows:
            lst.append(row[0])
        return lst