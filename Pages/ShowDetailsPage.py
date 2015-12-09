import webium
from selenium.webdriver.remote.webelement import WebElement
import random as rand
__author__ = 'brian.menzies'
from webium import Find, Finds
from appium.webdriver.common.mobileby import MobileBy as By
from hotdog.FindEither import FindEither
from Helpers.BaseTest import BaseTest
from Helpers.BasePage import CBCWebBase
from selenium.webdriver.remote.webelement import WebElement
from time import sleep

class EpisodeDetail(WebElement):
    imgShowImage = Find(by=By.CLASS_NAME, value='media-image')
    txtEpisodeDetail = Find(by=By.CLASS_NAME, value='episode-meta')
    txtEpisodeTitle = FindEither(selectors=[[By.CLASS_NAME, 'episode-title'],
                                  [By.CLASS_NAME, 'asset-title']])
    txtEpisodeDescription = Find(by=By.CLASS_NAME, value='description')
    txtEpisodeNumber = Find(by=By.CLASS_NAME, value='episode-number-short')
    txtDuration = Find(by=By.CSS_SELECTOR, value="li[aria-label~='Duration:']")

class ShowDetailsPage(CBCWebBase):
    txtSeriesTitle = Find(by=By.CLASS_NAME, value='series-title')
    txtActiveSeason = Find(by=By.CLASS_NAME, value='active')
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
        season = self._driver.find_elements_by_id('selected')
        season[0].click()
        print(season)

    def goToPreviousSeason(self):
        #Instantiates the Variables
        i = 0
        listOfSeasons = []

        #Finds the Season Name as it is in a list of Elements
        activeSeasonSearch = self.driver.find_elements_by_class_name('active')

        #Takes the Names of the Found Elements and Puts Them in An Array
        for season in range(len(activeSeasonSearch)):
            listOfSeasons.insert(i, activeSeasonSearch[i].text)
            i += 1

        #Splits the Season and Its Number Out
        currentSeason = listOfSeasons[2].split()
        currentSeasonNumber = int(currentSeason[1])
        assert currentSeasonNumber > 1, 'There is only One Season Present. A Previous Season Can Not Be Navigated To.'
        previousSeasonNumber = currentSeasonNumber - 1

        #Searches for the Previous Season and Clicks on It
        seasonToFind = 'SEASON ' + str(previousSeasonNumber)
        Find(context=self, by=By.PARTIAL_LINK_TEXT, value=seasonToFind).click()

    def goToNextSeason(self):
        #Instantiates the Variables
        i = 0
        listOfSeasons = []

        #Finds the Season Name as it is in a list of Elements
        activeSeasonSearch = self.driver.find_elements_by_class_name('active')

        #Takes the Names of the Found Elements and Puts Them in An Array
        for season in range(len(activeSeasonSearch)):
            listOfSeasons.insert(i, activeSeasonSearch[i].text)
            i += 1

        #Splits the Season and Its Number Out
        currentSeason = listOfSeasons[2].split()
        currentSeasonNumber = int(currentSeason[1])
        previousSeasonNumber = currentSeasonNumber + 1

        #Searches for the Previous Season and Clicks on It
        seasonToFind = 'SEASON ' + str(previousSeasonNumber)
        Find(context=self, by=By.PARTIAL_LINK_TEXT, value=seasonToFind).click()

    def verifyOnSeason(self, seasonNumber):
        i = 0
        listOfSeasons = []

        #Finds the Season Name as it is in a list of Elements
        activeSeasonSearch = self.driver.find_elements_by_class_name('active')

        #Takes the Names of the Found Elements and Puts Them in An Array
        for season in range(len(activeSeasonSearch)):
            listOfSeasons.insert(i, activeSeasonSearch[i].text)
            i += 1

        #Splits the Season and Its Number Out
        currentSeason = listOfSeasons[2].split()
        currentSeasonNumber = int(currentSeason[1])

        assert seasonNumber == currentSeasonNumber, 'Expected Value [%s]. Actual Value was [%s]' % (seasonNumber, currentSeasonNumber)

    def sync(self, title, timeout=20):
        self.driver.implicitly_wait(timeout)
        Find(by=By.XPATH, value="//h1[contains(@class, 'series-title') and text() = '%s']" % title, context=self)
        self.driver.implicitly_wait(webium.settings.implicit_timeout)