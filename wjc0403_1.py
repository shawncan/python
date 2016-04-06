#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	def run(self):
		print('Dog is running...')

class Cat(Dog):
	def run(self):
		print('Cat is running...')


animal = Animal()
dog = Dog()
cat = Cat()

print(type(animal))
print('cat指向的对象Cat:', isinstance(cat, Cat))
print('cat指向的对象Dog:', isinstance(cat, Dog))
print('cat指向的对象Animal:', isinstance(cat, Animal))
print()
print('dog指向的对象Cat:', isinstance(dog, Cat))
print('dog指向的对象Dog:', isinstance(dog, Dog))
print('dog指向的对象Animal:', isinstance(dog, Animal))
print()
#print(dir('animal'))
'''

class MyObiect(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x
	def power_1(self):
		return self.y * self.y

obj = MyObiect()

print('有属性‘x’吗?:', hasattr(obj, 'x'))
print('obj.x = ', obj.x)
print('获取属性‘x’ =', getattr(obj, 'x'))
print('有属性‘y’吗?:', hasattr(obj, 'y'))
setattr(obj, 'y', 19)# 通过setattr()函数设置了y属性
print('有属性‘y’吗?:', hasattr(obj, 'y'))
print('获取属性‘y’ =',getattr(obj, 'y'))
print('obj.y = ', obj.y)
print('获取属性‘z’ =',getattr(obj, 'z', 404))
print(obj.power_1())