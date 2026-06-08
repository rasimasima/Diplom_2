import pytest
import allure
import requests

from data.urls import Urls
from data.user_data import User

class TestLoginUser:
    @allure.description('Успешный логин под существующим пользователем')
    @allure.title('Логин пользователя под существующим пользователем')
    def test_login_user_success(self):
        with allure.step("Отправляем запрос на логин пользователя"):
            response = requests.post(Urls.url_login_user, data = User.data_correct)
        assert response.status_code == 200 and response.json().get('success') == True

    @allure.description('Ошибка при попытке входа с неверным логином и паролем')
    @allure.title('Логин пользователя с неверным логином и паролем')
    def test_login_with_uncorrect_data_error(self):
        with allure.step("Отправляем запрос на логин пользователя"):
            response = requests.post(Urls.url_login_user, data = User.data_incorrect)
        assert response.status_code == 401 and response.json().get('success') == False