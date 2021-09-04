# -*- coding: utf-8 -*-
# @Author  : ZENGLINGLING
# @Email   : 984355579@qq.com
# @Software: PyCharm
# @Time    : 2021/9/3 15:48
# @File    : handletime.py
import datetime
import json

from dateutil.relativedelta import relativedelta

from webDemo.common.timeToJson import DateEncoder


class handle_time(DateEncoder):
    def start_zero(self, years=0, months=0, week=0, day=0):
        now = datetime.datetime.now()
        startTime = now + relativedelta(years=years) + relativedelta(months=months) + datetime.timedelta(
            weeks=week) + datetime.timedelta(days=day) - datetime.timedelta(hours=now.hour, minutes=now.minute,
                                                                            seconds=now.second,
                                                                            microseconds=now.microsecond) + datetime.timedelta(
            microseconds=+1)
        return eval(json.dumps(startTime.replace(microsecond=0), cls=DateEncoder))

    def end_zero(self, years=0, months=0, week=0, day=0):
        now = datetime.datetime.now()
        startTime = now + relativedelta(years=years) + relativedelta(months=months) + datetime.timedelta(
            weeks=week) + datetime.timedelta(days=day) - datetime.timedelta(hours=now.hour, minutes=now.minute,
                                                                            seconds=now.second,
                                                                            microseconds=now.microsecond) + datetime.timedelta(
            microseconds=-1)
        return eval(json.dumps(startTime.replace(microsecond=0), cls=DateEncoder))

    def nowTime(self, years=0, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0, microseconds=0):
        now = datetime.datetime.now()
        startTime = now + relativedelta(years=years, months=months, weeks=weeks, days=days, hours=hours,
                                        minutes=minutes, seconds=seconds, microseconds=microseconds)
        return eval(json.dumps(startTime.replace(microsecond=0), cls=DateEncoder))


if __name__ == '__main__':
    do_time = handle_time()
    # print(do_time.start_zero(day=-1))
    # print(do_time.end_zero(day=+1))
    # print(do_time.nowTime())
