===================
Creation of project
===================

Init
====

You can create project by using ``pet init`` command.

This leads to creating `start.sh` and `stop.sh` files in which you can add all
the commands that should be run every time you start or stop project.

|Pet| uses current directory name as projects name if one is not provided.
You can provide one with use of ``-n`` flag:

.. code::

    pet init -n my_awesome_project

Create with templates
=====================

During creation you can specify which templates to use with ``-t`` flag.
Templates contain files that are going to be integrated to your project.

Basically it accumulates `start.sh` and `stop.sh` from every template
to your new project.

To do that execute:

.. code::

    $ pet init -t first_template -t secound_template...
    # or
    $ pet init -t=first_template,secound_template...

After accumulating commands from given templates it passes editing to you
with notes from which template which part of a code comes from.

Create in place
===============

You can create project and store it's files in .pet folder in project
directory by using -i flag. This can be very useful if you want to
share pet project with others by adding .pet folder to repository

.. code::

    $ pet init -i
