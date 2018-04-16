from selenium.webdriver.common.by import By

from Helpers.BasePage import BasePage


class EmployeesPage(BasePage):

    _employees_per_page_label = (By.CLASS_NAME, 'edit_employee')
    _search_bar = (By.ID, 'search-bar')
    _employees_table = (By.TAG_NAME, 'tbody')
    _table_header = (By.TAG_NAME, 'tr > th')
    _table_rows = (By.TAG_NAME, 'tr')

    _sync_element = _employees_per_page_label

    # resource-content > div.table-responsive > table > tbody > tr:nth-child(2)
    # resource-content > div.table-responsive > table > tbody > tr:nth-child(3)


    @property
    def employees_per_page(self):
        return self.find('_employees_per_page')

    @property
    def search_bar(self):
        return self.find('_search_bar')

    @property
    def table_headers(self):
        return self.finds('_table_header')

    @property
    def table_rows(self):
        return self.finds('_table_rows')

    @property
    def first_name_header(self):
        return self.table_headers[0]

    @property
    def last_name_header(self):
        return self.table_headers[1]

    @property
    def first_names(self):
        return self.finds('_table_columns')[0]

    def search_full_name(self, first_name, last_name):
        rows_on_page = self.table_rows
        first_name = []
        last_name = []
        for row_on_page in rows_on_page:
            first_name.append(row_on_page.text)
            #last_name.append(row_on_page.text)

        return True

