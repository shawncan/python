#!/usr/local/bin/Python3"default_encoding": "UTF-8",
# -*- coding: utf-8 -*-

# 20161112 二进制的表示

# print(5 >> 4)
# print(5 << 1)
# print(8 & 5)
# print(9 | 1)
# print(12 ^ 4)
# print(~88)


# print(0b1)
# print(0b10)
# print(0b11)
# print(0b100)
# print(0b101)
# print(0b110)
# print(0b111)
# print("******")
# print(0b1 + 0b11)
# print(0b11 * 0b11)


one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100
text = bin(201)  # 查询数字的2进制表示
# print(one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve)


# 20161112 位运算符

# shift_right = 0b1100
# shift_left = 0b1
# print(bin(shift_right), bin(shift_left))
# print(bin(shift_right >> 2))
# print(bin(shift_left << 2))


# print(bin(0b1110 & 0b101))

# print(bin(0b1110 | 0b101))

# print(bin(0b1110 ^ 0b101))

# print(bin(~0b1110))


# 20161112 综合操作


# def check_bit4(integer):
#     mask = 0b1000
#     desired = integer & mask
#     if desired >= 8:
#         return "on"
#     else:
#         return "off"
# test = int(0b1000)
# test = bin(13)
# print(check_bit4(int(input("请输入："))))


# a = 0b1101
# mask = 0b100
# desired = a | mask
# print(bin(desired))

# a = 0b11101110
# mask = 0b11111111
# desired = a ^ mask
# print(bin(desired))


def flip_bit(number, n):
    mask = (0b01 << (n - 1))
    print(bin(mask))
    result = number ^ mask
    return result

print(bin(flip_bit(0b101, 1)))
