from subprocess import call

from dokku_client.commands import BaseCommand

class PromptCommand(BaseCommand):
    """Open a prompt

    usage:
        dokku-client prompt [options]

    global options:
        [[include global options]]
    """
    
    def main(self, args):
        cmd = 'docker run -i -t app/%s /bin/bash' % args['--app']
        call_args = ['ssh', '-t', args['--host'], cmd]
        print "Running command: %s" % ' '.join(call_args)
        call(call_args)
