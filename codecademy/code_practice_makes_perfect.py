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
    text1 = list(text)
    text2 = []
    for i in text1:
        text2.insert(0, i)
    text3 = ''.join(text2)
    return text3


# 其他的2种方法
# def reverse1(text):
#     text1 = list(text)
#     text2 = []
#     for i in reversed(text1):
#         text2.append(i)
#     text3 = ''.join(text2)
#     return text3
#
# def reverse2(text):
#     return text[::-1]


def anti_vowel(text):
    original = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    text1 = []
    for i in text:
        if i in original:
            continue
        else:
            text1.append(i)
    text2 = ''.join(text1)
    return text2


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


def scrabble_score(word):
    word1 = word.lower()
    total = 0
    for i in word1:
        total += score[i]
    return total


print(scrabble_score("Helix"))