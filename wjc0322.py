def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax 
	return sum

f = lazy_sum(1, 3, 5, 7, 9)
print(f())

def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i * i
		fs.append(f)
	return fs
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

def count():
	def f(j):#先创建一个f函数
		def g():
			return j * j
		return g
	fs = []
	for i in range(1, 4):
		fs.append(f(i))#再调用f函数去应用到i上面去
	return fs
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())