#!/usr/local/bin/Python3
# -*- coding: utf-8 -*-

import time, datetime, random

from random import randint

'''
# 生成时间戳,先生成当前时间戳,然后再打印成需要的
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
time_stamp = "Thu Aug 18 10:00:00 2016"
print(time.mktime(time.strptime(time_stamp, "%a %b %d %H:%M:%S %Y")))
'''

#把秒转换为时间
date = time.strftime("%Y-%m-%d ", time.localtime())

time = time.strftime("%H:%M:%S", time.localtime(random.randint(1471485600, 1471514400)))

date_time = ("%s %s" % (date, time))

# print(date_time)

'''
# #先格式化一个时间,然在把时间随机
# test = time.strftime("%Y-%m-%d ", time.localtime())
#
# a = "{}:{}:{}".format(randint(10, 18), randint(10, 59), randint(10, 59))
#
# date_time = ("%s %s" % (test, a))
#
# print(date_time)
'''