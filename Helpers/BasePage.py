from hotdog.BasePage import HotDogBasePage
import webium

webium.settings.implicit_timeout = 30

class CBCWebBase(HotDogBasePage):

    def __init__(self, *args, **kwargs):
        webium.settings.implicit_timeout = 30
        super().__init__(*args, **kwargs)

    def back(self):
        self.driver.execute_script("window.history.go(-1)");