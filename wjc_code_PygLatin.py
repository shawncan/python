#!/usr/local/bin/Python3"default_encoding": "UTF-8",
# -*- coding: utf-8 -*-

pyg = 'ay'

original = input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print(original)
else:
    print('empty')

word = original.lower()

first = word[0]

new_word = word + first + pyg 

print(word)
print(first)
print(new_word)
