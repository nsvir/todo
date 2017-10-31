CREATE table lists (
name char(50),
desable int,
hour char(5),
hebdo int,
desable_hebdo int,
hour_hebdo char(5)
);

CREATE table tasks (

  name char(50),
  isDone boolean,
  listname char(50),
  visible boolean,
  login char(50)
);

CREATE table listtasks (
    listname char(50),
    login char(50)
);

CREATE table users (
    login char(50),
    password char(50)
);

insert into users values('test', 'test');
