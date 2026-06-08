import pytest
import requests
from data.urls import Urls

@pytest.fixture
def delete_user():
    tokens_to_delete = []
    yield tokens_to_delete
    for token in tokens_to_delete:
        requests.delete(Urls.url_delete_user,headers={'Authorization': token})