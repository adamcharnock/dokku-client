import re

from dokku_client.command_tools import global_opts_doc

class BaseCommand(object):
    check_config = True

    def __init__(self, name, *args, **kwargs):
        super(BaseCommand, self).__init__(*args, **kwargs)
        self._name = name

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