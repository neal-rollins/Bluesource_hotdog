from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage
from Elements.AdminMenuBar import AdminMenuBar
from Elements.WebTable import WebTable


class AdminLandingPage(BasePage):

    _page_header = (By.XPATH, '// *[ @ id = "ng-app"]')

    _admin_menu_bar = (By.CSS_SELECTOR, 'header.navbar', AdminMenuBar)

    @property
    def admin_menu_bar(self):
        return self.find('_admin_menu_bar')

    @property
    def departments(self):
        return self.find(self)



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