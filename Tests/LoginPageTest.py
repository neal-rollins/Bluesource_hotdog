from Helpers.BaseTest import BaseTest
from Helpers.CommonFunctions import CommonFunctions
from Pages.AdminLandingPage import AdminLandingPage
from hotdog.TestStep import TestStep
from hotdog.Config import GetConfig


class LoginPageTest(BaseTest):

    def test_login_to_bluesource(self):

        _username = GetConfig('COMPANY_ADMIN')
        _password = GetConfig('PASSWORD')

        login_step = TestStep('Attempt login with valid admin credentials')
        CommonFunctions.login_to_bluesource(self, _username, _password)
        login_step('Complete')

        login_verification = TestStep('Verify user is logged in with admin permissions')
        admin = AdminLandingPage(self.driver)
        admin.sync()
        login_verification('Complete')
