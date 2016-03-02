from time import sleep

from Helpers.Retry import Retry

__author__ = 'brian.menzies'
from webium import Find, Finds
from appium.webdriver.common.mobileby import MobileBy as By
from hotdog.FindEither import FindEither
from Helpers.BaseTest import BaseTest
from Helpers.BasePage import CBCWebBase

class ContentDetailPage(CBCWebBase):

    txtBreadcrumbs = Find(by=By.CSS_SELECTOR, value='.series-name a')
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
        timeElapsed = self.driver.execute_script("return document.getElementsByClassName('jw-text-elapsed')[0].innerHTML")
        timeElapsed = timeElapsed.split(':')
        minutes = int(timeElapsed[0]) * 60
        seconds = int(timeElapsed[1])
        timeStamp = minutes + seconds
        return timeStamp

    @Retry
    def wait_for_video_load(self):
        sleep(5)
        ad_text =self.driver.execute_script("return document.getElementsByClassName('jw-text-alt')[0].innerHTML")
        if ad_text == 'Loading':
            raise AssertionError('Video failed to load')
    @Retry
    def ad_playing(self):
        ad_text = self.driver.execute_script("return document.getElementsByClassName('jw-text-alt')[0].innerHTML")
        if ad_text.find('This ad will end') == -1:
            raise AssertionError('Failed to play ad. Ad text [%s]' % ad_text)

    @Retry
    def wait_for_ad(self):

        ad_text = self.driver.execute_script("return document.getElementsByClassName('jw-text-alt')[0].innerHTML")

        sleep([int(s) for s in ad_text.split() if s.isdigit()][0])
        sleep(5)
        ad_text = self.driver.execute_script("return document.getElementsByClassName('jw-text-alt')[0].innerHTML")
        if ad_text.find('This ad will end') != -1:
            raise AssertionError('Ad Failed to end. Ad text [%s]' % ad_text)

    @Retry
    def isVideoPlaying(self):
        playback_index = self.driver.execute_script("return document.getElementsByClassName('jw-text-elapsed')[0].innerHTML")
        sleep(2)
        if playback_index == self.driver.execute_script("return document.getElementsByClassName('jw-text-elapsed')[0].innerHTML"):
            raise AssertionError('Video failed to play. Index = %s' % playback_index)

    def play_for_time(self, seconds):
        playback_index = self.getTimeStamp()
        sleep(2)
        while self.getTimeStamp() - playback_index <  seconds:
            pass

