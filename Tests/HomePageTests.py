from Helpers.BaseTest import BaseTest
from Pages.HomePage import HomePage
from time import sleep

class HomePageTests(BaseTest):

    def test_page_header(self):
        home = HomePage(self.driver)

        self.driver.get(self.page_url)
        home.sync()

        assert home.page_header.is_displayed(),"Header was not displayed"
        print("Test Passed")

    def test_example_header(self):
        home = HomePage(self.driver)
        self.driver.get(self.page_url)
        home.sync()

        assert home.examples_header.is_displayed(),"Examples header was not displayed"
        print("Test Passed")
