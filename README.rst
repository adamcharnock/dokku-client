Heroku-like command line interface for Dokku
============================================

**Note:** This project is in the very early stages of development. 
You can help by adding commands (see below)

Installation
------------

.. code-block:: bash

    pip install dokku-client

Configuration
-------------

You can specify the Dokku host & app on the command line, but you may 
find it convenient to set the following environment variables instead:

.. code-block:: bash

    export DOKKU_HOST=ubuntu@myserver.com
    export DOKKU_APP=my-app-name

Setting these variables in your virtualenv's `postactivate` hook may 
be useful.

Usage
-----

Once installed, usage is simple:

.. code-block:: bash

    dokku-client help

Produces:

.. code-block:: none

    Client for Dokku

    usage:
        dokku-client <command> [<args>...]
        dokku-client help

    global options:
        -H <host>, --host=<host>      Host address
        -a <app>, --app=<app>         App name

    full list of available commands:

        prompt  Open a prompt
        help    Show this help message

    See 'git help <command>' for more information on a specific command.
