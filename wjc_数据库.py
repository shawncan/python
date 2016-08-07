#!/usr/local/bin/Python3
# -*- coding: utf-8 -*-

import pymysql

conn = pymysql.connect("192.168.0.5", "root", "wjc0216wjc", "wjc")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

sql = "SHOW DATABASES;"

try:
    cursor.execute(sql)
except:
    conn.rollback()
# 关闭数据库连接
conn.close()