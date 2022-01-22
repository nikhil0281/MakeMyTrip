import time
from logging import exception

from selenium.webdriver.common.by import By
from MakeMyTrip import Utilites
from MakeMyTrip.AllElementsPath import Test_AllElementsPath
from MakeMyTrip.HomePageObjects import Test_HomePage


class Test_Flight(Test_AllElementsPath):
    global Logs
    global FlightLink
    Logs = Utilites.getlogs()



    def __init__(self,driver):
        self.driver = driver

    def OneWayRadioButton(self):
        try:
            global TestHomePageObj
            TestHomePageObj = Test_HomePage(self.driver)
            FlightNavigationLink = self.driver.find_element_by_xpath("//span[@class='false chNavText darkGreyText']")
            Utilites.webelementclick(self.driver,FlightNavigationLink)
            time.sleep(2)
            RadioValue = self.driver.find_element_by_xpath("//ul[@class='fswTabs latoBlack greyText']/li[1]").get_attribute("class")
            assert str(RadioValue) == "selected"
            Logs.info("One Way Radio Button is default selected")
            flightfrom = self.driver.find_element(By.XPATH,"//span[contains(text(),'From')]")
            Logs.info("Flight " + str(flightfrom.text) + " section is appearing")
            flightto = self.driver.find_element(By.XPATH, "//span[contains(text(),'Top')]")
            Logs.info("Flight " + str(flightto.text) + " section is appearing")


        except Exception as e:
            raise Exception(e)

    def FlightBooking(self):
        global TestHomePageObj
        try:
            TestHomePageObj = Test_HomePage(self.driver)
            FlightFromInput = TestHomePageObj.FlightFrom()
            Utilites.webelementclick(self.driver, FlightFromInput)
            TestHomePageObj.FlightFromInputBox().send_keys("Delhi")
            time.sleep(1)
            CitySelect = self.driver.find_element_by_xpath("//p[contains(text(),'New Delhi, India')]")
            Utilites.webelementclick(self.driver, CitySelect)
            print("#########")
            CityValue = self.driver.find_element_by_xpath("//input[@id='fromCity']").get_attribute("value")
            print("@@@@@@@@@")
            if str(CityValue) == "New Delhi":
                Logs.info(str(CityValue) + " is selected")
        except Exception as e:
            raise Exception(e)
        try:
            Logs.info("Verifying flight TO drop down....")
            FlightToInput = TestHomePageObj.FlightTo()
            Utilites.webelementclick(self.driver, FlightToInput)
            time.sleep(2)
            TestHomePageObj.FlightFromInputBox().send_keys("Mumbai")
            time.sleep(1)
            CitySelect1 = self.driver.find_element_by_xpath("//p[contains(text(),'Mumbai, India')]")
            Utilites.webelementclick(self.driver, CitySelect1)
            CityValue1 = self.driver.find_element_by_xpath("//input[@id='toCity']").get_attribute("value")
            if str(CityValue1) == "Mumbai":
                Logs.info(str(CityValue1) + " is selected")
            Logs.info(str(CityValue1) + " is selected")
        except Exception as e:
            raise Exception(e)


