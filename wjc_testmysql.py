#!/usr/local/bin/Python3
# -*- coding: utf-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","shawn@0216","wjc_user" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 查询语句
sql = "SHOW TABLES;"

try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   print ("wjc_user数据库表" % results)
except:
   print ("Error: unable to fecth data")

# 关闭数据库连接
db.close()