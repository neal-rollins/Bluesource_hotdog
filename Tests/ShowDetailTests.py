from time import sleep
from Helpers.BaseTest import BaseTest
from Pages.Common import CommonPage
from Pages.ContentDetailPage import ContentDetailPage
from Pages.ShowDetailsPage import ShowDetailsPage
from Pages.ShowsPage import ShowsPage


class ShowDetailsTest(BaseTest):

    def test_showDetailsElements(self):
        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()
        common.navigateToSection('SHOWS')

        #Navigate to all shows
        sleep(1)
        shows = ShowsPage(driver=self.driver)
        isMobile = shows.isMobile
        showTitle = shows.clickOnShow(random=True)

        #Validate Show Detail Elements
        sleep(1)
        showDetail = ShowDetailsPage(driver=self.driver)
        showDetail.assert_element_present('imgHero', timeout=20)
        showDetail.assert_element_present('txtSeriesTitle', timeout=20)
        showDetail.assert_element_present('imgAd', timeout=20)
        self.assertGreater(len(showDetail.listEpisodes), 0, 'No Episodes found for show [%s]' % showTitle)
        for episode in showDetail.listEpisodes:
            self.assert_element_exists(episode.imgShowImage, 'Episode Image')
            self.assert_element_exists(episode.txtEpisodeDetail, 'Episode Detail')
            self.assert_element_exists(episode.txtEpisodeTitle, 'Episode Title')
            if not isMobile:
                self.assert_element_exists(episode.txtEpisodeDescription, 'Episode Description')

    def test_navigateContentDetail(self):
        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()
        common.navigateToSection('SHOWS')

        #Navigate to all shows
        shows = ShowsPage(driver=self.driver)
        shows.sync()
        showTitle = shows.clickOnShow(random=True)

        #Validate Content Detail Loads
        sleep(1)
        for x in range(1):

            showDetail = ShowDetailsPage(driver=self.driver)
            showDetail.sync(showTitle)
            sleep(3)

            episodeTitle = showDetail.clickOnEpisode(random=True)
            contentDetail = ContentDetailPage(driver=self.driver)
            self.assertEqual(episodeTitle.lower(), contentDetail.txtEpisodeTitle.text.lower())
            contentDetail.back()

    def test_NavigatingThroughSeasons(self):
        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()
        common.navigateToSection('SHOWS')

        #Navigate to all shows and select show
        sleep(1)
        shows = ShowsPage(driver=self.driver)
        isMobile = shows.isMobile
        showTitle = shows.clickOnShow(title='Blackstone')

        #Verify Elements Season 2
        showDetail = ShowDetailsPage(driver=self.driver)
        for episode in showDetail.listEpisodes:
            showDetail.assert_element_exists(episode.imgShowImage, "Show Image")
            showDetail.assert_element_exists(episode.txtEpisodeDetail, "Episode Detail")
            showDetail.assert_element_exists(episode.txtEpisodeTitle, "Episode Title")
            if not isMobile:
                showDetail.assert_element_exists(episode.txtEpisodeDescription, "Episode Description")
            showDetail.assert_element_exists(episode.txtEpisodeNumber, "Episode Number")
            showDetail.assert_element_exists(episode.txtDuration, "Episode Duration")

        #Go To Previous Season, Verify on That Season
        showDetail.goToPreviousSeason()
        showDetail.verifyOnSeason(1)

        #Verify Elements Season 1
        showDetail = ShowDetailsPage(driver=self.driver)
        for episode in showDetail.listEpisodes:
            showDetail.assert_element_exists(episode.imgShowImage, "Show Image")
            showDetail.assert_element_exists(episode.txtEpisodeDetail, "Episode Detail")
            showDetail.assert_element_exists(episode.txtEpisodeTitle, "Episode Title")
            if not isMobile:
                showDetail.assert_element_exists(episode.txtEpisodeDescription, "Episode Description")
            showDetail.assert_element_exists(episode.txtEpisodeNumber, "Episode Number")
            showDetail.assert_element_exists(episode.txtDuration, "Episode Duration")

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
        contentDetail.sync()
        self.assertEqual(episodeTitle.lower(), contentDetail.txtEpisodeTitle.text.lower())
        contentDetail.back()

        #Verify Still on Right Season
        showDetail.verifyOnSeason(2)