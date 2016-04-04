#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
class Student(object):
	def __init__(self, name):
		self.name = name
'''

class Student(object):
	name = 'Student'

s = Student() #创建实例s

print(s.name) #打印实例s的name属性
print(Student.name) #打印类Student的name属性

s.name = 'Michael' #绑定实例s的name的属性为Minchael

print(s.name)  #打印实例s的name属性
print(Student.name) #打印类Student的name属性

del s.name #删除实例s的name属性

print(s.name) #打印实例s的name属性