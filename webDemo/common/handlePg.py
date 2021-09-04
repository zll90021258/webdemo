# -*- coding: utf-8 -*-
# @Author  : ZENGLINGLING
# @Email   : 984355579@qq.com
# @Software: PyCharm
# @Time    : 2021/9/3 18:26
# @File    : handlePg.py
import psycopg2


class handle_oracle():
    def __init__(self):
        self.con = psycopg2.connect(database, user, password, host, port)
        self.cursor = self.con.cursor()

    def select(self, select_sql, vars=None):
        self.cursor.execute(select_sql, vars)
        return self.cursor.fetchall()

    def update(self, update_sql, vars=None):
        self.cursor.execute(update_sql, vars)
        self.con.commit()

    def insert(self, insert_sql, vars=None):
        self.cursor.execute(insert_sql, vars)
        self.con.commit()

    def delete(self, delete_sql, vars=None):
        self.cursor.execute(delete_sql, vars)
        self.con.commit()

    def close(self):
        self.cursor.close()
        self.con.close()
