<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="css/index.css">
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
            <a onclick="this.href='listSettings/{{row}}'"><span class="edit">✎</span></a>
        </li></a>
      </ul>
    %end
</div>
<div id="todo">
<div id="myDIV" class="header">
  <h2>{{list}} - Tâches</h2>
  <form action="/">
    <input id="inputTask" type="text" placeholder="Enter a task" value="">
    <input id="addTask" type="submit" value="Submit">
  </form>

</div>

%for row in rows:
  <ul id="myUL">
    <li>
        <a href="#"><input type="checkbox" /></a>
        {{row}}
        <a href="#"><span class="close">×</span></a>
        <a href="#"><span class="edit">✎</span></a>
    </li>
  </ul>
%end
</div>
</body>
</html>
