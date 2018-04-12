from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage
from Elements.AdminMenuBar import AdminMenuBar

class TitlesPage(BasePage):

    _page_header = (By.TAG_NAME, 'h1')
    _admin_menu_bar = (By.CSS_SELECTOR, 'header.navbar', AdminMenuBar)
    _titles_listing_table = (By.CSS_SELECTOR, '#content > table')
    _table_rows = (By.TAG_NAME, 'tr')
    _new_title_btn = (By.CSS_SELECTOR, '#content > a')
    _first_title_listed = (By.CSS_SELECTOR, '#content > table > tbody > tr:nth-child(1) > td')
    _edit_btn_first_title_listed = (By.CSS_SELECTOR, '#content > table > tbody > tr:nth-child(1) > td > div > a:nth-child(1)')
    _delete_btn_first_title_listed = (By.CSS_SELECTOR, '#content > table > tbody > tr:nth-child(1) > td > div > a:nth-child(2)')
    _title_creation_msg = (By.CSS_SELECTOR, '#content > div')

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
    def first_title_listed(self):
        return self.find('_first_title_listed')

    @property
    def edit_btn_first_title_listed(self):
        return self.find('_edit_btn_first_title_listed')

    @property
    def delete_btn_first_title_listed(self):
        return self.find('_delete_btn_first_title_listed')

    @property
    def title_creation_msg(self):
        return self.find('_title_creation_msg')

    def new_title(self):
        self.new_title_btn.scroll_element_to_center().click()

    def search_table(self, search):
        rows = self.titles_listing_table.find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            return search == row.find_element_by_tag_name('td').text

#content > table > tbody > tr:nth-child(1) > td > div > a:nth-child(1)
#content > table > tbody > tr:nth-child(2) > td > div > a:nth-child(1)