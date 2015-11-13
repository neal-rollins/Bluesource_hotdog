__author__ = 'brian.menzies'
from webium import Find, Finds
from appium.webdriver.common.mobileby import MobileBy as By
from hotdog.FindEither import FindEither
from Helpers.BaseTest import BaseTest
from Helpers.BasePage import CBCWebBase

class ContentDetailPage(CBCWebBase):

    btnPlay = Find(by=By.CLASS_NAME, value='play-icon')
    btnVideoPlayer = Find(by=By.ID, value='jwplayer')
    txtElapsedTime = Find(by=By.CLASS_NAME, value='jw-text-elapsed')
    txtDuration = Find(by=By.CLASS_NAME, value='duration')
    txtBreadcrumbs = Find(by=By.CLASS_NAME, value='breadcrumbs')

    def pauseVideoPlayer(self):
        self.btnVideoPlayer.click()
        self.assert_element_present('txtPausedState', timeout=3), 'The Video Player Was Not Paused'

    def getTimeStamp(self):
        timeElapsed = self.txtElapsedTime.text
        timeElapsed.split(':')
        minutes = int(timeElapsed[0]) * 60
        seconds = int(timeElapsed[1])
        timeStamp = minutes + seconds
        return timeStamp

    def verifyVideoHasPlayed(self, timeAtStart, timeAtEnd):
        assert timeAtEnd > timeAtStart, 'Expected [%s] to be greater than [%s]' % (timeAtEnd, timeAtStart)

    def playVideo(self):
        self.btnPlay.click()





