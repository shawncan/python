#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

'''对象的JSON格式转换
d = dict(name='Bob', age=20, score=88)

print(json.dumps(d))
'''

'''JSON反序列化对象
json_str = '{"score": 80, "age": 25, "name": "Bob"}'
print(json.loads(json_str))
'''

#用类的方法序列化JOSN
class Student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return{
    'name' : std.name,
    'age' : std.age,
    'score' : std.score
    }

s = Student('Bob', 20, 88)

print(json.dumps(s, default=student2dict))
#print(json.dumps(s, default=lambda obj: obj.__dict__))