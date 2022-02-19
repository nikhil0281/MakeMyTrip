

import pytest
from selenium import webdriver
import time

from MakeMyTrip import Utilites
from MakeMyTrip.AllElementsPath import Test_AllElementsPath


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--url_value", action="store", default="dv")


@pytest.fixture(scope="class")
def launchbrowser(request):
    # a = "chrome"
    global driver
    browser_name = request.config.getoption("browser_name")
    ChromeOptions = webdriver.ChromeOptions()
    ChromeOptions.add_argument('--start-maximized')
    FireFoxOptions = webdriver.FirefoxOptions()
    FireFoxOptions.add_argument('--start-maximized')
    # ChromeOptions.add_argument('--headless')
    if browser_name == "chrome":
        (time.localtime())
        print("Chrome is launching....")
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe", options=ChromeOptions)

    elif browser_name == "firefox":
        print("firefox is launching....")
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe", options=FireFoxOptions)
    else:
        print("IE is not installed")
    driver.implicitly_wait(20)


    request.cls.driver = driver
    # yield
    # driver.close()

@pytest.fixture()
def WebSiteUrl(request):
    LifeCycle = request.config.getoption("url_value")
    # LifeCycle = "dv"
    if LifeCycle == "dv":
            url = "https://www.makemytrip.com/"
    elif LifeCycle == "qa":
            url = "https://www.google.com"
    else:
            url = "https://yahoo.com"
    return url

