class UserRepository: 

    def __init__(self, connection):
        self.connection = connection

    def get_all_list(self):
        cur = self.connection.cursor()
        cur.execute("SELECT * from users")
        return cur.fetchall()