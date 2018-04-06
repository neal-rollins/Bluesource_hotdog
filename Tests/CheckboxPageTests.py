from Helpers.BaseTest import BaseTest
from Pages.Common import CommonPage


class CheckboxPageTests(BaseTest):

    def test_elements_verification(self):
        self.driver.get('https://the-internet.herokuapp.com/checkboxes')

        common = CommonPage(driver=self.driver)
        common.sync()

        home = HomePage(driver=self.driver)
        page_header = home.page_header()


        # Get the checkboxes
        boxes = common.get_checkboxes()

        # Verify the checkboxes work properly
        for box in boxes:
            box.check()
            box.uncheck()
            assert not box.is_checked()

        # Verify the Elemental Link
        selenium_link = common.find('selenium_link')
        selenium_link.click()
        common.sync()

        self.driver.switch_to_window(self.driver.window_handles[-1])

        self.assertTrue('elementalselenium.com' in self.driver.current_url)


