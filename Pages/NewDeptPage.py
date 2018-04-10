from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage

class NewDeptPage(BasePage):

    _new_dept_form = (By.XPATH, '//*[@id="new_department"]')

    _name_textbox = (By.XPATH, '//*[@id="department_name"]')
    _parent_dept_textbox = (By.NAME, 'department[department_id]')
    _minimum_hour_increment = (By.XPATH, '//*[@id="department_minimum_hour_increment"]')
    _alt_approver = (By.XPATH, '//*[@id="department_alternate_approver_id"]')
    _create_dept = (By.XPATH, '//*[@id="new_department"]/div[6]/input')

    _sync_element = _new_dept_form

    @property
    def new_dept_form(self):
        return self.find('_new_dept_form')

    @property
    def name_textbox(self):
        return self.find('_name_textbox')

    @property
    def parent_dept_textbox(self):
        return self.find('_parent_dept_textbox')

    @property
    def minimum_hour_increment(self):
        return self.find('_minimum_hour_increment')

    @property
    def alt_approver(self):
        return self.find('_alt_approver')

    @property
    def create_dept(self):
        return self.find('_create_dept')