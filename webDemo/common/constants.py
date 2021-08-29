import os
one_path = os.path.abspath(__file__)
two_path = os.path.dirname(one_path)   # 获取当前路径的上一级目录所在的绝对路径
three_path = os.path.dirname(two_path)
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


CASE_DIR = os.path.join(BASE_DIR,"cases")
CASE_FILE_PATH = os.path.join(CASE_DIR,"test_unittest_register.py")

'''配置文件'''
configs_path = os.path.join(BASE_DIR, "configs")
testconf_path = os.path.join(configs_path, "test.conf")

DATA_DIR = os.path.join(BASE_DIR,"datas")
DATA_FILE_PATH = os.path.join(DATA_DIR,"cases.xlsx")

LIB_DIR = os.path.join(BASE_DIR,"libs")
LIB_FILE_PATH = os.path.join(LIB_DIR,"ddt.py")

'''报告'''
REPORT_DIR = os.path.join(BASE_DIR,"reports")
result_path = "report_" + datetime.strftime(datetime.now(), "%Y%m%d%H%M%S") +".html"
result_path1 = "report_" + datetime.strftime(datetime.now(), "%Y%m%d%H%M%S") +".html"
result_path2 = "report_" + datetime.strftime(datetime.now(), "%Y%m%d%H%M%S") +".txt"
REPORT_FILE_PATH= os.path.join(REPORT_DIR,result_path)
REPORT_FILE_PATH1= os.path.join(REPORT_DIR,result_path1)
REPORT_FILE_PATH2= os.path.join(REPORT_DIR,result_path2)

'''日志'''
logs_path = os.path.join(BASE_DIR, "logs")
logs_records_pth = os.path.join(logs_path, "logResult.log")



