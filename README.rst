.. default-role:: code

=====================================
  TODO LIST
=====================================


.. contents:: Table of contents:
   :local:
   :depth: 2

Introduction
============

TodoList with multiple functionalities
Add a list and add multiple tasks
We can check task to stop it and we can remove it
We can change name of task 
For each list, we can configure time and at the end, the task is removed or is invisible


Execution
=========

Before, database should be created with file in src/db/create.sql

Install dependencies
--------------------

This project use python3!

.. code:: bash
   pip3 install -r requirements.txt

   sudo pip3 install -r requirements.txt

Or if you have no root permissions:

.. code:: bash

   pip3 --pre install -r requirements.txt --user


Launching
-----------

.. code:: bash

   python ./src/main.py


Launching unit test and coverage
-----------

.. code:: bash

  nosetests --with-coverage --cover-erase --cover-branches --with-doctest --cover-html test

.. code:: bash

  nosetests --with-coverage --cover-erase --cover-branches --with-doctest --cover-package=somme -v test/test_somme.py

Acceptance Test
===============

.. code:: bash

   python -m robot acceptance/

.. code:: robotframework

   *** Test Case ***
   User can add a Task
	  When she write a task
	  And she click submit
	  Then she see the task in the list

   *** Keywords ***
   She write a task
   She click submit
   She see the task in the list


Architecture
============

.. code:: bash

	src
	├── controller	(manage the routes and redirect to the service; initialized in init.py)
	├── db		(directory of the database used by repository)
	├── model	(objects representing the data)
	├── repository	(function to save the data in the database)
	├── service	(function doing the work)
	└── web		(static pages: css / templates / etc.)
