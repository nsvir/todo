class ListRepository:

    """
    repository list
    """

    def __init__(self, connection):
        self.connection = connection

    def add_list_into_repository(self, name, desapear, hour):
        cur = self.connection.cursor()
        cur.execute("INSERT into lists values ('" + name +"', "+ str(desapear) + ", '" + hour + "')")
        self.connection.commit()

    def get_list_name_repository(self):
        cur = self.connection.cursor()
        cur.execute("SELECT * from lists")
        rows = cur.fetchall()
        lst = []
        for row in rows:
            lst.append(row[0])
        return lst

    def update_settings(self, name, desapear, hour):
        cur = self.connection.cursor()
        cur.execute("UPDATE lists set desable = " + str(desapear) +", hour = '"+ hour + "' where name='" + name + "'")
        self.connection.commit()

    def get_all_list(self):
        cur = self.connection.cursor()
        cur.execute("SELECT * from lists")
        return cur.fetchall()