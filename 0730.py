#!/usr/local/bin/Python3
# -*- coding: utf-8 -*-

# for i in range(1,4):
#     for w in range(1,3):
#         print(" " * w)
#     print("1" * i)

# 金字塔行数
n = 5

# 多少行循环多少次
for i in range(n):
    # 输出空格需要对 n 进行修改,故新起变量 blank
    blank = n
    
    # range 的list 是从 0 开始的,这里需要从 1 开始
    i +=1

    j = 1
    star = ""

    # 空格
    while blank - i > 0:
        star += " "
        blank -= 1

    # 星
    while j <= (i - 1) * 2+1:
        star += "1"
        j +=1
    print(star)