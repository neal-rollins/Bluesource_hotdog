from time import sleep, time
from types import MethodType

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium import Find, Finds
from webium.base_page import is_element_present, webium

from Helpers.BasePage import CBCWebBase
import random as rand

from Helpers.Retry import Retry


class GenreDropdown(WebElement):
    btnBiography = Find(by=By.LINK_TEXT, value='BIOGRAPHY')
    btnHealth = Find(by=By.LINK_TEXT, value='HEALTH')
    btnScienceTech = Find(by=By.LINK_TEXT, value='SCIENCE & TECHNOLOGY')
    btnWildlife = Find(by=By.LINK_TEXT, value='WILDLIFE')
    listDropdownOptions = Finds(by=By.CLASS_NAME, value='dropdown-option')


class SubNav(WebElement):
    btnAll = Find(by=By.LINK_TEXT, value='ALL')
    btnGenre = Find(by=By.CSS_SELECTOR, value='.dropdown .controls')
    dropdownGenre = Find(GenreDropdown, by=By.CLASS_NAME, value='menu')
    mobileControls = Find(by=By.CLASS_NAME, value='selected-mobile')

    def openMenuIfMobile(self):
        try:
            self.mobileControls.click()
            sleep(2)
            self.isMobile = True
            return True
        except:
            return False

    @property
    def currentGenre(self):
        try:
            if self.mobileControls.is_displayed():
                return self.mobileControls.text.lower().replace('+', '').replace('-','').strip()
            else:
                return self.btnGenre.text.lower()
        except:
            return self.btnGenre.text.lower()

class ShowsCard(WebElement):
    imgShowBanner = Find(by=By.CLASS_NAME, value='media-banner')
    txtTitle = Find(by=By.CLASS_NAME, value='asset-title')


class DocumentariesPage(CBCWebBase):
    subnav = Find(SubNav, by=By.CLASS_NAME, value='menu-bar')
   # shows = Finds(ShowsCard, by=By.CLASS_NAME, value='media-card')
    syncElement =  (By.CSS_SELECTOR, '.selected[href="/documentaries/"]')

    @property
    def shows(self):
        shows = self.driver.find_elements_by_class_name('media-card')
        for show in shows:
            show.__class__ = ShowsCard
            show.is_element_present = MethodType(is_element_present, show)
            show.implicitly_wait = webium.settings.implicit_timeout
        return shows

    @property
    def isMobile(self):
        return self.subnav.mobileControls.is_displayed()

    def navigateSubNav(self, title):
        if title.lower() == 'all':
            self.subnav.btnAll.click()
        else:
            raise ValueError('[%s] is not a valid subsection' % title)

    def getGenreList(self):
        isMobile = self.subnav.openMenuIfMobile()
        self.driver.execute_script("arguments[0].click()", self.subnav.btnGenre)
        sleep(1)
        genrelist = []
        for genre in self.subnav.dropdownGenre.listDropdownOptions:
            if isMobile:
                genrelist.append(genre.text.replace('+', '').replace('-','').strip())
            else:
                genrelist.append(genre.text)
        self.subnav.btnGenre.click()
        self.subnav.openMenuIfMobile()
        return genrelist

    def navigateGenreDropdown(self, genre):
        self.subnav.openMenuIfMobile()
        self.subnav.btnGenre.click()
        try:
            optGenre = Find(by=By.LINK_TEXT, value=genre.upper(), context=self.subnav.dropdownGenre)
            optGenre.click()
        except:
            raise ValueError('Failed to navigate to genre [%s]' % genre)


    def getTitles(self):
        titles = []
        for show in self.shows:
            titles.append(show.txtTitle.text)

        return titles

    @Retry
    def getShows(self):
        shows = self.shows
        assert len(shows) > 0, "No Shows Found"
        return shows

    @Retry
    def clickOnShow(self, title=None, index=0, random=False):

        if random:
            show = rand.choice(self.shows)
            showTitle = show.txtTitle.text
            show.imgShowBanner.click()
        elif title:
            found = False
            for show in self.shows:
                if show.txtTitle.text.lower() == title.lower():
                    showTitle = show.txtTitle.text
                    show.imgShowBanner.click()
                    found = True
                    break
            if not found:
                raise AssertionError('Could not find show with title [%s]' % title)
        else:
            showTitle = self.shows[index].txtTitle.text
            self.shows[index].imgShowBanner.click()

        return showTitle
