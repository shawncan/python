#!/usr/local/bin/Python3"default_encoding": "UTF-8",
# -*- coding: utf-8 -*-

my_dict = {
    "Name": "shawn",
    "Age": 25,
    "height": "170cm"
}

# print(my_dict.keys())
# print(my_dict.values())
#
# for i in my_dict:
#     print(i, my_dict[i])

# evens_to_50 = [i for i in range(51) if i % 2 == 0]
#
# print(evens_to_50)

doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]

cubes_by_four = [i ** 3 for i in range(1, 11) if (i ** 3) % 4 == 0]

test = ["a", "b", "c", "d", "e"]

my_list = [i for i in range(1, 11)]

to_21 = [i for i in range(1, 22)]

odds = to_21[::2]

middle_third = to_21[7:14:1]

my_list_1 = [i for i in range(16)]

print(my_list_1)

a = lambda x:  x + 1

print(a(4))
