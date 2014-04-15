# -*- coding: utf-8 -*-
__version__ = "0.1.0"

from clint import arguments
import sys
import ConfigParser
config = ConfigParser.RawConfigParser()


# class Hipchat:
#     def __init__(self):
#         setup_hipchat()

#     def setup_hipchat(self):
        

def main():
    print("Executing hiptoslack version %s." % __version__)
    print("List of argument strings: %s" % arguments.Args())

    config.read('hiptoslack.cfg')
    print config.get('hipchat', 'token')


