<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="../css/index.css">
  <title>SuperTodo Application</title>
</head>
<body>

<div id="menu">
    <h3>Listes</h3>
        <input type="text" id="inputListe" name="inputListe" placeholder="Nouvelle Liste">
    <a onclick="this.href='addList/'+document.getElementById('inputListe').value"><span class="addBtn" id="addList" name="addList">+</span></a>
    </br>
    %for row in lists:
      <ul id="myList">
        <a href="#"><li>
            {{row}}
            <a href="#"><span class="close">×</span></a>
            <a onclick="this.href='listSettings/{{row}}'"><span class="edit" name="list_{{row}}">✎</span></a>
        </li></a>
      </ul>
    %end
</div>
<div id="todo">
<div id="myDIV" class="header">
  <h2>{{list}} - Settings</h2>
  </div>
  <div>
  <form action="/">
    <input id="desapearTask" type="checkbox" value="" /> Faire disparaître les tâches 
    </br>
    <input type="time" name="timeDisapear"/>
    <input type="hidden" value="{{list}}"/>
    <input id="settingsSubmit" type="submit" value="Submit">
  </form>

</div>
</div>
</body>
</html>
