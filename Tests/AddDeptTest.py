from Helpers.BaseTest import BaseTest
#from Pages.LoginPage import LoginPage
from Pages.AdminLandingPage import AdminLandingPage
from Pages.DeptPage import DeptPage
from Pages.NewDeptPage import NewDeptPage
from hotdog.TestStep import TestStep
from Tests.LoginPageTest import LoginPageTest
#from selenium.webdriver.support.ui import Select
from time import sleep

class AddDeptTest(BaseTest):

    def test_admin_header(self):

        LoginPageTest.test_login_header(self)
        LoginPageTest.test_login_to_bluesource(self)

        admin = AdminLandingPage(self.driver)
        admin.sync()

        #assert admin.admin_menu.isDisplayed(), 'Admin menu was not displayed'
        print('Test passed')
        #sleep(2)

    def test_add_dept(self):

        self.test_admin_header()

        project_name = 'Rollins Project'
        parent_dept = 'ScarletFire' #value=1724

        admin = AdminLandingPage(self.driver)
        dept = DeptPage(self.driver)
        new_dept = NewDeptPage(self.driver)

        admin.sync()

        admin.admin_menu.click()
        admin.admin_menu_departments.click()

        #dept.sync()

        dept.add_dept_btn.scroll_element_to_center().click()

        ##issue - cannot interact with dropdown menu. element is identified but not clickable
        add_new_dept_step = TestStep('Attempt to add a new department')
        new_dept.sync()
        new_dept.name_textbox.send_keys(project_name)

        #select = Select(new_dept.parent_dept_textbox)
        #select.select_by_value(parent_dept)
        #select.select_by_visible_text(parent_dept)
        #sleep(2)

        menu = new_dept.parent_dept_textbox
        menu.scroll_element_to_center()
        menu.click()
        sleep(2)
        new_dept.create_dept.click()
        add_new_dept_step('Complete')