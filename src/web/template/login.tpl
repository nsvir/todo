<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="css/index.css">
  <title>SuperTodo Application</title>
</head>
<body>

<div id="identification">

{{status}}

  <form onSubmit="this.action = 'submitLogin'" id="loginForm" method="post">
    <input type="text" id="login" name="login" placeholder="Login">
    <input type="password" id="password" name="password" placeholder="Mot de passe">
    <input id="loginSubmit" type="submit" value="Submit" name="login_submit">
  </form>
</div>
</body>
</html>
