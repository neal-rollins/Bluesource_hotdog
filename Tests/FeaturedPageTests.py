from time import sleep
from selenium.webdriver.common.by import By
from Helpers.BaseTest import BaseTest
from Pages.FeaturedPage import FeaturedPage
from Pages.Common import CommonPage
from hotdog.FindEither import FindEither

class FeaturedPageTests(BaseTest):

    def test_headerElements(self):
        #Open App
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com')
        common.open()

        #Validate On Feature Page
        self.assertIn('active', common.navbar.btnFeatured.get_attribute('class'), 'Featured is not active tab')

        #Validate Header Elements
        self.assert_element_exists(common.navbar.btnShows, 'Shows Button')
        self.assert_element_exists(common.navbar.btnFeatured, 'Featured Button')
        self.assert_element_exists(common.navbar.btnDocumentaries, 'Documentaries Button')
        self.assert_element_exists(common.navbar.btnKids, 'Kids Button')
        self.assert_element_exists(common.btnHome, 'CBC Logo')

    def test_footerElements(self):
        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com')
        common.open()

        #Validate On Feature Page
        self.assertIn('active', common.navbar.btnFeatured.get_attribute('class'), 'Featured is not active tab')

        self.assert_element_exists(common.footer.linkTermsOfUse, 'Terms of Use')
        self.assert_element_exists(common.footer.linkPrivacyPolicy, 'linkPrivacyPolicy')
        self.assert_element_exists(common.footer.linkReusePermission, 'linkReusePermission')
        self.assert_element_exists(common.footer.linkHelp, 'linkHelp')
        self.assert_element_exists(common.footer.imgFooterLogo, 'imgFooterLogo')
        self.assert_element_exists(common.footer.txtCopywrite, 'txtCopywrite')
        self.assertEqual(common.footer.txtCopywrite.text, '©2015 CBC/Radio-Canada. All rights reserved')

    def test_featuredPageElements(self):
        #Open App
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com')
        common.open()

        #Validate On Feature Page
        self.assertIn('active', common.navbar.btnFeatured.get_attribute('class'), 'Featured is not active tab')

        featured = FeaturedPage(driver=self.driver)
        for show in featured.shows:
            self.assert_element_exists(show.imgShowBanner, 'Show Image')
            self.assert_element_exists(show.txtTitle, 'Show Title')

    def test_featuredItemNavigation(self):
        #Open App
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com')
        common.open()

        #Validate On Feature Page
        self.assertIn('active', common.navbar.btnFeatured.get_attribute('class'), 'Featured is not active tab')

        featured = FeaturedPage(driver=self.driver)
        for x in range(len(featured.shows)):
            featured = FeaturedPage(driver=self.driver)
            show = featured.shows[x]
            showTitle = show.txtTitle.text
            show.click()
            title = FindEither(context=common, selectors=[[By.CLASS_NAME, 'series-title'],
                                                  [By.CLASS_NAME, 'detail-title']]).text
            self.assertEqual(showTitle.lower(), title.lower(), 'Failed to navigate to correct detail screen.  Expected [%s].  Actual [%s]' % (showTitle, title))
            common.back()
            sleep(1)

    def test_footerLinks(self):
        assert False, 'Footer links are currently not functional'

    def test_testCarousels(self):
        #Open App
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com')
        common.open()

        #Validate On Feature Page
        self.assertIn('active', common.navbar.btnFeatured.get_attribute('class'), 'Featured is not active tab')
        common.pauseCarousel()
        common.testCarousel()

        #Navigate to Shows Section
        common.navigateToSection('SHOWS')
        self.assertIn('active', common.navbar.btnShows.get_attribute('class'), 'Shows is not active tab')
        common.pauseCarousel()
        common.testCarousel()