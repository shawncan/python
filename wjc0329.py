import functools

int2 = functools.partial(int, base=2)

print('1000000=', int2('1000000'))
print(int2('1000'))
print(int2('100000'))

print(int('12345'))

def int3(x, base=2):
	return int(x, base)

print(int3('100000'))
#print(int2('100000', bese=10))