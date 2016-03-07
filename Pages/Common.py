from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from Helpers.BasePage import CBCWebBase
from hotdog.BaseElement import BaseElement

class Checkboxes(BaseElement):

    checkbox1 = (By.CSS_SELECTOR, "input[type='checkbox']")


class CommonPage(CBCWebBase):

    checkboxLoc = (By.ID, 'checkboxes')
    seleniumLink = (By.LINK_TEXT, 'Elemental Selenium')

    @property
    def Checkboxes(self):
        return self.find('checkboxLoc', type=Checkboxes)



