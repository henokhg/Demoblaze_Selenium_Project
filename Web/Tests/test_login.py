import allure
import pytest

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Web.Pages.page_login import Login_Steps
from Web.Utils.utils import *
from Web.Base.base import Base_test
from Web.Pages.page_signUp import SignUp_Steps

class Test_Login_Page(Base_test):

    @allure.description("test_login_valid")
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_valid(self):
        driver = self.driver
        login = Login_Steps(driver)
        login.click_on_login_button()
        login.wait = WebDriverWait(self.driver, 10)
        login.enter_name("henokk")
        login.enter_password("12345")
        login.click_login()
        assert login.logout_text() == "Log out"

    @allure.description('test_login_invalid_null Username and password')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_invalid_null(self):
        driver = self.driver
        login = Login_Steps(driver)
        login.click_on_login_button()
        login.wait = WebDriverWait(self.driver, 10)
        login.enter_name("")
        login.enter_password("")
        login.click_login()
        alert = driver.switch_to.alert
        assert alert.text == "Please fill out Username and Password."

    @allure.description('test_login_invalid_password null')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_invalid_password_null(self):
        driver = self.driver
        login = Login_Steps(driver)
        login.click_on_login_button()
        login.wait = WebDriverWait(self.driver, 10)
        login.enter_name("henok")
        login.enter_password("")
        login.click_login()
        alert = driver.switch_to.alert
        assert alert.text == "Please fill out Username and Password."

    @allure.description('test_login_invalid_username null')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_invalid_username_null(self):
        driver = self.driver
        login = Login_Steps(driver)
        login.click_on_login_button()
        login.wait = WebDriverWait(self.driver, 10)
        login.enter_name("")
        login.enter_password("2233")
        login.click_login()
        alert = driver.switch_to.alert
        assert alert.text == "Please fill out Username and Password."

    @allure.description('test_login_Using Special Character')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_Special_Character(self):
        driver = self.driver
        login = Login_Steps(driver)
        login.click_on_login_button()
        login.wait = WebDriverWait(self.driver, 10)
        login.enter_name(".!@#$%")
        login.enter_password(".!@#$%")
        login.click_login()
        alert = driver.switch_to.alert
        assert alert.text == "User does not exist."
        alert.accept()

    @allure.description('test_login_Using Special Character')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_Special_Character(self):
        driver = self.driver
        signup = SignUp_Steps(driver)
        signup.click_on_signup_button()
        signup.enter_User_name("henok123")
        signup.enter_password("meheret")
        login = Login_Steps(driver)
        login.click_on_login_button()
        login.enter_name(".!@#$%")
        login.enter_password(".!@#$%")
        login.click_login()
        alert = driver.switch_to.alert
        assert alert.text == "User does not exist."
        alert.accept()
