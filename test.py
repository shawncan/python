#!/usr/local/bin/Python3
# -*- coding: utf-8 -*-

import string, random


def id_generator(size=2, chars=string.ascii_uppercase + string.digits):
    test = ''.join(random.choice(chars) for _ in range(size))
    if test[0] == test[1]:
        print("error")
        exit()
    else:
        return test

print(id_generator())