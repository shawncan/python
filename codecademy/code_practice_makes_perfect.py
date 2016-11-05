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


# 传入参数然后倒序输出
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

# 传入字符串把原因字母提出后输入
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


# 传入字符串根据字典里面的值计算
def scrabble_score(word):
    word1 = word.lower()
    total = 0
    for i in word1:
        total += score[i]
    return total


# 根据输入的字符屏蔽相应的文本
def censor(text, word):
    asterisk_list = []
    digit = len(word)
    while digit > 0:
        asterisk_list.append('*')
        digit -= 1
    asterisk = ''.join(asterisk_list)
    return text.replace(word, asterisk)


# 在输入的列表中找字符找出一共出现了几次
def count(sequence, item):
    digit = 0
    for i in sequence:
        if i == item:
            digit += 1
        else:
            continue
    return digit


# 输入的列表中返回只有偶数的列表
def purify(sequence):
    even = []
    for i in sequence:
        if i % 2 == 0:
            even.append(i)
        else:
            continue
    return even


# 输入的列表中返回列表的乘积数
def product(sequence):
    multiply = 1
    for i in sequence:
        multiply *= i
    return multiply


# 输入的列表中删除列表中一样的值
def remove_duplicates(sequence):
    sequence_1 = []
    for i in sequence:
        if i not in sequence_1:
            # 如果i不在sequence_1列表中则执行下面的代码
            sequence_1.append(i)
    return sequence_1

'''
# 输入的列表中返回中位数
我去转换了字符串然后再去计算，这样的话列表只有1个的时候就无法计算了，所以会有问题，而直接去列表取值就不会有问题了，饶了一个大湾路
def median(sequence):
    digital = len(sequence)
    sequence.sort()
    sequence_1 = ''.join([str(i) for i in sequence])
    if digital % 2 == 0:
        return (int(sequence_1[int(digital / 2)]) + int(sequence_1[int( (digital / 2) - 1)])) / 2
    else:
        return sequence_1[int((digital / 2) - 0.5)]
'''

# 输入的列表中返回中位数
def median(sequence):
    digital = len(sequence)
    sequence.sort()
    if digital % 2 == 0:
        return (int(sequence[int(digital / 2)]) + int(digital[int( (digital / 2) - 1)])) / 2
    else:
        return sequence[int((digital / 2) - 0.5)]

print(median([2]))
