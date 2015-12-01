from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium import Find, Finds
from Helpers.BasePage import CBCWebBase
import random as rand

class GenreDropdown(WebElement):
    btnBiography = Find(by=By.LINK_TEXT, value='BIOGRAPHY')
    btnHealth = Find(by=By.LINK_TEXT, value='HEALTH')
    btnScienceTech = Find(by=By.LINK_TEXT, value='SCIENCE & TECHNOLOGY')
    btnWildlife = Find(by=By.LINK_TEXT, value='WILDLIFE')
    listDropdownOptions = Finds(by=By.CLASS_NAME, value='dropdown-option')


class SubNav(WebElement):
    btnAll = Find(by=By.LINK_TEXT, value='ALL')
    btnGenre = Find(by=By.CLASS_NAME, value='dropdown')
    dropdownGenre = Find(GenreDropdown, by=By.CLASS_NAME, value='menu')


class ShowsCard(WebElement):
    imgShowBanner = Find(by=By.CLASS_NAME, value='media-banner')
    txtTitle = Find(by=By.CLASS_NAME, value='asset-title')


class DocumentariesPage(CBCWebBase):
    subnav = Find(SubNav, by=By.CLASS_NAME, value='menu-bar')
    shows = Finds(ShowsCard, by=By.CLASS_NAME, value='media-card')
    syncElement =  (By.CSS_SELECTOR, '.selected[href="/documentaries/"]')

    def navigateSubNav(self, title):
        if title.lower() == 'all':
            self.subnav.btnAll.click()
        else:
            raise ValueError('[%s] is not a valid subsection' % title)

    def getGenreList(self):
        self.subnav.btnGenre.click()
        sleep(1)
        genrelist = []
        for genre in self.subnav.dropdownGenre.listDropdownOptions:
            genrelist.append(genre.text)
        self.subnav.btnGenre.click()
        return genrelist

    def navigateGenreDropdown(self, genre):
        self.subnav.btnGenre.click()

        if genre.lower() == 'biography':
            self.subnav.dropdownGenre.btnBiography.click()
        elif genre.lower() == 'health':
            self.subnav.dropdownGenre.btnHealth.click()
        elif genre.lower() == 'science & technology':
            self.subnav.dropdownGenre.btnScienceTech.click()
        elif genre.lower() == 'wildlife':
            self.subnav.dropdownGenre.btnWildlife.click()
        else:
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
