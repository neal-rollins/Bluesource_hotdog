import random
from time import sleep
from Helpers.BaseTest import BaseTest
from Pages.Common import CommonPage
from Pages.ContentDetailPage import ContentDetailPage
from Pages.DocumentariesPage import DocumentariesPage


class DocumentaryTest(BaseTest):

    def test_NavigateToDocumentaries(self):
        #Launch the Web App
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com/')
        common.open()

        #Web App is Launched, Navigate to Shows Section
        common.navigateToSection('Documentaries')

        #Validate elements of Shows page
        docs = DocumentariesPage(driver=self.driver)
        self.assert_element_exists(docs.subnav.btnAll, 'All Documentaries Button')
        self.assert_element_exists(docs.subnav.btnGenre, 'Documentaries Genre Button')
        self.assertIn('active', docs.subnav.btnAll.get_attribute('class'), 'All not active tab')
        self.assertGreater(len(docs.getTitles()), 0, 'No Shows found on shows page')
        for show in docs.shows:
            self.assert_element_exists(show.imgShowBanner, 'Show Image')
            self.assert_element_exists(show.txtTitle, 'Show Title')


    def test_navigateToDocumentariesGenres(self):

        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com')
        common.open()
        common.navigateToSection('DOCUMENTARIES')

        #Navigate to all shows
        docs = DocumentariesPage(driver=self.driver)
        genreList = docs.getGenreList()
        genres = ['Biography', 'Health', 'Science & Technology', 'Wildlife']
        self.assertEqual(len(genreList), len(genres), 'Unexpected number of genres found. Expected [%s].  Actual [%s].' % (len(genres), len(genreList)))
        self.assertAlphabetical(genreList)
        for genre in genres:
            docs.navigateGenreDropdown(genre)
            sleep(1)
            showTitles = docs.getTitles()
            self.assertEqual(genre.lower(), docs.subnav.btnGenre.text.lower())
            self.assertGreater(len(showTitles), 0, 'No Shows found on shows page')
            for show in docs.shows:
                assert show.imgShowBanner
                assert show.txtTitle

    def test_nagivateToContentDetailsDocumentary(self):
        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com')
        common.open()
        common.navigateToSection('DOCUMENTARIES')

        #Validate Random Shows
        for i in range(5):
            sleep(1)
            docs = DocumentariesPage(driver=self.driver)
            showTitle = docs.clickOnShow(random=True)
            contentDetail = ContentDetailPage(driver=self.driver)
            contentDetail.assert_element_present('txtEpisodeTitle', timeout=5)
            self.assertEqual(showTitle.lower(), contentDetail.txtEpisodeTitle.text.lower(),
                             'Loaded incorrect Content Detail page for [%s]. Actually loaded [%s]' % (showTitle, contentDetail.txtEpisodeTitle.text))
            contentDetail.back()

    def test_nagivateToContentDetailsDocumentaryGenres(self):
        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com')
        common.open()
        common.navigateToSection('DOCUMENTARIES')

        #Get Genre List
        docs = DocumentariesPage(driver=self.driver)
        genreList = docs.getGenreList()

        #Validate Random Shows with Random Genre
        for i in range(5):
            sleep(1)
            docs = DocumentariesPage(driver=self.driver)

            #Select Random Genre
            docs.navigateGenreDropdown(random.choice(genreList))
            sleep(1)

            #Select Random Show
            showTitle = docs.clickOnShow(random=True)
            contentDetail = ContentDetailPage(driver=self.driver)
            contentDetail.assert_element_present('txtEpisodeTitle', timeout=5)
            self.assertEqual(showTitle.lower(), contentDetail.txtEpisodeTitle.text.lower(),
                             'Loaded incorrect Content Detail page for [%s]. Actually loaded [%s]' % (showTitle, contentDetail.txtEpisodeTitle.text))
            contentDetail.back()
