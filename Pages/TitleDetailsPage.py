from selenium.webdriver.common.by import By

from Elements.AdminMenuBar import AdminMenuBar
from Helpers.BasePage import BasePage


class TitleDetailsPage(BasePage):

    _page_header = (By.CSS_SELECTOR, '#content > h1')
    _admin_menu_bar = (By.CSS_SELECTOR, 'header.navbar', AdminMenuBar)
    _title_name_textbox = (By.CSS_SELECTOR, '#title_name')
    _commit_title_btn = (By.CSS_SELECTOR, 'input[type="submit"]')

    _sync_element = _page_header

    @property
    def page_header(self):
        return self.find('_page_header')

    @property
    def title_name_textbox(self):
        return self.find('_title_name_textbox')

    @property
    def commit_title_btn(self):
        return self.find('_commit_title_btn')

