from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium import Find, Finds
from Helpers.BasePage import CBCWebBase
import random as rand

class GenreDropdown(WebElement):
    btnNewsCurrentAffairs = Find(by=By.LINK_TEXT, value='NEWS & CURRENT AFFAIRS')
    btnComedy = Find(by=By.LINK_TEXT, value='COMEDY')
    btnDocumentary = Find(by=By.LINK_TEXT, value='DOCUMENTARY')
    btnDrama = Find(by=By.LINK_TEXT, value='DRAMA')
    listDropdownOptions = Finds(by=By.CLASS_NAME, value='dropdown-option')


class SubNav(WebElement):
    btnNewReleases = Find(by=By.LINK_TEXT, value='NEW RELEASES')
    btnAll = Find(by=By.LINK_TEXT, value='ALL')
    btnGenre = Find(by=By.CSS_SELECTOR, value='.dropdown .controls')
    dropdownGenre = Find(GenreDropdown, by=By.CLASS_NAME, value='menu')


class ShowsCard(WebElement):
    imgShowBanner = Find(by=By.CLASS_NAME, value='media-banner')
    txtTitle = Find(by=By.CLASS_NAME, value='asset-title')


class ShowsPage(CBCWebBase):
    subnav = Find(SubNav, by=By.CLASS_NAME, value='menu-bar')
    shows = Finds(ShowsCard, by=By.CLASS_NAME, value='media-card')
    syncElement =  (By.CSS_SELECTOR, '.selected[href="/shows/"]')

    def navigateSubNav(self, title):
        if title.lower() == 'new releases':
            self.subnav.btnNewReleases.click()
        elif title.lower() == 'all':
            self.subnav.btnAll.click()
        else:
            raise ValueError('[%s] is not a valid subsection' % title)

    def getGenreList(self):
        self.driver.execute_script("arguments[0].click()", self.subnav.btnGenre)
        sleep(1)
        genrelist = []
        for genre in self.subnav.dropdownGenre.listDropdownOptions:
            genrelist.append(genre.text)
        self.subnav.btnGenre.click()
        return genrelist

    def navigateGenreDropdown(self, genre):
        self.subnav.btnGenre.click()
        try:
            optGenre = Find(by=By.LINK_TEXT, value=genre.upper(), context=self.subnav.dropdownGenre)
            optGenre.click()
        except:
            raise ValueError('[%s] is not a valid genre' % genre)


    def getTitles(self):
        titles = []
        for show in self.shows:
            titles.append(show.txtTitle.text)

        return titles

    def clickOnShow(self, title=None, index=0, random=False):

        if random:
            show = rand.choice(self.shows)
            showTitle = show.txtTitle.text
            show.imgShowBanner.click()
        elif title is not None:
            found = False
            for show in self.shows:
                showTitle = show.txtTitle.text
                if showTitle.lower() == title.lower():
                    show.imgShowBanner.click()
                    found = True
                    break
            if not found:
                raise AssertionError('Could not find show with title [%s]' % title)
        else:
            showTitle = self.shows[index].txtTitle.text
            self.shows[index].imgShowBanner.click()

        return showTitle
