from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage

class NewTitlePage(BasePage):

    _page_header = (By.CSS_SELECTOR, '#content > h1')
    _title_name_textbox = (By.CSS_SELECTOR, '#title_name')
    _create_title_btn = (By.CSS_SELECTOR, '#new_title > div.actions > input')

    @property
    def page_header(self):
        return self.find('_page_header')

    @property
    def title_name_textbox(self):
        return self.find('_title_name_textbox')

    @property
    def create_title_btn(self):
        return self.find('_create_title_btn')

