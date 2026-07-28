from playwright.sync_api import expect

from pages.login_page import LoginPage
from utils.config import ADMIN_URL, ADMIN_USERNAME, ADMIN_PASSWORD, require_config


def test_admin_login_page_can_open(page):
    url = require_config("ADMIN_URL", ADMIN_URL)

    login_page = LoginPage(page)
    login_page.open(url)
    login_page.check_login_page_loaded()


def test_admin_login_success(page):
    url = require_config("ADMIN_URL", ADMIN_URL)
    username = require_config("ADMIN_USERNAME", ADMIN_USERNAME)
    password = require_config("ADMIN_PASSWORD", ADMIN_PASSWORD)

    login_page = LoginPage(page)
    login_page.open(url)
    login_page.login(username, password)

    expect(page.locator(".admin-header h1")).to_have_text("工作台")
    expect(page.locator("button.save-button")).to_be_visible()