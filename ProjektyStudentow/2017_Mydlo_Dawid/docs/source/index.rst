.. pet documentation master file, created by
   sphinx-quickstart on Thu Mar 30 11:52:45 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=============================
Pet: Project Environment Tool
=============================

.. raw:: html

    <iframe src="https://showterm.io/5ce94c75126066ac40688#fast" width="640" height="480"></iframe>

Quickstart
==========

.. _installation-guide:

Installation
------------

To install |pet|, open an interactive shell and run:

.. code::

    bash -c "$(curl -fsSL https://raw.githubusercontent.com/limebrains/pet/master/install.bash)"

Or to specify installation directory and type of shell:

.. code::

    bash -c "shell='bash_or_zsh';install_dir='absolute_path';$(curl -fsSL https://raw.githubusercontent.com/limebrains/pet/master/install.bash)"

Using Pet
---------

To start using |pet|, you need to first create a project:

.. code::

    $ pet init

.. note::

    If name for new project is not passed |pet| uses current directory name.
    To use custom name invoke it with ``pet init -n chosen_name``

It will edit two files `start.sh` and `stop.sh` which commands are going to
be executed accordingly during start of project and after closing

If you want to start project:

.. code::

    pet project_name

Now you are in subshell created using your standard files (like `.bashrc` or `.profile`)
and `start.sh`

User Guide
==========

Here you can read more about how |pet| works.

This part provides examples of use and explores all |pet| commands and its possibilities.

.. toctree::
    :maxdepth: 3

    user/index

.. toctree::
    :maxdepth: 2

    modules/index

Indices and tables
==================

* :ref:`genindex`
