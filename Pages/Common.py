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
    btnCarouselNext = Find(by=By.XPATH, value='//*[@id="main-content"]/div/div/div/div/ul/li[2]/button')
    btnCarouselPrevious = Find(by=By.XPATH, value='//*[@id="main-content"]/div/div/div/div/ul/li[1]/button')
    txtCarouselTagline = Find(by=By.CSS_SELECTOR, value='#main-content > div > div > div > div > span > div > div > figure > figcaption > h2')


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