#! /usr/bin/env python
"""Client for Dokku

usage:
    dokku-client <command> [<args>...]
    dokku-client help

global options:
    -H <host>, --host=<host>      Host address
    -a <app>, --app=<app>         App name

----

See 'git help <command>' for more information on a specific command.
"""
import sys
from subprocess import call

from docopt import docopt

from dokku_client import __version__
from dokku_client.command_tools import load_commands, command_by_name, apply_defaults, root_doc


def main():
    commands = load_commands()

    args = docopt(root_doc(), version='dokku-client version %s' % __version__, options_first=True)
    command_name = args['<command>'] or 'help'

    if command_name == 'version':
        # docopt will handle version printing for us if use '--version'
        exit(call(['dokku-client', '--version']))

    # Get the command object for the specified command name
    command = command_by_name(command_name, commands)
    if not command:
        sys.stderr.write("Unknown command. Use 'dokku-client help' for list of commands.\n")
        exit(1)
    else:
        # Use docopt to parse the options based upon the class' doc string
        command_args = docopt(command.doc)
        # Load default values from the users' environment
        command_args = apply_defaults(command_args)
        if command.check_config:
            # Sanity check the config
            if not command_args.get('--host', None):
                sys.stderr.write("Could not determine host. Specify --host or set DOKKU_HOST.\n")
                exit(1)
            if not command_args.get('--app', None):
                sys.stderr.write("Could not determine app. Specify --app or set DOKKU_APP.\n")
                exit(1)
        # Ok, let's run the command
        command.args = command_args
        command.main()

if __name__ == '__main__':
    main()