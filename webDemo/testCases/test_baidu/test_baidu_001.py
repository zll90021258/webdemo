import pytest


class Test_baidu():
    def test_baidu_select(self, open_page):
        context, page = open_page
        page.click("input[name=\"wd\"]")
        page.fill("input[name=\"wd\"]", "python")

        with page.expect_navigation():
            page.press("input[name=\"wd\"]", "Enter")
        with context.expect_page() as new_page_info:
            page.click("text=你都用 Python 来做什么? - 知乎")
        page1 = new_page_info.value
        page1.click("[aria-label=\"关闭\"]")

        with context.expect_page() as new_page_info:
            page1.click("text=《大胆，都是哪些程序员在反对996？！》")
        page2 = new_page_info.value
        page2.wait_for_timeout(timeout=2000)

        page4 = context.new_page()
        page4.goto("https://mail.qq.com/")
        page4.frame(name="login_frame").fill("input[name=\"u\"]", "984355579")

        with context.expect_page() as new_page_info:
            page.click("text=Python(计算机编程语言) - 百度百科")
        page5 = new_page_info.value


if __name__ == '__main__':
    pytest.main()
