from Pages.LoginPage import LoginPage
from Pages.AdminLandingPage import AdminLandingPage
from Helpers.BaseTest import BaseTest
from hotdog.TestStep import TestStep
from Helpers.BasePage import BasePage
from Elements.AdminMenuBar import AdminMenuBar
from selenium.webdriver.common.by import By


class CommonFunctions(BaseTest):

    _admin_menu_bar = (By.CSS_SELECTOR, 'header.navbar', AdminMenuBar)

    def login_to_bluesource(self, username, password):

        # assign driver and navigate to url
        home = LoginPage(self.driver)
        self.driver.get(self.page_url)
        home.sync()

        home.username_textbox.send_keys(username)
        home.password_textbox.send_keys(password)
        home.submit_login()

        admin = AdminLandingPage(self.driver)
        admin.sync()