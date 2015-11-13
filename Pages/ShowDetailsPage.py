from selenium.webdriver.remote.webelement import WebElement
import random as rand
__author__ = 'brian.menzies'
from webium import Find, Finds
from appium.webdriver.common.mobileby import MobileBy as By
from hotdog.FindEither import FindEither
from Helpers.BaseTest import BaseTest
from Helpers.BasePage import CBCWebBase
from selenium.webdriver.remote.webelement import WebElement

class EpisodeDetail(WebElement):
    imgShowImage = Find(by=By.CLASS_NAME, value='media-image')
    txtEpisodeDetail = Find(by=By.CLASS_NAME, value='episode-meta')
    txtEpisodeTitle = Find(by=By.CLASS_NAME, value='episode-title')
    txtEpisodeDescription = Find(by=By.CLASS_NAME, value='description')

class ShowDetailsPage(CBCWebBase):
    txtSeriesTitle = Find(by=By.CLASS_NAME, value='series-title')
    listEpisodes = Finds(EpisodeDetail, by=By.CSS_SELECTOR, value='figure.media-card')
    imgHero = Find(by=By.CLASS_NAME, value='media-hero')
    imgAd = Find(by=By.ID, value='showAd')


    def clickOnEpisode(self, title=None, index=0, random=False):

        if random:
            episode = rand.choice(self.listEpisodes)
            episodeTitle = episode.txtEpisodeTitle.text
            episode.click()
        elif title:
            found = False
            for episode in self.listEpisodes:
                if episode.txtEpisodeTitle.text.lower() == title.lower():
                    episodeTitle = episode.txtEpisodeTitle.text
                    episode.click()
                    found = True
                    break
            if not found:
                raise AssertionError('Could not find show with title [%s]' % title)
        else:
            episodeTitle = self.listEpisodes[index].txtEpisodeTitle.text
            self.listEpisodes[index].click()

        return episodeTitle

    def getCurrentSeason(self):
        season = Find(context=self, by=By.CLASS_NAME, value='active')
        season.text
        print(season.text)
        return season.text

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






