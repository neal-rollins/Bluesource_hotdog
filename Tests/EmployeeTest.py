import random
from time import sleep

from hotdog.Config import GetConfig
from hotdog.TestStep import TestStep
from selenium.webdriver.support.ui import Select

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
        _title_name = GetConfig('TITLE')

        #_new_username = GetConfig('NEW_USERNAME')
        # _employee_first_name = GetConfig('FIRST_NAME')
        # _employee_last_name = GetConfig('LAST_NAME')

        _employee_username = 'Username_%d' % (random.randint(0, 9999))
        _employee_first_name = 'First_%d' % (random.randint(0, 9999))
        _employee_last_name = 'Last_%d' % (random.randint(0, 9999))
        _employee_cell_phone = '(804) %d-%d' % (random.randint(290, 999), random.randint(1000, 9999))
        _name_string = '%s %s' % (_employee_first_name, _employee_last_name)
        _search_string = '%s, %s, %s' % (_employee_first_name, _employee_last_name, _employee_cell_phone)

        login_to_bluesource(self, _username, _password)
        admin.sync()

        add_new_employee_step = TestStep('Attempt to add a new employee')

        admin.add_employee()

        admin.modal_username_field.send_keys(_employee_username)
        admin.modal_first_name_field.send_keys(_employee_first_name)
        admin.modal_last_name_field.send_keys(_employee_last_name)

        admin.modal_titles_drop_down.scroll_element_to_center()
        select_titles = Select(admin.modal_titles_drop_down)
        select_titles.select_by_visible_text(_title_name)

        admin.modal_cell_phone_field.scroll_element_to_center().send_keys(_employee_cell_phone)

        admin.modal_depts_drop_down.scroll_element_to_center()
        select_depts = Select(admin.modal_depts_drop_down)
        select_depts.select_by_visible_text(_dept_name)

        admin.create_employee()
        admin.sync()

        # cant locate search bar
        # admin.search_bar
        # admin.search_bar.send_keys(_name_string)
        sleep(5)

        admin.verify_employee(_employee_first_name, _employee_last_name, _employee_cell_phone)

        assert admin.action_success_msg.is_displayed(), 'Employee was not successfully created'

        add_new_employee_step('Complete')

    def test_edit_employee(self):

        admin = AdminLandingPage(self.driver)

        _username = GetConfig('COMPANY_ADMIN')
        _password = GetConfig('PASSWORD')
        _dept_name = GetConfig('DEPT_NAME')
        _title_name = GetConfig('TITLE')

        _employee_username = 'Username_%d' % (random.randint(0, 9999))
        _employee_first_name = 'First_%d' % (random.randint(0, 9999))
        _employee_last_name = 'Last_%d' % (random.randint(0, 9999))
        _employee_cell_phone = '(804) %d-%d' % (random.randint(290, 999), random.randint(1000, 9999))

        _name_string = '%s %s' % (_employee_first_name, _employee_last_name)
        _search_string = '%s, %s, %s' % (_employee_first_name, _employee_last_name, _employee_cell_phone)

        login_to_bluesource(self, _username, _password)
        admin.sync()

        assert admin.verify_employee('6', '5', '(804) 749-2525'), 'Employee is not listed.'

