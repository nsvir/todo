<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="css/index.css">
</head>
<body>

<div id="menu">
    <h3>Listes</h3>
        <input type="text" id="inputListe" placeholder="Nouvelle Liste">
    <a onclick="this.href='addList/'+document.getElementById('inputListe').value"><span class="addBtn" id="addList">+</span></a>
    </br>
    %for row in lists:
      <ul id="myList">
        <a href="#"><li>
            {{row}}
            <a href="#"><span class="close">×</span></a>
        </li></a>
      </ul>
    %end
</div>
<div id="todo">
<div id="myDIV" class="header">
  <h2>{{list}} - Tâches</h2>
  <input type="text" id="myInput" placeholder="Nouvelle Tâche">
  <a href="#"><span class="addBtn">+</span></a>
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
