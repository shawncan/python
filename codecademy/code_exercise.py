#!/usr/local/bin/Python3"default_encoding": "UTF-8",
# -*- coding: utf-8 -*-

#计算购物清单总价
def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total = total + prices[item]
            stock[item] = stock[item] - 1
    return total

#库存
stock = {"banana": 6,"apple": 0, "orange": 32, "pear": 15}

#单价    
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}

#购物清单
shopping_list = ["banana", "orange", "apple", "pear"]
print(compute_bill(shopping_list))
print(stock)
