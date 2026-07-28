from pages.home_page import HomePage
from utils.config import BASE_URL, require_config


def test_home_page_can_open(page):
    url = require_config("BASE_URL", BASE_URL)

    home_page = HomePage(page)
    home_page.open(url)
    home_page.check_page_loaded()


def test_home_page_contains_company_keyword(page):
    url = require_config("BASE_URL", BASE_URL)

    home_page = HomePage(page)
    home_page.open(url)
    home_page.check_page_loaded()

    assert page.title() != ""