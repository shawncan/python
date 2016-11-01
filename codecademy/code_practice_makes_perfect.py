#!/usr/local/bin/Python3"default_encoding": "UTF-8",
# -*- coding: utf-8 -*-


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def is_int(y):
    if y == int(y):
        return True
    else:
        return False


def digit_sum(n):
    integer = str(n)
    digit = 0
    for i in integer:
        digit += int(i)
    return digit


def factorial(x):
    digit = 1
    for i in range(1, x + 1):
        digit *= i
    return digit


# 另外一种实现的方法
#  def factorial1(x):
#     fact = 1
#     while x > 0:
#         fact = fact * x
#         x -= 1
#     return fact


def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2, x):
        if x % n == 0:
            return False
            break
    else:
        return True


def reverse(text):
    a = list(text)
    return a


print(reverse("abcd"))
