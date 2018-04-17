from selenium.webdriver.common.by import By

from Elements.AdminMenuBar import AdminMenuBar
from Helpers.BasePage import BasePage


class AdminLandingPage(BasePage):

    _admin_menu_bar = (By.CSS_SELECTOR, 'header.navbar', AdminMenuBar)

    _action_success_msg = (By.CLASS_NAME, 'alert-success')
    _search_bar = (By.ID, 'search-bar')
    _search_bar = (By.CSS_SELECTOR, '[type="text"]')
    _add_employee_btn = (By.CSS_SELECTOR, '#all-content>div.header-btn-section>div>div.btn-group.pull-right>button')
    _modal_username_field = (By.ID, 'employee_username')
    _modal_first_name_field = (By.ID, 'employee_first_name')
    _modal_last_name_field = (By.ID, 'employee_last_name')
    _modal_cell_phone_field = (By.ID, 'employee_cell_phone')
    _modal_drop_downs = (By.CLASS_NAME, 'form-control')
    _modal_commit_employee_btn = (By.NAME, 'commit')

    _employee_table_headers = (By.CSS_SELECTOR, 'tr > th')
    _table_cells = (By.CSS_SELECTOR, 'tr > td')

    _sync_element = _admin_menu_bar

    _search_result = None


    @property
    def admin_menu_bar(self):
        return self.find('_admin_menu_bar')

    @property
    def action_success_msg(self):
        return self.find('_action_success_msg')

    @property
    def search_bar(self):
        self.find('_search_bar')

    @property
    def add_employee_btn(self):
        return self.find('_add_employee_btn')

    @property
    def modal_username_field(self):
        return self.find('_modal_username_field')

    @property
    def modal_first_name_field(self):
        return self.find('_modal_first_name_field')

    @property
    def modal_last_name_field(self):
        return self.find('_modal_last_name_field')

    @property
    def modal_cell_phone_field(self):
        return self.find('_modal_cell_phone_field')

    @property
    def modal_drop_downs(self):
        return self.finds('_modal_drop_downs')

    @property
    def modal_titles_drop_down(self):
        return self.modal_drop_downs[5]

    @property
    def modal_depts_drop_down(self):
        return self.modal_drop_downs[17]

    @property
    def modal_commit_employee_btn(self):
        return self.find('_modal_commit_employee_btn')

    @property
    def employee_table(self):
        self.find('_employee_table')

    @property
    def employee_table_headers(self):
        return self.finds('_employee_table_headers')

    @property
    def first_name_header(self):
        self.employee_table_headers[1]

    @property
    def last_name_header(self):
        self.employee_table_headers[2]

    @property
    def table_cells(self):
        return self.finds('_table_cells')

    def add_employee(self):
        self.add_employee_btn.scroll_element_to_center().click()

    def create_employee(self):
        self.modal_commit_employee_btn.scroll_element_to_center().click()

    def verify_employee(self, first_name, last_name, cell_phone):
        cells = self.table_cells
        cells_length = len(cells)
        num_rows = cells_length / 11
        i = 26

        while i < num_rows:
            fname_cell = cells[(i * 11)]
            lname_cell = cells[(i * 11) + 1]
            cell_phone_cell = cells[(i * 11) + 9]
            if first_name == fname_cell.text and last_name == lname_cell.text and cell_phone == cell_phone_cell.text:
                print(cells[(i * 11)].text + ' ' + cells[(i * 11) + 1].text + ' ' + cells[(i * 11) + 9].text)
                AdminLandingPage._search_result = fname_cell
                return True
                break
            i += 1

    def edit_employee(self):
        AdminLandingPage._search_result.click()