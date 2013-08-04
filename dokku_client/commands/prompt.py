from subprocess import call

from dokku_client.commands import BaseCommand

class PromptCommand(BaseCommand):
    """Open a prompt

    usage:
        dokku-client prompt [options]

    global options:
        [[include global options]]
    """
    
    def main(self):
        cmd = 'docker run -i -t app/%s /bin/bash' % self.args['--app']
        call_args = ['ssh', '-t', self.args['--host'], cmd]
        print "Running command: %s" % ' '.join(call_args)
        call(call_args)
