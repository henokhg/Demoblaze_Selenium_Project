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
        signin.click_on_login_button()
        signin.wait = WebDriverWait(self.driver, 10)
        signin.enter_fist_name("henok")
        signin.enter_password("meheret")
        signin_button = SignUp_Steps(driver)
        signin_button.click_login()
        alert = driver.switch_to.alert
        alert.accept()
