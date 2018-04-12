from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage
from Elements.AdminMenuBar import AdminMenuBar


class TitlesPage(BasePage):

    _page_header = (By.TAG_NAME, 'h1')
    _admin_menu_bar = (By.CSS_SELECTOR, 'header.navbar', AdminMenuBar)
    _titles_listing_table = (By.CSS_SELECTOR, '#content > table')
    _table_rows = (By.TAG_NAME, 'tr')
    _new_title_btn = (By.CSS_SELECTOR, '#content > a')
    _title_creation_msg = (By.CLASS_NAME, 'alert-success')

    _sync_element = _page_header

    @property
    def page_header(self):
        return self.find('_page_header')

    @property
    def titles_listing_table(self):
        return self.find('_titles_listing_table')

    @property
    def table_rows(self):
        return self.finds('_table_rows')

    @property
    def new_title_btn(self):
        return self.find('_new_title_btn')

    @property
    def title_creation_msg(self):
        return self.find('_title_creation_msg')

    def new_title(self):
        self.new_title_btn.scroll_element_to_center().click()