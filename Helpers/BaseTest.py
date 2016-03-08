from hotdog.Config import GetConfig
import os
import time
from Helpers.FilePath import get_full_path
from hotdog.Retry import Retry
os.environ['PROJECTFOLDER'] = get_full_path('')
import builtins
from hotdog.BaseTest import HotDogBaseTest


class BaseTest(HotDogBaseTest):

    page_url = GetConfig('APP_URL')

    @classmethod
    def setUpClass(cls):
        super().setUpClass(platform='desktop')

    def setUp(self):
        super().setUp()
        self.driver.implicitly_wait(30)

    def assertAlphabetical(self, list):
        for i in range(len(list)-1):
            assert list[i].lower() < list[i+1].lower(), 'Items not in alphabetical order.  Found entry [%s] before [%s]' % (list[i], list[i+1])

    @Retry
    def assert_in_url(self, string):
        assert string in self.driver.current_url, 'Did not load page with string [%]' % string


    def assert_element_exists(self, element, name, timeout=30):
        start = time.time()
        while True:
            try:
                assert element.is_displayed(), 'The element [%s] was not found' % name
                return True
            except:
                if time.time() - start > timeout:
                    raise

    @classmethod
    def RemoveApp(self):
        if 'mobile' in builtins.threadlocal.config['options']['provider']:
            try: builtins.threadlocal.driver.close_app()
            except: pass
            try: builtins.threadlocal.driver.remove_app(GetConfig('IOS_BUNDLE_ID'))
            except: pass
            try: builtins.threadlocal.driver.remove_app(GetConfig('ANDROID_BUNDLE_ID'))
            except: pass
        try: builtins.threadlocal.driver.quit()
        except: pass
        builtins.threadlocal.driver = None

    @Retry
    def assertEqual(self, first, second, msg=None):
        super().assertEqual(first, second, msg)