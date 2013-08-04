import sys

from dokku_client import client
from dokku_client.commands import BaseCommand
from dokku_client.command_tools import command_by_name, root_doc

class HelpCommand(BaseCommand):
    """Show this help message

    usage:
        dokku-client help [COMMAND]
    """
    check_config = False
    sort_order = 5
    
    def main(self):
        if not self.args['COMMAND']:
            print root_doc()
        else:
            command = command_by_name(self.args['COMMAND'])
            if not command:
                sys.stderr.write("Unknown command. Use 'dokku-client help' for list of commands.\n")
            else:
                print command.doc
