import allure
import pytest

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from Web.Pages.page_contact import Contact_Detail
from Web.Utils.utils import *
from Web.Base.base import Base_test


class Test_Contact_Page(Base_test):

    @allure.description('contact page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_contact_us_valid(self):
        driver = self.driver
        contact = Contact_Detail(driver)
        contact.click_on_contact_button()
        contact.enter_user_email("henok@gmail.com")
        contact.enter_contact_name("henok")
        contact.write_message("im so exited")
        contact.click_send_message()

    @allure.description("test_coutact_us_invalid null")
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_contact_us_invalid_null_fields(self):
        driver = self.driver
        contact = Contact_Detail(driver)
        contact.click_on_contact_button()
        contact.enter_user_email("")
        contact.enter_contact_name("")
        contact.write_message("")
        contact.click_send_message()

    @allure.description('test_contact_us_invalid name null')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_contact_us_invalid_name_field_null(self):
        driver = self.driver
        contact = Contact_Detail(driver)
        contact.click_on_contact_button()
        contact.enter_user_email("henok@gmail.com")
        contact.enter_contact_name("")
        contact.write_message("im so exited")
        contact.click_send_message()

    @allure.description('test_contact_us_invalid email null')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_contact_us_invalid_email_field_null(self):
        driver = self.driver
        contact = Contact_Detail(driver)
        contact.click_on_contact_button()
        contact.enter_user_email("")
        contact.enter_contact_name("henok")
        contact.write_message("im so exited")
        contact.click_send_message()

    @allure.description('test_contact_us_invalid message null')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_contact_us_invalid_message_field_null(self):
        driver = self.driver
        contact = Contact_Detail(driver)
        contact.click_on_contact_button()
        contact.enter_user_email("henok@gmail.com")
        contact.enter_contact_name("henok")
        contact.write_message(" ")
        contact.click_send_message()

    @allure.description('test_contact_us_invalid both name and message null')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_contact_us_invalid_both_name_and_message_field_null(self):
        driver = self.driver
        contact = Contact_Detail(driver)
        contact.click_on_contact_button()
        contact.enter_user_email("henok@gmail.com")
        contact.enter_contact_name(" ")
        contact.write_message(" ")
        contact.click_send_message()



    @allure.description('test_contact_us_invalid both email and contact name null')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_contact_us_invalid_both_name_and_message_field_null(self):
        driver = self.driver
        contact = Contact_Detail(driver)
        contact.click_on_contact_button()
        contact.enter_user_email("")
        contact.enter_contact_name("")
        contact.write_message("im so exited ")
        contact.click_send_message()

    @allure.description('test_contact_us_invalid both email and message field null')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_contact_us_invalid_both_name_and_message_field_null(self):
        driver = self.driver
        contact = Contact_Detail(driver)
        contact.click_on_contact_button()
        contact.enter_user_email("")
        contact.enter_contact_name("henok")
        contact.write_message("")
        contact.click_send_message()
