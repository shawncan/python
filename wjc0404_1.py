#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	pass

class Graduate(Student):
	__slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 25
s.score = 99
print(s.name)
print(s.age)
print(s.score)

g = Graduate()
#g.score = 9999
#print(g.score)


'''
def set_age(self, age):
	self.age = age

def set_score(self, score):
	self.score = score


s = Student()
s2 = Student()
s.name = 'Michael'

print(s.name)

from types import MethodType
#s.set_age = MethodType(set_age, s)  #给实例绑定一个方法
Student.set_age = MethodType(set_age, Student) #  给类绑定一个方法

s.set_age(25)
print(s.age)

s2.set_age(60)
print(s2.age)
#Student.set_score = MethodType(set_score, Student)

s.set_score(100)
print(s.score)

s2.set_score(99)
print(s2.score)
'''