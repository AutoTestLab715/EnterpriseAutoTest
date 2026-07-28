from pages.admin_page import AdminPage


class NewsPage(AdminPage):
    SECTION_NAME = "新闻管理"

    def open(self):
        self.goto_section(self.SECTION_NAME)

    def first_news_title(self):
        return self.field("新闻标题")

    def first_news_summary(self):
        return self.field("新闻摘要")

    def first_news_date(self):
        return self.field("发布日期")
