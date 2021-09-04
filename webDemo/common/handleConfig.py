# -*- coding: utf-8 -*-
# @Author  : ZENGLINGLING
# @Email   : 984355579@qq.com
# @Software: PyCharm
# @Time    : 2021/9/3 10:00
# @File    : handleConfig.py
from configparser import ConfigParser


class handle_config():
    def __init__(self, filePath):
        self.filePath = filePath
        self.config = ConfigParser()
        self.config.read(self.filePath,encoding="utf-8")

    def get_value(self, section, option):
        return self.config.get(section, option)
    def get_int(self, section, option):
        return self.config.getint(section, option)
    def write_config(self,section, option,value):
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, option,value)
        with open(self.filePath,"w") as f:
            self.config.write(f)
    def del_config(self,section, option=None):
        if option is None:
            self.config.remove_section(section)
        else:
            self.config.remove_option(section,option)

