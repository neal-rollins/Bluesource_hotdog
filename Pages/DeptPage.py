from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage

class DeptPage(BasePage):

    _page_header = (By.XPATH, '//*[@id="content"]/h1')
    _add_dept_btn = (By.XPATH, '//*[@id="content"]/a')

    _sync_element = _page_header

    @property
    def page_header(self):
        return self.find('_page_header')

    @property
    def add_dept_btn(self):
        return self.find('_add_dept_btn')

    def add_new_dept(self):
        add_dept = self.find('_add_dept_btn')
        add_dept.scroll_element_to_center().click()

