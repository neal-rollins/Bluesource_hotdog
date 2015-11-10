__author__ = 'brian.menzies'
from webium import Find, Finds
from selenium import webdriver
from appium.webdriver.common.mobileby import MobileBy as By
from hotdog.FindEither import FindEither
from Helpers.BaseTest import BaseTest
from Helpers.BasePage import CBCWebBase

class CommonPage(CBCWebBase):
    btnHomeIcon = Find(by=By.CSS_SELECTOR, value='#catalog-menu > div.nav-bar-logo > a')
    btnFeatured = Find(by=By.CSS_SELECTOR, value='#catalog-menu > div.nav-bar-section.menu-toggling.toggle-mobile > ul > li:nth-child(1) > a')
    btnShows = Find(by=By.CSS_SELECTOR, value='#catalog-menu > div.nav-bar-section.menu-toggling.toggle-mobile > ul > li:nth-child(2) > a')
    btnDocumentaries = Find(by=By.CSS_SELECTOR, value='#catalog-menu > div.nav-bar-section.menu-toggling.toggle-mobile > ul > li:nth-child(3) > a')
    btnKids = Find(by=By.CSS_SELECTOR, value='#catalog-menu > div.nav-bar-section.menu-toggling.toggle-mobile > ul > li:nth-child(4) > a')
    genreDropdown = Find(by=By.CLASS_NAME, value='controls-label')
    # genreDropdown = Find(by=By.CSS_SELECTOR, value='#main-content > div > nav > div > ul > li:nth-child(2) > div > button > span')
    btnCarouselNext = Find(by=By.CSS_SELECTOR, value='#main-content > div > div > div > div > ul > li:nth-child(2) > button')
    btnCarouselPrevious = Find(by=By.CSS_SELECTOR, value='#main-content > div > div > div > div > ul > li:nth-child(1) > button')
    # txtCarouselTagline = Find(by=By.CLASS_NAME, value='tagline-title')
    txtCarouselTagline = Find(by=By.CSS_SELECTOR, value='#main-content > div > div > div > div > span > div > div > figure > figcaption > h2')

    def navigateToSection(self, SectionName):
        section = SectionName.lower()
        if section == 'home':
            self.btnHomeIcon.click()
        elif section == 'featured':
            self.btnFeatured.click()
        elif section == 'shows':
            self.btnShows.click()
        elif section == 'documentaries':
            self.btnDocumentaries.click()
        elif section == 'kids':
            self.btnKids.click()
        else:
            pass

    def clickFeaturedItem(self, listOfItems, numberOfItem):
        print(listOfItems)
        number = int(numberOfItem) - 1
        listOfItems[number].click()

    def assertDropdownIsPresent(self):
        dropdownText = self.genreDropdown.text
        loweredText = dropdownText.lower()
        assert loweredText == 'genre', 'The Genre Dropdown Could Not Be Found'

    def clickCarousel(self, directionToClick):
        direction = directionToClick.lower()
        if direction == 'left':
            self.btnCarouselPrevious.click()
        elif direction == 'right':
            self.btnCarouselNext.click()
        else:
            pass

    def assertTwoThingsEqual(self, thing1, thing2):
        assert thing1 == thing2, 'Expected Equal Values. Instead [%s] and [%s] were found' % (thing1, thing2)

    def assertTwoThingsNotEqual(self, thing1, thing2):
        assert thing1 != thing2, 'Expected Different Values. Instead [%s] and [%s] were found' % (thing1, thing2)

    def getCurrentCarouselTitle(self):
        tagline = self.txtCarouselTagline.text
        return tagline