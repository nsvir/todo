<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="../css/index.css">
  <title>SuperTodo Application</title>
</head>
<body>

<div id="todo">
<div id="myDIV" class="header">
  <h2>{{task}}</h2>
  <a href="../" class="accueil"  name="home"><button type="button">Accueil</button></a>
  </div>
  <div>
    <label>Changer le nom de la tâche :</label>
    <input type="text" name="newTaskName" id="newTaskName" value="{{task}}"/>
    <a onclick="this.href='submitUpdateTask/{{task}}/'+document.getElementById('newTaskName').value" id="submitUpdateTask"><button>OK</button></a>
    
  </form>

</div>
</div>
</body>
</html>
