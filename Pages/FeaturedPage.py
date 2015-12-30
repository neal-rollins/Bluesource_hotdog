from types import MethodType

import webium
from selenium.webdriver.remote.webelement import WebElement
from webium import Find, Finds
from appium.webdriver.common.mobileby import MobileBy as By
from webium.base_page import is_element_present

from Helpers.BasePage import CBCWebBase
from time import sleep

from Helpers.Retry import Retry


class ShowsCard(WebElement):
    imgShowBanner = Find(by=By.CLASS_NAME, value='media-banner')
    txtTitle = Find(by=By.CLASS_NAME, value='asset-title')


class FeaturedPage(CBCWebBase):

    #shows = Finds(ShowsCard, by=By.CLASS_NAME, value='media-card')
    btnActiveCarouselDot = Find(by=By.CLASS_NAME, value='carousel-dot-active')
    btnCarouselDots = Finds(by=By.CLASS_NAME, value='carousel-dot')
    btnCarouselButtons = Finds(by=By.CLASS_NAME, value='carousel-control')
    btnCarouselNext = Find(by=By.NAME, value='Next')
    txtCarouselTagline = Find(by=By.CLASS_NAME, value='tagline-title')

    syncElement =  (By.CSS_SELECTOR, '.selected[href="/"]')

    @property
    def shows(self):
        shows = self.driver.find_elements_by_class_name('media-card')
        for show in shows:
            show.__class__ = ShowsCard
            show.is_element_present = MethodType(is_element_present, show)
            show.implicitly_wait = webium.settings.implicit_timeout
        return shows

    def cycleThroughCarousel(self, directionToClick):
        carouselInfo = str(self.btnActiveCarouselDot.text)
        splitNumbers = carouselInfo.split()
        firstArrayNumber = splitNumbers[1]
        finalArrayNumber = splitNumbers[3]
        firstNumber = int(firstArrayNumber)
        finalNumber = int(finalArrayNumber) - 1

        if directionToClick == 'Right':
            number = firstNumber
            for item in range(finalNumber):
                currentCarouselTitle = self.getCurrentCarouselTitle()
                self.btnCarouselDots[number].click()
                newCarouselTitle = self.getCurrentCarouselTitle()
                assert currentCarouselTitle != newCarouselTitle, 'Expected Different Values. Instead (%s) and (%s) were found' % (currentCarouselTitle, newCarouselTitle)
                number += 1
        if directionToClick == 'Left':
            number = finalNumber -  1
            for items in range(finalNumber):
                currentCarouselTitle = self.getCurrentCarouselTitle()
                self.btnCarouselDots[number].click()
                newCarouselTitle = self.getCurrentCarouselTitle()
                print('started on ' + currentCarouselTitle)
                print('ended on ' + newCarouselTitle)
                assert currentCarouselTitle != newCarouselTitle, 'Expected Different Values. Instead (%s) and (%s) were found' % (currentCarouselTitle, newCarouselTitle)
                number -= 1

    def getCurrentCarouselTitle(self):
        tagline = self.txtCarouselTagline.text
        return tagline

    @Retry
    def getShows(self):
        shows = self.shows
        assert len(shows) > 0, "No Shows Found"
        return shows
