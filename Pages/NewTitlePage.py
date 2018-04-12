from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage
from Elements.AdminMenuBar import AdminMenuBar


class NewTitlePage(BasePage):

    _page_header = (By.CSS_SELECTOR, '#content > h1')
    _admin_menu_bar = (By.CSS_SELECTOR, 'header.navbar', AdminMenuBar)
    _title_name_textbox = (By.CSS_SELECTOR, '#title_name')
    _create_title_btn = (By.CSS_SELECTOR, '#new_title > div.actions > input')

    _sync_element = _page_header

    @property
    def page_header(self):
        return self.find('_page_header')

    @property
    def title_name_textbox(self):
        return self.find('_title_name_textbox')

    @property
    def create_title_btn(self):
        return self.find('_create_title_btn')

