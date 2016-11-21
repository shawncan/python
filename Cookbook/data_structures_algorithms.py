#!/usr/local/bin/Python3"default_encoding": "UTF-8",
# -*- coding: utf-8 -*-

import heapq

# record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
# name, email, *_, phone_numbers = record

# print(name)
# print(email)
# print(phone_numbers)


"""查找最大或最小的N个元素"""
# nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# print(heapq.nlargest(3, nums))
# heapq.heapify(nums)
# print(nums)
# print(heapq.heappop(nums))
# print(heapq.heappop(nums))
# print(heapq.heappop(nums))
# print(min(nums))
# print(max(nums))
# print(heapq.nlargest(3, nums))
# print(heapq.nsmallest(3, nums))
# print((sorted(nums)[:3]))
# print((sorted(nums)[-3:]))


"""优先级队列"""


# class PriorityQueue(object):
#     def __init__(self):
#         self._queue = []
#         self._index = 0
#
#     def push(self, item, priority):
#         heapq.heappush(self._queue, (-priority, self._index, item))
#         self._index += 1
#
#     def pop(self):
#         return heapq.heappop(self._queue)[-1]
#
#
# class Item(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return 'Item({!r})'.format(self.name)
#
#
# q = PriorityQueue()
# q.push(Item('foo'), 1)
# q.push(Item('bar'), 5)
# q.push(Item('spam'), 4)
# print(q.pop())
# print(q.pop())
# print(q.pop())

a = []
heapq.heappush(a, (-1, "wangjiac"))
heapq.heappush(a, (-2, "2222"))
print(heapq.heappop(a)[-1])
print(heapq.heappop(a)[-1])