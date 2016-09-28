#!/usr/local/bin/Python3
# -*- coding: utf-8 -*-
import random, string, time


# 随机生成车牌地区编码
def region():
    reg = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", 'L']
    return random.choice(reg)


# 随机生成车牌到后2位
def second(size=2, chars=string.ascii_uppercase + string.digits):
    end = ''.join(random.choice(chars) for _ in range(size))
    if end[0] == end[1]:
        print("Error: repeat tail number")
        exit()
    elif end == "I" or end == "O":
        print("Generating License Plate error")
        exit()
    else:
        return end


# 随机生成车牌
def license():
    b = region()
    c = second()
    licenseplate = ("浙%s***%s" % (b, c))
    return licenseplate


# 随机生成时间
def time_purchase():
    data = time.strftime("%Y-%m-%d ", time.localtime())
    period = time.strftime("%H:%M:%S", time.localtime(random.randint(1471485600, 1471514400)))
    date_time = ("%s %s" % (data, period))
    return date_time


# 随机生成数据
def generate():
    license_plate = license()
    period = time_purchase()
    fee = random.randint(1000, 2000)
    with open('/Users/wangjiacan/Desktop/cesi.txt', 'a') as test:
        test.write('\n' + license_plate + '  ' + period + '  ￥' + str(fee))
        test.close()

for i in range(10):
    generate()

print("程序运行成功,快去看看吧!!!")
