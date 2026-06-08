import random
import string 

username_random = ''.join(random.choices(string.ascii_lowercase, k=7))
email_random = ''.join(random.choices(string.ascii_lowercase, k=7))+'@yandex.ru'
password_random = str(random.randint(100000, 900000))

username_registered = 'Margorita'
email_registered = 'ivanova@yandex.ru'
password_registered = '7654321'

class User:
    data_without_email = {
        "email": '',
        "password": "pass5972",
        "name": "Hogwarts"}

    data_without_password = {
        "email": 'adambldor@yandex.ru',
        "password": "",
        "name": "Hogwarts"}

    data_without_name = {
        "email": 'adambldor@yandex.ru',
        "password": "pass5972",
        "name": ""}
    
    data_correct = {
        "email": 'adambldor@yandex.ru',
        "password": "pass5972"}

    data_incorrect = {
        "email": 'dambldora@yandex.ru',
        "password": "pass5972"}