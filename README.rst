.. default-role:: code

=====================================
  TODO LIST
=====================================


.. contents:: Table of contents:
   :local:
   :depth: 2

Introduction
============

Execution
=========

Install dependencies
--------------------

.. code:: bash
   pip install -r requirements.txt

   sudo pip install -r requirements.txt

Or if you have no root permissions:

.. code:: bash

   pip --pre install -r requirements.txt --user


Launching
-----------

.. code:: bash

   python ./src/main.py


Launching unit test and coverage
-----------

.. code:: bash

  nosetests --with-coverage --cover-erase --cover-branches --with-doctest test

  nosetests --with-coverage --cover-erase --cover-branches --with-doctest --cover-package=somme -v test/test_somme.py



Acceptance Test
===============

.. code:: bash

   python -m robot README.rst

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

   *** Test Case ***
   User can add a List
    When he writes a list
    And he clicks submit
    Then he see the list in the list

   *** Keywords ***
   He write a list
   He click submit
   He see the list in the list
