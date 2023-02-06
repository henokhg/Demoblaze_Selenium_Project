import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from Web.Locators.login import *
from Web.Utils.utils import Utils


class Login_Steps():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.login_button = LoginId.LOGIN_BUTTON
        self.nameID = LoginId.NAME
        self.passwordID = LoginId.PASSWORD
        self.login_click = LoginId.LOGIN_CLICK
        self.logout_link = LoginId.LOGOUT_CLICK

    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button).click()
        self.driver.implicitly_wait(100)
        time.sleep(2)


    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def enter_name(self, User_name):
        # Utils(self.driver).assertion(self.driver.current_url)
        username = self.driver.find_element(By.ID, self.nameID)
        username.clear()
        username.send_keys(User_name)
        self.driver.implicitly_wait(10)
        time.sleep(2)
        Utils(self.driver).assertion(User_name, username.get_attribute('value'))
        return username


    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def enter_password(self, User_password):
        userpassword = self.driver.find_element(By.ID, self.passwordID)
        userpassword.clear()
        userpassword.send_keys(User_password)
        self.driver.implicitly_wait(10)
        time.sleep(2)
        Utils(self.driver).assertion(User_password, userpassword.get_attribute('value'))
        return userpassword

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_click).click()
        self.driver.implicitly_wait(10)
        time.sleep(5)

    def enter_username(self, param):
        pass

    def logout_text(self):
        Logout = self.driver.find_element(By.XPATH, self.logout_link).text
        return Logout
