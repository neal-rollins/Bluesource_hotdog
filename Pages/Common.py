from time import sleep
from appium.webdriver.common.mobileby import MobileBy as By
from Helpers.BasePage import CBCWebBase
from hotdog.BaseElement import BaseElement
from Elements.Checkbox import Checkbox

class Checkboxes(BaseElement):

    checkboxesLoc = (By.CSS_SELECTOR, "input[type='checkbox']", Checkbox)

    @property
    def checkboxes(self):
        return self.finds('checkboxesLoc')

class CommonPage(CBCWebBase):

    headerText = (By.CSS_SELECTOR, '.example h3')
    checkboxLoc = (By.ID, 'checkboxes', Checkbox)
    seleniumLink = (By.LINK_TEXT, 'Elemental Selenium')

    @property
    def Checkboxes(self):
        return self.find('checkboxLoc', type=Checkboxes)
