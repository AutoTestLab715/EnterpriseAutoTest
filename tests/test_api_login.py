import requests
from utils.config import LOGIN_API, ADMIN_USERNAME, ADMIN_PASSWORD, require_config


def test_admin_login_success():
    url = require_config("LOGIN_API", LOGIN_API)
    username = require_config("ADMIN_USERNAME", ADMIN_USERNAME)
    password = require_config("ADMIN_PASSWORD", ADMIN_PASSWORD)

    payload = {
        "username": username,
        "password": password
    }

    response = requests.post(url, json=payload, timeout=10)

    assert response.status_code in [200, 201]


def test_admin_login_fail_with_wrong_password():
    url = require_config("LOGIN_API", LOGIN_API)
    username = require_config("ADMIN_USERNAME", ADMIN_USERNAME)

    payload = {
        "username": username,
        "password": "wrong_password_123456"
    }

    response = requests.post(url, json=payload, timeout=10)

    assert response.status_code in [400, 401, 403]