Heroku-like command line interface for `Dokku`_
===============================================

**Note:** This project is in the very early stages of development. 
You can help by adding commands (see below).

.. image:: https://badge.fury.io/py/dokku-client.png
    :target: https://badge.fury.io/py/dokku-client

.. image:: https://pypip.in/d/dokku-client/badge.png
    :target: https://pypi.python.org/pypi/dokku-client

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

        help       Show this help message
        configget  Set one or more config options
        configset  Set one or more config options in the app's ENV file
        prompt     Open a prompt
        restart    Restart the container

    See 'git help <command>' for more information on a specific command.

Contributing new commands
-------------------------

Dokku-client allows any developer to hook in extra commands. This is done using 
exactly the same mechanism that dokku-client uses internally, that of entry points
provided by ``setuptools``.

First, create a python package. You may have your own favorite way of doing this, but I 
use seed_:

.. code-block:: bash
    
    mkdir dokku-client-mycommand
    cd dokku-client-mycommand
    pip install seed
    seed create
    ls

Second, create a class which extends ``dokku_client.BaseCommand`` and implements the method
``main(args)``. Also, the doc-block at the top 
of the class will be used by docopt_ to parse any command line arguments, so make 
sure you include that. See the `prompt command`_ for an example.

And third, in your new ``setup.py`` file, specify your new class as an entry point:

.. code-block:: python

    entry_points={
        'dokku_client.commands': [
            'mycommand = dokku_client_mycommand.mycommand:MyCommand',
        ],
    }

Run ``setup.py`` so that the new entry point is initialized:

.. code-block:: bash
    
    # Run in develop mode, so files will not be copied away.
    # You can continue to edit your code as usual
    python setup.py develop

You should now find that your new command is available in dokku-client, 
run ``dokku-client help`` to check.

Once done, you can release your package to PyPi using ``seed release --initial``.

.. _Dokku: https://github.com/progrium/dokku
.. _docopt: http://docopt.org/
.. _prompt command: https://github.com/adamcharnock/dokku-client/blob/master/dokku_client/commands/prompt.py
.. _seed: https://github.com/adamcharnock/seed
