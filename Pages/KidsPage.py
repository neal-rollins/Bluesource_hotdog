from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium import Find, Finds
from Helpers.BasePage import CBCWebBase
import random as rand


class SubNav(WebElement):
    btnAll = Find(by=By.LINK_TEXT, value='ALL')


class ShowsCard(WebElement):
    imgShowBanner = Find(by=By.CLASS_NAME, value='media-banner')
    txtTitle = Find(by=By.CLASS_NAME, value='asset-title')


class KidsPage(CBCWebBase):
    subnav = Find(SubNav, by=By.CLASS_NAME, value='menu-bar')
    shows = Finds(ShowsCard, by=By.CLASS_NAME, value='media-card')

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
