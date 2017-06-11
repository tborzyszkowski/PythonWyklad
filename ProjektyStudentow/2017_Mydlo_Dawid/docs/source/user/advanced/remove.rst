========
Deletion
========

To delete project, task or locks you can use *remove* command.

Using remove
============

*remove* command if given name removes task if there is active
project or removes project if non is active, also can be used
to delete all lock files that prevent from initializing
project too many times.

.. code::

    [project] $ pet remove task_name
    # or
    $ pet remove project_name
    # delete locks
    $ pet remove -l
