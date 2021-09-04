# -*- coding: utf-8 -*-
# @Author  : ZENGLINGLING
# @Email   : 984355579@qq.com
# @Software: PyCharm
# @Time    : 2021/9/3 10:19
# @File    : handleBase.py
import os.path
import re
import time


class handle_base():
    def __init__(self,context,page):
        self.context = context
        self.page = page
        self.page.wait_for_load_state(state="networkidle")

    def element_handle(self, element):
        start_time = time.time()
        while True:
            end_time = time.time()
            if end_time - start_time <= 10:
                time.sleep(0.02)
                if not ".document" in element:
                    try:
                        self.page.wait_for_selector(element, state="attached", timeout=100)
                        return self.page
                    except Exception as e:
                        for fr in range(len(self.page.frames)):
                            frame = self.page.frames[fr].name
                            try:
                                self.page.frame(frame).wait_for_selector(element, state="attached", timeout=50)
                                return self.page.frame(frame)
                            except:
                                continue
                else:
                    start, middle, end = element.partition(".value=")
                    el_readonly = self.page.evaluate(start + ".getAttribute('readonly')")

                    try:
                        if not el_readonly is None:
                            self.page.evaluate(start + ".removeAttribute('readonly')")
                        self.page.evaluate(element)
                    except:
                        for fr in range(len(self.page.frames)):
                            frame = self.page.frames[fr].name
                            try:
                                if not el_readonly is None:
                                    self.page.frame(frame).evaluate(start + ".removeAttribute('readonly')")
                                self.page.frame(frame).evaluate(element)
                            except:
                                continue
            else:
                raise

    def goto_url(self, url):
        return self.page.goto(url,wait_until="networkidle")
    def element_click(self, element):
        r = handle_base(self.context,self.page).element_handle(element)
        r.click(element)



    def download_file(self, element, download_path):
        r = handle_base(self.context,self.page).element_handle(element)
        with r.expect_download() as download_info:
            download = download_info.value
        name = download.suggested_filename
        download.save_as(path=os.path.join(download_path, name))

    def click_open_new_page(self, element):
        r = handle_base(self.context,self.page).element_handle(element)
        with self.context.expect_page() as new_page_info:
            r.click(element)
        new_page = new_page_info.value
        self.new_page = new_page
        return self.new_page

    def upload_file(self, element, file_path):
        r = handle_base(self.context,self.page).element_handle(element)
        with r.expect_file_chooser() as file_info:
            r.click(element)
        uploadPage = file_info.value
        uploadPage.set_files(file_path)
        self.uploadPage = uploadPage
        return self.uploadPage

    # r.set_input_files(element,file_path)
    def navigat(self, element):
        r = handle_base(self.context,self.page).element_handle(element)
        with r.expect_navigation():
            r.click(element)

    def input_vaule(self, element, value):
        r = handle_base(self.context,self.page).element_handle(element)
        r.fill(element, value)

    def open_new_page(self):
        new_page = self.context.new_page()
        self.new_page = new_page
        return self.new_page
