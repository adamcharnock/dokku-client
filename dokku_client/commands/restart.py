from subprocess import call

from dokku_client.commands import BaseCommand

class RestartCommand(BaseCommand):
    """Restart the container

    usage:
        dokku-client restart [options]

    global options:
        [[include global options]]
    """
    
    def main(self):
        self.restart_container()
