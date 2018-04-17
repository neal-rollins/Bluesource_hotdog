import random

from hotdog.Config import GetConfig
from hotdog.TestStep import TestStep

from Helpers.BaseTest import BaseTest
from Pages.AdminLandingPage import AdminLandingPage
from Pages.TitleDetailsPage import TitleDetailsPage
from Pages.TitlesPage import TitlesPage
from Steps.CommonSteps import login_to_bluesource


class TitlesTests(BaseTest):

    _title_name = "Title_%d" % (random.randint(0, 9999))
    _updated_title_name = "Title_%d" % (random.randint(0, 9999))

    def test_create_title(self):

        admin = AdminLandingPage(self.driver)
        titles = TitlesPage(self.driver)
        new_title = TitleDetailsPage(self.driver)

        _username = GetConfig('COMPANY_ADMIN')
        _password = GetConfig('PASSWORD')

        login_to_bluesource(self, _username, _password)
        admin.sync()

        create_title_step = TestStep('Attempt to create a title.')

        admin.admin_menu_bar.navigate_titles()
        titles.sync()

        titles.new_title()
        new_title.sync()

        new_title.title_name_textbox.send_keys(TitlesTests._title_name)
        new_title.commit_title_btn.click()
        titles.sync()

        assert titles.action_success_msg, 'Title not created successfully'
        assert titles.verify_title_listed(TitlesTests._title_name), 'Title not listed'

        create_title_step('Complete')

    def test_edit_title(self):

        admin = AdminLandingPage(self.driver)
        titles = TitlesPage(self.driver)
        edit_title = TitleDetailsPage(self.driver)

        _username = GetConfig('COMPANY_ADMIN')
        _password = GetConfig('PASSWORD')

        login_to_bluesource(self, _username, _password)
        admin.sync()

        edit_title_step = TestStep('Attempt to edit a title.')

        admin.admin_menu_bar.navigate_titles()
        titles.sync()

        assert titles.verify_title_listed(TitlesTests._title_name), 'Specified title not listed.'

        titles.edit_title(TitlesTests._title_name).scroll_element_to_center().click()
        edit_title.sync()

        edit_title.title_name_textbox.clear().send_keys(TitlesTests._updated_title_name)
        edit_title.commit_title_btn.click()
        titles.sync

        assert titles.action_success_msg, 'Title not edited successfully.'
        assert titles.verify_title_listed(TitlesTests._updated_title_name), 'Edited title not listed.'

        edit_title_step('Complete')

    def test_delete_title(self):

        admin = AdminLandingPage(self.driver)
        titles = TitlesPage(self.driver)
        delete_title = TitleDetailsPage(self.driver)

        _username = GetConfig('COMPANY_ADMIN')
        _password = GetConfig('PASSWORD')

        login_to_bluesource(self, _username, _password)
        admin.sync()

        delete_title_step = TestStep('Attempt to delete a title.')

        admin.admin_menu_bar.navigate_titles()
        titles.sync()

        assert titles.verify_title_listed(TitlesTests._updated_title_name), 'Specified title not listed.'

        titles.delete_title(TitlesTests._updated_title_name).scroll_element_to_center().click()
        self.driver.switch_to.alert.accept()
        titles.sync()

        assert titles.action_success_msg, 'Title not deleted successfully.'
        assert not(titles.verify_title_listed(TitlesTests._updated_title_name)), 'Specified title is still listed'

        delete_title_step('Complete')













