import re
import os
import pkg_resources

def load_commands():
    commands = []
    for entry_point in pkg_resources.iter_entry_points(group='dokku_client.commands'):
        command_class = entry_point.load()
        command = command_class(name=entry_point.name)
        commands.append(command)
    commands = sorted(commands, key=lambda c: (c.sort_order, c.name))
    return commands

def command_list_doc(commands=None):
    commands = commands or load_commands()

    doc = "full list of available commands:\n\n"
    names = []
    descriptions = []

    for command in commands:
        names.append(command.name)
        descriptions.append(command.description)

    name_col_length = max(len(n) for n in names)
    for name, description in zip(names, descriptions):
        doc += "    %s  %s\n" % (name.ljust(name_col_length), description)

    return doc.strip()

def root_doc(commands=None):
    from dokku_client import client
    doc = client.__doc__.replace('----', command_list_doc())
    return doc.strip()


def command_by_name(name, commands=None):
    commands = commands or load_commands()
    for command in commands:
        if command.name == name:
            return command
    return None

def global_opts_doc():
    from dokku_client import client
    lines = client.__doc__.split("\n")
    lines = filter(lambda l: re.match(r'\s*-[a-zA-Z].*', l), lines)
    return "\n".join(lines)

def apply_defaults(args):
    for key, val in args.items():
        if not val:
            env_var = 'DOKKU_%s' % key.replace('--', '').upper()
            if os.environ.get(env_var):
                args[key] = os.environ.get(env_var).strip()
    return args


