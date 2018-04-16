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

    def test_create_title(self):

        admin = AdminLandingPage(self.driver)
        titles = TitlesPage(self.driver)
        new_title = TitleDetailsPage(self.driver)

        _username = GetConfig('COMPANY_ADMIN')
        _password = GetConfig('PASSWORD')

        login_to_bluesource(self, _username, _password)
        admin.sync()

        create_title_step = TestStep('Verify title was created successfully.')

        admin.admin_menu_bar.navigate_titles()
        titles.sync()

        titles.new_title()
        new_title.sync()

        new_title.title_name_textbox.send_keys(TitlesTests._title_name)
        new_title.commit_title_btn.click()
        titles.sync()

        assert titles.title_creation_msg, 'Title not created successfully'
        assert titles.verify_title_listed(TitlesTests._title_name), 'Title not listed'

        create_title_step('Complete')

    def test_edit_title(self):

        admin = AdminLandingPage(self.driver)
        titles = TitlesPage(self.driver)
        edit_title = TitleDetailsPage(self.driver)

        _username = GetConfig('COMPANY_ADMIN')
        _password = GetConfig('PASSWORD')
        _updated_title_name = "Title_%d" % (random.randint(0, 9999))

        login_to_bluesource(self, _username, _password)
        admin.sync()

        edit_title_step = TestStep('Verify title was successfully edited.')

        admin.admin_menu_bar.navigate_titles()
        titles.sync()

        assert titles.verify_title_listed('3Fzja6Ve19RTitle_9874'), 'Title not listed.'

        titles.edit_title('3Fzja6Ve19RTitle_9874').scroll_element_to_center().click()
        edit_title.sync()

        edit_title.title_name_textbox.clear().send_keys(_updated_title_name)
        edit_title.commit_title_btn.click()
        titles.sync

        assert titles.title_creation_msg, 'Title not created successfully.'
        assert titles.verify_title_listed(_updated_title_name), 'Title not listed.'

        edit_title_step('Complete')






