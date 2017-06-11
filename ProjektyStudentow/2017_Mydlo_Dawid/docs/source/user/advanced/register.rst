========
Register
========

Registers current directory as folder with project configuration files for pet
if found all required files:

- `start.sh`

- `stop.sh`

- tasks (directory)

.. code::

    $ pet register

You can add it under specific name different than directory name by passing
parameter with -n flag

.. code::

    $ pet register -n project_name

This might be useful if you want to share same environment in shell for each
member of a project - just add it to git repository with your project.

Whenever someone makes changes you are going to be using same environment.

This is accomplished by adding symbolic link to folder with projects
