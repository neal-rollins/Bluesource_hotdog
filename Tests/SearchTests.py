import time
from Helpers.BaseTest import BaseTest
from Pages.Common import CommonPage

class SearchTests(BaseTest):

    def test_contentDetailsElements(self):

        self.driver.debug = True
        self.driver.get('https://the-internet.herokuapp.com/checkboxes')

        common = CommonPage(driver=self.driver, url=self.page_url)
        common.sync()

        headerText = common.find('headerText')
        headerText.click()

        box1  = common.Checkboxes.find('checkbox1')
        box1.check()
        box1.uncheck()
        assert not box1.is_checked()

        seleniumLink = common.find('seleniumLink')
        seleniumLink.click()



