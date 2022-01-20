from selenium.webdriver.common.by import By


class HomePage():
    AlertHindiXpath = (By.XPATH, "//span[@class='newGreenTag appendLeft5']")

    def __init__(self,driver):
        self.driver = driver

    def AlertHindi(self):
        return self.driver.find_element(*HomePage.AlertHindiXpath)