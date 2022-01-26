import inspect
import logging
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from MakeMyTrip import Utilites
from MakeMyTrip.AllElementsPath import Test_AllElementsPath


class Test_HomePage(Test_AllElementsPath):
    AlertHindiXpath = Test_AllElementsPath.AlertHindiXpath
    AlertCrossButton = Test_AllElementsPath.AlertCrossButton
    NavHeader = Test_AllElementsPath.NavHeader
    NavLink = Test_AllElementsPath.NavLink
    Flight_From_City = Test_AllElementsPath.Flight_From_Keyword
    MMTLogo = Test_AllElementsPath.MMTLogo_Keyword
    Activities = Test_AllElementsPath.Activity_Tab_Keyword

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

    def FlightFrom(self):
        return self.driver.find_element(*Test_HomePage.Flight_From_City)

    def FlightTo(self):
        return self.driver.find_element(*self.Flight_To_City)

    def FlightFromInputBox(self):
        return self.driver.find_element(*self.Flight_From_City_Text_Box)

    def FlightToInputBox(self):
        return self.driver.find_element(*self.Flight_To_City_Text_Box)

    def SearchButton(self):
        return self.driver.find_element(*self.Search_Button_Keyword)

    def FlightSearch(self):
        return self.driver.find_elements(*self.Flight_Search_Results_Keyword)

    def MMTLogoClick(self):
        return self.driver.find_element(*self.MMTLogo)

    def ActivitiesTab(self):
        return self.driver.find_element(*self.Activities)

    def ActivitiesMore(self):
        return self.driver.find_element(*self.Activity_More_keyword)

    def ActivitesList(self):
        return self.driver.find_elements(*self.Activity_List_Keyword)




