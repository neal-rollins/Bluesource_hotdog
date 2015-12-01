import random
from time import sleep
from Helpers.BaseTest import BaseTest
from Pages.Common import CommonPage
from Pages.ContentDetailPage import ContentDetailPage
from Pages.DocumentariesPage import DocumentariesPage
from Pages.KidsPage import KidsPage
from Pages.ShowDetailsPage import ShowDetailsPage


class KidsTests(BaseTest):

    def test_NavigateToKids(self):
        #Launch the Web App
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com/')
        common.open()

        #Web App is Launched, Navigate to Kids Section
        common.navigateToSection('Kids')

        #Validate elements of Kids page
        kids = KidsPage(driver=self.driver)
        self.assert_element_exists(kids.subnav.btnAll, 'All Documentaries Button')
        self.assertIn('active', kids.subnav.btnAll.get_attribute('class'), 'All not active tab')
        self.assertGreater(len(kids.getTitles()), 0, 'No Shows found on shows page')
        self.assertAlphabetical(kids.getTitles())
        for show in kids.shows:
            self.assert_element_exists(show.imgShowBanner, 'Show Image')
            self.assert_element_exists(show.txtTitle, 'Show Title')

    def test_nagivateToShowDetailsKids(self):
        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com')
        common.open()
        common.navigateToSection('KIDS')

        #Validate Random Shows
        for i in range(5):
            Kids = KidsPage(driver=self.driver)
            Kids.sync()

            showTitle = Kids.clickOnShow(random=True)
            showDetail = ShowDetailsPage(driver=self.driver)
            showDetail.assert_element_present('txtSeriesTitle', timeout=5)
            self.assertEqual(showTitle, showDetail.txtSeriesTitle.text, 'Loaded incorrect Show Detail page for [%s]. Actually loaded [%s]' % (showTitle, showDetail.txtSeriesTitle.text))
            showDetail.back()

