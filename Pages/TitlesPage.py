from time import sleep

from selenium.webdriver.common.by import By

from Elements.AdminMenuBar import AdminMenuBar
from Helpers.BasePage import BasePage


class TitlesPage(BasePage):

    _page_header = (By.TAG_NAME, 'h1')
    _admin_menu_bar = (By.CSS_SELECTOR, 'header.navbar', AdminMenuBar)
    _titles = (By.CSS_SELECTOR, 'tr > td')
    _edit_btns = (By.CSS_SELECTOR, '.pull-right')
    _delete_btns = (By.CSS_SELECTOR, '[data-method="delete"]')
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
    def titles(self):
        return self.finds('_titles')

    @property
    def edit_btns(self):
        return self.finds('_edit_btns')

    @property
    def delete_btns(self):
        return self.finds('_delete_btns')

    @property
    def new_title_btn(self):
        return self.find('_new_title_btn')

    @property
    def title_creation_msg(self):
        return self.find('_title_creation_msg')


    def new_title(self):
        sleep(2)
        self.new_title_btn.scroll_element_to_center().click()

    def verify_title_listed(self, query_title):
        sleep(2)
        titles = self.titles
        for title in titles:
            if query_title == title.text:
                return True
        return False

    def edit_title(self, title_name):
        sleep(2)
        titles = self.titles
        edit_btns = self.edit_btns
        title_names = []
        for title in titles:
            title_names.append(title.text)
        return edit_btns[title_names.index(title_name)]

    def delete_title(self, title_name):
        sleep(2)
        titles = self.titles
        delete_btns = self.delete_btns
        title_names = []
        for title in titles:
            title_names.append(title.text)
        return delete_btns[title_names.index(title_name)]