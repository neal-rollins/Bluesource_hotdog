from selenium.webdriver.common.by import By

from Helpers.BasePage import BasePage


class DeptDetails(BasePage):

    _name_textbox = (By.CSS_SELECTOR, '[type="text"]')
    _form = (By.CLASS_NAME, 'form-group')
    _commit_dept_btn = (By.CSS_SELECTOR, 'input[type="submit"]')

    _sync_element = _name_textbox

    @property
    def name_textbox(self):
        return self.find('_name_textbox')

    @property
    def forms(self):
        return self.finds('_form')

    @property
    def commit_dept_btn(self):
        return self.find('_commit_dept_btn')