from locust import HttpLocust, TaskSet, task

"""
Hélène Meyer
TP Test de performance
OPL
04/11/2017
"""
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
        Se connecter
        """
        self.client.get('/login')
        self.client.post("/submitLogin",
                {"login":"test",
                "password":"test",
                "login_submit":"submit"
                })

    def settings_page(self):
        """
        Ajouter une liste et acceder à sa page de configuration
        """
        self.add_liste()
        self.client.get('/listSettings/newlist')

    @task(1)
    def post_change_settings_list(self):
        """
        Ajouter une liste, acceder à sa page de configuration et envoyer le formulaire avec de bons parametres
        """
        self.add_liste()
        self.settings_page()
        self.client.post('/listSettings/settingsForm/newlist', {"timeDisapear":"00:00", "desapearTask": "1", "hebdo":"0", "desapearTaskHebdo": "0", "timeDisapearHebdo": "00:00", "users" : {"test"}})

    @task(1)
    def post_change_settings_list_bad_input_time(self):
        """
        Ajouter une liste, acceder à sa page de configuration et envoyer le formulaire avec un mauvais parametre
        """
        self.add_liste()
        self.settings_page()
        self.client.post('/listSettings/settingsForm/newlist', {"timeDisapear":"00:99", "desapearTask": "1", "hebdo":"0", "desapearTaskHebdo": "0", "timeDisapearHebdo": "0", "users" : {"test"}})
		
    @task(2)
    def add_task(self):
        """
        Ajouter une liste et ajouter une tache
        """
        self.client.get("/addList/listToAddTask")
        self.client.get("/addTask/listToAddTask/taskOneToAddTask")

    @task(2)
    def remove_task(self):
        """
        Ajouter une liste et une tache et supprimer la tache
        """
        self.client.get("/addList/listToRemoveTask")
        self.client.get("/addTask/listToRemoveTask/taskOneToDeleteTask")
        self.client.get("/removeTask/listToRemoveTask")
		
    @task(2)
    def update_task(self):
        """
        Ajouter une liste et une tâche et changer le nom de la tache
        """
        self.client.get("/addList/listToUpdateTask")
        self.client.get("/addTask/listToUpdateTask/taskOneToUpdateTask")
        self.client.get("/updateTask/submitUpdateTask/taskOneToUpdateTask/newname")
		
    @task(2)
    def done_task(self):
        """
        Ajouter une liste et une tpache et la passer à done
        """
        self.client.get("/addList/listToDoneTask")
        self.client.get("/addTask/listToDoneTask/taskOneToDoneTask")
        self.client.get("/taskDone/listToDoneTask")
		
    @task(2)
    def remove_list(self):
        """
        Ajouter une liste et une tache et supprimer la liste
        """
        self.client.get("/addList/listToRemoveList")
        self.client.get("/addTask/listToRemoveList/taskOneToDeleteList")
        self.client.get("/deleteList/listToRemoveList")
		
    @task(2)
    def add_liste(self):
        """
        Ajouter une liste
        """
        self.client.get("/addList/newlist")

    @task(3)
    def todo(self):
        """
        Visualiser toutes les tâches et liste de tâches
        """
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
    min_wait = 1000 #5000
    max_wait = 3000 #9000
