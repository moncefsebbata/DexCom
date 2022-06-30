class LoginPage:
    dexcom_clarity_home_users = "//a[contains(text(),'Dexcom Clarity for Home Users')]"
    login_field = "//input[@id='username']"
    password_field = "//input[@id='password']"
    login_button = "//input[@type='submit']"
    name_title = "//p[@class='home-user-header__name']"
    logout_button = "//a[@class='home-user-header__logout cui-link']"

    def __init__(self, driver):
        self.driver = driver

    def clickHomeUser(self):
        self.driver.find_element_by_xpath(self.dexcom_clarity_home_users).click()

    def setUserName(self, username):
        return self.driver.find_element_by_xpath(self.login_field).send_keys(username)

    def setPassword(self, password):
        return self.driver.find_element_by_xpath(self.password_field).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element_by_xpath(self.login_button).click()

    def readText(self):
        return self.driver.find_element_by_xpath(self.name_title).text

    def is_logoutButton_displayed(self):
        self.driver.find_element_by_xpath(self.login_button).is_displayed()
