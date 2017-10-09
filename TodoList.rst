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

Requierement
------------

Bottle installed and in PYTHONPATH variable
.. code:: bash
   $pip install --target=<installed_directory> bottle
   $export PYTHONPATH=<installed_directory>


Launching
-----------

.. code:: bash
   $python ./src/main.py

Acceptance Test
===============

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
