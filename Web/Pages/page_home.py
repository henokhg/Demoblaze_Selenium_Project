import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from Web.Locators.home import *
from Web.Utils.utils import Utils


class home_menus():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.home_button = home.HOME_BUTTON
        self.contact_button = home.CONTACT_BUTTON
        self.login_button = home.LOGIN_BUTTON
        self.signup_button = home.SIGNUP_BUTTON
        self.categories_button = home.CATEGORIES
        self.phone_button = home.PHONE
        self.laptop = home.LAPTOP
        self.monitors = home.MONITORS
        self.product_store = home.PRODUCT_STORE
        self.samsung_galaxy = home.SAMSUNG_GALAXY
        self.next_button = home.NEXT_BUTTON
        self.previous_button = home.PREVIOUS_BUTTON
        self.cart_page = home.CART_PAGE



    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_home_button(self):
        self.driver.find_element(By.XPATH, self.home_button).click()
        self.driver.implicitly_wait(100)
        time.sleep(2)

    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_contact_button(self):
        self.driver.find_element(By.XPATH, self.contact_button).click()
        self.driver.implicitly_wait(100)
        time.sleep(2)

    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button).click()
        self.driver.implicitly_wait(100)
        time.sleep(2)

    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_signup_button(self):
        self.driver.find_element(By.XPATH, self.signup_button).click()
        self.driver.implicitly_wait(100)
        time.sleep(2)


    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_categories(self):
        self.driver.find_element(By.ID, self.categories_button).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)

    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_phone_category(self):
        self.driver.find_element(By.ID, self.phone_button).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)



    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_laptop_category(self):
        self.driver.find_element(By.XPATH, self.laptop).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)


    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_monitors_category(self):
        self.driver.find_element(By.XPATH, self.monitors).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)

    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_samsung_galaxyssword_link(self):
        self.driver.find_element(By.XPATH, self.samsung_galaxy).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)


    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_next_button(self):
        self.driver.find_element(By.XPATH, self.next_button).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)


    @allure.step
    @allure.description('Clear and insert data to contact name input')
    def click_on_previous_button(self):
        self.driver.find_element(By.ID, self.previous_button).click()
        self.driver.implicitly_wait(10)
        time.sleep(2)

    @allure.step
    @allure.description('click on Back button')
    def Click_Back(self):
        self.driver.back()
        self.driver.back()

    @allure.step
    @allure.description('click on Phone product from phone')
    def Add_from_phone_product_Category(self):
        count = 0
        for i in range(7):
            time.sleep(1)
            self.click_on_phone_category()
            self.driver.find_element(By.XPATH, f"/html[1]/body[1]/div[5]/div[1]/div[2]/div[1]/div[{count+1}]/div[1]/div[1]/h4[1]/a[1]").click()
            self.driver.implicitly_wait(5)
            time.sleep(1)
            self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[5]/div[1]/div[2]/div[2]/div[1]/a[1]").click()
            time.sleep(2)
            self.driver.switch_to.alert.accept()
            self.Click_Back()
            count += 1

    @allure.step
    @allure.description('click on product from laptop')
    def Add_from_Laptop_product_Category(self):
        count = 0
        for i in range(6):
            time.sleep(1)
            self.click_on_laptop_category()
            self.driver.find_element(By.XPATH,
                                     f"/html[1]/body[1]/div[5]/div[1]/div[2]/div[1]/div[{count+1}]/div[1]/div[1]/h4[1]/a[1]").click()
            self.driver.implicitly_wait(5)
            time.sleep(1)
            self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[5]/div[1]/div[2]/div[2]/div[1]/a[1]").click()
            time.sleep(2)
            self.driver.switch_to.alert.accept()
            self.Click_Back()
            count += 1

    @allure.step
    @allure.description('click on product from monitor')
    def Add_from_Monitor_product_Category(self):
        count = 0
        for i in range(2):
            time.sleep(1)
            self.click_on_monitors_category()
            self.driver.find_element(By.XPATH,
                                     f"/html[1]/body[1]/div[5]/div[1]/div[2]/div[1]/div[{count+1}]/div[1]/div[1]/h4[1]/a[1]").click()
            self.driver.implicitly_wait(5)
            time.sleep(1)
            self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[5]/div[1]/div[2]/div[2]/div[1]/a[1]").click()
            time.sleep(2)
            self.driver.switch_to.alert.accept()
            self.Click_Back()
            count += 1

    @allure.step
    @allure.description('click on Back button')
    def Click_Cart_option(self):
        self.driver.find_element(By.XPATH, self.cart_page).click()
        time.sleep(5)

