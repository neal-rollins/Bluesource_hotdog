from Pages.TitlesPage import TitlesPage
from Pages.NewTitlePage import NewTitlePage
from Helpers.BaseTest import BaseTest
from hotdog.Config import GetConfig
from hotdog.TestStep import TestStep


class AddTitleTest(BaseTest):

    def test_create_title(self):

        titles = TitlesPage(self.driver)
        new_title = NewTitlePage(self.driver)

        _title_name = GetConfig('TITLE')

        create_title_step = TestStep('Verify title was created successfully.')
        titles.new_title()
        new_title.sync()
        new_title.title_name_textbox.send_keys(_title_name)
        new_title.create_title_btn.click()
        assert titles.title_creation_msg, 'Title not created successfully'
        create_title_step('Complete')