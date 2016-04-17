#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
f = open('/Users/wangjiacan/Desktop/python/material/practice.txt', 'r')
print(f.read())
f.close()
'''
with open('/Users/wangjiacan/Desktop/python/material/practice.txt', 'w', encoding='utf-8') as f:
    f.write('王')

with open('/Users/wangjiacan/Desktop/python/material/practice.txt', 'a', encoding='utf-8') as f:
    f.write('佳灿是帅哥中的战斗机')

with open('/Users/wangjiacan/Desktop/python/material/practice.txt', 'r', encoding='utf-8') as f:
    print(f.read())