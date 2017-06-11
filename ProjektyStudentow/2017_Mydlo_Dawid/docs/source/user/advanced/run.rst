=================================
Running a task outside of project
=================================

To run task outside of a project you can use *run* command

Using run
=========

Run command runs task from a project in projects environment.

It is run in subshell.

To stay in shell after task is completed you can use `-i` flag
which stands for interactive mod

.. code::

    $ pet run project_name task_name
    # or
    $ pet run project_name task_name -i
