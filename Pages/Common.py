from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage
from Elements.Checkbox import Checkbox

class CommonPage(BasePage):

    header_text = (By.CSS_SELECTOR, '.example h3')
    checkboxes = (By.CSS_SELECTOR, 'input', Checkbox)
    selenium_link = (By.LINK_TEXT, 'Elemental Selenium')

    def get_checkboxes(self):
        checkboxes = self.finds('checkboxes')
        return checkboxes