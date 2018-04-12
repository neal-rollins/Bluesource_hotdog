from Pages.AdminLandingPage import AdminLandingPage
from Helpers.BaseTest import BaseTest
from Steps.CommonSteps import login_to_bluesource
from hotdog.Config import GetConfig
from hotdog.TestStep import TestStep


class EmployeeTests(BaseTest):

    def test_add_employee(self):

        _username = GetConfig('COMPANY_ADMIN')
        _password = GetConfig('PASSWORD')
        _dept_name = GetConfig('DEPT_NAME')
        _new_username = GetConfig('NEW_USERNAME')
        _employee_first_name = GetConfig('FIRST_NAME')
        _employee_last_name = GetConfig('LAST_NAME')

        admin = AdminLandingPage(self.driver)

        login_to_bluesource(self, _username, _password)
        admin.sync()

        add_new_employee_step = ('Attempt to add a new employee')

        admin.add_employee()

        admin.username_field.send_keys(_new_username)
        admin.first_name_field.send_keys(_employee_first_name)
        admin.last_name_field.send_keys(_employee_last_name)

        admin.create_employee()

        assert admin.employee_creation_msg.is_displayed(), 'Employee was not successfully created'

        add_new_employee_step('Complete')