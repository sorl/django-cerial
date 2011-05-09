#!/usr/bin/env python
import imp
import os
import sys
from django.core.management import execute_manager
from os.path import abspath, dirname, join as pjoin
try:
    imp.find_module('settings') # Assumed to be in the same directory.
except ImportError:
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

here = abspath(dirname(__file__))
sys.path.append(pjoin(here, os.pardir, os.pardir))

import settings

if __name__ == "__main__":
    execute_manager(settings)
