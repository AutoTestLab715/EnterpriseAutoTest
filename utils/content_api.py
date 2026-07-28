import requests

from utils.config import CONTENT_API, require_config


def fetch_content():
    url = require_config("CONTENT_API", CONTENT_API)
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    assert data.get("ok") is True
    return data["content"]
