def now():
	print('2016-3-24')

f = now
print(f())
print(now.__name__)
print(f.__name__)

def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log
def now():
	print('2016-3-24')

print(now())


def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@log('execute')
def now():
	print('2016-3-24')
print(now())
print(now.__name__)


import functools

'''
def logger(text):
	def decorator(func):
		@functools.wrapper(func)
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@logger('wangjiacan')
def today():
	print('2016-3-25')
print(today())
'''

def log()

