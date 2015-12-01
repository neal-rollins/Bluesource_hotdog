from selenium.webdriver.remote.webelement import WebElement
from webium import Find, Finds
from appium.webdriver.common.mobileby import MobileBy as By
from Helpers.BasePage import CBCWebBase
from time import sleep


class ShowsCard(WebElement):
    imgShowBanner = Find(by=By.CLASS_NAME, value='media-banner')
    txtTitle = Find(by=By.CLASS_NAME, value='asset-title')


class FeaturedPage(CBCWebBase):

    shows = Finds(ShowsCard, by=By.CLASS_NAME, value='media-card')
    btnActiveCarouselDot = Find(by=By.CLASS_NAME, value='carousel-dot-active')
    btnCarouselDots = Finds(by=By.CLASS_NAME, value='carousel-dot')
    btnCarouselButtons = Finds(by=By.CLASS_NAME, value='carousel-control')
    btnCarouselNext = Find(by=By.NAME, value='Next')
    txtCarouselTagline = Find(by=By.CLASS_NAME, value='tagline-title')
    syncElement =  (By.CSS_SELECTOR, '.selected[href="/"]')

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