=======
Editing
=======

To edit project, task or locales you can use *edit* command.

Using edit
==========

*edit* command helps you edit project or task if there is
active project or edit project if non is active

.. code::

    # edits task
    [project] $ pet edit task_name
    # edits current project
    [project] $ pet edit
    # edits project
    $ pet edit project_name

It opens accordingly task file or `start.sh` and `stop.sh` in $EDITOR

To edit locals you can use:

.. code::

    [project] $ pet edit task_name -l
    # or
    $ pet edit project_name -l
