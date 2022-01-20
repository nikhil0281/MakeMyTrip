import pytest

from MakeMyTrip import Utilites
from MakeMyTrip.HomePageObjects import Test_HomePage


@pytest.mark.usefixtures("launchbrowser")
class Test_MMT(Test_HomePage):
    global Logs
    Logs = Utilites.getlogs()

    def test_SiteOpen(self,WebSiteUrl):
        print(WebSiteUrl)
        Logs.info("Web Url is : " + str(WebSiteUrl))
        self.driver.get(WebSiteUrl)

    def test_hindipopup(self):
        HindiMessage = self.AlertHindi()
        # Utilites.explicitwait(self.driver,HindiMessage,10)
        print(HindiMessage.text)





