import time
from logging import exception

import pytest

from MakeMyTrip import Utilites
from MakeMyTrip.Actvities import Test_Activites
from MakeMyTrip.FlightTab import Test_Flight
from MakeMyTrip.HolidayPackages import Test_HolidayPackages
from MakeMyTrip.HomePageObjects import Test_HomePage


@pytest.mark.usefixtures("launchbrowser")
class Test_MMT():
    global Logs
    Logs = Utilites.getlogs()


    def test_SiteOpen(self,WebSiteUrl):
        print(WebSiteUrl)
        Logs.info("Web Url is : " + str(WebSiteUrl))
        self.driver.get(WebSiteUrl)

    def test_hindipopup(self):
        global TestHomePageObj
        TestHomePageObj = Test_HomePage(self.driver)
        time.sleep(3)
        try:
            Navigation = TestHomePageObj.NavigationHeader()
            Utilites.webelementclick(self.driver, Navigation)
            Logs.info("User details section Close")
            time.sleep(1)
            HindiAlertClose = TestHomePageObj.CrossLink()
            Utilites.webelementclick(self.driver, HindiAlertClose)
            Logs.info("Hindi Alert Close")
        except:
            raise Exception("Some exception occoured")



    # def test_NavigationVerification(self):
    #     NavAllLinks = TestHomePageObj.NavigationLinks()
    #     j = 0
    #     LinksCount = len(NavAllLinks)
    #     for i in NavAllLinks:
    #         Utilites.webelementclick(self.driver,i)
    #         Logs.info(str(i.text) + " link clicked")
    #         j = j+1
    #         if j == LinksCount:
    #             Logs.info("Successfully Clicked on All links ")
    #
    # def test_flighttab(self):
    #     FlightTab = Test_Flight(self.driver)
    #     FlightTab.OneWayRadioButton()
    #     FlightTab.FlightBooking()
    #
    # def test_activite(self):
    #     ActivitesTab = Test_Activites(self.driver)
    #     ActivitesTab.Activites()

    def test_HolidayPackage(self):
        HolidayPackageTab = Test_HolidayPackages(self.driver)
        HolidayPackageTab.HolidayPackagesMethod()



    def test_print(self):
        print("Hurryyyyyyyyyyyyyyyyyyyyyyy")









