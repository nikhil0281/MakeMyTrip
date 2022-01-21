import time
from logging import exception

from selenium.webdriver.common.by import By
from MakeMyTrip import Utilites

class Test_Flight:
    global Logs
    global FlightLink
    Logs = Utilites.getlogs()



    def __init__(self,driver):
        self.driver = driver

    def OneWayRadioButton(self):
        try:
            FlightLink = self.driver.find_element_by_xpath("//span[@class='false chNavText darkGreyText']")
            Utilites.webelementclick(self.driver,FlightLink)
            time.sleep(2)
            RadioValue = self.driver.find_element_by_xpath("//ul[@class='fswTabs latoBlack greyText']/li[1]").get_attribute("class")
            assert str(RadioValue) == "selected"
            Logs.info("One Way Radio Button is default selected")

        except exception as e:
            Logs.info(e)

