===============
Configuring pet
===============

You can configure pet by using *config* command.

You can set:
- editor that is going to be used to edit files used by |pet|

- directory in which pet files are going to be stored

- files used to initialize shell (such as .bashrc or .profile)

Using config
============

.. code::

    $ pet config editor

Helps you set EDITOR variable in config file, this editor is
going to be used to edit files used by |pet|

.. code::

    $ pet config projects_folder

Informs you that pet stores files in directory that either is
equal to *PET_FOLDER* variable that can be exported in shell
profile file, if is unset uses ~/.pet folder

.. code::

    $ pet config shell

Helps you edit file that is going to be used to initialize
new shells
