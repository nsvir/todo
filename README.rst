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

   sudo pip install -r requirements.txt

Or if you have no root permissions:

.. code:: bash

   pip install -r requirements.txt --user
   

Launching
-----------

.. code:: bash

   python ./src/main.py

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
