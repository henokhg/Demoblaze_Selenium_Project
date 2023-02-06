import allure
import pytest

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Web.Pages.page_cart import cart_steps
from Web.Utils.utils import *
from Web.Base.base import Base_test

from Web.Pages.page_placeOrder import place_order


class Test_Place_Order(Base_test):

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_add_to_cart(self):
        driver = self.driver
        home = cart_steps(driver)
        home.click_on_home_button()
        home.wait = WebDriverWait(self.driver, 10)
        home.click_on_categories()
        home.click_on_phone()
        home.click_on_samsung_galaxyssword()
        home.click_on_add_to_cart()
        home.alert = driver.switch_to.alert
        home.alert.accept()
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("henok")
        order.insert_data_to_country_input("israel")
        order.insert_data_to_city_input("beer sheva")
        order.insert_data_to_credit_card_input("15432454")
        order.insert_data_to_month_input("9")
        order.insert_data_to_year_input("1990")
        order.verify_purchase_clickable()

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_add_to_cart_empty_name(self):
        driver = self.driver
        home = cart_steps(driver)
        home.click_on_home_button()
        home.wait = WebDriverWait(self.driver, 10)
        home.click_on_categories()
        home.click_on_phone()
        home.click_on_samsung_galaxyssword()
        home.click_on_add_to_cart()
        home.alert = driver.switch_to.alert
        home.alert.accept()
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("  ")
        order.insert_data_to_country_input("israel")
        order.insert_data_to_city_input("beer sheva")
        order.insert_data_to_credit_card_input("15432454")
        order.insert_data_to_month_input("9")
        order.insert_data_to_year_input("1990")
        alert = order.driver.switch_to.alert
        alert.accept()

    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_close_button_clicable(self):
        driver = self.driver
        home = cart_steps(driver)
        home.click_on_home_button()
        home.wait = WebDriverWait(self.driver, 10)
        home.click_on_categories()
        home.click_on_phone()
        home.click_on_samsung_galaxyssword()
        home.click_on_add_to_cart()
        home.alert = driver.switch_to.alert
        home.alert.accept()
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.verify_close_clickable()

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_to_cart_no_inserted_data_in_country_field(self):
        driver = self.driver
        home = cart_steps(driver)
        home.click_on_home_button()
        home.wait = WebDriverWait(self.driver, 10)
        home.click_on_categories()
        home.click_on_phone()
        home.click_on_samsung_galaxyssword()
        home.click_on_add_to_cart()
        home.alert = driver.switch_to.alert
        home.alert.accept()
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("henok")
        order.insert_data_to_country_input("")
        order.insert_data_to_city_input("beer sheva")
        order.insert_data_to_credit_card_input("15432454")
        order.insert_data_to_month_input("9")
        order.insert_data_to_year_input("1990")
        order.verify_purchase_clickable()

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_to_cart_no_inserted_data_in_city_field(self):
        driver = self.driver
        home = cart_steps(driver)
        home.click_on_home_button()
        home.wait = WebDriverWait(self.driver, 10)
        home.click_on_categories()
        home.click_on_phone()
        home.click_on_samsung_galaxyssword()
        home.click_on_add_to_cart()
        home.alert = driver.switch_to.alert
        home.alert.accept()
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("henok")
        order.insert_data_to_country_input("israel")
        order.insert_data_to_city_input(" ")
        order.insert_data_to_credit_card_input("15432454")
        order.insert_data_to_month_input("9")
        order.insert_data_to_year_input("1990")
        order.verify_purchase_clickable()

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_to_cart_no_inserted_data_in_creditCard_field(self):
        driver = self.driver
        home = cart_steps(driver)
        home.click_on_home_button()
        home.wait = WebDriverWait(self.driver, 10)
        home.click_on_categories()
        home.click_on_phone()
        home.click_on_samsung_galaxyssword()
        home.click_on_add_to_cart()
        home.alert = driver.switch_to.alert
        home.alert.accept()
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("henok")
        order.insert_data_to_country_input("israel")
        order.insert_data_to_city_input("beer sheva")
        order.insert_data_to_credit_card_input("")
        order.insert_data_to_month_input("9")
        order.insert_data_to_year_input("1990")
        alert = order.driver.switch_to.alert
        alert.accept()

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_to_cart_no_inserted_data_in_Month_field(self):
        driver = self.driver
        home = cart_steps(driver)
        home.click_on_home_button()
        home.wait = WebDriverWait(self.driver, 10)
        home.click_on_categories()
        home.click_on_phone()
        home.click_on_samsung_galaxyssword()
        home.click_on_add_to_cart()
        home.alert = driver.switch_to.alert
        home.alert.accept()
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("henok")
        order.insert_data_to_country_input("israel")
        order.insert_data_to_city_input("beer sheva")
        order.insert_data_to_credit_card_input("15432454")
        order.insert_data_to_month_input("")
        order.insert_data_to_year_input("1990")
        order.verify_purchase_clickable()

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_to_cart_no_inserted_data_in_Year_field(self):
        driver = self.driver
        home = cart_steps(driver)
        home.click_on_home_button()
        home.wait = WebDriverWait(self.driver, 10)
        home.click_on_categories()
        home.click_on_phone()
        home.click_on_samsung_galaxyssword()
        home.click_on_add_to_cart()
        home.alert = driver.switch_to.alert
        home.alert.accept()
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("henok")
        order.insert_data_to_country_input("israel")
        order.insert_data_to_city_input("beer sheva")
        order.insert_data_to_credit_card_input("15432454")
        order.insert_data_to_month_input("9")
        order.insert_data_to_year_input("")
        order.verify_purchase_clickable()

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_to_cart_no_inserted_data_in_Month_and_Year_field(self):
        driver = self.driver
        home = cart_steps(driver)
        home.click_on_home_button()
        home.wait = WebDriverWait(self.driver, 10)
        home.click_on_categories()
        home.click_on_phone()
        home.click_on_samsung_galaxyssword()
        home.click_on_add_to_cart()
        home.alert = driver.switch_to.alert
        home.alert.accept()
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("henok")
        order.insert_data_to_country_input("israel")
        order.insert_data_to_city_input("beer sheva")
        order.insert_data_to_credit_card_input("15432454")
        order.insert_data_to_month_input("")
        order.insert_data_to_year_input("")
        order.verify_purchase_clickable()

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_add_to_cart_no_inserted_data_in_Month_Year_city_field(self):
        driver = self.driver
        home = cart_steps(driver)
        home.click_on_home_button()
        home.wait = WebDriverWait(self.driver, 10)
        home.click_on_categories()
        home.click_on_phone()
        home.click_on_samsung_galaxyssword()
        home.click_on_add_to_cart()
        home.alert = driver.switch_to.alert
        home.alert.accept()
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("henok")
        order.insert_data_to_country_input("israel")
        order.insert_data_to_city_input("beer sheva")
        order.insert_data_to_credit_card_input("123456789")
        order.insert_data_to_month_input("")
        order.insert_data_to_year_input("")
        order.verify_purchase_clickable()

    @allure.description('Test_Place_Order')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_add_to_cart_empty_name_and_CreditCard(self):
        driver = self.driver
        home = cart_steps(driver)
        home.click_on_home_button()
        home.wait = WebDriverWait(self.driver, 10)
        home.click_on_categories()
        home.click_on_phone()
        home.click_on_samsung_galaxyssword()
        home.click_on_add_to_cart()
        home.alert = driver.switch_to.alert
        home.alert.accept()
        order = place_order(driver)
        order.varify_cart_clickable()
        order.varify_place_order_clickable()
        order.insert_data_to_name_input("  ")
        order.insert_data_to_country_input("israel")
        order.insert_data_to_city_input("beer sheva")
        order.insert_data_to_credit_card_input("")
        order.insert_data_to_month_input("9")
        order.insert_data_to_year_input("1990")
        alert = order.driver.switch_to.alert
        alert.accept()

