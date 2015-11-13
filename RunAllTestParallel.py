import os
import itertools
from Helpers.FilePath import get_full_path
import unittest
from nose.core import collector
import threading
import builtins

os.environ['PROJECTFOLDER'] = get_full_path('')

from appium_selector.DeviceSelector import DeviceSelector





os.environ['AddMustard'] = 'True'


builtins.threadlocal = threading.local()

def run_all_test(device=None, test=None):
    builtins.threadlocal.config = device
    runner = unittest.TextTestRunner()
    runner.run(test)

threads =[]
loader = unittest.TestLoader()
tests = loader.discover('./Tests', pattern='*Tests.py')
devices = DeviceSelector(True).getDevice()

for test in itertools.product(tests, devices):
        t = threading.Thread(target=run_all_test, args=[test[1], test[0]])
        threads.append(t)
        t.start()

