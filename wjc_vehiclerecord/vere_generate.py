#!/usr/local/bin/Python3
# -*- coding: utf-8 -*-

import os, vere_licenseplate, vere_time

def generate():
    wjc = vere_licenseplate
    ti = vere_time
    with open('test.txt', 'a') as test:
        test.write('\n' + wjc + '  ' + ti)
        test.close()

# for i in range(10):
#     os.system("python wjc_licenseplate.py")

os.system("python wjc_licenseplate.py")

gener = generate()







