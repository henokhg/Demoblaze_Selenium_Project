from API.locator.login_locators import Login_Locators
import allure
import pytest
import requests


class Test_SignUp:
    @allure.description('SignUp correctly using Valid UserName and Password')
    @pytest.mark.sanity
    def test_SignUp_correctly(self):
        url = Login_Locators.url_login
        data = Login_Locators.valid_UserName_and_password
        Req = requests.post(url, json=data)
        assert Req.status_code == 200
        assert Req.elapsed.total_seconds() < 10

    @allure.description('SignUp when password incorrectly')
    def test_SignUp_with_incorrectly_password(self):
        url = Login_Locators.url_login
        data = Login_Locators.Invalid_password
        Req = requests.post(url, json=data)
        assert Req.status_code == 404
        assert Req.elapsed.total_seconds() < 10

    @allure.description('SignUp when UserName incorrectly')
    def test_SignUp_with_incorrectly_UserName(self):
        url = Login_Locators.url_login
        data = Login_Locators.Invalid_UserName
        Req = requests.post(url, json=data)
        assert Req.status_code == 404
        assert Req.elapsed.total_seconds() < 10

    @allure.description('SignUp when UserName & password incorrectly')
    def test_SignUp_with_incorrectly_UserName_and_password(self):
        url = Login_Locators.url_login
        data = Login_Locators.Invalid_password_and_UserName
        Req = requests.post(url, json=data)
        assert Req.status_code == 404
        assert Req.elapsed.total_seconds() < 10

    @allure.description('SignUp when UserName & password are null')
    def test_SignUp_with_null_UserName_and_password(self):
        url = Login_Locators.url_login
        data = {}
        Req = requests.post(url, json=data)
        assert Req.status_code == 404
        assert Req.elapsed.total_seconds() < 10
