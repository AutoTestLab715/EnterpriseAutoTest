import requests
from utils.config import BASE_URL, CONTENT_API, require_config


def test_home_page_status_code():
    url = require_config("BASE_URL", BASE_URL)

    response = requests.get(url, timeout=10)

    assert response.status_code == 200


def test_content_api_status_code():
    url = require_config("CONTENT_API", CONTENT_API)

    response = requests.get(url, timeout=10)

    assert response.status_code == 200


def test_content_api_has_data():
    url = require_config("CONTENT_API", CONTENT_API)

    response = requests.get(url, timeout=10)
    data = response.json()

    assert response.status_code == 200
    assert data is not None