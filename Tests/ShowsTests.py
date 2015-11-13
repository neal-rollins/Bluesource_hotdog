from time import sleep
from Helpers.BaseTest import BaseTest
from Pages.Common import CommonPage
from Pages.ShowsPage import ShowsPage


class ShowsTest(BaseTest):

    def test_NavigateToShows(self):
        #Launch the Web App
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com/')
        common.open()

        #Web App is Launched, Navigate to Shows Section
        common.navigateToSection('Shows')

        #Assert Elements Present on Page and that Items Are Present
        shows = ShowsPage(driver=self.driver)
        shows.assert_element_present('subnav')
        shows.assert_element_present('subnav.btnNewReleases')
        shows.assert_element_present('subnav.btnAll')
        shows.assert_element_present('subnav.btnGenre')
        self.assertIn('active', shows.subnav.btnNewReleases.get_attribute('class'), 'New Releases not active tab')
        self.assertGreater(len(shows.getTitles()), 0, 'No Shows found on shows page')


    def test_AllSeriesClickHero(self):
        #Launch Web App, Navigate to Shows Section
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com')
        common.open()
        common.navigateToSection('SHOWS')

        #Click The All Button to Show All Shows
        shows = ShowsPage(driver=self.driver)
        shows.subnav.btnAll.click()

        #Assert All Shows Are in Alphabetical Order
        sleep(1)
        showTitles = shows.getTitles()
        self.assertAlphabetical(showTitles)

        #Click on a Random Show
        shows.clickOnShow(random=True)


