__author__ = 'brian.menzies'
from webium import Find, Finds
from appium.webdriver.common.mobileby import MobileBy as By
from hotdog.FindEither import FindEither
from Helpers.BaseTest import BaseTest
from Helpers.BasePage import CBCWebBase
from selenium.webdriver.remote.webelement import WebElement

class ShowDetailsPage(CBCWebBase):
    btnPlay = Find(by=By.CLASS_NAME, value='play-icon')
    btnPauseIcon = Find(by=By.CLASS_NAME, value='jw-icon-playback')
    btnVideoPlayer = Find(by=By.ID, value='jwplayer')
    txtElapsedTime = Find(by=By.CLASS_NAME, value='jw-text-elapsed')
    episodeTitle = Find(by=By.CLASS_NAME, value='episode-title')
    episodeNumber = Find(by=By.CLASS_NAME, value='episode-number')
    episodeDescription = Find(by=By.CLASS_NAME, value='description')
    listOfEpisodes = Finds(by=By.CLASS_NAME, value='media-thumbnail-container')
    currentSeason = Find(by=By.CLASS_NAME, value='active')
    # currentSeason = Find(by=By.CSS_SELECTOR, value='#main-content > div > nav > div > div > div > ul > li.selected > a')



    # txtElapsedTime = Find(by=By.CSS_SELECTOR, value='#jwplayer > div.jw-controls.jw-reset > div.jw-controlbar.jw-background-color.jw-reset > div.jw-group.jw-controlbar-left-group.jw-reset > span')

    def clickShow(self, listOfShows, numberOfShowToClick):
        number = int(numberOfShowToClick) - 1
        listOfShows[number].click()

    def clickEpisode(self, numberEpisodeToClick):
        episodes = self.listOfEpisodes
        number = int(numberEpisodeToClick) - 1
        episodes[number].click()

    def getCurrentSeason(self):
        season = Find(context=self, by=By.CLASS_NAME, value='selected')
        print(season)
        # season.text()
        # print(season.text())
        return season.text()

    def goToPreviousSeason(self):
        #Get Season and Season Number
        currentSeasonInfo = self.currentSeason.text

        #Break The Number Apart from the Text
        seasonArray = currentSeasonInfo.split(' ')
        print(seasonArray[0])
        print(seasonArray[1])
        currentSeasonNumber = int(seasonArray[1])

        #Subtract 1 From the Season Number, Making Sure It Isn't 0
        previousSesaonNumber = int(currentSeasonNumber) - 1
        assert (previousSesaonNumber > 0), 'There Is Only One Season. A Previous Season Could Not Be Found.'

        #Add in the Word Season so the Combined String Can Be Found
        previousSeason = 'Season ' + str(previousSesaonNumber)
        return previousSeason

    def pauseVideoPlayer(self):
        self.btnPauseIcon.click()
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





