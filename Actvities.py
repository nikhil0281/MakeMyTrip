import time
from logging import exception

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from MakeMyTrip import Utilites
from MakeMyTrip.AllElementsPath import Test_AllElementsPath
from MakeMyTrip.HomePageObjects import Test_HomePage


class Test_Activites(Test_AllElementsPath):
    global Logs
    global MoreActivitesText
    Logs = Utilites.getlogs()
    MoreActivitesText = []

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
                a = ActionChains(self.driver)
                a.move_to_element(ActivityMoreLink).perform()
                MoreActivitesWebElementList = TestHomePageObj.ActivitesList()
                for ActivitesText in MoreActivitesWebElementList:
                    MoreActivitesText.append(ActivitesText.text)
                LISTOFALLACTIVITES = self.ListOfActivites()
                j = 0
                for MAT in MoreActivitesText:
                    try:
                        assert MAT ==  LISTOFALLACTIVITES[j]
                        Logs.info(str(MAT) + " Exist in drop down")
                    except Exception as e:
                        Logs.error(str(MAT) + " Not exist in drop down")
                        raise Exception(e)
                    j = j+1

            except AssertionError:
                Logs.error("Activity link doesn't exist")

        except Exception as e:
            raise Exception(e)

    def ListOfActivites(self):
        listofact = ["Charter Flights", "Activities", "Trip Ideas", "Giftcards", "Nearby Getaways", "Trip Money"]
        return listofact

