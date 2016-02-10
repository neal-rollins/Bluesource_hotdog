import random
from time import sleep
from Helpers.BaseTest import BaseTest
from Pages.Common import CommonPage
from Pages.ShowDetailsPage import ShowDetailsPage
from Pages.ShowsPage import ShowsPage

class ShowsTest(BaseTest):

    def test_NavigateToShows(self):
        #Launch the Web App
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()

        #Web App is Launched, Navigate to Shows Section
        common.navigateToSection('Shows')

        #Validate elements of Shows page
        shows = ShowsPage(driver=self.driver)
        self.assert_element_exists(shows.carousel, 'Carousel')
        shows.subnav.openMenuIfMobile()
        self.assert_element_exists(shows.subnav.btnAll, 'All Shows Button')
        self.assert_element_exists(shows.subnav.btnGenre, 'Shows Genre Button')
        self.assertIn('active', shows.subnav.btnAll.get_attribute('class'), 'All not active tab')
        self.assertGreater(len(shows.getTitles()), 0, 'No Shows found on shows page')
        for show in shows.shows:
            self.assert_element_exists(show.imgShowBanner, 'Show Image')
            self.assert_element_exists(show.txtTitle, 'Show Title')

    def test_navigateAllShows(self):
        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()
        common.navigateToSection('SHOWS')

        #Click The All Button to Show All Shows
        shows = ShowsPage(driver=self.driver)
        shows.subnav.openMenuIfMobile()
        shows.subnav.btnAll.click()

        #Assert All Shows Are in Alphabetical Order and that Each Show has a Banner and a Title
        sleep(1)
        showTitles = shows.getTitles()
        self.assertGreater(len(showTitles), 0, 'No Shows found on shows page')
        self.assertAlphabetical(showTitles)

        for show in shows.shows:
            self.assert_element_exists(show.imgShowBanner, 'Show Image')
            self.assert_element_exists(show.txtTitle, 'Show Title')

    def test_navigateToShowGenres(self):

        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()
        common.navigateToSection('SHOWS')

        #Navigate to all shows
        shows = ShowsPage(driver=self.driver)
        sleep(2)

        genreList = shows.getGenreList()
        self.assertAlphabetical(genreList)

        genres =  shows.getGenreList()

        self.assertGreater(len(genreList), 0, 'No Genres Found for Shows')
        #self.assertEqual(len(genreList), len(genres), 'Unexpected number of genres found.  Expected [%s]. Actual [%s]' % (len(genres), len(genreList)))
        for genre in genres:
            shows.navigateGenreDropdown(genre)
            sleep(3)
            showTitles = shows.getTitles()
            self.assertEqual(genre.lower(), shows.subnav.currentGenre)
            self.assertGreater(len(showTitles), 0, 'No Shows found on shows page')
            for show in shows.shows:
                self.assert_element_exists(show.imgShowBanner, 'Show Image')
                self.assert_element_exists(show.txtTitle, 'Show Title')

    def test_nagivateToShowDetails(self):
        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()
        common.navigateToSection('SHOWS')

        #Validate Random Shows
        for i in range(1):
            shows = ShowsPage(driver=self.driver)
            shows.sync()
            sleep(1)
            showTitle = shows.clickOnShow(random=True)
            showDetail = ShowDetailsPage(driver=self.driver)
            showDetail.assert_element_present('txtSeriesTitle', timeout=5)
            self.assertEqual(showTitle, showDetail.txtSeriesTitle.text, 'Loaded incorrect Show Detail page for [%s]. Actually loaded [%s]' % (showTitle, showDetail.txtSeriesTitle.text))
            showDetail.back()

    def test_nagivateToContentDetailsShowsGenres(self):
        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()
        common.navigateToSection('SHOWS')

        #Get Genre List
        shows = ShowsPage(driver=self.driver)
        genreList = shows.getGenreList()

        #Validate Random Shows with Random Genre
        for i in range(1):
            shows = ShowsPage(driver=self.driver)
            shows.sync()

            #Select Random Genre
            shows.navigateGenreDropdown(random.choice(genreList))
            sleep(1)

            #Select Random Show
            showTitle = shows.clickOnShow(random=True)
            showDetail = ShowDetailsPage(driver=self.driver)
            showDetail.assert_element_present('txtSeriesTitle', timeout=5)
            self.assertEqual(showTitle.lower(), showDetail.txtSeriesTitle.text.lower(),
                             'Loaded incorrect Content Detail page for [%s]. Actually loaded [%s]' % (showTitle, showDetail.txtSeriesTitle.text))
            showDetail.back()
