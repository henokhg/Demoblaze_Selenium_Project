import allure
import pytest

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Web.Pages.page_signUp import SignUp_Steps
from Web.Utils.utils import *
from Web.Base.base import Base_test


class Test_Contact_Page(Base_test):

    @allure.description('contact page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_valid(self):
        driver = self.driver
        signin = SignUp_Steps(driver)
        signin.click_on_signup_button()
        signin.wait = WebDriverWait(self.driver, 10)
        signin.enter_User_name("henok123")
        signin.enter_password("meheret")
        signin_button = SignUp_Steps(driver)
        signin_button.click_login()
        alert = driver.switch_to.alert
        assert alert.text == "Sign up successful."
        alert.accept()

    @allure.description('SignUp page  null UserName and Password')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_Invalid_UserName_and_Password(self):
        driver = self.driver
        signin = SignUp_Steps(driver)
        signin.click_on_signup_button()
        signin.wait = WebDriverWait(self.driver, 10)
        signin.enter_User_name("")
        signin.enter_password("")
        signin_button = SignUp_Steps(driver)
        signin_button.click_login()
        alert = driver.switch_to.alert
        assert alert.text == "Please enter User name and password properly"
        alert.accept()

    @allure.description('SignUp page test null user name')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_Invalid_userName(self):
        driver = self.driver
        signin = SignUp_Steps(driver)
        signin.click_on_signup_button()
        signin.wait = WebDriverWait(self.driver, 10)
        signin.enter_User_name("")
        signin.enter_password("12345")
        signin_button = SignUp_Steps(driver)
        signin_button.click_login()
        alert = driver.switch_to.alert
        assert alert.text == "Please enter User name properly"
        alert.accept()

    @allure.description('SignUp page test null password')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_Invalid_password(self):
        driver = self.driver
        signin = SignUp_Steps(driver)
        signin.click_on_signup_button()
        signin.wait = WebDriverWait(self.driver, 10)
        signin.enter_User_name("Henok")
        signin.enter_password("")
        signin_button = SignUp_Steps(driver)
        signin_button.click_login()
        alert = driver.switch_to.alert
        assert alert.text == "Please enter Password properly"
        alert.accept()

    @allure.description('SignUp page test Special Characters')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_Invalid_Special_characters(self):
        driver = self.driver
        signin = SignUp_Steps(driver)
        signin.click_on_signup_button()
        signin.wait = WebDriverWait(self.driver, 10)
        signin.enter_User_name("!@#$%^")
        signin.enter_password("!@#$%^")
        signin_button = SignUp_Steps(driver)
        signin_button.click_login()
        alert = driver.switch_to.alert
        assert alert.text == "Please enter User name properly"
        alert.accept()

    @allure.description('SignUp page test Numbers in username')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_Using_numerical_name(self):
        driver = self.driver
        signin = SignUp_Steps(driver)
        signin.click_on_signup_button()
        signin.wait = WebDriverWait(self.driver, 10)
        signin.enter_User_name("1122334455")
        signin.enter_password("123456")
        signin_button = SignUp_Steps(driver)
        signin_button.click_login()
        alert = driver.switch_to.alert
        print(alert.text)
        assert alert.text == "Please enter User name properly"
        alert.accept()

    @allure.description('SignUp page test AlphaNumerical in username')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_Using_AlphaNumerical_name(self):
        driver = self.driver
        signin = SignUp_Steps(driver)
        signin.click_on_signup_button()
        signin.wait = WebDriverWait(self.driver, 10)
        signin.enter_User_name("Henok123456788910")
        signin.enter_password("123456")
        signin_button = SignUp_Steps(driver)
        signin_button.click_login()
        alert = driver.switch_to.alert
        assert alert.text == "Please enter User name properly"
        alert.accept()
