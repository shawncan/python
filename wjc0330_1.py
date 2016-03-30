#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s: %s' % (self.name, self.score))

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

bare = Student('Jiacan Wang', 59)
lise = Student('Jiacan Shacan', 90)

print('名字：', bare.name)
print('分数：', bare.score)
#bare.print_score()
print('成绩：', bare.get_grade())

lise.print_score()
print('成绩：', lise.get_grade())
