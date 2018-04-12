from hotdog.BaseElement import BaseElement
from selenium.webdriver.common.by import By


class AdminMenuBar(BaseElement):

    _dropdown_menus = (By.CLASS_NAME, 'dropdown') #admin and calendar
    _admin_menu_departments = (By.CSS_SELECTOR, '.dropdown-menu a[href="/admin/departments"]')
    _admin_menu_titles = (By.CSS_SELECTOR, '.dropdown-menu a[href="/admin/titles"]')
    _admin_menu_email_users = (By.CSS_SELECTOR, 'a[data-target="#email_all_modal"]')
    _message_center = (By.CSS_SELECTOR, 'a[data-target="#notification_modal"]')
    _calendar = (By.CSS_SELECTOR, 'a[href="/calendar]')
    _calendar_menu_reporting = (By.CSS_SELECTOR, 'a[data-target="#vacation_reporting_modal"]')
    _directory = (By.CSS_SELECTOR, 'a[href="/directory"]')
    _projects = (By.CSS_SELECTOR, 'a[href="/projects"]')
    _employees = (By.CSS_SELECTOR, 'a[href="/employees"]')
    _logout = (By.CSS_SELECTOR, 'a[href="/logout"]')

    @property
    def admin_menu(self):
        return self.finds('_dropdown_menus')[0]

    @property
    def calendar_menu(self):
        return self.finds('dropdown_menus')[1]

    @property
    def admin_menu_departments(self):
        return self.find('_admin_menu_departments')

    @property
    def admin_menu_titles(self):
        return self.find('_admin_menu_titles')

    @property
    def message_center(self):
        return self.find('_message_center')

    @property
    def calendar(self):
        return self.find('_calendar')

    @property
    def reporting(self):
        return self.find('_reporting')

    @property
    def directory(self):
        return self.find('_directory')

    @property
    def projects(self):
        return self.find('_projects')

    @property
    def employees(self):
        return self.find('_employees')

    @property
    def logout(self):
        return self.find('_logout')

    def navigate_department(self):
        self.admin_menu.click()
        self.admin_menu_departments.click()

    def navigate_titles(self):
        self.admin_menu.click()
        self.admin_menu_titles.click()

    def navigate_reporting(self):
        self.calendar_menu.click()
        self._calendar_menu_reporting.click()