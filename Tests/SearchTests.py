import time

from selenium.webdriver.common.by import By

from Elements.Checkbox import Checkbox
from Helpers.BaseTest import BaseTest
from Pages.Common import CommonPage, Checkboxes


class SearchTests(BaseTest):

    def test_contentDetailsElements(self):

        self.driver.debug = True
        self.driver.get('https://the-internet.herokuapp.com/checkboxes')

        common = CommonPage(driver=self.driver, url=self.page_url)
        common.sync()

        #Find single element untyped
        headerText = common.find_element(By.CSS_SELECTOR, '.example h3')
        headerText = common.find_element(by=By.CSS_SELECTOR, value='.example h3')
        headerText = common.find('headerText')
        headerText.click()

        #Find single element typed
        checkboxes = common.find_element(By.ID, 'checkboxes', Checkbox)
        checkboxes = common.find_element(by=By.ID, value='checkboxes', type=Checkboxes)
        checkboxes = common.Checkboxes

        #Find multiple elements untyped
        boxes = checkboxes.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        boxes = checkboxes.find_elements(by=By.CSS_SELECTOR, value="input[type='checkbox']")
        boxes = checkboxes.finds('checkboxesLoc')
        boxes = checkboxes.checkboxes

        #Find multiple elements typed
        boxes = checkboxes.find_elements(By.CSS_SELECTOR, "input[type='checkbox']", Checkbox)
        boxes = checkboxes.find_elements(by=By.CSS_SELECTOR, value="input[type='checkbox']", type=Checkbox)
        boxes = checkboxes.finds('checkboxesLoc')
        boxes = checkboxes.checkboxes

        for box in boxes:
            box.check()
            box.uncheck()
            assert not box.is_checked()

        seleniumLink = common.find('seleniumLink')
        seleniumLink.click()



