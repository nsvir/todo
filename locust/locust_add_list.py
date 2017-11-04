from locust import HttpLocust, TaskSet, task


########################################################################
# des lecteurs de todo
########################################################################

class ReadTodos(TaskSet):
    """
    Définition des tâches rassemblées dans un TaskSet
    """

    def on_start(self):
        '''
        Méthode appelée par covention qd un locust démarre, avant tout appel de task.
        '''
        self.login()

    def login(self):
        """
        Cette méthode n'est pas une tâche.
        """
        self.client.get('/login')
        self.client.post("/submitLogin",
                {"login":"test",
                "password":"test",
                "login_submit":"submit"
                })

    def settings_page(self):
        self.client.get('/listSettings/newlist')

    @task(1)
    def post_change_settings_list(self):
        self.add_liste()
        self.settings_page()
        self.client.post('/listSettings/settingsForm/newlist', {"timeDisapear":"00:00", "desapearTask": "1", "hebdo":"0", "desapearTaskHebdo": "0", "timeDisapearHebdo": "0", "users" : {"test"}})

    @task(2)
    def add_liste(self):
        self.login()
        self.client.get("/addList/newlist")

    @task(3)
    def todo(self):
        '''Cette méthode est une tâche, de poid 2,
        a 2 fois plus de chances d'être appelée qu'une méthode de poid 1.
        '''
        self.client.get("/")


class ReadTodosUser(HttpLocust):
    """
    Classe représentant un utilisateur du site.
    min_wait et max_wait = combien de temps l'utilisateur attend entre l'exécution de 2 tâches, en ms.
    task_set = les tâches qui définissent le "comportement" de l'utilisateur.
    HttpLocust hérite de Locust en lui ajoutant un attribut "client" qui est
    une instance de HttpSession, permettant de faire des requètes HTTP.
    """
    task_set = ReadTodos
    min_wait = 1000  #5000
    max_wait = 2000 #9000
