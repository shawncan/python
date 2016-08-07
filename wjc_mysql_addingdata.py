#!/usr/local/bin/Python3
# -*- coding: utf-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","shawn@0216","wjc_user")
#db = pymysql.connect(host='localhost',port=3306, user='root', passwd='shawn@0216', db='wjc_user')

#db = pymysql.connect()
cursor = db.cursor()
# SQL 插入语句
sql = """INSERT INTO test_wjc_user (phone, name, age, height, birthday) VALUES ("15088603208", "Lucinedrew", "26", "159", "1990-09-19");"""

try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()

# 关闭数据库连接
db.close()