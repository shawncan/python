#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
from io import StringIO

f = StringIO()

f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())


f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。') 
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
'''

from io import BytesIO
'''
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
'''

data = '人闲桂花落，夜静春山空。月出惊山鸟，时鸣春涧中。'.encode('utf-8')
f = BytesIO(data)
print(f.read)
