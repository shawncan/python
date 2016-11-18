#!/usr/local/bin/Python3"default_encoding": "UTF-8",
# -*- coding: utf-8 -*-

my_list = [i**2 for i in range(1, 11)]

my_file = open("output.txt", "r+")

for i in my_list:
    my_file.write(str(i))
    my_file.write("\n")
my_file.close()
print("打印完成")
