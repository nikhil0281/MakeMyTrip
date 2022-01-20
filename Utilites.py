import inspect
import logging
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def getlogs():
    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(loggername)
    fileHandler = logging.FileHandler('MakeMyTripLogs.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.DEBUG)
    return logger

# def explicitwait(driver, elementxpath, time):
#     try:
#         # wait 10 seconds before looking for element
#         element = WebDriverWait(driver, time).until(
#             EC.presence_of_element_located((By.XPATH, str(elementxpath))
#         ))
#     finally:
#         print("Ok done")
