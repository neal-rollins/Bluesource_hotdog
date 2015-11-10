__author__ = 'brian.menzies'
from webium import Find, Finds
from selenium import webdriver
from appium.webdriver.common.mobileby import MobileBy as By
from hotdog.FindEither import FindEither
from Helpers.BaseTest import BaseTest
from Helpers.BasePage import CBCWebBase

class CommonPage(CBCWebBase):
    btnHomeIcon = Find(by=By.CLASS_NAME, value='client-logo-nav')
    # btnHomeIcon = Find(by=By.CSS_SELECTOR, value='#catalog-menu > div.nav-bar-logo > a')
    btnFeatured = Find(by=By.CLASS_NAME, value='active')
    # btnFeatured = Find(by=By.CSS_SELECTOR, value='#catalog-menu > div.nav-bar-section.menu-toggling.toggle-mobile > ul > li:nth-child(1) > a')
    btnShows = Find(by=By.CLASS_NAME, value='/shows/')
    # btnShows = Find(by=By.CSS_SELECTOR, value='#catalog-menu > div.nav-bar-section.menu-toggling.toggle-mobile > ul > li:nth-child(2) > a')
    btnDocumentaries = Find(by=By.CLASS_NAME, value='/documentaries/')
    # btnDocumentaries = Find(by=By.CSS_SELECTOR, value='#catalog-menu > div.nav-bar-section.menu-toggling.toggle-mobile > ul > li:nth-child(3) > a')
    btnKids = Find(by=By.CLASS_NAME, value='/kids/')
    # btnKids = Find(by=By.CSS_SELECTOR, value='#catalog-menu > div.nav-bar-section.menu-toggling.toggle-mobile > ul > li:nth-child(4) > a')
    genreDropdown = Find(by=By.CLASS_NAME, value='controls-label')
    # genreDropdown = Find(by=By.CSS_SELECTOR, value='#main-content > div > nav > div > ul > li:nth-child(2) > div > button > span')


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

    def clickFeaturedItem(self, numberOfItem):
        listOfFeaturedItems = Finds(by=By.CLASS_NAME, value='asset-info')
        listOfFeaturedItems[numberOfItem].click()

    def assertDropdownIsPresent(self):
        dropdownText = self.genreDropdown.text
        loweredText = dropdownText.lower()
        assert loweredText == 'genre', 'The Genre Dropdown Could Not Be Found'

