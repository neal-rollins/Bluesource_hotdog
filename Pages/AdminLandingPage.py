from selenium.webdriver.common.by import By

from Elements.AdminMenuBar import AdminMenuBar
from Helpers.BasePage import BasePage


class AdminLandingPage(BasePage):

    _page_header = (By.XPATH, '// *[ @ id = "ng-app"]')

    _admin_menu_bar = (By.CSS_SELECTOR, 'header.navbar', AdminMenuBar)

    _add_employee_btn = (By.CSS_SELECTOR, '#all-content > div.header-btn-section > div > div.btn-group.pull-right > button')
    _username_field = (By.ID, 'employee_username')
    _first_name_field = (By.ID, 'employee_first_name')
    _last_name_field = (By.ID, 'employee_last_name')
    _create_employee_btn = (By.NAME, 'commit')
    _employee_creation_msg = (By.CLASS_NAME, 'alert-success')
    _sync_element = _admin_menu_bar


    @property
    def admin_menu_bar(self):
        return self.find('_admin_menu_bar')

    @property
    def add_employee_btn(self):
        return self.find('_add_employee_btn')

    @property
    def username_field(self):
        return self.find('_employee_username')

    @property
    def first_name_field(self):
        return self.find('_employee_first_name')

    @property
    def last_name_field(self):
        return self.find('_employee_last_name')

    @property
    def create_employee_btn(self):
        return self.find('_create_employee_btn')

    @property
    def employee_creation_msg(self):
        return self.find('_employee_creation_msg')

    def add_employee(self):
        self.add_employee_btn.scroll_element_to_center().click()

    def create_employee(self):
        self.create_employee_btn.scroll_element_to_center().click()

    '''
    _admin_menu = (By.XPATH, '/html/body/header/div/nav/ul/li[1]')
    _admin_menu_departments = (By.XPATH, '/html/body/header/div/nav/ul/li[1]/ul/li/a[1]')
    _admin_menu_titles = (By.XPATH, '/html/body/header/div/nav/ul/li[1]/ul/li/a[2]')
    _admin_menu_email_users = (By.XPATH, '/html/body/header/div/nav/ul/li[1]/ul/li/a[3]')
    _message_center = (By.XPATH, '/html/body/header/div/nav/ul/li[2]')
    _calendar = (By.XPATH, '/html/body/header/div/nav/ul/li[3]')
    _calendar_menu_btn = (By.XPATH, '/html/body/header/div/nav/ul/li[4]/a') #must be clicked to access _calendar_reporting
    _calendar_reporting = (By.XPATH, '/html/body/header/div/nav/ul/li[4]/ul/li/a')
    _directory = (By.XPATH, '/html/body/header/div/nav/ul/li[5]')
    _projects = (By.XPATH, '/html/body/header/div/nav/ul/li[6]')
    _employees = (By.XPATH, '/html/body/header/div/nav/ul/li[7]')
    _logout = (By.XPATH, '/html/body/header/div/nav/ul/li[8]')
    _search_textbox = (By.CSS_SELECTOR, '#search-bar')
    _employee_table = (By.TAG_NAME, 'tbody', WebTable)

    _sync_element = _admin_menu

    @property
    def admin_menu(self):
        return self.find('_admin_menu')

    @property
    def admin_menu_departments(self):
        return self.find('_admin_menu_departments')

    @property
    def admin_menu_titles(self):
        return self.find('_admin_menu_titles')

    @property
    def admin_menu_email_users(self):
        return self.find('_admin_menu_email_users')

    @property
    def message_center(self):
        return self.find('_message_center')

    @property
    def calendar_menu(self):
        self.find('_calendar_menu')

    @property
    def calendar_menu_btn(self):
        self.find('_calendar_menu_btn')

    @property
    def calendar_reporting(self):
        self.find('_calendar_reporting')

    @property
    def directory(self):
        self.find('_directory')

    @property
    def projects(self):
        self.find('_projects')

    @property
    def employees(self):
        self.find('_employees')

    @property
    def logout(self):
        self.find('_logout')
        '''

    @property
    def search_textbox(self):
        self.finds('_search_textbox')

    @property
    def employee_table(self):
        self.find('_employee_table')