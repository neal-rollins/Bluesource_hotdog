from time import sleep

from hotdog.BasePage import HotDogBasePage
import webium
from selenium.webdriver.common.by import By
from webium import Find

webium.settings.implicit_timeout = 30

class CBCWebBase(HotDogBasePage):

    def __init__(self, *args, **kwargs):
        webium.settings.implicit_timeout = 30
        super().__init__(*args, **kwargs)

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
            Find(by=self.syncElement[0], value=self.syncElement[1], context=self)
        else:
            sleep(5)
        self.driver.implicitly_wait(webium.settings.implicit_timeout)