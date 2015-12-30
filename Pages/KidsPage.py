from time import sleep
from types import MethodType

import webium
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium import Find, Finds
from webium.base_page import is_element_present

from Helpers.BasePage import CBCWebBase
import random as rand

from Helpers.Retry import Retry


class SubNav(WebElement):
    btnAll = Find(by=By.LINK_TEXT, value='ALL')
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


class KidsPage(CBCWebBase):
    subnav = Find(SubNav, by=By.CLASS_NAME, value='menu-bar')
    #shows = Finds(ShowsCard, by=By.CLASS_NAME, value='media-card')
    syncElement =  (By.CSS_SELECTOR, '.selected[href="/kids/"]')

    @property
    def shows(self):
        shows = self.driver.find_elements_by_class_name('media-card')
        for show in shows:
            show.__class__ = ShowsCard
            show.is_element_present = MethodType(is_element_present, show)
            show.implicitly_wait = webium.settings.implicit_timeout
        return shows

    def navigateSubNav(self, title):
        if title.lower() == 'all':
            self.subnav.btnAll.click()
        else:
            raise ValueError('[%s] is not a valid subsection' % title)

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
        shows = self.getShows()
        if random:
            show = rand.choice(shows)
            showTitle = show.txtTitle.text
            show.imgShowBanner.click()
        elif title:
            found = False
            for show in shows:
                if show.txtTitle.text.lower() == title.lower():
                    showTitle = show.txtTitle.text
                    show.imgShowBanner.click()
                    found = True
                    break
            if not found:
                raise AssertionError('Could not find show with title [%s]' % title)
        else:
            showTitle = shows[index].txtTitle.text
            shows[index].imgShowBanner.click()

        return showTitle
