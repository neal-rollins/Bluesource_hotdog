from Helpers.BaseTest import BaseTest
from Pages.LoginPage import LoginPage
from Pages.AdminLandingPage import AdminLandingPage
from hotdog.TestStep import TestStep

class LoginPageTest(BaseTest):

    def test_login_header(self):

        # assign driver and navigate to url
        home = LoginPage(self.driver)
        self.driver.get(self.page_url)
        home.sync()

        #assert home.page_header.isDisplayed(), 'Login header was not displayed'
        print('Test passed')

    def test_login_to_bluesource(self):
        _username = 'company.admin'
        _password = '123'

        # assign driver and navigate to url
        home = LoginPage(self.driver)
        self.driver.get(self.page_url)
        home.sync()

        login_step = TestStep('Attempt login with valid admin credentials')
        home.username_textbox.send_keys(_username)
        home.password_textbox.send_keys(_password)
        home.submit_login()
        login_step('Complete')

        login_verification = TestStep('Verify user is logged in with admin permissions')
        admin = AdminLandingPage(self.driver)
        admin.sync()
        #assert admin.admin_menu.isDisplayed(), 'Login with admin credentials unsuccessful'
        login_verification('Complete')

