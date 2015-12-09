import os

from hotdog.Config import GetConfig
from sauceclient import SauceClient
import sys
from Helpers.FilePath import get_full_path
os.environ['PROJECTFOLDER'] = get_full_path('')

import builtins
import threading
from appium_selector.DeviceSelector import DeviceSelector
from hotdog.BaseTest import HotDogBaseTest


class BaseTest(HotDogBaseTest):

    page_url = GetConfig('APP_URL')

    @classmethod
    def setUpClass(cls):
        if not hasattr(builtins, 'threadlocal'):
            builtins.threadlocal = threading.local()
            builtins.threadlocal.config = DeviceSelector(platform='desktop').getDevice()[0]

    def setUp(self):
        super().setUp()
        self.driver.implicitly_wait(30)

    def assertAlphabetical(self, list):
        for i in range(len(list)-1):
            assert list[i].lower() < list[i+1].lower(), 'Items not in alphabetical order.  Found entry [%s] before [%s]' % (list[i], list[i+1])

    def assert_element_exists(self, element, name):
        assert element.is_displayed(), 'The element [%s] was not found' % name



