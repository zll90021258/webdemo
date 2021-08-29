import os
from playwright.sync_api import sync_playwright
from py._xmlgen import html
import pytest


@pytest.fixture(scope="package",autouse=True)
def open_page():
    playwright = sync_playwright().start()
    # Use playwright.chromium, playwright.firefox or playwright.webkit
    # Pass headless=False to launch() to see the browser UI
    # [playwright.chromium, playwright.firefox, playwright.webkit]
    for browser_type in [playwright.chromium]:
        browser = browser_type.launch(args=["--start-maximized"],headless=False)
        context = browser.new_context(viewport=None,record_video_dir="./videos",record_video_size={"width": 640, "height": 800},accept_downloads=True)
        page = context.new_page()
        page.goto("https://www.baidu.com/")
        yield context, page
        browser.close()
        playwright.stop()


def pytest_configure(config):
    config._metadata["项目名称"] = "百度"
    config._metadata["接口地址"] = "https://www.baidu.com/"
    config._metadata.pop("JAVA_HOME")


# @pytest.mark.optionalhook
# def pytest_html_results_summary(prefix):
#     prefix.extend([html.p("所属部门: xx测试中心")])
#     prefix.extend([html.p("测试人员: 曾xx")])