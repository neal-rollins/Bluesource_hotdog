from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage

class TitlesPage(BasePage):

    _page_header = (By.TAG_NAME, 'h1')

    _table = (By.CSS_SELECTOR, '#content > table')
    _new_title_btn = (By.CSS_SELECTOR, '#content > a')
    _first_title_listed = (By.CSS_SELECTOR, '#content > table > tbody > tr:nth-child(1) > td')
    _edit_btn_first_title_listed = (By.CSS_SELECTOR, '#content > table > tbody > tr:nth-child(1) > td > div > a:nth-child(1)')
    _delete_btn_first_title_listed = (By.CSS_SELECTOR, '#content > table > tbody > tr:nth-child(1) > td > div > a:nth-child(2)')

    _sync_element = _page_header

    @property
    def page_header(self):
        return self.find('_page_header')

    @property
    def new_title_btn(self):
        return self.find('_new_title_btn')

    @property
    def first_title_listed(self):
        return self.find('_first_title_listed')

    @property
    def edit_btn_first_title_listed(self):
        return self.find('_edit_btn_first_title_listed')

    @property
    def delete_btn_first_title_listed(self):
        return self.find('_delete_btn_first_title_listed')

    def new_title(self):
        self._new_title_btn.scroll_element_to_center().click()




