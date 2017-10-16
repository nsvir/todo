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
        <li>
            {{row}}
            <a onclick="this.href='deleteList/{{row}}'"><span class="close" name="delete_list_{{row}}">×</span></a>
            <a onclick="this.href='listSettings/{{row}}'"><span class="edit" name="list_{{row}}">✎</span></a>
        </li>
      </ul>
    %end
</div>
<div id="todo">
<div id="myDIV" class="header">
  <h2>{{list}} - Tâches</h2>
  <input type="text" id="inputTask" name="inputTask" placeholder="Enter a Task">
  <select name="selectList" id="selectList">
    %for row in lists:
      <option value="{{row}}">{{row}}</option>
    %end
  </select>
  <a onclick="this.href='addTask/'+document.getElementById('inputTask').value + '/'+ document.getElementById('selectList').value">
    <input type="button" id="addTask" value="Add Task">
  </a>
</div>

%for task in tasks:
  <ul id="myUL">
    <li>
        <a href="taskDone/{{task.name()}}"><input id="done{{task.name()}}" type="checkbox"
          %if task.done():
            checked="checked" disabled="disabled"
          %end
          /></a>
        {{task.listname()}} - {{task.name()}}
        <a href="removeTask/{{task.name()}}"><span id="remove{{task.name()}}" class="close">x</span></a>
        <a href="updateTask/{{task.name()}}"><span id="update{{task.name()}}" class="edit">✎</span></a>
    </li>
  </ul>
%end
</div>
</body>
</html>
