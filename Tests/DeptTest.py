import random
from time import sleep

from hotdog.Config import GetConfig
from hotdog.TestStep import TestStep

from Helpers.BaseTest import BaseTest
from Pages.AdminLandingPage import AdminLandingPage
from Pages.DeptDetails import DeptDetails
from Pages.DeptPage import DeptPage
from Steps.CommonSteps import login_to_bluesource


class DeptTest(BaseTest):

    _dept_name = "Dept_%d" % (random.randint(0, 9999))

    def test_add_dept(self):

        admin = AdminLandingPage(self.driver)
        dept = DeptPage(self.driver)
        dept_details = DeptDetails(self.driver)

        _username = GetConfig('COMPANY_ADMIN')
        _password = GetConfig('PASSWORD')
        #_dept_name = "Dept_%d" % (random.randint(0, 9999))

        login_to_bluesource(self, _username, _password)
        admin.sync()

        add_new_dept_step = TestStep('Attempt to add a new department')
        admin.admin_menu_bar.navigate_department()
        dept.sync()

        dept.add_dept_btn.scroll_element_to_center().click()
        dept_details.sync()

        dept_details.name_textbox.send_keys(self._dept_name)
        dept_details.commit_dept_btn.click()
        dept.sync()

        assert dept.dept_creation_msg.is_displayed(), 'Department not created successfully'

        print(self._dept_name)
        dept.verify_dept_listed(self._dept_name)

        add_new_dept_step('Complete')

    def test_edit_dept(self):

        admin = AdminLandingPage(self.driver)
        dept = DeptPage(self.driver)
        dept_details = DeptDetails(self.driver)

        _username = GetConfig('COMPANY_ADMIN')
        _password = GetConfig('PASSWORD')
        _dept_name = GetConfig('DEPT_NAME')

        updated_dept_name = "Dept_%d" % (random.randint(0, 9999))

        login_to_bluesource(self, _username, _password)
        admin.sync()

        # Find specified dept and modify its name
        edit_dept_test = TestStep("Attempt to edit a department.")

        admin.admin_menu_bar.navigate_department()
        dept.edit_dept(_dept_name).scroll_element_to_center().click()
        dept_details.sync()

        dept_details.name_textbox.clear()
        dept_details.name_textbox.send_keys(updated_dept_name)
        dept_details.commit_dept_btn.click()
        assert dept.verify_dept_listed(updated_dept_name), 'Department not edited successfully.'

        edit_dept_test('Complete')

    def test_delete_dept(self):

        admin = AdminLandingPage(self.driver)
        dept = DeptPage(self.driver)

        _username = GetConfig('COMPANY_ADMIN')
        _password = GetConfig('PASSWORD')
        _dept_name = GetConfig('DEPT_NAME')

        login_to_bluesource(self, _username, _password)
        admin.sync()

        # Find specified dept and delete it
        delete_dept_test = TestStep("Attempt to delete a department.")

        admin.admin_menu_bar.navigate_department()
        admin.sync()

        dept.delete_dept(self._dept_name).scroll_element_to_center().click()
        sleep(1)

        self.driver.switch_to.alert.accept()

        assert dept.verify_dept_listed(_dept_name), 'Department was not successfully deleted.'

        delete_dept_test("Complete")