# -*- coding: utf-8 -*-
# @Author  : ZENGLINGLING
# @Email   : 984355579@qq.com
# @Software: PyCharm
# @Time    : 2021/9/3 18:38
# @File    : handleScreen.py
import time
from functools import wraps


def caseScreen(datas):
    def middle(func):
        @wraps(func)
        def wrapper(self,*args,**kwargs):
            for data in datas:
                try:
                    f=func(self,data)
                    picture_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
                    sucessScreen=picture_time+".png"
                    continue
                except Exception as e:
                    picture_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
                    failScreen=picture_time+".png"
                    continue
        return wrapper
    return middle





