from Helpers.BasePage import BasePage
from Elements.AdminMenuBar import AdminMenuBar
from selenium.webdriver.common.by import By


class DeptPage(BasePage):

    #_page_header = (By.XPATH, '//*[@id="content"]/h1')
    _admin_menu_bar = (By.CSS_SELECTOR, 'header.navbar', AdminMenuBar)
    _add_dept_btn = (By.XPATH, '//*[@id="content"]/a')
    _depts = (By.CLASS_NAME, 'list-group-item')
    _dept_creation_msg = (By.CLASS_NAME, 'alert-success')

    _sync_element = _admin_menu_bar

    @property
    def page_header(self):
        return self.find('_page_header')

    @property
    def add_dept_btn(self):
        return self.find('_add_dept_btn')

    @property
    def depts(self):
        return self.finds('_depts')

    @property
    def dept_creation_msg(self):
        return self.find('_dept_creation_msg')

    def add_new_dept(self):
        self.add_dept_btn.scroll_element_to_center().click()

    def verify_dept_added(self, new_dept):
        depts = self.depts
        for dept in depts:
            if new_dept == dept.text():
                return True
        return False

