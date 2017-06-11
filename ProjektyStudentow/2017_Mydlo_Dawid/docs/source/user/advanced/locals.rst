=================
Using local files
=================

If you want to use relative paths or have some additional
settings but eg. you share pet project in repository you can
achieve that by using *local* files.

Add `*.local*` to .gitignore to not share local files

Locals in projects
==================

Before executing `start.sh` and `stop.sh` pet looks for local
files for each of these files. If they exist they are used before
and after executing `start.sh` and `stop.sh`.

Workflow:
`start.local.entry.sh` -> `start.sh` -> `start.local.exit.sh`

*work*

`stop.local.entry.sh` -> `stop.sh` -> `stop.local.exit.sh`

To edit this files you can use:

.. code::

    $ pet edit project_name -l

Locals in tasks
===============

Before executing task file pet looks for `task_name.local.entry.sh`
and `task_name.local.exit.sh`. If they exits they are used before
and after executing task.

Workflow:
`start.local.entry.sh` -> `task` -> `start.local.exit.sh`

To edit this files you can use:

.. code::

    [project] $ pet edit task_name -l
