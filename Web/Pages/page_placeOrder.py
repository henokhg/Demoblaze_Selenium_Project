import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from Web.Locators.locator_order_place import *
from Web.Utils.utils import Utils


class place_order():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.cart = order_place.CART
        self.place_order = order_place.PLACE_ORDER
        self.name = order_place.NAME
        self.country = order_place.COUNTRY
        self.city = order_place.CITY
        self.credit_card = order_place.CREDIT_CARD
        self.month = order_place.MONTH
        self.year = order_place.YEAR
        self.purchase = order_place.PURCHASE
        self.close = order_place.CLOSE
        self.SCROLL_PAUSE_TIME = 5

    @allure.step
    @allure.description('varify_cart_clickable')
    def varify_cart_clickable(self):
        self.driver.find_element(By.XPATH, self.cart).click()
        time.sleep(1)

    @allure.step
    @allure.description('varify_place_order_clickable')
    def varify_place_order_clickable(self):
        self.driver.find_element(By.XPATH, self.place_order).click()
        time.sleep(1)

    @allure.step
    @allure.description('insert_data_to_name_input')
    def insert_data_to_name_input(self, user_Name):
        userName = self.driver.find_element(By.ID, self.name)
        userName.clear()
        userName.send_keys(user_Name)
        time.sleep(1)
        Utils(self.driver).assertion(user_Name, userName.get_attribute('value'))
        return userName

    @allure.step
    @allure.description('insert_data_to_country_input')
    def insert_data_to_country_input(self, user_country):
        userContry = self.driver.find_element(By.ID, self.country)
        userContry.clear()
        userContry.send_keys(user_country)
        time.sleep(1)
        Utils(self.driver).assertion(user_country, userContry.get_attribute('value'))
        return userContry

    @allure.step
    @allure.description('insert_data_to_country_input')
    def insert_data_to_city_input(self, user_city):
        userCity = self.driver.find_element(By.ID, self.city)
        userCity.clear()
        userCity.send_keys(user_city)
        time.sleep(1)
        Utils(self.driver).assertion(user_city, userCity.get_attribute('value'))
        return userCity

    @allure.step
    @allure.description('insert_data_to_credit_card_input')
    def insert_data_to_credit_card_input(self, user_creditCard):
        userCreditCard = self.driver.find_element(By.ID, self.credit_card)
        userCreditCard.clear()
        userCreditCard.send_keys(user_creditCard)
        self.driver.implicitly_wait(10)
        time.sleep(1)
        Utils(self.driver).assertion(user_creditCard, userCreditCard.get_attribute('value'))
        return userCreditCard

    @allure.step
    @allure.description('insert_data_to_month_input')
    def insert_data_to_month_input(self, user_month):
        userMonth = self.driver.find_element(By.ID, self.month)
        userMonth.clear()
        userMonth.send_keys(user_month)
        self.driver.implicitly_wait(10)
        time.sleep(2)
        Utils(self.driver).assertion(user_month, userMonth.get_attribute('value'))
        return userMonth

    @allure.step
    @allure.description('insert_data_to_year_input')
    def insert_data_to_year_input(self, user_Year):
        userYear = self.driver.find_element(By.ID, self.year)
        userYear.clear()
        userYear.send_keys(user_Year)
        self.driver.implicitly_wait(10)
        time.sleep(2)
        Utils(self.driver).assertion(user_Year, userYear.get_attribute('value'))
        return userYear

    @allure.step
    @allure.description('varify_cart_clickable')
    def scrolling_the_page(self):
        self.driver.execute_script("window.scrollTo(0, 200)")
        time.sleep(self.SCROLL_PAUSE_TIME)

    @allure.step
    @allure.description('verify_purchase_clickable')
    def verify_purchase_clickable(self):
        self.driver.find_element(By.XPATH, self.purchase).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)

    @allure.step
    @allure.description('verify_close_clickable')
    def verify_close_clickable(self):
        self.driver.find_element(By.XPATH, self.close).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)
