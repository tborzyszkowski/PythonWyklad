==================
Stopping a project
==================

To stop a project you can use `pet stop` or ^D, both work same way

Using stop
==========

*stop* sends SIGKILL to current shell.

Commands in `stop.sh` are executed before exiting a project by using
``trap 'source /path/.../stop.sh' EXIT``

.. code::

    [project] $ pet stop
