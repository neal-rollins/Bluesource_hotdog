from Helpers.BaseTest import BaseTest
from Pages.LoginPage import LoginPage
from hotdog.TestStep import TestStep

class LoginPageTest(BaseTest):

    def login_to_bluesource(self):
        _username = 'company.admin'
        _password = '123'

        home = LoginPage(self.driver)

        #navigate to url defined in Config.xml
        self.driver.get(self.page_url)
        home.sync()

        ##pickup here
        login_step = TestStep('Attempt login with valid credentials')



