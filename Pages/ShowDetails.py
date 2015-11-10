__author__ = 'brian.menzies'
from webium import Find, Finds
from appium.webdriver.common.mobileby import MobileBy as By
from hotdog.FindEither import FindEither
from Helpers.BaseTest import BaseTest
from Helpers.BasePage import CBCWebBase

class ShowDetailsPage(CBCWebBase):
    episodeTitle = Find(by=By.CLASS_NAME, value='episode-title')
    episodeNumber = Find(by=By.CLASS_NAME, value='episode-number')
    episodeDescription = Find(by=By.CLASS_NAME, value='description')

    currentSeason = Find(by=By.CLASS_NAME, value='active')
    # currentSeason = Find(by=By.CSS_SELECTOR, value='#main-content > div > nav > div > div > div > ul > li.selected > a')

    def clickShow(self, numberOfShowToClick):
        self.episodeTitle.click()
