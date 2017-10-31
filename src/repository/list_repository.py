class ListRepository:

    """
    repository list
    """

    def __init__(self, connection):
        self.connection = connection

    def add_list_into_repository(self, name, desapear, hour, hebdo, desapearHebdo, hourHebdo, listUsers):
        cur = self.connection.cursor()
        cur.execute("INSERT into lists values ('" + name +"', "+ str(desapear) + ", '" + hour + "', " +str(hebdo)+ ", "+ str(desapearHebdo)+", '"+hourHebdo+"')")
        self.connection.commit()
        for user in listUsers:
            cur.execute("INSERT into userlists values ('" + name +"', '"+ user + "')")
            self.connection.commit()

    def get_list_name_repository_by_user_name(self, session):
        cur = self.connection.cursor()
        cur.execute("SELECT listname from userlists where login = '" + session.login()+ "'")
        rows = cur.fetchall()
        lst = []
        for row in rows:
            lst.append(row[0])
        return lst

    def update_settings(self, name, desapear, hour, hebdo, desapearHebdo, hourHebdo, listUsers):
        cur = self.connection.cursor()
        cur.execute("UPDATE lists set desable = " + str(desapear) +", hour = '"+ hour + "', hebdo = " +str(hebdo)+ ", desable_hebdo = "+ str(desapearHebdo)+", hour_hebdo = '"+hourHebdo+"' where name='" + name + "'")
        self.connection.commit()
        cur.execute("DELETE from userlists where listname='" + name + "'")
        self.connection.commit()
        for user in listUsers:
            cur.execute("INSERT into userlists values ('" + name +"', '"+ user + "')")
            self.connection.commit()

    def get_all_list(self):
        cur = self.connection.cursor()
        cur.execute("SELECT * from lists")
        return cur.fetchall()

    def remove_list_into_repository(self, listname):
        cur = self.connection.cursor()
        cur.execute("DELETE from userlists where listname='" + listname + "'")
        self.connection.commit()
        cur.execute("DELETE from lists where name='" + listname + "'")
        self.connection.commit()

    def getAllUsersByListName(self, listname):
        cur = self.connection.cursor()
        cur.execute("SELECT login from userlists where listname = '" + listname + "'")
        rows = cur.fetchall()
        lst = []
        for row in rows:
            lst.append(row[0])
        return lst