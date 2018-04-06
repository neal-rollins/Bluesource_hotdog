from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage
from Elements.WebTable import WebTable

class TablesPage(BasePage):

    _page_header = (By.TAG_NAME,'h3')
    _page_description = (By.XPATH,'//*[@id="content"]/div/p[1]')

    _example_headers = (By.TAG_NAME, 'h4')
    _example_descriptions = (By.TAG_NAME, 'p')

    _example_1_table = (By.ID,'table1', WebTable)
    _example_2_table = (By.ID,'table2', WebTable)


    @property
    def example_1_header(self):
        return self.finds('_example_headers')[0]

    @property
    def example_1_description(self):
        return self.finds('_example_descriptions')[1]

    @property
    def example_1_table(self):
        return self.find('_example_1_table')

    @property
    def example_2_header(self):
        return self.finds('_example_headers')[1]

    @property
    def example_2_description(self):
        return self.finds('_example_descriptions')[2]

    @property
    def example_2_table(self):
        return self.find('_example_2_table')
