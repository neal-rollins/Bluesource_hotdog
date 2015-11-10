__author__ = 'brian.menzies'
import unittest
from selenium import webdriver
from time import sleep
from Helpers.BaseTest import BaseTest
from Pages.Common import CommonPage
from Pages.ShowDetails import ShowDetailsPage

class HomePageTests(BaseTest):

    def test_NavigateToSeries(self):
        #Launch the Web App
        self.launchWebApp()

        #Web App is Launched, Navigate to Shows Section
        common = CommonPage(driver=self.driver)
        common.navigateToSection('Shows')
        common.assertDropdownIsPresent()

    def test_StreamFor5Minutes(self):
        common = CommonPage(self)
        common.clickFeaturedItem(1)
        showDetail = ShowDetailsPage(self)
        showDetail.clickShow(1)





