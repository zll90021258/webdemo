# -*- coding: utf-8 -*-
# @Author  : ZENGLINGLING
# @Email   : 984355579@qq.com
# @Software: PyCharm
# @Time    : 2021/9/4 14:21
# @File    : 1.py

def aa():
    a=1
    b=3
    return a,b
def bb(a,b):
    return a+b
if __name__ == '__main__':
    a=aa()[0]
    b=aa()[1]
    print(bb(a,b))
