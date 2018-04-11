from Helpers.BaseTest import BaseTest
from Pages.AdminLandingPage import AdminLandingPage
from Pages.TitlesPage import TitlesPage
from Pages.NewTitlePage import NewTitlePage
from hotdog.TestStep import TestStep
from Tests.LoginPageTest import LoginPageTest
from time import sleep

class AddTitleTest(BaseTest):

    def test_title_header(self):

        LoginPageTest.test_login_header(self)
        LoginPageTest.test_login_to_bluesource(self)

        admin = AdminLandingPage(self.driver)
        titles = TitlesPage(self.driver)

        admin.sync()

        admin.admin_menu.click()
        admin.admin_menu_titles.click()

        titles.sync()

    def test_create_title(self):

        AddTitleTest.test_title_header(self)

        _title_name = 'Title23'

        titles = TitlesPage(self.driver)
        new_title = NewTitlePage(self.driver)

        titles.new_title()

        new_title.sync()

        create_title_step = TestStep('Verify title was created successfully.')
        new_title.title_name_textbox.send_keys(_title_name)
        new_title.create_title_btn.click()
        assert 'successfully' in titles.title_creation_msg.text, 'Title not created successfully'
        create_title_step('Complete')