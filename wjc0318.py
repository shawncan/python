def is_odd(n):
	return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
#保留偶数数据，删掉奇数数据

def is_odd(n):
	return n % 2 == 0

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
#如果n是偶数返回，n是奇数不返回

def not_empty(s):
	return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))
#如果s中没有空格则保留数据，s中有空格丢弃该数据

def not_empty(s):
	return s == 'A'

print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))
#如果s等于A就返回数据
