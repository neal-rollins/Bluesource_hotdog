from time import sleep
from selenium.webdriver.common.by import By
from Helpers.BaseTest import BaseTest
from Pages.FeaturedPage import FeaturedPage
from Pages.Common import CommonPage
from hotdog.FindEither import FindEither

class FeaturedPageTests(BaseTest):

    def test_headerElements(self):
        #Open App
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()

        # If Mobile open menu
        if common.navbar.btnToggle.is_displayed():
            isMobile = True
            common.navbar.btnToggle.click()
            sleep(3)
        else:
            isMobile = False

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
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()

        # If Mobile open menu
        if common.navbar.btnToggle.is_displayed():
            isMobile = True
            common.navbar.btnToggle.click()
            sleep(3)
        else:
            isMobile = False

        #Validate On Feature Page
        self.assertIn('active', common.navbar.btnFeatured.get_attribute('class'), 'Featured is not active tab')
        if isMobile:
            common.navbar.btnToggle.click()
            sleep(3)
            common.txtFooterHeader.click()
            sleep(3)

        self.assert_element_exists(common.footer.linkTermsOfUse, 'Terms of Use')
        self.assert_element_exists(common.footer.linkPrivacyPolicy, 'linkPrivacyPolicy')
        self.assert_element_exists(common.footer.linkReusePermission, 'linkReusePermission')
        self.assert_element_exists(common.footer.linkHelp, 'linkHelp')
        self.assert_element_exists(common.footer.txtCopywrite, 'txtCopywrite')
        self.assertEqual(common.footer.txtCopywrite.text, '©2015 CBC/Radio-Canada. All rights reserved')

    def test_featuredPageElements(self):
        #Open App
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()

        # If Mobile open menu
        if common.navbar.btnToggle.is_displayed():
            isMobile = True
            common.navbar.btnToggle.click()
            sleep(3)
        else:
            isMobile = False

        #Validate On Feature Page
        self.assertIn('active', common.navbar.btnFeatured.get_attribute('class'), 'Featured is not active tab')

        if isMobile:
            common.navbar.btnToggle.click()

        featured = FeaturedPage(driver=self.driver)
        featured.assert_element_exists(featured.carousel, 'Carousel')
        for show in featured.shows:
            self.assert_element_exists(show.imgShowBanner, 'Show Image')
            self.assert_element_exists(show.txtTitle, 'Show Title')

    def test_featuredItemNavigation(self):
        #Open App
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()

        #If Mobile open menu
        if common.navbar.btnToggle.is_displayed():
            isMobile = True
            common.navbar.btnToggle.click()
            sleep(3)
        else:
            isMobile = False

        #Validate On Feature Page
        self.assertIn('active', common.navbar.btnFeatured.get_attribute('class'), 'Featured is not active tab')
        if isMobile:
            common.navbar.btnToggle.click()

        featured = FeaturedPage(driver=self.driver)
        for x in range(len(featured.shows)):
            #featured = FeaturedPage(driver=self.driver)
            featured.sync()

            show = featured.getShows()[x]
            showTitle = show.txtTitle.text
            show.click()
            title = common.getShowOrContentTitle()
            self.assertEqual(showTitle.lower(), title.lower(), 'Failed to navigate to correct detail screen.  Expected [%s].  Actual [%s]' % (showTitle, title))

            common.sync()
            common.navigateToSection('Featured')
            sleep(1)

    def test_footerLinksTermsOfUse(self):
         #Open App
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()

        # If Mobile open menu
        if common.navbar.btnToggle.is_displayed():
            isMobile = True
            common.footer.btnFooterMenu.click()
            sleep(3)
        else:
            isMobile = False

        common.footer.linkTermsOfUse.click()
        sleep(5)
        self.assert_in_url('termsofuse')

    def test_footerLinksPrivacy(self):
         #Open App
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()

        # If Mobile open menu
        if common.navbar.btnToggle.is_displayed():
            isMobile = True
            common.footer.btnFooterMenu.click()
            sleep(3)
        else:
            isMobile = False

        common.footer.linkPrivacyPolicy.click()
        sleep(5)
        self.assert_in_url('privacy')

    def test_footerLinksReuse(self):
         #Open App
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()

        # If Mobile open menu
        if common.navbar.btnToggle.is_displayed():
            isMobile = True
            common.footer.btnFooterMenu.click()
            sleep(3)
        else:
            isMobile = False

        common.footer.linkReusePermission.click()
        sleep(5)
        self.assert_in_url('permissions')


    def test_footerLinksHelp(self):
         #Open App
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()

        # If Mobile open menu
        if common.navbar.btnToggle.is_displayed():
            isMobile = True
            common.footer.btnFooterMenu.click()
            sleep(3)
        else:
            isMobile = False

        common.footer.linkHelp.click()
        sleep(5)
        self.assert_in_url('connects')


    def test_footerLinksContactUs(self):
         #Open App
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()

        # If Mobile open menu
        if common.navbar.btnToggle.is_displayed():
            isMobile = True
            common.footer.btnFooterMenu.click()
            sleep(3)
        else:
            isMobile = False

        common.footer.linkContact.click()
        sleep(5)
        self.assert_in_url('connects')

