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
  visible boolean
);
