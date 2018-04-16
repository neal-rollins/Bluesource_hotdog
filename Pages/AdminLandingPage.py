from selenium.webdriver.common.by import By

from Elements.AdminMenuBar import AdminMenuBar
from Helpers.BasePage import BasePage


class AdminLandingPage(BasePage):

    _page_header = (By.XPATH, '// *[ @ id = "ng-app"]')

    _admin_menu_bar = (By.CSS_SELECTOR, 'header.navbar', AdminMenuBar)

    _add_employee_btn = (By.CSS_SELECTOR, '#all-content > div.header-btn-section > div > div.btn-group.pull-right > button')
    _username_field = (By.ID, 'employee_username')
    _first_name_field = (By.ID, 'employee_first_name')
    _last_name_field = (By.ID, 'employee_last_name')
    _create_employee_btn = (By.NAME, 'commit')
    _employee_creation_msg = (By.CLASS_NAME, 'alert-success')
    _sync_element = _admin_menu_bar


    @property
    def admin_menu_bar(self):
        return self.find('_admin_menu_bar')

    @property
    def add_employee_btn(self):
        return self.find('_add_employee_btn')

    @property
    def username_field(self):
        return self.find('_username_field')

    @property
    def first_name_field(self):
        return self.find('_first_name_field')

    @property
    def last_name_field(self):
        return self.find('_last_name_field')

    @property
    def create_employee_btn(self):
        return self.find('_create_employee_btn')

    @property
    def employee_creation_msg(self):
        return self.find('_employee_creation_msg')

    def add_employee(self):
        self.add_employee_btn.scroll_element_to_center().click()

    def create_employee(self):
        self.create_employee_btn.scroll_element_to_center().click()

    @property
    def search_textbox(self):
        self.finds('_search_textbox')

    @property
    def employee_table(self):
        self.find('_employee_table')