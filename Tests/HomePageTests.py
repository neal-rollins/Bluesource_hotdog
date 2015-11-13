from Pages.ShowsPage import ShowsPage

__author__ = 'brian.menzies'
import unittest
from selenium import webdriver
from time import sleep
from Helpers.BaseTest import BaseTest
from Pages.Common import CommonPage
from Pages.ShowDetailsPage import ShowDetailsPage

class HomePageTests(BaseTest):



    def test_StreamFor5Minutes(self):
        #Launch the Web App
        common = CommonPage(driver=self.driver)
        self.driver.maximize_window()
        self.driver.get('http://project-igloo.maple.willowtreemobile.com/')

        #Click Featured Item
        sleep(10)
        featuredList = self.driver.find_elements_by_class_name('asset-info')
        common.clickFeaturedItem(featuredList, 1)

        #Click First Episode
        showDetail = ShowDetailsPage(self)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        showList = self.driver.find_elements_by_class_name('media-image')
        showDetail.clickShow(showList, 1)

        #Click Play
        showDetail.playVideo()
        showDetail.pauseVideoPlayer()
        startTime = showDetail.getTimeStamp()
        showDetail.playVideo()

        #Let Video Play For a Minute
        sleep(55)

        #Pause Video and Record Time Stamp
        showDetail.pauseVideoPlayer()
        endTime = showDetail.getTimeStamp()
        showDetail.verifyVideoHasPlayed(startTime, endTime)

    def test_TestHomeCarousel(self):
        #Launch the Web App
        common = CommonPage(driver=self.driver)
        self.driver.maximize_window()
        self.driver.get('http://project-igloo.maple.willowtreemobile.com/')
        sleep(5)
        #Click the Right Carousel Arrow
        carouselTitle1 = common.getCurrentCarouselTitle()
        print(carouselTitle1)
        common.clickCarousel('Right')

        #Get Title and Compare It
        carouselTitle2 = common.getCurrentCarouselTitle()
        print(carouselTitle2)
        common.assertTwoThingsNotEqual(carouselTitle1, carouselTitle2)

        #Click the Left Carousel Arrow then Compare it
        common.clickCarousel('Left')
        carouselTitle3 = common.getCurrentCarouselTitle()
        print(carouselTitle3)
        common.assertTwoThingsEqual(carouselTitle3, carouselTitle1)

    def test_EpisodeNumbers(self):
        #Launch the Web App
        common = CommonPage(driver=self.driver)
        self.driver.maximize_window()
        self.driver.get('http://project-igloo.maple.willowtreemobile.com/')
        sleep(5)

        #Click Series Section
        common.navigateToSection('Shows')
        showDetails = ShowDetailsPage(driver=self.driver)
        showList = self.driver.find_elements_by_class_name('media-image')
        showDetails.clickShow(showList, 0)
        showDetails.getCurrentSeason()
        showDetails.goToPreviousSeason()

