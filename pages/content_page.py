from pages.admin_page import AdminPage


class ContentPage(AdminPage):
    SECTION_NAME = "基础信息"

    def open(self):
        self.goto_section(self.SECTION_NAME)

    def site_title(self):
        return self.field("集团名称")

    def site_subtitle(self):
        return self.field("网站副标题")

    def welcome_text(self):
        return self.field("欢迎语")

    def hotline(self):
        return self.field("服务热线")
