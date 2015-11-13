__author__ = 'brian.menzies'
from webium import Find, Finds
from appium.webdriver.common.mobileby import MobileBy as By
from hotdog.FindEither import FindEither
from Helpers.BaseTest import BaseTest
from Helpers.BasePage import CBCWebBase
from selenium.webdriver.remote.webelement import WebElement

class ShowDetailsPage(CBCWebBase):
    txtSeriesTitle = Find(by=By.CLASS_NAME, value='series-title')
    episodeTitle = Find(by=By.CLASS_NAME, value='episode-title')
    episodeNumber = Find(by=By.CLASS_NAME, value='episode-number')
    episodeDescription = Find(by=By.CLASS_NAME, value='description')
    listOfEpisodes = Finds(by=By.CLASS_NAME, value='media-thumbnail-container')
    currentSeason = Find(by=By.CLASS_NAME, value='active')


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






