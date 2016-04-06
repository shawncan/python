#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
	pass

class Runnable(object):
	def run(self):
		print('能跑的动物...')

class Flyable(object):
	def fly(self):
		print('能飞的动物...')

class Mamal(Animal):
	def ning(self):
		print('哺乳动物...')

class Bird(Animal):
	def bir(self):
		print('鸟类')

class Dog(Mamal, Runnable):#Dog既是Mamal的子类也是Runnable的子类
	pass

class Bat(Bird, Flyable):
	pass


dog = Dog()
dog.run()
dog.ning()


bat = Bat()
bat.bir()
bat.fly()
