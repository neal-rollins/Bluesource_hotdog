from Helpers.BaseTest import BaseTest
from Pages.AdminLandingPage import AdminLandingPage
from Tests.LoginPageTest import LoginPageTest
from hotdog.TestStep import TestStep

class EmployeeTableTest(BaseTest):

    def test_employee_table(self):

        table = AdminLandingPage(self.driver)

        LoginPageTest.test_login_to_bluesource(self)

        extract_first_names_step = TestStep('Attempt to extract first names from visible table')
        first_names = table.employee_table.get_first_names()

        for name in first_names:
            print(name)