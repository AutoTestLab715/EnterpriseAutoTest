import pytest

from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from utils.config import ADMIN_PASSWORD, ADMIN_URL, ADMIN_USERNAME, require_config


@pytest.fixture
def admin_page(page):
    url = require_config("ADMIN_URL", ADMIN_URL)
    username = require_config("ADMIN_USERNAME", ADMIN_USERNAME)
    password = require_config("ADMIN_PASSWORD", ADMIN_PASSWORD)

    login_page = LoginPage(page)
    login_page.open(url)
    login_page.login(username, password)
    page.wait_for_selector(".admin-app", timeout=10000)

    return AdminPage(page)
