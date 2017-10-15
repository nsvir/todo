<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="{{css}}">
  <title>SuperTodo Application</title>
</head>
<body>

<div id="todo">
<div id="myDIV" class="header">
  <h2>{{list}} - Settings</h2>
  <a href="../" class="accueil"  name="home"><button type="button">Accueil</button></a>
  </div>
  <div>
  <form onSubmit="this.action = 'settingsForm/{{list}}'" id="settingsForm" method="post">
    <input id="hebdo" type="checkbox" value="hebdo" name="hebdo" {{hebdo}}/> <label>Tâches hebdomadaires </label>
    </br>
    <input id="desapearTaskHebdo" type="checkbox" value="desapearHebdo" name="desapearTaskHebdo" {{desapearHebdo}}/> <label>Faire disparaître les tâches hebdomadaires</label>
    <input type="time" name="timeDisapearHebdo" id="timeDisapearHebdo" value="{{hourHebdo}}"/>
    </br>
    <input id="desapearTask" type="checkbox" value="desapear" name="desapearTask" {{desapear}}/> <label>Faire disparaître les tâches </label>
    <input id="settingsSubmit" type="submit" value="Submit" name="settings_submit">
    <input type="time" name="timeDisapear" id="timeDisapear" value="{{hour}}"/>
    <input type="hidden" value="{{list}}"/>
    
  </form>

</div>
</div>
</body>
</html>
