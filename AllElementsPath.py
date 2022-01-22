from selenium.webdriver.common.by import By


class Test_AllElementsPath:
    AlertHindiXpath = (By.CLASS_NAME, "font20 latoBlack blackText appendBottom5 makeFlex hrtlCenter")
    AlertCrossButton = (By.XPATH, "//span[@class='langCardClose']")
    NavHeader = (By.XPATH, "//div[@class='loginModal displayBlock modalLogin dynHeight personal ']")
    NavLink = (By.XPATH, "//ul[@class='makeFlex font12']/li/a/span/following-sibling::span")
    Flight_From_Keyword = (By.XPATH, "//span[contains(text(),'From')]")
    Flight_To_Keyword = (By.XPATH,"//span[contains(text(),'To')]")
    Flight_From_City = (By.XPATH, "//input[@id='fromCity']")
    Flight_From_City_Text_Box = (By.XPATH, "//input[@class='react-autosuggest__input react-autosuggest__input--open']")
    Flight_To_City = (By.XPATH, "//input[@id='toCity']")
    Flight_To_City_Text_Box = (By.XPATH, "//div[@class='fsw_inputBox searchToCity inactiveWidget activeWidget']/div/div/div/div/input[@class='react-autosuggest__input react-autosuggest__input--open']")