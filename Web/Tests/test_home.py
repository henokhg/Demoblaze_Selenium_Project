import allure
import pytest

from Web.Base.base import Base_test
from Web.Pages.page_home import home_menus


class Test_Home_Page(Base_test):

    @allure.description('home page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_home_button_clickable(self):
        driver = self.driver
        login = home_menus(driver)
        login.click_on_home_button()

    @allure.description('home page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_contact_button_clickable(self):
        driver = self.driver
        login = home_menus(driver)
        login.click_on_contact_button()

    @allure.description('home page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_login_button_clickable(self):
        driver = self.driver
        login = home_menus(driver)
        login.click_on_login_button()

    @allure.description('home page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_signup_button_clickable(self):
        driver = self.driver
        login = home_menus(driver)
        login.click_on_signup_button()

    @allure.description('home page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_categories_button_clickable(self):
        driver = self.driver
        login = home_menus(driver)
        login.click_on_categories()

    @allure.description('home page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_phone_button_clickable(self):
        driver = self.driver
        login = home_menus(driver)
        login.click_on_phone_category()

    @allure.description('home page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_laptop_category_button_clickable(self):
        driver = self.driver
        login = home_menus(driver)
        login.click_on_laptop_category()

    @allure.description('home page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_monitors_category_button_clickable(self):
        driver = self.driver
        login = home_menus(driver)
        login.click_on_monitors_category()

    @allure.description('home page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_samsung_galaxyssword_link_clickable(self):
        driver = self.driver
        login = home_menus(driver)
        login.click_on_laptop_category()

    @allure.description('home page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_next_button_clickable(self):
        driver = self.driver
        login = home_menus(driver)
        login.click_on_next_button()

    @allure.description('home page test')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_verify_previous_clickable(self):
        driver = self.driver
        login = home_menus(driver)
        login.click_on_previous_button()

    @allure.description('Add product from phone ')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_E2E_Add_from_phone(self):
        driver = self.driver
        login = home_menus(driver)
        login.Add_from_phone_product_Category()
        assert login.driver.title == "STORE"

    @allure.description('Add product from Laptop')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_E2E_Add_from_Laptop(self):
        driver = self.driver
        login = home_menus(driver)
        login.Add_from_Laptop_product_Category()
        assert login.driver.title == "STORE"

    @allure.description('Add product from Monitor')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_E2E_Add_from_Monitor(self):
        driver = self.driver
        login = home_menus(driver)
        login.Add_from_Monitor_product_Category()
        assert login.driver.title == "STORE"

    @allure.description('Add product from ALL Category')
    @pytest.mark.sanity
    @allure.severity(allure.severity_level.NORMAL)
    def test_E2E_Add_All_Product(self):
        driver = self.driver
        login = home_menus(driver)
        login.Add_from_phone_product_Category()
        login.Add_from_Laptop_product_Category()
        login.Add_from_Monitor_product_Category()
        login.Click_Cart_option()
        assert login.driver.title == "STORE"


