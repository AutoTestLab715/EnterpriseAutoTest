from playwright.sync_api import expect


class HomePage:
    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def check_page_loaded(self):
        expect(self.page.locator("body")).to_be_visible()

    def check_text_visible(self, text):
        expect(self.page.get_by_text(text).first).to_be_visible()