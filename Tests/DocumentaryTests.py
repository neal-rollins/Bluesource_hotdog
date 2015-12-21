import random
from time import sleep
from Helpers.BaseTest import BaseTest
from Pages.Common import CommonPage
from Pages.ContentDetailPage import ContentDetailPage
from Pages.DocumentariesPage import DocumentariesPage


class DocumentaryTest(BaseTest):

    def test_NavigateToDocumentaries(self):
        #Launch the Web App
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()

        #Web App is Launched, Navigate to Documentaries Section
        common.navigateToSection('Documentaries')

        #Validate elements of Documentaries page
        docs = DocumentariesPage(driver=self.driver)
        docs.subnav.openMenuIfMobile()
        self.assert_element_exists(docs.subnav.btnAll, 'All Documentaries Button')
        self.assert_element_exists(docs.subnav.btnGenre, 'Documentaries Genre Button')
        self.assertIn('active', docs.subnav.btnAll.get_attribute('class'), 'All not active tab')
        self.assertGreater(len(docs.getTitles()), 0, 'No Shows found on shows page')
        for show in docs.shows:
            self.assert_element_exists(show.imgShowBanner, 'Show Image')
            self.assert_element_exists(show.txtTitle, 'Show Title')


    def test_navigateToDocumentariesGenres(self):

        #Open App and Navigate to Documentaries
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()
        common.navigateToSection('DOCUMENTARIES')

        #Navigate to all Documentaries
        docs = DocumentariesPage(driver=self.driver)
        genreList = docs.getGenreList()
        self.assertAlphabetical(genreList)
        for genre in genreList:
            docs.navigateGenreDropdown(genre)
            sleep(3)
            showTitles = docs.getTitles()
            self.assertEqual(genre.lower(), docs.subnav.currentGenre)
            self.assertGreater(len(showTitles), 0, 'No Shows found on shows page')
            for show in docs.shows:
                assert show.imgShowBanner
                assert show.txtTitle

    def test_nagivateToContentDetailsDocumentary(self):
        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()
        common.navigateToSection('DOCUMENTARIES')

        #Validate Random Documentary Episode
        for i in range(1):
            docs = DocumentariesPage(driver=self.driver)
            docs.sync()
            showTitle = docs.clickOnShow(random=True)
            contentDetail = ContentDetailPage(driver=self.driver)
            contentDetail.assert_element_present('txtEpisodeTitle', timeout=5)
            self.assertEqual(showTitle.lower(), contentDetail.txtEpisodeTitle.text.lower(),
                             'Loaded incorrect Content Detail page for [%s]. Actually loaded [%s]' % (showTitle, contentDetail.txtEpisodeTitle.text))
            contentDetail.back()

    def test_nagivateToContentDetailsDocumentaryGenres(self):
        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()
        common.navigateToSection('DOCUMENTARIES')

        #Get Genre List
        docs = DocumentariesPage(driver=self.driver)
        genreList = docs.getGenreList()

        #Validate Random Shows with Random Genre
        for i in range(1):
            docs = DocumentariesPage(driver=self.driver)
            docs.sync()

            #Select Random Genre
            docs.navigateGenreDropdown(random.choice(genreList))
            sleep(1)

            #Select Random Documentary
            showTitle = docs.clickOnShow(random=True)
            contentDetail = ContentDetailPage(driver=self.driver)
            contentDetail.assert_element_present('txtEpisodeTitle', timeout=5)
            self.assertEqual(showTitle.lower(), contentDetail.txtEpisodeTitle.text.lower(),
                             'Loaded incorrect Content Detail page for [%s]. Actually loaded [%s]' % (showTitle, contentDetail.txtEpisodeTitle.text))
            contentDetail.back()
