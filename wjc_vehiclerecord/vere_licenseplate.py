#!/usr/local/bin/Python3
# -*- coding: utf-8 -*-

import random, string

# 随机生成车牌地区编码Coding region
def region():
    reg = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", 'L']
    return random.choice(reg)


# 随机生成车牌到后2位
def second(size=2, chars=string.ascii_uppercase + string.digits):
    end = ''.join(random.choice(chars) for _ in range(size))
    if end[0] == end[1]:
        print("Error: repeat tail number")
        exit()
    else:
        if end =="I" or end == "O":
            print("Generating License Plate error")
            exit()
        else:
            return end



region = region()
second = second()

# 生成车牌
licenseplate = ("浙%s***%s" % (region, second))