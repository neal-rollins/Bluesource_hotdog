__author__ = 'brian.menzies'
import unittest
from selenium import webdriver
from time import sleep
from Helpers.BaseTest import BaseTest
from Pages.Common import CommonPage
from Pages.FeaturedPage import FeaturedPage
from Pages.ShowsPage import ShowsPage
from Pages.ShowDetailsPage import ShowDetailsPage

class HomePageTests(BaseTest):

    def test_StreamFor5Minutes(self):
        #Launch the Web App
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com/')
        common.open()
        self.driver.maximize_window()
        common.assert_element_present('navbar')
        common.assert_element_present('carousel')
        common.assert_element_present('carouselDots')

        #Navigate To Shows Page and Run Asserts
        common.navigateToSection('Shows')
        common.assert_element_present('navbar')
        common.assert_element_present('carousel')
        common.assert_element_present('carouselDots')
        shows = ShowsPage(driver=self.driver)

        #Click First Featured Item
        print(shows.getTitles())
        shows.clickOnShow(index=0)

        #Click First Episode
        showDetail = ShowDetailsPage(self)
        showDetail.clickOnEpisode(random=True)

        #Click Play
        showDetail.playVideo()
        # showDetail.pauseVideoPlayer()
        # startTime = showDetail.getTimeStamp()
        # showDetail.playVideo()

        #Let Video Play For a Minute
        sleep(55)

        #Pause Video and Record Time Stamp
        # showDetail.pauseVideoPlayer()
        # endTime = showDetail.getTimeStamp()
        # showDetail.verifyVideoHasPlayed(startTime, endTime)

    def test_TestHomeCarousel(self):
        #Launch the Web App
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com/')
        common.open()
        self.driver.maximize_window()

        #Stop the Carousel by Clicking the Pause Button
        featured = FeaturedPage(driver=self.driver)
        featured.btnPlayPauseCarousel.click()
        carouselTitle1 = featured.getCurrentCarouselTitle()
        print(carouselTitle1)

        #Click the Right Carousel Arrow
        featured.cycleThroughCarousel('Right')
        sleep(3)

        #Get Title and Compare It
        carouselTitle2 = featured.getCurrentCarouselTitle()
        print(carouselTitle2)
        self.assertNotEqual(carouselTitle1, carouselTitle2)

        #Click the Left Carousel Arrow then Compare it
        featured.cycleThroughCarousel('Left')
        carouselTitle3 = featured.getCurrentCarouselTitle()
        print(carouselTitle3)
        self.assertEqual(carouselTitle3, carouselTitle1)

    def test_EpisodeNumbers(self):
        #Launch the Web App
        common = CommonPage(driver=self.driver, url='http://project-igloo.maple.willowtreemobile.com/')
        common.open()
        self.driver.maximize_window()

        #Click Series Section
        common.navigateToSection('Shows')
        shows = ShowsPage(driver=self.driver)
        shows.navigateSubNav('all')
        showDetails = ShowDetailsPage(driver=self.driver)
        showDetails.clickOnEpisode(random=True)
        showDetails.getCurrentSeason()
        showDetails.goToPreviousSeason()