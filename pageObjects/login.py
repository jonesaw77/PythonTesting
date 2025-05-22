from selenium.webdriver.common.by import By

from pytestsE2eFramework2.pageObjects.shopPage import ShopPage
from pytestsE2eFramework2.utils.browserutils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver: object) -> None:
        super().__init__(driver)
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.terms = (By.ID, "terms")
        self.signIn = (By.ID, "signInBtn")

    def login(self, username: str, password: str):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.terms).click()
        self.driver.find_element(*self.signIn).click()
        shop_page = ShopPage(self.driver)
        return shop_page
