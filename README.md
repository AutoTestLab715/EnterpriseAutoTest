# Enterprise Auto Test

## 项目简介

基于 pytest、requests、Playwright、pytest-html 搭建企业官网自动化测试体系，覆盖官网首页、内容接口、后台登录、内容管理、新闻管理、字段一致性校验及编辑保存流程，共设计 **15 条**自动化测试用例并全部通过；结合 HTML 测试报告和 GitHub Actions 实现自动化回归验证。

## 测试范围

| 模块 | 测试内容 |
|------|----------|
| 官网首页 | 页面可访问、包含企业关键词 |
| 内容接口 | 状态码校验、数据返回校验 |
| 后台登录接口 | 正确/错误密码登录 |
| 后台登录页面 | 页面可打开、登录成功 |
| 内容管理 | 页面可打开、字段与接口一致、副标题编辑保存 |
| 新闻管理 | 页面可打开、字段与接口一致、标题编辑保存 |

## 测试用例（15 条）

- `test_home_page_status_code` — 官网首页状态码
- `test_home_page_can_open` — 官网首页可访问
- `test_home_page_contains_company_keyword` — 首页包含企业关键词
- `test_content_api_status_code` — 内容接口状态码
- `test_content_api_has_data` — 内容接口返回数据
- `test_admin_login_success` — 后台登录接口（正确密码）
- `test_admin_login_fail_with_wrong_password` — 后台登录接口（错误密码）
- `test_admin_login_page_can_open` — 后台登录页可打开
- `test_admin_login_success` (Web) — 后台登录页登录成功
- `test_content_section_can_open` — 内容管理页可打开
- `test_content_fields_match_api` — 内容字段与接口一致
- `test_content_subtitle_can_be_edited_and_saved` — 副标题编辑保存
- `test_news_section_can_open` — 新闻管理页可打开
- `test_news_fields_match_api` — 新闻字段与接口一致
- `test_news_title_can_be_edited_and_saved` — 新闻标题编辑保存

## 技术栈

- Python 3.11
- pytest
- requests
- Playwright
- pytest-html

## 项目结构

```text
EnterpriseAutoTest/
├── .github/workflows/python-test.yml   # GitHub Actions 自动测试
├── pages/                              # Page Object 页面对象
├── tests/                              # 测试用例
├── utils/                              # 配置与工具
├── requirements.txt
├── pytest.ini
└── .env                                # 本地环境变量（勿提交）
```

## 本地运行

### 1. 创建并激活虚拟环境

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

### 2. 安装依赖

```powershell
pip install -r requirements.txt
python -m playwright install chromium
```

### 3. 配置环境变量

在项目根目录创建 `.env` 文件（**不要上传到 GitHub**）：

```env
BASE_URL=https://your-company-site.com
ADMIN_URL=https://your-admin-site.com
ADMIN_USERNAME=your_username
ADMIN_PASSWORD=your_password
CONTENT_API=https://your-api/content
LOGIN_API=https://your-api/login
```

### 4. 运行测试

```powershell
python -m pytest --html=test-report.html --self-contained-html
```

测试完成后，打开 `test-report.html` 查看 HTML 报告。

## GitHub Actions 自动测试

代码推送到 GitHub 后，会在 `push` 和 `pull_request` 时自动运行测试。

### 配置 Secrets

在 GitHub 仓库 **Settings → Secrets and variables → Actions** 中添加以下 Secrets：

| Secret 名称 | 说明 |
|-------------|------|
| `BASE_URL` | 企业官网地址 |
| `ADMIN_URL` | 管理后台地址 |
| `ADMIN_USERNAME` | 后台登录账号 |
| `ADMIN_PASSWORD` | 后台登录密码 |
| `CONTENT_API` | 内容接口地址 |
| `LOGIN_API` | 登录接口地址 |

> `.env` 文件已在 `.gitignore` 中忽略，敏感信息请仅通过 GitHub Secrets 注入 CI 环境。

## 后续计划：JMeter 性能测试

功能测试完成后，可使用 JMeter 对企业网站进行性能压测，建议覆盖：

- 官网首页
- 内容接口
- 管理后台登录接口
- 新闻接口

起步参数：线程数 10、Ramp-up 10 秒、循环 1 次，目标 Error = 0；后续逐步加压至 50、100 线程。
