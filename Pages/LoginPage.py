from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage

class LoginPage(BasePage):

    _page_header = (By.TAG_NAME, 'h1')

    _username_textbox = (By.ID, 'employee_username')
    _password_textbox = (By.ID, 'employee_password')

    _login_btn = (By.NAME, 'commit')

    _sync_element = _page_header

    @property
    def page_header(self):
        return self.find('_page_header')

    @property
    def username_textbox(self):
        return self.find('_username_textbox')

    @property
    def password_textbox(self):
        return self.find('_password_textbox')

    def submit_login(self):
        submit_login_info = self.find('_login_btn')
        submit_login_info.click()






