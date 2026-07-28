import pytest
from playwright.sync_api import expect

from pages.content_page import ContentPage
from utils.content_api import fetch_content


@pytest.fixture
def content_page(admin_page):
    page = ContentPage(admin_page.page)
    page.open()
    return page


def test_content_section_can_open(content_page):
    assert content_page.header_title() == "基础信息"
    expect(content_page.site_title()).to_be_visible()
    expect(content_page.site_subtitle()).to_be_visible()


def test_content_fields_match_api(content_page):
    content = fetch_content()

    expect(content_page.site_title()).to_have_value(content["site"]["title"])
    expect(content_page.site_subtitle()).to_have_value(content["site"]["subtitle"])
    expect(content_page.welcome_text()).to_have_value(content["site"]["welcome"])
    expect(content_page.hotline()).to_have_value(content["site"]["hotline"])


def test_content_subtitle_can_be_edited_and_saved(content_page):
    subtitle_input = content_page.site_subtitle()
    original_value = subtitle_input.input_value()
    updated_value = f"{original_value}-auto-test"

    try:
        subtitle_input.fill(updated_value)
        content_page.save()

        updated_content = fetch_content()
        assert updated_content["site"]["subtitle"] == updated_value
    finally:
        subtitle_input.fill(original_value)
        content_page.save()
        restored_content = fetch_content()
        assert restored_content["site"]["subtitle"] == original_value
