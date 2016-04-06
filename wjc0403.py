#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	def run(self):
		print('Dog is running...')

class Cat(Animal):
	def run(self):
		print('Cat is running...')
class Timer(object):
	def run(self):
		print('Start...')
class Tiger(object):
	def run(self):
		print('tiger.....')

def run_twice(animal):
	animal.run()
	animal.run()

animal = Animal()
dog = Dog()
cat = Cat()

animal.run()
dog.run()
cat.run()

run_twice(Animal())
run_twice(Cat())
run_twice(Dog())
run_twice(Timer())
run_twice(Tiger())

