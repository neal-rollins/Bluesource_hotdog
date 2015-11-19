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

    def test_NavigatingThroughSeasons(self):
        #Open App and Naviaget to Blackstone Show
        common = CommonPage(driver=self.driver , url='http://project-igloo.maple.willowtreemobile.com/blackstone/season-2/9044f2f1-f9d9-43c7-8b8e-6eb8ee1f7044')
        common.open()
        self.driver.maximize_window()
        sleep(1)

        #Go To Previous Season, Verify on That Season
        showDetail = ShowDetailsPage(driver=self.driver)
        showDetail.goToPreviousSeason()
        showDetail.verifyOnSeason(1)

        #Click a Random Episode then Return Back
        episodeTitle = showDetail.clickOnEpisode(random=True)
        contentDetail = ContentDetailPage(driver=self.driver)
        self.assertEqual(episodeTitle.lower(), contentDetail.txtEpisodeTitle.text.lower())
        contentDetail.back()

        #Verify Still on Right Season
        showDetail.verifyOnSeason(1)

        #Go To Next Season, Verify on That Season
        showDetail.goToNextSeason()
        showDetail.verifyOnSeason(2)

        #Click a Random Episode then Return Back
        episodeTitle = showDetail.clickOnEpisode(random=True)
        contentDetail = ContentDetailPage(driver=self.driver)
        self.assertEqual(episodeTitle.lower(), contentDetail.txtEpisodeTitle.text.lower())
        contentDetail.back()

        #Verify Still on Right Season
        showDetail.verifyOnSeason(2)