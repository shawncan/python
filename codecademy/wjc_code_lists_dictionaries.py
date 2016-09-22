#!/usr/local/bin/Python3"default_encoding": "UTF-8",
# -*- coding: utf-8 -*-

'''
#0909
figure = ["1", "2", "3", "55", "100"]

figure[3] = 99

# print(figure[3])

fee = figure[1:]

print(fee)

start_list = [5, 3, 1, 2, 4]
square_list = []

'''

'''
#0911
for figure in start_list:
    square_list.append(figure ** 2)

square_list.sort()

print(square_list)
'''

def fizz_count(x):
    count = 0
    for n in x:
        if n == "fizz":
            count = count + 1
    return count
    
x = ["fizz","cat","fizz"]
sound = fizz_count(x)
print(sound)