from Helpers.BaseTest import BaseTest
from Helpers.CommonFunctions import CommonFunctions
from Pages.AdminLandingPage import AdminLandingPage
from Pages.DeptPage import DeptPage
from Pages.NewDeptPage import NewDeptPage
from hotdog.TestStep import TestStep
from hotdog.Config import GetConfig
from selenium.webdriver.support.ui import Select
from time import sleep


class AddDeptTest(BaseTest):

    def test_add_dept(self):

        admin = AdminLandingPage(self.driver)
        dept = DeptPage(self.driver)
        new_dept = NewDeptPage(self.driver)

        _username = GetConfig('COMPANY_ADMIN')
        _password = GetConfig('PASSWORD')
        _dept_name = GetConfig('DEPT_NAME')

        CommonFunctions.login_to_bluesource(self, _username, _password)
        admin.sync()

        add_new_dept_step = TestStep('Attempt to add a new department')
        admin.admin_menu_bar.navigate_department()
        dept.sync()
        dept.add_dept_btn.scroll_element_to_center().click()
        new_dept.sync()
        new_dept.name_textbox.send_keys(_dept_name)
        new_dept.create_dept.click()
        dept.sync()
        assert dept.dept_creation_msg.is_displayed, 'Department not created successfully'
        print(dept.verify_dept_added(_dept_name))
        add_new_dept_step('Complete')