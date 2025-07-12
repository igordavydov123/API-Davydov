import pytest
import requests


BASE_URL = "https://postman-echo.com"

# get запрос
def test_get():
    response = requests.get(f"{BASE_URL}/get")
    assert response.status_code == 200
    assert "args" in response.json()
    assert response.json()["url"] == f"{BASE_URL}/get"

