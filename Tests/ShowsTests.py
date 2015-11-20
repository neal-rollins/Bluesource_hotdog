import random
from time import sleep
from Helpers.BaseTest import BaseTest
from Pages.Common import CommonPage
from Pages.ShowDetailsPage import ShowDetailsPage
from Pages.ShowsPage import ShowsPage


expectedGenres = ['News & Current Affairs', 'Comedy', 'Documentary', 'Drama']

class ShowsTest(BaseTest):

    def test_NavigateToShows(self):
        #Launch the Web App
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com/')
        common.open()

        #Web App is Launched, Navigate to Shows Section
        common.navigateToSection('Shows')

        #Validate On Shows Page
        self.assertIn('active', common.navbar.btnShows.get_attribute('class'), 'Featured is not active tab')

        #Validate elements of Shows page
        shows = ShowsPage(driver=self.driver)
        self.assert_element_exists(shows.subnav.btnAll, 'All Shows Button')
        self.assert_element_exists(shows.subnav.btnGenre, 'Shows Genre Button')
        self.assertIn('active', shows.subnav.btnAll.get_attribute('class'), 'All not active tab')
        self.assertGreater(len(shows.getTitles()), 0, 'No Shows found on shows page')
        for show in shows.shows:
            self.assert_element_exists(show.imgShowBanner, 'Show Image')
            self.assert_element_exists(show.txtTitle, 'Show Title')


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

        for show in shows.shows:
            self.assert_element_exists(show.imgShowBanner, 'Show Image')
            self.assert_element_exists(show.txtTitle, 'Show Title')

    def test_navigateToShowGenres(self):

        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com')
        common.open()
        common.navigateToSection('SHOWS')

        #Navigate to all shows
        shows = ShowsPage(driver=self.driver)
        sleep(2)
        shows.subnav.btnGenre.click()
        genreList = shows.getGenreList()
        self.assertAlphabetical(genreList)
        shows.subnav.btnGenre.click()
        genres = expectedGenres
        self.assertGreater(len(genreList), 0, 'No Genres Found for Shows')
        #self.assertEqual(len(genreList), len(genres), 'Unexpected number of genres found.  Expected [%s]. Actual [%s]' % (len(genres), len(genreList)))
        for genre in genres:
            shows.navigateGenreDropdown(genre)
            sleep(1)
            showTitles = shows.getTitles()
            self.assertEqual(genre.lower(), shows.subnav.btnGenre.text.lower())
            self.assertGreater(len(showTitles), 0, 'No Shows found on shows page')
            for show in shows.shows:
                self.assert_element_exists(show.imgShowBanner, 'Show Image')
                self.assert_element_exists(show.txtTitle, 'Show Title')

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
            showDetail.assert_element_present('txtSeriesTitle', timeout=5)
            self.assertEqual(showTitle, showDetail.txtSeriesTitle.text, 'Loaded incorrect Show Detail page for [%s]. Actually loaded [%s]' % (showTitle, showDetail.txtSeriesTitle.text))
            showDetail.back()

    def test_nagivateToContentDetailsDocumentaryGenres(self):
        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com')
        common.open()
        common.navigateToSection('SHOWS')

        #Get Genre List
        shows = ShowsPage(driver=self.driver)
        genreList = expectedGenres

        #Validate Random Shows with Random Genre
        for i in range(5):
            sleep(1)
            shows = ShowsPage(driver=self.driver)

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