import requests
import pytest

BASE_URL = "https://reqres.in/api"
API_KEY = "reqres-free-v1"  # Use your actual API key here
print("Loaded test_wallet_api.py")

@pytest.fixture(scope="module")
def get_token():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    headers = {
        "x-api-key": API_KEY
    }
    response = requests.post(f"{BASE_URL}/login", json=data, headers=headers)
    assert response.status_code == 200
    return response.json()['token']


def test_login_success(get_token):
    assert get_token is not None


def test_login_failure():
    data = {
        "email": "wrong@example.com",
        "password": "invalid"
    }
    headers = {
        "x-api-key": API_KEY
    }
    response = requests.post(f"{BASE_URL}/login", json=data, headers=headers)
    assert response.status_code == 400


def test_get_user(get_token):
    headers = {
        "Authorization": f"Bearer {get_token}",
        "x-api-key": API_KEY
    }
    response = requests.get(f"{BASE_URL}/users/2", headers=headers)
    assert response.status_code == 200
    assert response.json()['data']['id'] == 2
