# -*- coding: utf-8 -*-
# @Author  : ZENGLINGLING
# @Email   : 984355579@qq.com
# @Software: PyCharm
# @Time    : 2021/9/4 12:46
# @File    : baiduPage.py
from webDemo.common.handleBase import handle_base
class baidu(handle_base):
    def baidu_page(self):
        handle_base(self.context,self.page).goto_url("https://www.baidu.com/")
        handle_base(self.context,self.page).element_click("input[name=\"wd\"]")
        handle_base(self.context,self.page).input_vaule("input[name=\"wd\"]", "python")
        handle_base(self.context,self.page).element_click("#su")
        page1=handle_base(self.context,self.page).click_open_new_page("text=你都用 Python 来做什么? - 知乎")
        handle_base(self.context,page1).element_click("[aria-label=\"关闭\"]")
        page2=handle_base(self.context,page1).click_open_new_page("text=《大胆，都是哪些程序员在反对996？！》")
        page3=handle_base(self.context,self.page).open_new_page()
        handle_base(self.context,page3).goto_url("https://mail.qq.com/")
        handle_base(self.context,page3).input_vaule("input[name=\"u\"]", "984355579")
        page4=handle_base(self.context,self.page).click_open_new_page("text=Python(计算机编程语言) - 百度百科")


