#!/usr/bin/env python

from os.path import exists
from setuptools import setup, find_packages

from dokku_client import __version__

setup(
    name='dokku-client',
    version=__version__,
    author='Adam Charnock',
    author_email='adam@adamcharnock.com',
    packages=find_packages(),
    scripts=[],
    url='https://github.com/adamcharnock/dokku-client',
    license='MIT',
    description='Heroku-style command line interface for Dokku',
    long_description=open('README.rst').read() if exists("README.rst") else "",
    install_requires=[
        'docopt>=0.6.1',
        'sarge==0.1.1'
    ],
    entry_points={
        'dokku_client.commands': [
            'prompt = dokku_client.commands.prompt:PromptCommand',
            'help = dokku_client.commands.help:HelpCommand',
            'configset = dokku_client.commands.config:ConfigSetCommand',
            'configget = dokku_client.commands.config:ConfigGetCommand',
            'restart = dokku_client.commands.restart:RestartCommand',
        ],
        'console_scripts': [
            'dokku-client = dokku_client.client:main',
        ]
    }
)
