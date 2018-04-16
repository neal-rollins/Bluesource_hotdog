from time import sleep

from selenium.webdriver.common.by import By

from Elements.AdminMenuBar import AdminMenuBar
from Helpers.BasePage import BasePage


class DeptPage(BasePage):

    _page_header = (By.XPATH, '//*[@id="content"]/h1')
    _admin_menu_bar = (By.CSS_SELECTOR, 'header.navbar', AdminMenuBar)
    _add_dept_btn = (By.XPATH, '//*[@id="content"]/a')
    _depts = (By.CLASS_NAME,'list-group')
    _edit_btns = (By.CSS_SELECTOR, '.pull-right')
    _delete_btns = (By.CSS_SELECTOR, '[data-method="delete"]')
    _dept_creation_msg = (By.CLASS_NAME, 'alert-success')
    _sync_element = _add_dept_btn


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
    def edit_btns(self):
        return self.finds('_edit_btns')

    @property
    def delete_btns(self):
        return self.finds('_delete_btns')

    @property
    def dept_creation_msg(self):
        return self.find('_dept_creation_msg')

    def add_new_dept(self):
        self.add_dept_btn.scroll_element_to_center().click()

    def verify_dept_listed(self, query_dept):
        sleep(3)
        depts = self.depts
        for dept in depts:
            #account for nested dept by looping on '/n'
            if '\n' in dept.text:
                sub_dept_names = dept.text.splitlines()
                for sub_dept_name in sub_dept_names:
                    if query_dept == sub_dept_name[:-18]:
                        return True
            elif query_dept == dept.text[:-18]:
                        return True
        return False


    def get_dept_index(self, dept_name):
        sleep(3)
        depts = self.depts
        dept_names = []
        for dept in depts:
            dept_names.append(dept.text[:-18])
        return dept_names.index(dept_name)


    def edit_dept(self, dept_name):
        sleep(3)
        depts = self.depts
        edit_btns = self.edit_btns
        dept_names = []
        for dept in depts:
            # account for nested dept by looping on '/n'
            if '\n' in dept.text:
                sub_dept_names = dept.text.splitlines()
                for sub_dept_name in sub_dept_names:
                    dept_names.append(sub_dept_name[:-18])
            else:
                dept_names.append(dept.text[:-18])
        return edit_btns[dept_names.index(dept_name)]

    def delete_dept(self, dept_name):
        sleep(3)
        depts = self.depts
        delete_btns = self.delete_btns
        dept_names = []
        for dept in depts:
            # account for nested dept by looping on '/n'
            if '\n' in dept.text:
                sub_dept_names = dept.text.splitlines()
                for sub_dept_name in sub_dept_names:
                    dept_names.append(sub_dept_name[:-18])
            else:
                dept_names.append(dept.text[:-18])

        return delete_btns[dept_names.index(dept_name)]




