from time import sleep
import webium
from hotdog.Config import GetConfig

from Helpers.BaseTest import BaseTest
from Pages.Common import CommonPage
from Pages.ContentDetailPage import ContentDetailPage
from Pages.ShowDetailsPage import ShowDetailsPage
from Pages.ShowsPage import ShowsPage

class ContentPlaysTests(BaseTest):

    def test_contentPlays(self):

        #Open App and Navigate to Shows
        common = CommonPage(driver=self.driver, url=self.page_url)
        common.open()
        common.navigateToSection('SHOWS')

        #Navigate to all shows and select show
        shows = ShowsPage(driver=self.driver)
        shows.sync()
        isMobile = shows.isMobile
        showTitle = shows.clickOnShow(random=True)

        #Navigate to Content Detail
        sleep(1)
        showDetail = ShowDetailsPage(driver=self.driver)
        showDetail.sync(showTitle)
        showDetail.clickOnEpisode(random=True)

        #Validate Content Detail Elements
        contentDetail = ContentDetailPage(driver=self.driver)
        contentDetail.sync()

        contentDetail.wait_for_video_load()
        contentDetail.ad_playing
        contentDetail.wait_for_ad
        contentDetail.isVideoPlaying
        contentDetail.play_for_time(30)