from Pages.LoginPage import LoginPage
from Pages.AdminLandingPage import AdminLandingPage


def login_to_bluesource(self, username, password):

    # assign driver and navigate to url
    home = LoginPage(self.driver)
    self.driver.get(self.page_url)
    home.sync()

    # input username and password and submit
    home.username_textbox.send_keys(username)
    home.password_textbox.send_keys(password)
    home.submit_login()

    # verify AdminLandingPage is displayed
    admin = AdminLandingPage(self.driver)
    admin.sync()