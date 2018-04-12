from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage
from Elements.AdminMenuBar import AdminMenuBar


class DeptPage(BasePage):

    _page_header = (By.XPATH, '//*[@id="content"]/h1')
    _admin_menu_bar = (By.CSS_SELECTOR, 'header.navbar', AdminMenuBar)
    _add_dept_btn = (By.XPATH, '//*[@id="content"]/a')
    _depts = (By.CLASS_NAME, 'list-group-item')
    _dept_creation_msg = (By.CSS_SELECTOR, '#content > div.alert.alert-success.alert-dismissable')

    _sync_element = _page_header

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
        return self.find('_dep_creation_msg')

    def add_new_dept(self):
        add_dept = self.find('_add_dept_btn')
        add_dept.scroll_element_to_center().click()

    def verify_dept_added(self, new_dept):
        depts = self.depts
        for dept in depts:
            return new_dept == dept.text()

