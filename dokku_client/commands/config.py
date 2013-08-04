import re

from dokku_client.commands import BaseCommand

class ConfigSetCommand(BaseCommand):
    """Set one or more config options in the app's ENV file

    usage:
        dokku-client configset [options] (<KEY>=<VALUE>)...

    global options:
        [[include global options]]
    """

    def main(self):
        key_values = dict([kv.split('=') for kv in self.args['<KEY>=<VALUE>']])
        app = self.args['--app']

        self.run_remote('sudo -u git touch /home/git/%s/ENV' % app)
        p = self.run_remote('sudo -u git cat /home/git/%s/ENV' % app)
        env = p.stdout.text.strip()
        lines = env.split("\n")
        # For each line in the form 'export KEY=...'
        for i, line in enumerate(lines):
            matches = re.match('^export (.*?)=', line)
            if matches:
                key = matches.group(1)
                # If the key has been specified, then replace the line
                if key in key_values:
                    lines[i] = 'export %s="%s"' % (key, key_values[key])
                    del key_values[key]

        # Now append the remaining lnes
        for key, value in key_values.items():
            lines.append('export %s=%s' % (key, value))

        env = "\n".join(lines)
        self.run_remote('sudo -u git tee /home/git/python-django-sample/ENV', input=env)

        print "Config set, resting container"
        self.restart_container()


class ConfigGetCommand(BaseCommand):
    """Set one or more config options

    usage:
        dokku-client configget [options]

    global options:
        [[include global options]]
    """

    def main(self):
        app = self.args['--app']
        p = self.run_remote('sudo -u git cat /home/git/%s/ENV' % app)
        env = p.stdout.text.strip()
        print env