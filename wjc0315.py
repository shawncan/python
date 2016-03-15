def f(x):
	return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list(r))

r = map(f, [90, 19])

print(list(r))
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

from functools import reduce
def fn(x, y):
	return x * 10 + y
print(reduce(fn, [1, 3, 5, 7, 9]))

def add(x, y):
	return x + y
print(reduce(add, [1, 3, 5, 7, 9]))