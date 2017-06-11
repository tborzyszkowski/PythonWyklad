=============
Creating task
=============

To create task you need to activate project first, than use
*task* command.

Using task
==========

Running *task* command will make a script that will be available
during use of a project.

You can specify what type of a file it's going to be, but name of
a task is understood as name of a file without extension.

If extension is not provided it will create `.sh` file.

You have to choose is this task going to be normal or local by using
either -s/ --save or -l/ --local flag.

Local tasks are stored with additional '.local' in their names

You might want to use local tasks if you are sharing pet project in repository.

.. code::

    [project] $ pet task task_name -s
    # or
    [project] $ pet task task_name.extension -s
    # or
    [project] $ pet task task_name -l
    # or
    [project] $ pet task task_name.extension -l

This opens task file in $EDITOR to let you edit it.

You can change file extension freely

Task without alias
==================

If you don't want to create alias to task eg. because it have a
name of shell command you can use -a flag.

.. code::

    [project] $ pet task task_name -s -a

Running task
============

To run a task you can do it from within project:

.. code::

    [project] $ pet task_name
    # or by using alias (if -a flag was not used) during every next invocation of a project
    [project] $ task_name

To run it from outside of a project you have to perform:

.. code::

    $ pet run project_name task_name
