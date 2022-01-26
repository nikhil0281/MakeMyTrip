import time
from logging import exception

from selenium.webdriver.common.by import By
from MakeMyTrip import Utilites
from MakeMyTrip.AllElementsPath import Test_AllElementsPath
from MakeMyTrip.HomePageObjects import Test_HomePage


class Test_Activites(Test_AllElementsPath):
    global Logs
    Logs = Utilites.getlogs()

    def __init__(self, driver):
        self.driver = driver

    def Activites(self):
        try:
            global TestHomePageObj

            TestHomePageObj = Test_HomePage(self.driver)
            MMTLogoLink = TestHomePageObj.MMTLogoClick()
            Utilites.webelementclick(self.driver, MMTLogoLink)
            time.sleep(3)
            Logs.info("::::::::::::::Verifying Activites tab::::::::::::::::::::::::::")
            Activitylink = TestHomePageObj.ActivitiesTab()
            Utilites.webelementclick(self.driver, Activitylink)
            ActivityMoreLink = TestHomePageObj.ActivitiesMore()
            try:
                assert ActivityMoreLink
                Logs.info("Activity More link exist")
                MoreActivitesList = TestHomePageObj.ActivitesList()
                for i in MoreActivitesList:
                    Logs.info(str(i.text))
                    if str(i.text) == "Charter Flights":
                        Logs.info(str(i.text) + " exist in list")
                    elif str(i.text) == "Activities":
                        Logs.info(str(i.text) + " exist in list")
                    elif str(i.text) == "Trip Ideas":
                        Logs.info(str(i.text) + " exist in list")
                    elif str(i.text) == "Giftcards":
                        Logs.info(str(i.text) + " exist in list")
                    elif str(i.text) == "Nearby Getaways":
                        Logs.info(str(i.text) + " exist in list")
                    elif str(i.text) == "Trip Money":
                        Logs.info(str(i.text) + " exist in list")
                    else:
                        Logs.error(str(i.text) + " Not found in list")

            except AssertionError:
                Logs.error("Activity link doesn't exist")

        except Exception as e:
            raise Exception(e)

