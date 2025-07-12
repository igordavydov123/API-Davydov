import pytest
import requests
import os


BASE_URL = "https://postman-echo.com"

# 1 get запрос
def test_get():
    response = requests.get(f"{BASE_URL}/get")

    assert response.status_code == 200

# 2 get с query
def test_get_with_query():
    params = {"name": "John", "age": "30", "city": "London"}
    response = requests.get(f"{BASE_URL}/get", params=params)
    data = response.json()

    assert response.status_code == 200
    assert data["args"] == params
    assert data["url"] == f"{BASE_URL}/get?name=John&age=30&city=London"


# 3 post с JSON
def test_post_with_json():
    payload = {"name": "Igor", "age": "35", "city": "Spb"}
    headers = {"Content-Type": "application/json"}

    response = requests.post(f"{BASE_URL}/post", json=payload, headers=headers)
    data = response.json()

    assert response.status_code == 200
    assert data["data"] == payload
    assert data["headers"]["content-type"] == "application/json"


# 4 post с form-data
def test_post_with_form_data():
    files = {
        "username": (None, "igor"),
        "password": (None, "vss123")
    }

    response = requests.post(f"{BASE_URL}/post", files=files)
    data = response.json()

    assert response.status_code == 200
    assert data["form"]["username"] == "igor"
    assert data["form"]["password"] == "vss123"


# 5 post с x-www-form
def test_post_with_x_www_form():
    payload = {"title": "Hello", "content": "World"}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.post(f"{BASE_URL}/post", data=payload, headers=headers)
    data = response.json()

    assert response.status_code == 200
    assert data["form"]["title"] == "Hell"
    assert data["form"]["content"] == "World"