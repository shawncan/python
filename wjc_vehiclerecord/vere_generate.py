#!/usr/local/bin/Python3
# -*- coding: utf-8 -*-

import os, random, vere_licenseplate, vere_time

def generate():
    os.system("python vere_licenseplate.py")
    os.system("python vere_time.py")
    wjc = vere_licenseplate.licenseplate
    ti = vere_time.date_time
    fee = random.randint(1000, 2000)
    with open('test.txt', 'a') as test:
        test.write('\n' + wjc + '  ' + ti + '  ￥' + str(fee))
        test.close()


generate()





