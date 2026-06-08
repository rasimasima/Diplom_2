import pytest
import allure
import requests

from data.urls import Urls
from data import user_data
from data.user_data import User


class TestCreateUser:

    @allure.description('Создание нового пользователя')
    @allure.title('Создание нового пользователя')
    def test_create_new_user_success(self):
        with allure.step('Подготовка  тестовых данных'):
            payload = {"name": user_data.username_random, "email": user_data.email_random, "password": user_data.password_random}
        with allure.step("Отправляем запрос на создание пользователя"):
            response = requests.post(Urls.url_create_user, data=payload)
        assert response.status_code == 200 and response.json()["success"] is True

    @allure.description('При создании дублирующего пользователя срабатывает allert ')
    @allure.title('Создание пользователя который уже есть в системе')
    def test_create_double_user_error(self):
        with allure.step('Подготовка  тестовых данных'):
            payload = {"name": user_data.username_registered, "email": user_data.email_registered, "password": user_data.password_registered}
        with allure.step("Отправляем запрос на создание пользователя"):
            response = requests.post(Urls.url_create_user, payload)
        with allure.step("Повторно отправляем запрос на создание пользователя"):
            response = requests.post(Urls.url_create_user, data=payload)   
        assert response.status_code == 403 and 'User already exists' in response.text

    @allure.description('При создании пользователя с некорректыми данными срабатывает allert')
    @allure.title('Создание пользователя с некорректными данными/ с незаполненными обязательными полями')
    @pytest.mark.parametrize("user_data", [User.data_without_email, User.data_without_password, User.data_without_name])
    def test_create_user_incorrect_data(self, user_data):
        with allure.step("Отправляем запрос на создание пользователя"):
            response = requests.post(Urls.url_create_user, data=user_data)
        assert response.status_code == 403 and 'Email, password and name are required fields' in response.text