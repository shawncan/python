#!/usr/local/bin/Python3
# -*- coding: utf-8 -*-

import random, string

#随机生成车牌地区编码Coding region
def region():
    reg = ["A", "B", "C", "D", "E", "F", "G", "H", "J", "K", "L"]
    return random.choice(reg)

#随机生成车牌倒数第二字符
# def second():
#     sec = chr(random.randint(65, 90))
#     if sec == "I" or sec == "O":
#         print("Generating Generate Sencond error")
#         exit()
#     else:
#         return sec


#随机生成车牌到后2位
def second(size=2, chars=string.ascii_uppercase + string.digits):

    # letter = chr(random.randint(65, 90))
    # digital = random.randint(0,9)
    # second = (digital or letter)

    # return second
    sec =  ''.join(random.choice(chars) for _ in range(size))
    if sec[0] == sec[1]:
        #print("Generating tail number error")
        exit()
    else:
        return sec


# #随机生成车牌到尾号
# def tail():

#     letter = chr(random.randint(65, 90))
#     digital = random.randint(0,9)
#     tai = (digital or letter)

#     return tai

#生成车牌
def licenseplate(region, second):

    # if second == tail :
    #     print("Generating License Plate error")
    #     exit()
    # elif second == "I" or second == "O":
    #     print("Generating Generate Sencond error")
    #     exit()
    # else:
    #     print("浙%s***%s%s" % (region, second, tail))
    if second == "I" or second == "O":
        #print("Generating License Plate error")
        exit()
    else:
        print("浙%s***%s" % (region, second))

if __name__ == "__main__":
    #生成地区编码
    region = region()
    #生成倒数第二字符
    second = second()
    # #生成车牌到尾号
    # tail = tail()

    licenseplate = licenseplate(region, second)


