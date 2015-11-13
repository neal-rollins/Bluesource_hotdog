from time import sleep
import webium
from Helpers.BaseTest import BaseTest
from Pages.Common import CommonPage
from Pages.ShowDetailsPage import ShowDetailsPage
from Pages.ShowsPage import ShowsPage



class ShowsTest(BaseTest):

    def test_NavigateToShows(self):
        #Launch the Web App
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com/')
        common.open()

        #Web App is Launched, Navigate to Shows Section
        common.navigateToSection('Shows')

        #Validate elements of Shows page
        shows = ShowsPage(driver=self.driver)
        assert shows.subnav.btnNewReleases
        assert shows.subnav.btnAll
        assert shows.subnav.btnGenre
        self.assertIn('active', shows.subnav.btnNewReleases.get_attribute('class'), 'New Releases not active tab')
        self.assertGreater(len(shows.getTitles()), 0, 'No Shows found on shows page')
        for show in shows.shows:
            assert show.imgShowBanner
            assert show.txtTitle


    def test_navigateAllShows(self):
        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com')
        common.open()
        common.navigateToSection('SHOWS')

        #Click The All Button to Show All Shows
        shows = ShowsPage(driver=self.driver)
        shows.subnav.btnAll.click()

        #Assert All Shows Are in Alphabetical Order
        sleep(1)
        showTitles = shows.getTitles()
        self.assertGreater(len(showTitles), 0, 'No Shows found on shows page')
        self.assertAlphabetical(showTitles)

        #Click on a Random Show
        shows.clickOnShow(random=True)

        for show in shows.shows:
            assert show.imgShowBanner
            assert show.txtTitle

    def test_navigateToShowGenres(self):

        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com')
        common.open()
        common.navigateToSection('SHOWS')

        #Navigate to all shows
        shows = ShowsPage(driver=self.driver)
        genres = ['News & Current Affairs', 'Comedy', 'Documentary', 'Drama']
        for genre in genres:
            shows.navigateGenreDropdown(genre)
            sleep(1)
            showTitles = shows.getTitles()
            self.assertEqual(genre.lower(), shows.subnav.btnGenre.text.lower())
            self.assertGreater(len(showTitles), 0, 'No Shows found on shows page')
            for show in shows.shows:
                assert show.imgShowBanner
                assert show.txtTitle

    def test_nagivateToShowDetails(self):
        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com')
        common.open()
        common.navigateToSection('SHOWS')

        #Validate Random Shows
        for i in range(5):
            sleep(1)
            shows = ShowsPage(driver=self.driver)
            showTitle = shows.clickOnShow(random=True)
            showDetail = ShowDetailsPage(driver=self.driver)
            showDetail = showDetail.assert_element_present('txtSeriesTitle', timeout=5)
            self.assertEqual(showTitle, showDetail.txtSeriesTitle.text, 'Loaded incorrect Show Detail page for [%]. Actually loaded [%s]' % (showTitle, showDetail.txtSeriesTitle.text))
            showDetail.back()

    def test_nagivateToShowDetailsAllShows(self):
        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com')
        common.open()
        common.navigateToSection('SHOWS')
        #Navigate to all shows
        shows = ShowsPage(driver=self.driver)
        shows.subnav.btnAll.click()

        #Validate Random shows
        for i in range(5):
            sleep(1)
            shows = ShowsPage(driver=self.driver)
            showTitle = shows.clickOnShow(random=True)
            showDetail = ShowDetailsPage(driver=self.driver)
            showDetail = showDetail.assert_element_present('txtSeriesTitle', timeout=5)
            self.assertEqual(showTitle, showDetail.txtSeriesTitle.text, 'Loaded incorrect Show Detail page for [%]. Actually loaded [%s]' % (showTitle, showDetail.txtSeriesTitle.text))
            showDetail.back()