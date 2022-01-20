import inspect
import logging
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class Test_HomePage:
    AlertHindiXpath = (By.XPATH, "//span[@class='newGreenTag appendLeft5']")

    def __init__(self,driver):
        self.driver = driver

    def AlertHindi(self):
        return self.driver.find_element(*Test_HomePage.AlertHindiXpath)