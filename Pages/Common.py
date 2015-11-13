__author__ = 'brian.menzies'
from webium import Find, Finds
from appium.webdriver.common.mobileby import MobileBy as By
from Helpers.BasePage import CBCWebBase
from selenium.webdriver.remote.webelement import WebElement


class NavBar(WebElement):
    btnHome = Find(by=By.CLASS_NAME, value='client-logo-nav')
    btnShows = Find(by=By.LINK_TEXT, value='SHOWS')
    btnFeatured = Find(by=By.LINK_TEXT, value='FEATURED')
    btnDocumentaries = Find(by=By.LINK_TEXT, value='DOCUMENTARIES')
    btnKids = Find(by=By.LINK_TEXT, value='KIDS')


class CommonPage(CBCWebBase):
    navbar = Find(ui_type=NavBar, by=By.CLASS_NAME, value='nav-menu')
    genreDropdown = Find(by=By.CLASS_NAME, value='controls-label')
    loadingContainer = Find(by=By.CLASS_NAME, value='loading-container')
    loadingIndicator = Find(by=By.CLASS_NAME, value='loading-indicator loading')
    loadingContent = Find(by=By.CLASS_NAME, value='loading')
    carousel = Find(by=By.CLASS_NAME, value='carousel')
    carouselDots = Find(by=By.CLASS_NAME, value='carousel-dots')

    def navigateToSection(self, SectionName):
        section = SectionName.lower()
        if section.lower() == 'home':
            self.navbar.btnHome.click()
        elif section.lower() == 'featured':
            self.navbar.btnFeatured.click()
        elif section.lower() == 'shows':
            self.navbar.btnShows.click()
        elif section.lower() == 'documentaries':
            self.navbar.btnDocumentaries.click()
        elif section.lower() == 'kids':
            self.navbar.btnKids.click()
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


    def assertTwoThingsEqual(self, thing1, thing2):
        assert thing1 == thing2, 'Expected Equal Values. Instead [%s] and [%s] were found' % (thing1, thing2)

    def assertTwoThingsNotEqual(self, thing1, thing2):
        assert thing1 != thing2, 'Expected Different Values. Instead [%s] and [%s] were found' % (thing1, thing2)