#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')

	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

bare = Student('Jiacan Wang', 59)
lise = Student('Jiacan Shacan', 90)

print(bare.get_name())
print(bare.get_score())

bare.set_score(80)
print(bare.get_score())

bare.set_score(100)
print(bare.get_score())
print(bare.get_score())

