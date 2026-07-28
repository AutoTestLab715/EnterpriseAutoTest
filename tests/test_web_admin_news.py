import pytest
from playwright.sync_api import expect

from pages.news_page import NewsPage
from utils.content_api import fetch_content


@pytest.fixture
def news_page(admin_page):
    page = NewsPage(admin_page.page)
    page.open()
    return page


def test_news_section_can_open(news_page):
    assert news_page.header_title() == "新闻管理"
    expect(news_page.first_news_title()).to_be_visible()
    expect(news_page.first_news_summary()).to_be_visible()


def test_news_fields_match_api(news_page):
    content = fetch_content()
    first_news = content["news"][0]

    expect(news_page.first_news_title()).to_have_value(first_news["title"])
    expect(news_page.first_news_summary()).to_have_value(first_news["summary"])
    expect(news_page.first_news_date()).to_have_value(first_news["date"])


def test_news_title_can_be_edited_and_saved(news_page):
    title_input = news_page.first_news_title()
    original_value = title_input.input_value()
    updated_value = f"{original_value}-auto-test"

    try:
        title_input.fill(updated_value)
        news_page.save()

        updated_content = fetch_content()
        assert updated_content["news"][0]["title"] == updated_value
    finally:
        title_input.fill(original_value)
        news_page.save()
        restored_content = fetch_content()
        assert restored_content["news"][0]["title"] == original_value
