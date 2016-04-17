#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Dog(object):
    def dog(self):
        print('dog')


def fn(self, name='world'):
    print('Hello, %s.' % name)

def bat(self):
    print('bat')

Hello = type('Hello', (Dog,), dict(hello=fn, d=bat)) 

h = Hello()

h.hello()
h.dog()
h.d()
print(type(Hello))
print(type(h))