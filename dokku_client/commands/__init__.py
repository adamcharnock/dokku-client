import re

from sarge import capture_stdout, run

from dokku_client.command_tools import global_opts_doc

class BaseCommand(object):
    check_config = True
    sort_order = 10

    def __init__(self, name):
        self._name = name
        # Set externally in client.py
        self.args = {}

    @property
    def doc(self):
        """Get the docs for this command

        The docs are used for display purposes, but also by 
        docopt (which uses them to the parse command line options)
        """

        doc = self.__doc__
        # Unindent by one level
        doc = re.sub(r'^( {4}|\t)', '',  doc, flags=re.MULTILINE)
        # Put the global options in place
        doc = re.sub(r'\s+\[\[include global options\]\]', "\n\n%s" % global_opts_doc(), doc)
        return doc

    @property
    def description(self):
        return self.__doc__.strip().split("\n")[0]

    @property
    def name(self):
        return self._name

    def main(self, global_args, command_args):
        raise NotImplementedError('Implement the main() method to implement your command')

    def run_remote(self, cmd, input=None):
        host = self.args['--host']
        return capture_stdout('ssh %s -- %s' % (host, cmd), input=input)

    def restart_container(self):
        app = self.args['--app']
        self.run_remote('docker restart `cat /home/git/%s/CONTAINER`' % app)
