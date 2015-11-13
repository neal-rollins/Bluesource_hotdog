from time import sleep
from Helpers.BaseTest import BaseTest
from Pages.Common import CommonPage
from Pages.ContentDetailPage import ContentDetailPage
from Pages.ShowDetailsPage import ShowDetailsPage
from Pages.ShowsPage import ShowsPage


class ShowDetailsTest(BaseTest):

    def test_showDetailsElements(self):
        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com')
        common.open()
        common.navigateToSection('SHOWS')

        #Navigate to all shows
        sleep(1)
        shows = ShowsPage(driver=self.driver)
        showTitle = shows.clickOnShow(title='Doc Zone')

        #Validate Show Detail Elements
        sleep(1)
        showDetail = ShowDetailsPage(driver=self.driver)
        showDetail.assert_element_present('imgHero')
        showDetail.assert_element_present('txtSeriesTitle')
        showDetail.assert_element_present('imgAd')
        self.assertGreater(len(showDetail.listEpisodes), 0, 'No Episodes found for show [%s]' % showTitle)
        for episode in showDetail.listEpisodes:
            self.assert_element_exists(episode.imgShowImage, 'Episode Image')
            self.assert_element_exists(episode.txtEpisodeDetail, 'Episode Detail')
            self.assert_element_exists(episode.txtEpisodeTitle, 'Episode Title')
            self.assert_element_exists(episode.txtEpisodeDescription, 'Episode Description')

    def test_navigateContentDetail(self):
        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com')
        common.open()
        common.navigateToSection('SHOWS')

        #Navigate to all shows
        sleep(1)
        shows = ShowsPage(driver=self.driver)
        showTitle = shows.clickOnShow(title='Doc Zone')

        #Validate Content Detail Loads
        sleep(1)
        for x in range(5):
            showDetail = ShowDetailsPage(driver=self.driver)
            episodeTitle = showDetail.clickOnEpisode(random=True)
            contentDetail = ContentDetailPage(driver=self.driver)
            self.assertEqual(episodeTitle.lower(), contentDetail.txtEpisodeTitle.text.lower())
            contentDetail.back()
