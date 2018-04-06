from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage

class HomePage(BasePage):

    _heading = (By.CLASS_NAME, 'heading')
    _examples_header = (By.TAG_NAME,'h2')

    _sortable_data_table = (By.XPATH,'//*[@id="content"]/ul/li[36]/a')

    sync_element = _heading

    @property
    def page_header(self):
        return self.find('_heading')

    @property
    def examples_header(self):
        return self.find('_examples_header')


    def navigate_to_data_table_page(self):
        navigation_link = self.find('_sortable_data_table')
        navigation_link.scroll_element_to_center().click()