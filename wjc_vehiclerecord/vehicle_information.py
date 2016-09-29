#!/usr/local/bin/Python3
# -*- coding: utf-8 -*-
import random, string, time


# 随机生成车牌地区编码
def letter():
    coding = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", 'L']
    return random.choice(coding)


# 随机生成车牌最后2位
def tail_number(size=2, chars=string.ascii_uppercase + string.digits):
    tail = ''.join(random.choice(chars) for _ in range(size))
    if tail[0] == tail[1]:
        print("Error: repeat tail number")
        exit()
    elif tail == "I" or tail == "O":
        print("Generating License Plate error")
        exit()
    else:
        return tail


# 随机生成车牌
def license_plate():
    coding = letter()
    figure = tail_number()
    licenseplate = ("浙%s***%s" % (coding, figure))
    return licenseplate


# 随机购买生成时间
def time_purchase():
    data = time.strftime("%Y-%m-%d ", time.localtime())
    period = time.strftime("%H:%M:%S", time.localtime(random.randint(1471485600, 1471514400)))
    date_time = ("%s %s" % (data, period))
    return date_time


# 随机生成数据
def generate():
    licenseplate = license_plate()
    timepurchase = time_purchase()
    fee = random.randint(1000, 2000)
    with open('/Users/wangjiacan/Desktop/cesi.txt', 'a') as test:
        test.write('\n' + licenseplate + '  ' + timepurchase + '  ￥' + str(fee))
        test.close()

frequency = input("请输入输出次数:")

for i in range(int(frequency)):
    generate()

print("程序运行成功,快去看看吧!!!")