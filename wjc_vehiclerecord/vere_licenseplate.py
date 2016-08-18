#!/usr/local/bin/Python3
# -*- coding: utf-8 -*-

import random, string

# 随机生成车牌地区编码Coding region
def region():
    reg = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L"]
    return random.choice(reg)


# 随机生成车牌到后2位
def second(size=2, chars=string.ascii_uppercase + string.digits):
    sec = ''.join(random.choice(chars) for _ in range(size))
    if sec[0] == sec[1]:
        # print("Generating tail number error")
        exit()
    else:
        return sec


# 生成车牌
def plate(region, second):
    if second == "I" or second == "O":
        # print("Generating License Plate error")
        exit()
    else:
        # print("浙%s***%s" % (region, second))
        licen = ("浙%s***%s" % (region, second))
        return licen

# def generate():
#     with open('test.txt', 'a') as test:
#         test.write('\n' + licenseplate)
#         test.close()

region = region()
second = second()
licenseplate = plate(region, second)
# gener = generate()