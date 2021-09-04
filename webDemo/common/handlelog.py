# coding=utf-8
import re
import logging
from webDemo.common.singleton import Singleton
from logging import handlers
from webDemo.common.constants import logs_records_pth

class handleLog(Singleton):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }


    def __init__(self):
        # 创建日志收集器
        self.log = logging.getLogger(logs_records_pth)
        #  收集器日志等级设置
        self.log.setLevel(logging.DEBUG)  # 当日志级别高于debug，debug打印不了
        # 输出到控制台，设置日志级别，设置简洁日志输出格式，收集日志和接收日志的对接
        format = '%(asctime)s- %(pathname)s[line:%(lineno)d] - %(levelname)s:%(message)s'

        console = logging.StreamHandler()
        console.setLevel(logging.DEBUG)
        formatter = logging.Formatter(format)
        console.setFormatter(formatter)
        self.log.addHandler(console)

        # # # 输出到文件，设置日志级别，设置详细日志输出格式，收集日志和接收日志的对接
        file_log = (logging.FileHandler(logs_records_pth, encoding="utf-8"))

        # # # 日志文件初始化 (每次会清除上次的日志(最好不设置))
        # logging.basicConfig(
        #     level=logging.DEBUG,
        #     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s - %(name)s - %(lineno)d',
        #     datefmt='%a %d %b %Y %H:%M:%S',
        #     filename=testconf_path,  # 日志路径
        #     filemode='w')
        #
        # 输出到文件，设置日志级别，设置详细日志输出格式，收集日志和接收日志的对接
        # 每天生成一个日志文件，保留最近的日志文件(清理日志)
        # "%Y-%m-%d_%H-%M-%S.log" 表示设置是秒
        # 注意：filehanlder.suffix的格式必须这么写，才能自动删除旧文件，如果设定是天，就必须写成“ % Y - % m - % d.log”，写成其他格式会导致删除旧文件不生效
        '''按天数分割'''
        file_log = handlers.TimedRotatingFileHandler(filename=logs_records_pth, when="D", interval=1, backupCount=3,
                                                     encoding='utf-8', delay=False, utc=False, atTime=None)
        # '''按大小分割'''
        # file_log =handlers.RotatingFileHandler(filename=logs_records_pth, maxBytes=500, backupCount=5)
        file_log.suffix = "%Y-%m-%d_%H-%M-%S"
        file_log.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}$")
        file_format='%(asctime)s- %(pathname)s[line:%(lineno)d]-%(filename)s-%(thread)d-%(thread)s-%(levelname)s:%(message)s'
        file_log.setLevel(logging.DEBUG)
        formatter = logging.Formatter(file_format)
        file_log.setFormatter(formatter)
        self.log.addHandler(file_log)
        # self.log.handlers = self.log.handlers[:1]  # 解决日志重复打印问题
        # self.log.removeHandler(file_log) 移除了日志就没了。。。
        console.close()
        file_log.close()
    def logger(self):
        return self.log




if __name__ == '__main__':
    do_log = handleLog().logger()
    print(do_log.debug("哈哈"))

