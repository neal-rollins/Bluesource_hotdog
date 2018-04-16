import random
from time import sleep

from hotdog.Config import GetConfig
from hotdog.TestStep import TestStep

from Helpers.BaseTest import BaseTest
from Pages.AdminLandingPage import AdminLandingPage
from Pages.EmployeesPage import EmployeesPage
from Steps.CommonSteps import login_to_bluesource


class EmployeeTests(BaseTest):

    def test_add_employee(self):

        admin = AdminLandingPage(self.driver)
        employees = EmployeesPage(self.driver)

        _username = GetConfig('COMPANY_ADMIN')
        _password = GetConfig('PASSWORD')
        _dept_name = GetConfig('DEPT_NAME')
        #_new_username = GetConfig('NEW_USERNAME')
        _new_username = "Username_%d" % (random.randint(0, 9999))
        #_employee_first_name = GetConfig('FIRST_NAME')
        _employee_first_name = "First_%d" % (random.randint(0, 9999))
        #_employee_last_name = GetConfig('LAST_NAME')
        _employee_last_name = "Last_%d" % (random.randint(0, 9999))

        login_to_bluesource(self, _username, _password)
        admin.sync()

        add_new_employee_step = TestStep('Attempt to add a new employee')

        admin.add_employee()
        sleep(3)

        admin.username_field.send_keys(_new_username)
        admin.first_name_field.send_keys(_employee_first_name)
        admin.last_name_field.send_keys(_employee_last_name)

        admin.create_employee()
        sleep(3)

        employees.search_full_name('_employee_first_name', '_employee_last_name')

        assert admin.employee_creation_msg.is_displayed(), 'Employee was not successfully created'

        add_new_employee_step('Complete')