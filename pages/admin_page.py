from playwright.sync_api import Page, expect


class AdminPage:
    SECTIONS = ("工作台", "基础信息", "业务板块", "新闻管理", "联系与责任", "系统设置")

    def __init__(self, page: Page):
        self.page = page

    def goto_section(self, section_name: str):
        self.page.locator("nav button").filter(has_text=section_name).click()
        expect(self.page.locator(".admin-header h1")).to_have_text(section_name)

    def header_title(self) -> str:
        return self.page.locator(".admin-header h1").inner_text()

    def field(self, label: str):
        return self.page.get_by_label(label, exact=False).first

    def save(self):
        with self.page.expect_response(
            lambda response: "/api/content" in response.url
            and response.request.method == "PUT"
        ) as response_info:
            self.page.locator("button.save-button").click()

        response = response_info.value
        assert response.status == 200
        expect(self.page.locator(".save-status")).to_contain_text("同步")
