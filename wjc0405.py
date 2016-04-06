#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value

class Screen(object):

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, width):
    	self._width = width
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._width * self._height
    
	
	

s = Student()

s.score = 60
print(s.score)

s1 = Screen()

s1.width = 1024
s1.height = 768
print(s1.width)
print(s1.height)
print(s1.resolution)
#s.score = 101
#s.score = 1.39
