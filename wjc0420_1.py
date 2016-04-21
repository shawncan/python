#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

#print(os.name)
#print(os.getcwd())
os.chdir('/Users/wangjiacan/Desktop/python')
#print(os.getcwd())

#os.path.join('/Users/wangjiacan/Desktop/python','shawncan')#先把需要创建新目录的路径表现出来

#os.mkdir('/Users/wangjiacan/Desktop/python/shawncan')
#os.rmdir('/Users/wangjiacan/Desktop/python/shawncan')
#([x for x in os.listdir('.') if os.path.isdir(x)])
os.chdir('/Users/wangjiacan/Desktop/python/python')
#print(os.getcwd())
[x for x in os.listdir('.') if os.path.lsfile(x) and os.path.splitext(x)[1]=='.py']