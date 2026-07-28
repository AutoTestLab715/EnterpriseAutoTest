from playwright.sync_api import expect


class LoginPage:
    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def login(self, username, password):
        self.page.locator("input").nth(0).fill(username)
        self.page.locator("input").nth(1).fill(password)
        self.page.locator("button.login-button, button[type='submit']").first.click()
        self.page.wait_for_selector(".admin-app", timeout=10000)

    def check_login_page_loaded(self):
        expect(self.page.locator("input").nth(0)).to_be_visible()
        expect(self.page.locator("input").nth(1)).to_be_visible()