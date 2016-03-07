from time import sleep
from hotdog.BasePage import HotDogBasePage
from hotdog.Retry import Retry

class CBCWebBase(HotDogBasePage):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def find(self, objectName, type=None):
        locators = getattr(self, objectName)
        element = self.driver.find_element(locators[0], locators[1], type=type)
        return element

    def back(self):
        self.driver.execute_script("window.history.go(-1)");

    def elemenent_exists(self, element):
        try:
            displayed = element.is_displayed()
            return True if displayed else False
        except:
            return False

    def sync(self, timeout=20):
        self.driver.implicitly_wait(timeout)
        if hasattr(self, 'syncElement'):
            self.find('syncElement')
        else:
            sleep(5)
        self.driver.implicitly_wait(30)

    @Retry
    def assert_element_exists(self, element, name):
        assert self.elemenent_exists(element), 'Element [%s] not found' % name

    @Retry
    def assert_in_url(self, string):
        assert string in self.driver.current_url, 'Did not load page with string [%]' % string