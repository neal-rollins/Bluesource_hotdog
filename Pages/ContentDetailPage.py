from time import sleep

__author__ = 'brian.menzies'
from webium import Find, Finds
from appium.webdriver.common.mobileby import MobileBy as By
from hotdog.FindEither import FindEither
from Helpers.BaseTest import BaseTest
from Helpers.BasePage import CBCWebBase

class ContentDetailPage(CBCWebBase):

    txtBreadcrumbs = Find(by=By.CSS_SELECTOR, value='.breadcrumbs a')
    btnPlay = Find(by=By.CLASS_NAME, value='play-icon')
    videoPlayer = Find(by=By.ID, value='jwplayer')
    imgAd = Find(by=By.CLASS_NAME, value='ad-wrapper')
    txtElapsedTime = Find(by=By.CLASS_NAME, value='jw-text-elapsed')
    txtEpisodeNumber = Find(by=By.CLASS_NAME, value='episode-number')
    txtDuration = Find(by=By.CLASS_NAME, value='duration')
    txtEpisodeTitle = Find(by=By.CLASS_NAME, value='detail-title')
    txtDescription = Find(by=By.CLASS_NAME, value='description')
    txtCredits = Find(by=By.CLASS_NAME, value='credits')


    def pauseVideoPlayer(self):
        self.btnVideoPlayer.click()
        self.assert_element_present('txtPausedState', timeout=3), 'The Video Player Was Not Paused'

    def getTimeStamp(self):
        timeElapsed = self.txtElapsedTime.text
        timeElapsed = timeElapsed.split(':')
        minutes = int(timeElapsed[0]) * 60
        seconds = int(timeElapsed[1])
        timeStamp = minutes + seconds
        return timeStamp

    def verifyVideoHasPlayed(self, timeAtStart, timeAtEnd):
        assert timeAtEnd > timeAtStart, 'Expected [%s] to be greater than [%s]' % (timeAtEnd, timeAtStart)

    def playVideo(self, loadTime=10, adTime = 30, playTime=10):
        self.btnPlay.click()
        sleep(loadTime)
        sleep(adTime)
        self.videoPlayer.click()
        startTime = self.getTimeStamp()
        assert (startTime < 30), 'Expected Time on Video to be less than 30 seconds. Instead it was at [%s] seconds' % startTime
        self.videoPlayer.click()
        sleep(playTime)
        self.videoPlayer.click()
        endTime = self.getTimeStamp()
        self.verifyVideoHasPlayed(startTime, endTime)






