from webium import Find, Finds
from appium.webdriver.common.mobileby import MobileBy as By
from Helpers.BasePage import CBCWebBase

class FeaturedPage(CBCWebBase):
    btnCarouselButtons = Finds(by=By.CLASS_NAME, value='carousel-control')
    btnPlayPauseCarousel = Find(by=By.CLASS_NAME, value='carousel-play-pause')
    txtCarouselTagline = Find(by=By.CLASS_NAME, value='tagline-title')
    # txtCarouselTagline = Find(by=By.CSS_SELECTOR, value='#main-content > div > div > div > div > span > div > div > figure > figcaption > h2')

    def cycleThroughCarousel(self, directionToClick):
        carouselButtons = self.btnCarouselButtons
        if directionToClick == 'Left':
            carouselButtons[0].click()
        elif directionToClick == 'Right':
            carouselButtons[1].click()
        else:
            pass

    def getCurrentCarouselTitle(self):
        tagline = self.txtCarouselTagline.text
        return tagline