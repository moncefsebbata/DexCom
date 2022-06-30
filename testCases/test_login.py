from selenium import webdriver
from page_object_model.LoginPage import LoginPage


class Test_001_Login:
    baseUrl = "https://clarity.dexcom.com/"

    def test_homePageTitle(self):
        self.driver = webdriver.Chrome("C:/Windows/chromedriver")
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        actual_title = self.driver.title

        if actual_title == "Dexcom Clarity":
            assert True
        else:
            assert False
        self.driver.close()

    def test_login(self):
        self.driver = webdriver.Chrome("C:/Windows/chromedriver")
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.clickHomeUser()
        self.driver.implicitly_wait(3)
        self.lp.setUserName("nilepatest001")
        self.driver.implicitly_wait(3)
        self.lp.setPassword("Password@1")
        self.driver.implicitly_wait(3)
        self.lp.clickLoginButton()
        self.driver.implicitly_wait(3)

        if self.lp.readText() == "Nile PATest001":
            assert True
        else:
            assert False
        self.driver.close()
