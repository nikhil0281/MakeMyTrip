import inspect
import logging
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class Test_HomePage:
    AlertHindiXpath = (By.CLASS_NAME, "font20 latoBlack blackText appendBottom5 makeFlex hrtlCenter")
    AlertCrossButton = (By.XPATH, "//span[@class='langCardClose']")
    NavHeader = (By.XPATH,"//div[@class='loginModal displayBlock modalLogin dynHeight personal ']")
    NavLink = (By.XPATH,"//ul[@class='makeFlex font12']/li/a/span/following-sibling::span")

    def __init__(self,driver):
        self.driver = driver

    def AlertHindi(self):
        return self.driver.find_element(*Test_HomePage.AlertHindiXpath)

    def CrossLink(self):
        return self.driver.find_element(*Test_HomePage.AlertCrossButton)

    def NavigationHeader(self):
        return self.driver.find_element(*Test_HomePage.NavHeader)

    def NavigationLinks(self):
        return  self.driver.find_elements(*Test_HomePage.NavLink)