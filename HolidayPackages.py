import time
from logging import exception

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from MakeMyTrip import Utilites
from MakeMyTrip.AllElementsPath import Test_AllElementsPath
from MakeMyTrip.HomePageObjects import Test_HomePage


class Test_HolidayPackages(Test_AllElementsPath):
    global Logs
    Logs = Utilites.getlogs()

    def __init__(self, driver):
        self.driver = driver

    def HolidayPackagesMethod(self):
        global TestHomePageObj

        TestHomePageObj = Test_HomePage(self.driver)
        HolidayPackageClick = TestHomePageObj.HolidayPackageTab()
        time.sleep(3)
        Utilites.webelementclick(self.driver,HolidayPackageClick)
        Logs.info(":::::::HolidayPackages Tab clicked successfully::::")
        HPDestinationsClick = TestHomePageObj.HPDestinations()
        Utilites.webelementclick(self.driver,HPDestinationsClick)
        HPDestinationsGoaClick = TestHomePageObj.HPDestinationGoa()
        Utilites.webelementclick(self.driver,HPDestinationsGoaClick)
        CurrentWindow = Utilites.currentwindowhandle(self.driver)
        Logs.info("Current window handle is :")
        Logs.info(CurrentWindow)
        AllWindows = Utilites.AllWindowHandles(self.driver)
        Logs.info("All Window Handles are :")
        Logs.info(AllWindows)
        Utilites.SwitchWindow(self.driver, AllWindows[1])
        CurrentWindow1 = Utilites.currentwindowhandle(self.driver)
        Logs.info("Current window handle is :")
        Logs.info(CurrentWindow1)

