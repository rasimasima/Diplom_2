import pytest
import allure
import requests

from data.urls import Urls
from data import user_data
from data.ingredients_data import Ingredients

class TestCreateOrder:
    @allure.description('Успешное создание заказа с авторизованным пользователем')
    @allure.title('Создание заказа с авторизацией')
    def test_create_order_with_authorization(self):
        payload = {"email": user_data.email_registered, "password": user_data.password_registered}
        with allure.step("Отправляем запрос на создание заказа"):
            response = requests.post(Urls.url_create_order, headers=payload, data=Ingredients.correct_ingredients)
        assert response.status_code == 200 and response.json().get("success") is True

    @allure.description('Успешное создание заказа с неавторизованным пользователем')
    @allure.title('Создание заказа без авторизации')
    def test_create_order_not_authorization(self):
        with allure.step("Отправляем запрос на создание заказа"):
            response = requests.post(Urls.url_create_order, data=Ingredients.correct_ingredients)
        assert response.status_code == 200 and response.json().get("success") is True  

    @allure.description('Ошибка при создании заказа без ингредиентов')
    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingridients(self):
        with allure.step("Отправляем запрос на создание заказа"):
            response = requests.post(Urls.url_create_order)
        assert response.status_code == 400 and response.json()['message'] == "Ingredient ids must be provided"

    @allure.description('Ошибка при создании заказа с неверным хешем ингредиентов')
    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_invalid_hash_ingridient(self):
        with allure.step("Отправляем запрос на создание заказа"):
            response = requests.post(Urls.url_create_order, headers=Urls.headers, json=Ingredients.incorrect_ingredients)
        assert response.status_code == 500 and 'Internal Server Error' in response.text